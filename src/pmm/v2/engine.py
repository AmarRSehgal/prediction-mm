"""v2 paper engine: one arm per process.

    niche   v1's target universe (TARGET_SUBSECTORS), book-mid fair value
    crypto  KXBTCD / KXETHD hourly strikes, Binance-anchored fair value

Per market, every step: pick a mode (two-sided / quiet / reduce-only / pulled),
run the gates, compute fair value and its volatility, ask the edge curve for two
passive quotes, and reconcile them against the paper venue. Fills come off the
pushed tape. Nothing ever crosses the spread; positions that are not quoted out
are held to resolution and settled at 0 or 100 from Kalshi's own result.

Everything an analysis needs is appended to <data>/fills.jsonl and
<data>/settlements.jsonl; portfolio.json is the same Portfolio format v1 writes.
"""
from __future__ import annotations

import asyncio
import json
import logging
import signal
import time
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from pmm.kalshi.client import KalshiClient
from pmm.trader.config import TARGET_SUBSECTORS
from pmm.trader.events_calendar import is_subsector_blacked_out_by_calendar
from pmm.trader.fees import FeeBook
from pmm.trader.position import Fill, load_portfolio, save_portfolio
from pmm.trader.schedule import compute_window
from pmm.trader.subsector_tuning import get as get_tuning, is_in_blackout
from pmm.trader.universe import discover_markets
from pmm.v2.fairvalue import Anchor, BinanceSpot, EWVar, p_above, prob_sigma_c, twap_t_eff
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


NICHE = ArmConfig("v2_niche", "niche", EdgeParams(), step_s=2.0, universe_refresh_s=900.0)
CRYPTO = ArmConfig("v2_crypto", "crypto",
                   EdgeParams(order_size=3, q_max=10, k_base_c=1.0, k_vol=1.0, k_skew_c=2.0,
                              band_lo_c=8, band_hi_c=92),
                   step_s=0.5, universe_refresh_s=300.0)


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


class Engine:
    def __init__(self, cfg: ArmConfig, client: KalshiClient, series_df: pd.DataFrame, data_dir: Path):
        cfg.edge.check()
        self.cfg, self.client, self.series_df = cfg, client, series_df
        self.data = data_dir
        self.data.mkdir(parents=True, exist_ok=True)
        self.fee_book = FeeBook.from_series_frame(series_df)
        self.portfolio = load_portfolio(self.data / "portfolio.json", starting_cash=cfg.capital_dollars)
        self.venue = PaperVenue()
        self.stream = KalshiStream(client, self._on_print)
        self.spot = BinanceSpot(tuple(CRYPTO_SERIES.values())) if cfg.kind == "crypto" else None
        self.mkts: dict[str, Mkt] = {}
        self.gates: Counter = Counter()
        self.pending_markouts: list[dict] = []
        self.killed = False
        self._stop = asyncio.Event()

    # ---- recording ----
    def _append(self, name: str, row: dict):
        with open(self.data / name, "a") as f:
            f.write(json.dumps(row, default=str) + "\n")

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
                keep = {t: m for t, m in self.mkts.items()
                        if self.portfolio.positions.get(t) and self.portfolio.positions[t].yes_contracts}
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
    def _mode(self, m: Mkt, now: datetime) -> str:
        if now >= m.close_time:
            return PULLED
        if self.cfg.kind == "crypto":
            if (m.close_time - now).total_seconds() < self.cfg.pull_before_close_s:
                return PULLED
            return REDUCE_ONLY if self.killed else TWO_SIDED
        # v1 flattened across the spread in all of these; v2 only stops adding.
        win = compute_window(m.ticker, m.subsector, m.close_time, now)
        tune = get_tuning(m.subsector)
        hrs = (m.close_time - now).total_seconds() / 3600
        if (self.killed or win.state in ("EXIT", "CLOSED") or is_in_blackout(m.subsector, now.hour, now.weekday())
                or is_subsector_blacked_out_by_calendar(m.subsector, now)[0]
                or (tune.skip_if_close_within_hours and hrs < tune.skip_if_close_within_hours)):
            return REDUCE_ONLY
        return QUIET if win.state == "QUIET" else TWO_SIDED

    def _delta_by_symbol(self) -> dict[str, float]:
        """$ PnL for a +1% spot move, summed over every held strike of each underlying."""
        out: dict[str, float] = {}
        now = time.time()
        for t, pos in self.portfolio.positions.items():
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
        """(gate, fair value cents, sigma cents)."""
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

    def _step_market(self, m: Mkt, now: float, now_dt: datetime, deltas: dict[str, float]):
        mode = self._mode(m, now_dt)
        book = self.stream.books.get(m.ticker)
        if mode == PULLED:
            self.venue.cancel_ticker(now, m.ticker)
            self.gates[PULLED] += 1
            return
        if book is None or book.mid_c is None:
            self.venue.cancel_ticker(now, m.ticker)
            self.gates["no_book" if book is None else "book_one_sided"] += 1
            return
        pos = self.portfolio.position(m.ticker, m.subsector)
        pos.last_mid_dollars = book.mid_c / 100.0
        blocked, fv, sigma = self._fair(m, book, now)
        if blocked:
            self.venue.cancel_ticker(now, m.ticker)
            self.gates[blocked] += 1
            return
        q = pos.yes_contracts / self.cfg.edge.q_max
        side_block: set[str] = set()
        if self.cfg.kind == "crypto":
            d = deltas.get(m.symbol, 0.0)
            q = 0.5 * q + 0.5 * max(-1.0, min(1.0, d / self.cfg.delta_cap_dollars))
            if d >= self.cfg.delta_cap_dollars:
                side_block.add("buy")
            if d <= -self.cfg.delta_cap_dollars:
                side_block.add("sell")
        else:
            gross = sum(abs(p.yes_contracts) for t, p in self.portfolio.positions.items()
                        if t.rsplit("-", 1)[0] == m.event)
            if gross >= self.cfg.event_gross_cap:
                mode = REDUCE_ONLY
        days = (m.close_time - now_dt).total_seconds() / 86400
        bid, ask = desired_quotes(fv, sigma, pos.yes_contracts, q, book.best_bid, book.best_ask,
                                  days, mode, self.cfg.edge)
        self.gates["quoting_" + mode] += 1
        for side, qt in (("buy", bid), ("sell", ask)):
            w = self.venue.working(m.ticker, side)
            if qt is None or side in side_block:
                if w:
                    self.venue.cancel(now, w.oid)
                continue
            if w is not None:
                if (abs(w.price_c - qt.price_c) >= self.cfg.replace_ticks or w.size != qt.size) \
                        and now - w.sent_t >= self.cfg.min_order_life_s:
                    self.venue.cancel(now, w.oid)
                continue
            s = 1 if side == "buy" else -1
            adds = s * pos.yes_contracts >= 0
            inflight = self.venue.pending(m.ticker, side)
            if adds and s * pos.yes_contracts + inflight + qt.size > self.cfg.edge.q_max:
                continue
            if not adds and inflight + qt.size > abs(pos.yes_contracts):
                continue
            self.venue.place(now, m.ticker, side, qt.price_c, qt.size, qt.tactic, fv)

    async def _decide(self):
        while not self._stop.is_set():
            now = time.time()
            now_dt = datetime.now(timezone.utc)
            self.venue.advance(now, self.stream.books)
            deltas = self._delta_by_symbol() if self.spot else {}
            fresh = now - self.stream.last_msg < 30 and self.stream.connected_at > 0
            for m in list(self.mkts.values()):
                if fresh:
                    self._step_market(m, now, now_dt, deltas)
                else:
                    self.venue.cancel_ticker(now, m.ticker)
                    self.gates["stream_stale"] += 1
            self._markouts(now)
            self._check_kill()
            await asyncio.sleep(self.cfg.step_s)

    def _check_kill(self):
        pnl = sum(p.realized_pnl + p.unrealized_pnl(p.last_mid_dollars) for p in self.portfolio.positions.values())
        if not self.killed and pnl < -self.cfg.max_loss_dollars:
            self.killed = True
            log.error("KILL: session PnL $%.2f below -$%.2f; reduce-only everywhere", pnl, self.cfg.max_loss_dollars)
            self._append("events.jsonl", {"t": time.time(), "event": "kill", "pnl": pnl})

    # ---- fills ----
    def _on_print(self, pr: Print):
        m = self.mkts.get(pr.ticker)
        if m is None:
            return
        for f in self.venue.on_print(pr):
            pos = self.portfolio.position(f.ticker, m.subsector)
            fee = self.fee_book.for_market(f.ticker, m.series).fee_dollars(f.price_c / 100.0, int(f.size), False)
            pos.add_fill(Fill(ts=datetime.fromtimestamp(f.t, timezone.utc).isoformat(), ticker=f.ticker,
                              side="yes", action=f.side, count=int(f.size), price_dollars=f.price_c / 100.0,
                              order_id=f"v2-{f.oid}", fee_dollars=fee, is_taker=False))
            book = self.stream.books.get(f.ticker)
            self.pending_markouts.append({
                "arm": self.cfg.name, "t": f.t, "ticker": f.ticker, "subsector": m.subsector,
                "side": f.side, "price_c": f.price_c, "size": f.size, "fee": fee, "tactic": f.tactic,
                "fv_at_place_c": f.fv_at_place_c, "age_s": f.t - f.placed_t,
                "mid_c": book.mid_c if book else None, "position": pos.yes_contracts,
                "hours_to_close": (m.close_time.timestamp() - f.t) / 3600, "markouts": {}})
            log.info("FILL %s %s %d @ %dc (%s) -> pos %d", f.ticker, f.side, f.size, f.price_c, f.tactic,
                     pos.yes_contracts)

    def _markouts(self, now: float):
        keep = []
        for row in self.pending_markouts:
            for h in MARKOUT_S:
                if str(h) in row["markouts"] or now < row["t"] + h:
                    continue
                b = self.stream.books.get(row["ticker"])
                mid = b.mid_c if b else None
                s = 1 if row["side"] == "buy" else -1
                row["markouts"][str(h)] = None if mid is None else s * (mid - row["price_c"])
            (self._append("fills.jsonl", row) if len(row["markouts"]) == len(MARKOUT_S) else keep.append(row))
        self.pending_markouts = keep

    # ---- settlement ----
    def _settle_once(self):
        now = datetime.now(timezone.utc)
        for t, pos in list(self.portfolio.positions.items()):
            m = self.mkts.get(t)
            if not pos.yes_contracts or (m and now < m.close_time):
                continue
            try:
                mk = self.client.get_market(t).get("market") or {}
            except Exception as e:
                log.warning("settle lookup %s: %s", t, e)
                continue
            if mk.get("result") not in ("yes", "no"):
                continue
            px = 1.0 if mk["result"] == "yes" else 0.0
            qty = pos.yes_contracts
            pos.add_fill(Fill(ts=now.isoformat(), ticker=t, side="yes", action="sell" if qty > 0 else "buy",
                              count=abs(qty), price_dollars=px, order_id="SETTLE"))
            pos.last_mid_dollars = px
            self._append("settlements.jsonl", {"t": time.time(), "ticker": t, "result": mk["result"],
                                               "contracts": qty, "realized_after": pos.realized_pnl})
            log.info("SETTLED %s %s: %+d contracts, market realized $%.2f", t, mk["result"], qty, pos.realized_pnl)
            self.mkts.pop(t, None)

    async def _housekeeping(self):
        while not self._stop.is_set():
            try:
                await asyncio.to_thread(self._settle_once)
            except Exception:
                log.exception("settlement pass failed")
            save_portfolio(self.portfolio, self.data / "portfolio.json")
            self._write_status()
            try:
                await asyncio.wait_for(self._stop.wait(), 60)
            except asyncio.TimeoutError:
                pass

    def _write_status(self):
        pf = self.portfolio
        doc = {"t": time.time(), "arm": self.cfg.name, "markets": len(self.mkts),
               "books": len(self.stream.books), "ws_gaps": self.stream.gaps,
               "last_ws_msg_age_s": time.time() - self.stream.last_msg if self.stream.last_msg else None,
               "open_orders": len(self.venue.orders), "killed": self.killed,
               "realized": pf.realized_pnl_total(), "fees": pf.fees_paid_total(),
               "positions": sum(1 for p in pf.positions.values() if p.yes_contracts),
               "gates": dict(self.gates)}
        tmp = self.data / "status.json.tmp"
        tmp.write_text(json.dumps(doc, indent=1))
        tmp.replace(self.data / "status.json")

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
        for row in self.pending_markouts:
            self._append("fills.jsonl", row)
        save_portfolio(self.portfolio, self.data / "portfolio.json")
