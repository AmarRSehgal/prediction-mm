"""v2 paper engine. One process runs one strategy kind; it may carry several arms
that differ only in paper order latency (the latency ladder), sharing one feed,
one universe and one fair value per market, each with its own venue and book.

    niche   v1's target universe (TARGET_SUBSECTORS), book-mid fair value
    crypto  KXBTCD / KXETHD hourly strikes, Binance-anchored fair value

Per market, every step: pick a mode (two-sided / quiet / reduce-only / pulled),
run the gates, compute fair value and its volatility, ask the edge curve for two
passive quotes, and reconcile them against the paper venue. Fills come off the
pushed tape. Nothing ever crosses the spread; positions that are not quoted out
are held to resolution and settled at 0 or 100 from Kalshi's own result.

Everything an analysis needs is appended to <data>/<arm>/fills.jsonl and
settlements.jsonl; portfolio.json is the same Portfolio format v1 writes.
"""
from __future__ import annotations

import asyncio
import json
import logging
import signal
import time
from collections import Counter
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from pmm.kalshi.client import KalshiClient
from pmm.sleepwatch import SleepWatch
from pmm.trader.config import TARGET_SUBSECTORS
from pmm.trader.events_calendar import is_subsector_blacked_out_by_calendar
from pmm.trader.fees import FeeBook
from pmm.trader.position import Fill, load_portfolio, save_portfolio
from pmm.trader.schedule import compute_window
from pmm.trader.subsector_tuning import get as get_tuning, is_in_blackout
from pmm.trader.universe import discover_markets
from pmm.v2.fairvalue import Anchor, BinanceSpot, EWVar, SpotVol, p_above, prob_sigma_c, twap_t_eff
from pmm.v2.quote import QUIET, REDUCE_ONLY, TWO_SIDED, EdgeParams, desired_quotes
from pmm.v2.stream import KalshiStream, Print
from pmm.v2.venue import PaperVenue

log = logging.getLogger(__name__)

CRYPTO_SERIES = {"KXBTCD": "BTCUSDT", "KXETHD": "ETHUSDT"}
MARKOUT_S = (10, 60, 300, 3600)
PULLED = "pulled"


@dataclass(frozen=True)
class ArmConfig:
    name: str
    kind: str                         # "niche" | "crypto"
    edge: EdgeParams
    step_s: float
    universe_refresh_s: float
    capital_dollars: float = 3880.0   # v1's paper capital, so the two books are the same size
    max_loss_dollars: float = 194.0   # v1's daily stop: past this, reduce-only everywhere
    replace_ticks: int = 1
    min_order_life_s: float = 1.0
    impact_depth: float = 20.0
    pull_before_close_s: float = 600.0   # crypto: the hourly print is a cliff
    max_fv_gap_c: float = 8.0
    binance_stale_s: float = 3.0
    delta_cap_dollars: float = 3.0       # crypto: $ PnL per 1% move, per underlying
    event_gross_cap: int = 10            # niche: contracts across one event's markets
    strikes_per_expiry: int = 10
    expiries_per_asset: int = 3
    latency_s: float = 0.5               # paper order ack and cancel latency


NICHE = ArmConfig("v2_niche", "niche", EdgeParams(), step_s=2.0, universe_refresh_s=900.0)
CRYPTO = ArmConfig("v2_crypto", "crypto",
                   EdgeParams(order_size=3, q_max=10, k_base_c=1.0, k_vol=1.0, k_skew_c=2.0,
                              band_lo_c=8, band_hi_c=92),
                   step_s=0.5, universe_refresh_s=300.0)

# Latency ladders: the same strategy at five order latencies from instant to the
# existing arms' 0.5s, all on a faster step so the rungs differ only in latency.
LADDER_MS = (0, 125, 250, 375, 500)
CRYPTO_LADDER = tuple(replace(CRYPTO, name=f"v2_crypto_{ms}ms", latency_s=ms / 1000, step_s=0.1)
                      for ms in LADDER_MS)
NICHE_LADDER = tuple(replace(NICHE, name=f"v2_niche_{ms}ms", latency_s=ms / 1000, step_s=0.5)
                     for ms in LADDER_MS)


@dataclass
class Mkt:
    ticker: str
    subsector: str
    series: str
    event: str
    close_time: datetime
    strike: float = 0.0
    symbol: str = ""
    anchor: Anchor = field(default_factory=Anchor)
    fv_var: EWVar = field(default_factory=lambda: EWVar(1800.0, 1.0))
    last_var_t: float = 0.0


def _dt(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


class Arm:
    """One latency rung: its own paper venue, portfolio, record and kill switch."""

    def __init__(self, cfg: ArmConfig, data: Path):
        cfg.edge.check()
        self.cfg, self.data = cfg, data
        data.mkdir(parents=True, exist_ok=True)
        self.portfolio = load_portfolio(data / "portfolio.json", starting_cash=cfg.capital_dollars)
        self.venue = PaperVenue(ack_s=cfg.latency_s, cancel_s=cfg.latency_s)
        self.gates: Counter = Counter()
        self.pending_markouts: list[dict] = []
        self.killed = False

    def append(self, name: str, row: dict):
        with open(self.data / name, "a") as f:
            f.write(json.dumps(row, default=str) + "\n")

    def held(self, ticker: str) -> bool:
        p = self.portfolio.positions.get(ticker)
        return bool(p and p.yes_contracts)


class Engine:
    def __init__(self, cfgs: tuple[ArmConfig, ...] | ArmConfig, client: KalshiClient,
                 series_df: pd.DataFrame, data_root: Path):
        cfgs = (cfgs,) if isinstance(cfgs, ArmConfig) else tuple(cfgs)
        base = cfgs[0]
        # Arms in one process share the feed, the universe and the fair value, so they
        # may differ in nothing but name and latency. Anything else is a config error.
        for c in cfgs[1:]:
            if replace(c, name=base.name, latency_s=base.latency_s) != base:
                raise ValueError(f"{c.name} differs from {base.name} in more than latency")
        self.cfg, self.client, self.series_df = base, client, series_df
        self.arms = [Arm(c, data_root / c.name) for c in cfgs]
        self.fee_book = FeeBook.from_series_frame(series_df)
        self.stream = KalshiStream(client, self._on_print)
        self.spot = BinanceSpot(tuple(CRYPTO_SERIES.values())) if base.kind == "crypto" else None
        self.mkts: dict[str, Mkt] = {}
        self.watch = SleepWatch()
        self._stop = asyncio.Event()

    # ---- universe ----
    def _discover_niche(self) -> list[Mkt]:
        out = []
        for m in discover_markets(self.client, TARGET_SUBSECTORS, self.series_df):
            out.append(Mkt(m.ticker, m.subsector, m.series, m.ticker.rsplit("-", 1)[0], m.close_time))
        return out

    def _discover_crypto(self) -> list[Mkt]:
        now = datetime.now(timezone.utc)
        out = []
        for series, sym in CRYPTO_SERIES.items():
            spot = self.spot.mid.get(sym)
            if not spot:
                continue
            ms = self.client.list_markets(series_ticker=series, status="open", limit=1000,
                                         max_close_ts=int(now.timestamp()) + 26 * 3600).get("markets") or []
            by_exp: dict[str, list[dict]] = {}
            for m in ms:
                ct = _dt(m.get("close_time"))
                if m.get("strike_type") != "greater" or ct is None or m.get("floor_strike") is None:
                    continue
                if not 900 < (ct - now).total_seconds() <= 26 * 3600:
                    continue
                by_exp.setdefault(m["close_time"], []).append(m)
            for exp in sorted(by_exp)[: self.cfg.expiries_per_asset]:
                near = sorted(by_exp[exp], key=lambda m: abs(float(m["floor_strike"]) - spot))
                for m in near[: self.cfg.strikes_per_expiry]:
                    out.append(Mkt(m["ticker"], "crypto_" + sym[:3].lower(), series, m["event_ticker"],
                                   _dt(m["close_time"]), strike=float(m["floor_strike"]), symbol=sym))
        return out

    async def _universe(self):
        while not self._stop.is_set():
            try:
                fn = self._discover_crypto if self.cfg.kind == "crypto" else self._discover_niche
                found = await asyncio.to_thread(fn)
                keep = {t: m for t, m in self.mkts.items() if any(a.held(t) for a in self.arms)}
                fresh = {m.ticker: self.mkts.get(m.ticker, m) for m in found}
                self.mkts = {**fresh, **keep}
                self.stream.set_tickers(self.mkts)
                log.info("universe: %d markets (%d held outside it)", len(self.mkts), len(keep.keys() - fresh.keys()))
            except Exception:
                log.exception("universe refresh failed")
            try:
                await asyncio.wait_for(self._stop.wait(), self.cfg.universe_refresh_s)
            except asyncio.TimeoutError:
                pass

    # ---- per-market decision ----
    def _pulled(self, m: Mkt, now: datetime) -> bool:
        if now >= m.close_time:
            return True
        return self.cfg.kind == "crypto" and (m.close_time - now).total_seconds() < self.cfg.pull_before_close_s

    def _mode(self, arm: Arm, m: Mkt, now: datetime) -> str:
        if self.cfg.kind == "crypto":
            return REDUCE_ONLY if arm.killed else TWO_SIDED
        # v1 flattened across the spread in all of these; v2 only stops adding.
        win = compute_window(m.ticker, m.subsector, m.close_time, now)
        tune = get_tuning(m.subsector)
        hrs = (m.close_time - now).total_seconds() / 3600
        if (arm.killed or win.state in ("EXIT", "CLOSED") or is_in_blackout(m.subsector, now.hour, now.weekday())
                or is_subsector_blacked_out_by_calendar(m.subsector, now)[0]
                or (tune.skip_if_close_within_hours and hrs < tune.skip_if_close_within_hours)):
            return REDUCE_ONLY
        return QUIET if win.state == "QUIET" else TWO_SIDED

    def _delta_by_symbol(self, arm: Arm) -> dict[str, float]:
        """$ PnL for a +1% spot move, summed over every held strike of each underlying."""
        out: dict[str, float] = {}
        now = time.time()
        for t, pos in arm.portfolio.positions.items():
            m = self.mkts.get(t)
            if not m or not m.symbol or not pos.yes_contracts:
                continue
            S, sig = self.spot.mid.get(m.symbol), self.spot.vol[m.symbol].annual
            if not S:
                continue
            te = twap_t_eff(max(m.close_time.timestamp() - now, 0.0))
            d = p_above(S * 1.01, m.strike, te, sig) - p_above(S, m.strike, te, sig)
            out[m.symbol] = out.get(m.symbol, 0.0) + pos.yes_contracts * d
        return out

    def _fair(self, m: Mkt, book, now: float) -> tuple[str | None, float | None, float]:
        """(gate, fair value cents, sigma cents). Once per market per step, shared by every arm."""
        mid = book.mid_c
        if self.cfg.kind == "niche":
            fv = book.impact_mid(self.cfg.impact_depth)
            if fv is not None and now - m.last_var_t >= 60:
                m.fv_var.update(now, fv)
                m.last_var_t = now
            return None, fv, m.fv_var.sigma
        S = self.spot.mid.get(m.symbol)
        if not S or now - self.spot.updated.get(m.symbol, 0) > self.cfg.binance_stale_s:
            return "binance_stale", None, 0.0
        vol = self.spot.vol[m.symbol]
        if not vol.ready:
            return "vol_warmup", None, 0.0
        te = twap_t_eff(m.close_time.timestamp() - now)
        model = p_above(S, m.strike, te, vol.annual)
        m.anchor.update(now, mid / 100.0, model)
        v = m.anchor.value(model)
        if v is None:
            return "fv_unseeded", None, 0.0
        fv = v * 100.0
        if abs(fv - mid) > self.cfg.max_fv_gap_c:
            return "fv_gap", None, 0.0
        return None, fv, prob_sigma_c(S, m.strike, te, vol.annual, 10.0)

    def _quote(self, arm: Arm, m: Mkt, book, fv: float, sigma: float, now: float, now_dt: datetime,
               deltas: dict[str, float]):
        cfg = arm.cfg
        mode = self._mode(arm, m, now_dt)
        pos = arm.portfolio.position(m.ticker, m.subsector)
        pos.last_mid_dollars = book.mid_c / 100.0
        q = pos.yes_contracts / cfg.edge.q_max
        side_block: set[str] = set()
        if cfg.kind == "crypto":
            d = deltas.get(m.symbol, 0.0)
            q = 0.5 * q + 0.5 * max(-1.0, min(1.0, d / cfg.delta_cap_dollars))
            if d >= cfg.delta_cap_dollars:
                side_block.add("buy")
            if d <= -cfg.delta_cap_dollars:
                side_block.add("sell")
        else:
            gross = sum(abs(p.yes_contracts) for t, p in arm.portfolio.positions.items()
                        if t.rsplit("-", 1)[0] == m.event)
            if gross >= cfg.event_gross_cap:
                mode = REDUCE_ONLY
        days = (m.close_time - now_dt).total_seconds() / 86400
        bid, ask = desired_quotes(fv, sigma, pos.yes_contracts, q, book.best_bid, book.best_ask,
                                  days, mode, cfg.edge)
        arm.gates["quoting_" + mode] += 1
        for side, qt in (("buy", bid), ("sell", ask)):
            w = arm.venue.working(m.ticker, side)
            if qt is None or side in side_block:
                if w:
                    arm.venue.cancel(now, w.oid)
                continue
            if w is not None:
                if (abs(w.price_c - qt.price_c) >= cfg.replace_ticks or w.size != qt.size) \
                        and now - w.sent_t >= cfg.min_order_life_s:
                    arm.venue.cancel(now, w.oid)
                continue
            s = 1 if side == "buy" else -1
            adds = s * pos.yes_contracts >= 0
            inflight = arm.venue.pending(m.ticker, side)
            if adds and s * pos.yes_contracts + inflight + qt.size > cfg.edge.q_max:
                continue
            if not adds and inflight + qt.size > abs(pos.yes_contracts):
                continue
            arm.venue.place(now, m.ticker, side, qt.price_c, qt.size, qt.tactic, fv)

    def _pull(self, m: Mkt, now: float, gate: str):
        for arm in self.arms:
            arm.venue.cancel_ticker(now, m.ticker)
            arm.gates[gate] += 1

    def _step_market(self, m: Mkt, now: float, now_dt: datetime, deltas: dict[str, dict[str, float]]):
        if self._pulled(m, now_dt):
            return self._pull(m, now, PULLED)
        book = self.stream.books.get(m.ticker)
        if book is None or book.mid_c is None:
            return self._pull(m, now, "no_book" if book is None else "book_one_sided")
        for arm in self.arms:          # mark-to-mid even while a gate keeps the market quiet
            p = arm.portfolio.positions.get(m.ticker)
            if p is not None:
                p.last_mid_dollars = book.mid_c / 100.0
        blocked, fv, sigma = self._fair(m, book, now)
        if blocked:
            return self._pull(m, now, blocked)
        for arm in self.arms:
            self._quote(arm, m, book, fv, sigma, now, now_dt, deltas[arm.cfg.name])

    async def _decide(self):
        while not self._stop.is_set():
            now = time.time()
            now_dt = datetime.now(timezone.utc)
            slept = self.watch.check()
            if slept:
                self._on_wake(now, slept)
            for arm in self.arms:
                arm.venue.advance(now, self.stream.books)
            deltas = {a.cfg.name: (self._delta_by_symbol(a) if self.spot else {}) for a in self.arms}
            fresh = now - self.stream.last_msg < 30 and self.stream.connected_at > 0
            for m in list(self.mkts.values()):
                if fresh:
                    self._step_market(m, now, now_dt, deltas)
                else:
                    self._pull(m, now, "stream_stale")
            for arm in self.arms:
                self._markouts(arm, now)
                self._check_kill(arm)
            await asyncio.sleep(self.cfg.step_s)

    def _on_wake(self, now: float, slept: float):
        """The laptop was closed: a disconnect with cancel-on-disconnect. Resting paper
        orders are void, the books are re-snapshotted, and the fair values' memories
        (anchors, vol, fv variance) restart rather than read the gap as one huge move.
        Positions are kept; anything that resolved meanwhile settles on the next pass."""
        for arm in self.arms:
            arm.venue.orders.clear()
            arm.append("events.jsonl", {"t": now, "event": "wake", "slept_s": round(slept, 1)})
        self.stream.books = {}
        self.stream._resubscribe.set()
        for m in self.mkts.values():
            m.anchor = Anchor()
            m.fv_var = EWVar(1800.0, 1.0)
            m.last_var_t = 0.0
        if self.spot:
            for sym in list(self.spot.vol):
                self.spot.vol[sym] = SpotVol(sym)
                asyncio.get_running_loop().run_in_executor(None, self._seed_quietly, self.spot.vol[sym])
        log.info("woke after %.0fs asleep: paper orders voided, books and fair values reset", slept)

    @staticmethod
    def _seed_quietly(v: SpotVol):
        try:
            v.seed()
        except Exception as e:
            log.warning("vol re-seed %s failed (%s); it will warm from the live feed", v.symbol, e)

    def _check_kill(self, arm: Arm):
        pnl = sum(p.realized_pnl + p.unrealized_pnl(p.last_mid_dollars) for p in arm.portfolio.positions.values())
        if not arm.killed and pnl < -arm.cfg.max_loss_dollars:
            arm.killed = True
            log.error("KILL %s: session PnL $%.2f below -$%.2f; reduce-only everywhere",
                      arm.cfg.name, pnl, arm.cfg.max_loss_dollars)
            arm.append("events.jsonl", {"t": time.time(), "event": "kill", "pnl": pnl})

    # ---- fills ----
    def _on_print(self, pr: Print):
        m = self.mkts.get(pr.ticker)
        if m is None:
            return
        for arm in self.arms:
            for f in arm.venue.on_print(pr):
                pos = arm.portfolio.position(f.ticker, m.subsector)
                fee = self.fee_book.for_market(f.ticker, m.series).fee_dollars(f.price_c / 100.0, int(f.size), False)
                pos.add_fill(Fill(ts=datetime.fromtimestamp(f.t, timezone.utc).isoformat(), ticker=f.ticker,
                                  side="yes", action=f.side, count=int(f.size), price_dollars=f.price_c / 100.0,
                                  order_id=f"v2-{f.oid}", fee_dollars=fee, is_taker=False))
                book = self.stream.books.get(f.ticker)
                arm.pending_markouts.append({
                    "arm": arm.cfg.name, "t": f.t, "ticker": f.ticker, "subsector": m.subsector,
                    "side": f.side, "price_c": f.price_c, "size": f.size, "fee": fee, "tactic": f.tactic,
                    "fv_at_place_c": f.fv_at_place_c, "age_s": f.t - f.placed_t,
                    "mid_c": book.mid_c if book else None, "position": pos.yes_contracts,
                    "hours_to_close": (m.close_time.timestamp() - f.t) / 3600, "markouts": {}})
                log.info("FILL %s %s %s %d @ %dc (%s) -> pos %d", arm.cfg.name, f.ticker, f.side, f.size,
                         f.price_c, f.tactic, pos.yes_contracts)

    def _markouts(self, arm: Arm, now: float):
        keep = []
        for row in arm.pending_markouts:
            for h in MARKOUT_S:
                if str(h) in row["markouts"] or now < row["t"] + h:
                    continue
                b = self.stream.books.get(row["ticker"])
                # A mid read after the laptop slept through the horizon is not a markout.
                mid = b.mid_c if b and now - (row["t"] + h) <= 5.0 else None
                s = 1 if row["side"] == "buy" else -1
                row["markouts"][str(h)] = None if mid is None else s * (mid - row["price_c"])
            (arm.append("fills.jsonl", row) if len(row["markouts"]) == len(MARKOUT_S) else keep.append(row))
        arm.pending_markouts = keep

    # ---- settlement ----
    def _settle_once(self):
        now = datetime.now(timezone.utc)
        results: dict[str, str | None] = {}
        for arm in self.arms:
            for t, pos in list(arm.portfolio.positions.items()):
                m = self.mkts.get(t)
                if not pos.yes_contracts or (m and now < m.close_time):
                    continue
                if t not in results:
                    try:
                        results[t] = (self.client.get_market(t).get("market") or {}).get("result")
                    except Exception as e:
                        log.warning("settle lookup %s: %s", t, e)
                        results[t] = None
                if results[t] not in ("yes", "no"):
                    continue
                px = 1.0 if results[t] == "yes" else 0.0
                qty = pos.yes_contracts
                pos.add_fill(Fill(ts=now.isoformat(), ticker=t, side="yes", action="sell" if qty > 0 else "buy",
                                  count=abs(qty), price_dollars=px, order_id="SETTLE"))
                pos.last_mid_dollars = px
                arm.append("settlements.jsonl", {"t": time.time(), "ticker": t, "result": results[t],
                                                 "contracts": qty, "realized_after": pos.realized_pnl})
                log.info("SETTLED %s %s %s: %+d contracts, market realized $%.2f", arm.cfg.name, t,
                         results[t], qty, pos.realized_pnl)
        for t, r in results.items():
            if r in ("yes", "no") and not any(a.held(t) for a in self.arms):
                self.mkts.pop(t, None)

    async def _housekeeping(self):
        while not self._stop.is_set():
            try:
                await asyncio.to_thread(self._settle_once)
            except Exception:
                log.exception("settlement pass failed")
            for arm in self.arms:
                save_portfolio(arm.portfolio, arm.data / "portfolio.json")
                self._write_status(arm)
            try:
                await asyncio.wait_for(self._stop.wait(), 60)
            except asyncio.TimeoutError:
                pass

    def _write_status(self, arm: Arm):
        pf = arm.portfolio
        doc = {"t": time.time(), "arm": arm.cfg.name, "latency_s": arm.cfg.latency_s, "markets": len(self.mkts),
               "books": len(self.stream.books), "ws_gaps": self.stream.gaps,
               "last_ws_msg_age_s": time.time() - self.stream.last_msg if self.stream.last_msg else None,
               "open_orders": len(arm.venue.orders), "killed": arm.killed,
               "realized": pf.realized_pnl_total(), "fees": pf.fees_paid_total(),
               "positions": sum(1 for p in pf.positions.values() if p.yes_contracts),
               "gates": dict(arm.gates)}
        tmp = arm.data / "status.json.tmp"
        tmp.write_text(json.dumps(doc, indent=1))
        tmp.replace(arm.data / "status.json")

    async def run(self):
        if self.spot:
            await asyncio.to_thread(self.spot.seed)
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, self._stop.set)
        tasks = []
        if self.spot:
            tasks.append(asyncio.create_task(self.spot.run()))
            # Crypto discovery needs a spot price to pick strikes near the money.
            while not self.spot.mid and not self._stop.is_set():
                await asyncio.sleep(0.5)
        tasks += [asyncio.create_task(c) for c in
                  (self.stream.run(), self._universe(), self._decide(), self._housekeeping())]
        await self._stop.wait()
        log.info("stopping")
        self.stream.stop()
        if self.spot:
            self.spot.stop()
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        for arm in self.arms:
            for row in arm.pending_markouts:
                arm.append("fills.jsonl", row)
            save_portfolio(arm.portfolio, arm.data / "portfolio.json")
