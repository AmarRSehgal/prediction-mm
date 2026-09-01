"""Main trading loop.

Wiring:
  universe.discover_markets -> schedule.compute_window -> quoter.compute_quote
  -> risk.assess_market -> executor.{cancel_all, place_order}
  -> poll for fills -> persist portfolio state
  Every cycle. Forever until SIGTERM.
"""
from __future__ import annotations

import logging
import signal
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from pmm.config import Config
from pmm.kalshi.client import KalshiClient
from pmm.trader.config import TraderConfig
from pmm.trader.executor import LiveExecutor, OrderIntent, PaperExecutor
from pmm.trader.position import Portfolio, load_portfolio, save_portfolio
from pmm.trader.quoter import compute_quote
from pmm.trader.risk import assess_market
from pmm.trader.schedule import compute_window
from pmm.trader.events_calendar import is_subsector_blacked_out_by_calendar
from pmm.trader.subsector_tuning import get as get_tuning, is_in_blackout
from pmm.trader.universe import discover_markets

log = logging.getLogger(__name__)


def _sigma_cents_proxy(subsector: str) -> float:
    """Rough per-subsector realized-vol estimate in cents per trade.
    Derived from earlier comp analysis mean_abs_consecutive_move_c."""
    table = {
        "sports_baseball_kbo": 8.6,
        "sports_baseball_npb": 5.2,
        "sports_cricket_psl": 4.0,
        "sports_cricket_odi": 3.0,
    }
    return table.get(subsector, 5.0)


class TraderRunner:
    def __init__(self, tcfg: TraderConfig, client: KalshiClient, state_path: Path, series_df: pd.DataFrame):
        self.tcfg = tcfg
        self.client = client
        self.state_path = state_path
        self.series_df = series_df
        self.portfolio = load_portfolio(state_path, starting_cash=tcfg.risk.capital_dollars)
        if tcfg.dry_run:
            self.executor = PaperExecutor(portfolio=self.portfolio, client=client)
        else:
            self.executor = LiveExecutor(client=client, portfolio=self.portfolio)
        self._stop = False
        self._adverse_fills = 0
        # Trend detector: rolling mid history per ticker.
        from collections import deque
        self._mid_history: dict[str, deque] = {}
        self._MID_HISTORY_MAX = 30
        # Cache for per-subsector tuning to avoid recomputation
        from pmm.trader.subsector_tuning import TUNING
        sub_tuning_cache = {}  # kept local; populated in run()
        # Universe cache: discover_markets is expensive (O(N series) API calls).
        # Cache the result and only refresh every ~300s.
        self._universe_cache: list = []
        self._universe_cached_at: float = 0.0
        self._universe_refresh_seconds: float = 300.0

    def _install_signals(self):
        def _h(signum, frame):
            log.info("signal %s received, stopping", signum)
            self._stop = True
        signal.signal(signal.SIGINT, _h)
        signal.signal(signal.SIGTERM, _h)

    def flatten_market(self, ticker: str, subsector: str,
                       mid: float, yes_bid: float | None = None, yes_ask: float | None = None) -> None:
        """Cross the spread to exit inventory. In paper mode we simulate a taker
        fill at the appropriate TOB price; in live mode we place a marketable
        limit order."""
        pos = self.portfolio.position(ticker, subsector)
        qty = pos.yes_contracts
        if qty == 0:
            return
        if isinstance(self.executor, PaperExecutor):
            # Simulate: we TAKE the existing bid (to sell) or ask (to buy).
            # Price we receive: yes_bid (if long exit) or yes_ask (if short exit).
            from pmm.trader.position import Fill
            import uuid
            from datetime import datetime, timezone
            exit_price = None
            if qty > 0:
                # Sell qty at yes_bid (conservative: assume we hit the bid)
                exit_price = yes_bid if yes_bid is not None else mid - 0.01
                action = "sell"
            else:
                exit_price = yes_ask if yes_ask is not None else mid + 0.01
                action = "buy"
            fill = Fill(
                ts=datetime.now(tz=timezone.utc).isoformat(),
                ticker=ticker, side="yes", action=action,
                count=abs(qty), price_dollars=exit_price,
                order_id=f"paper-flatten-{uuid.uuid4()}",
            )
            pos.add_fill(fill)
            log.info("PAPER FLATTEN %s: %s %d contracts @ $%.2f -> inv=%d realized=$%.4f",
                     ticker, action, abs(qty), exit_price, pos.yes_contracts, pos.realized_pnl)
            return
        # Live: place a marketable limit at the far side
        if qty > 0:
            intent = OrderIntent(ticker=ticker, side="yes", action="sell",
                                 count=abs(qty), price_cents=max(1, int(mid * 100) - 2), post_only=False)
        else:
            intent = OrderIntent(ticker=ticker, side="yes", action="buy",
                                 count=abs(qty), price_cents=min(99, int(mid * 100) + 2), post_only=False)
        self.executor.place_order(intent, subsector)

    def run(self, duration_seconds: float | None = None) -> None:
        self._install_signals()
        t0 = time.monotonic()
        cycle = 0
        log.info("starting trader: dry_run=%s capital=$%.2f targets=%s",
                 self.tcfg.dry_run, self.tcfg.risk.capital_dollars, self.tcfg.target_subsectors)

        while not self._stop:
            cycle_start = time.monotonic()
            cycle += 1

            # 1. Universe (cached — refresh every _universe_refresh_seconds)
            if (time.monotonic() - self._universe_cached_at) > self._universe_refresh_seconds or not self._universe_cache:
                try:
                    universe = discover_markets(
                        self.client, self.tcfg.target_subsectors, self.series_df,
                    )
                    self._universe_cache = universe
                    self._universe_cached_at = time.monotonic()
                except Exception:
                    log.exception("universe discovery failed")
                    time.sleep(self.tcfg.risk.quote_refresh_seconds)
                    continue
            else:
                universe = self._universe_cache

            mids = {m.ticker: m.mid for m in universe}
            now = datetime.now(tz=timezone.utc)

            # 2. Kill switch check
            total_pnl = self.portfolio.realized_pnl_total()
            killed = total_pnl <= -self.tcfg.risk.daily_stop_loss_dollars

            # Per-subsector drawdown halts (2026-04-22): compute cumulative
            # realized + unrealized per subsector. If below threshold, halt
            # placement for the whole subsector.
            _sub_pnl: dict[str, float] = {}
            for _t, _p in self.portfolio.positions.items():
                _r = _p.realized_pnl
                _u = _p.yes_contracts * (mids.get(_t, _p.last_mid_dollars) - _p.avg_cost_dollars) if _p.yes_contracts != 0 else 0.0
                _sub_pnl[_p.subsector] = _sub_pnl.get(_p.subsector, 0.0) + _r + _u
            halted_subs = {
                s: v for s, v in _sub_pnl.items()
                if v < get_tuning(s).halt_subsector_drawdown_dollars
            }
            if halted_subs:
                for s, v in halted_subs.items():
                    log.warning("HALT subsector %s: pnl=$%.2f below threshold", s, v)
            if killed:
                log.warning("KILL SWITCH: realized PnL %.2f <= -%.2f", total_pnl, self.tcfg.risk.daily_stop_loss_dollars)

            # 3. Per-market processing
            last_save = time.monotonic()
            for m in universe:
                win = compute_window(
                    m.ticker, m.subsector, m.close_time, now,
                    exit_tte_hours=self.tcfg.schedule.exit_tte_hours,
                    widen_tte_hours=self.tcfg.schedule.widen_tte_hours,
                    min_age_hours=self.tcfg.schedule.min_age_hours,
                )
                pos = self.portfolio.position(m.ticker, m.subsector)
                # Persist current mid for mark-to-market in the PnL tracker
                pos.last_mid_dollars = m.mid

                # Exit / closed: cancel and flatten
                if win.state in ("EXIT", "CLOSED"):
                    self.executor.cancel_all(m.ticker)
                    if pos.yes_contracts != 0 and win.state == "EXIT":
                        self.flatten_market(m.ticker, m.subsector, m.mid,
                                             yes_bid=m.yes_bid, yes_ask=m.yes_ask)
                    continue

                # Per-subsector UTC-hour blackout (scheduled release / open / close).
                # ENHANCED 2026-04-22: on blackout, also flatten existing inventory
                # (not just cancel quotes). Wednesday overnight showed ent_music
                # -$12 bleed during Tuesday blackout because rule C realized
                # losses on pre-blackout inventory at adverse prices. Active
                # flatten gets us out sooner at fresher prices.
                if is_in_blackout(m.subsector, now.hour, now.weekday()):
                    self.executor.cancel_all(m.ticker)
                    if pos.yes_contracts != 0:
                        self.flatten_market(m.ticker, m.subsector, m.mid,
                                             yes_bid=m.yes_bid, yes_ask=m.yes_ask)
                    continue

                # Calendar-based event blackout (known tournaments / earnings / releases)
                blocked, reason = is_subsector_blacked_out_by_calendar(m.subsector, now)
                if blocked:
                    self.executor.cancel_all(m.ticker)
                    if pos.yes_contracts != 0:
                        self.flatten_market(m.ticker, m.subsector, m.mid,
                                             yes_bid=m.yes_bid, yes_ask=m.yes_ask)
                    continue

                # Close-time proximity blackout (tournament-in-progress / settlement-pending)
                sub_tune = get_tuning(m.subsector)
                if sub_tune.skip_if_close_within_hours > 0 and m.close_time is not None:
                    hrs_to_close = (m.close_time - now).total_seconds() / 3600
                    if hrs_to_close < sub_tune.skip_if_close_within_hours:
                        self.executor.cancel_all(m.ticker)
                        continue

                # Dynamic price-discovery gate: pull recent trades, measure
                # mean abs consecutive-trade move in the last 1 hour. If it
                # exceeds the per-subsector threshold, skip quoting — the
                # market is in price-discovery mode (news, live event, etc).
                try:
                    tresp = self.client.get_trades(ticker=m.ticker, limit=50)
                    trades = tresp.get("trades", []) or []
                    from datetime import timedelta
                    cutoff = now - timedelta(hours=1)
                    recent = []
                    for t in trades:
                        ct = t.get("created_time")
                        if not ct:
                            continue
                        try:
                            ts = datetime.fromisoformat(ct.replace("Z", "+00:00"))
                        except Exception:
                            continue
                        if ts >= cutoff:
                            try:
                                px = float(t.get("yes_price_dollars") or 0)
                            except Exception:
                                continue
                            recent.append(px)
                    if len(recent) >= 3:
                        diffs = [abs(recent[i] - recent[i + 1]) * 100 for i in range(len(recent) - 1)]
                        mean_abs_move_c = sum(diffs) / len(diffs)
                        threshold = get_tuning(m.subsector).max_recent_vol_c
                        if mean_abs_move_c > threshold:
                            self.executor.cancel_all(m.ticker)
                            log.info("SKIP %s: recent vol %.2fc > threshold %.2fc (%d trades in last 1h)",
                                     m.ticker, mean_abs_move_c, threshold, len(recent))
                            continue
                except Exception:
                    pass

                # Risk assessment
                decision = assess_market(self.portfolio, m.ticker, m.subsector, m.mid, mids,
                                         self.tcfg.risk, kill=killed)

                # Compute quote
                sigma_c = _sigma_cents_proxy(m.subsector)
                # For QUIET, widen via shortened TTE fraction
                tte_hours_to_exit = (win.exit_at - now).total_seconds() / 3600 if win.exit_at else 12.0
                if win.state == "QUIET":
                    tte_hours_to_exit = min(tte_hours_to_exit, 6.0)  # force tighter/widened reservation
                # Idea 3 (2026-04-22): halve order size in QUIET pre-game
                # windows. Less exposure when informed flow likely arriving.
                if win.state == "QUIET" and decision.max_order_size > 1:
                    from dataclasses import replace as _replace
                    decision = _replace(decision, max_order_size=max(1, decision.max_order_size // 2))

                # Per-subsector gamma override
                sub_tuning = get_tuning(m.subsector)
                from dataclasses import replace
                as_params = replace(self.tcfg.as_params, gamma=sub_tuning.gamma)

                # Subsector drawdown halt: if this subsector is net below
                # threshold, skip new placement (but manage existing).
                sub_halted = m.subsector in halted_subs
                # Rule G: if pnl/fill is persistently bad, don't add inventory.
                # Existing position still gets fill-check + aggressive-close
                # (handled below). This flag only suppresses quote placement.
                rule_g_skip_place = False
                if sub_tuning.rule_g_enabled and len(pos.fills) >= sub_tuning.min_fills_for_pnl_check:
                    pnl_total = pos.realized_pnl + pos.yes_contracts * (m.mid - pos.avg_cost_dollars)
                    pnl_per_fill = pnl_total / len(pos.fills)
                    if pnl_per_fill < sub_tuning.min_pnl_per_fill:
                        rule_g_skip_place = True

                # Trend detector (test C): track rolling mid, compute z-score.
                # Suppress new placement if market is trending (not mean reverting).
                from collections import deque
                hist = self._mid_history.setdefault(m.ticker, deque(maxlen=self._MID_HISTORY_MAX))
                hist.append(m.mid)
                trend_skip_place = False
                if sub_tuning.trend_detector_enabled and len(hist) >= sub_tuning.trend_min_samples:
                    import statistics
                    mean = statistics.fmean(hist)
                    try:
                        stdev = statistics.pstdev(hist)
                    except statistics.StatisticsError:
                        stdev = 0.0
                    if stdev > 0.001:
                        z = (m.mid - mean) / stdev
                        if abs(z) > sub_tuning.trend_z_threshold:
                            trend_skip_place = True

                quote = compute_quote(
                    mid_dollars=m.mid,
                    inventory_contracts=pos.yes_contracts,
                    tte_hours_to_exit=max(tte_hours_to_exit, 1.0),
                    current_bid_dollars=m.yes_bid,
                    current_ask_dollars=m.yes_ask,
                    sigma_cents=sigma_c,
                    order_size=decision.max_order_size,
                    params=as_params,
                    min_spread_cents=self.tcfg.risk.min_spread_cents,
                )

                # IMPORTANT: check fills against OLD orders first. If we cancel
                # before checking, any trade in the inter-cycle gap gets skipped
                # because new orders have ts > trade ts.
                if isinstance(self.executor, PaperExecutor):
                    try:
                        ob = self.client.get_orderbook(m.ticker, depth=5)
                        book = ob.get("orderbook_fp") or {}
                        yes_levels = book.get("yes_dollars") or []
                        no_levels = book.get("no_dollars") or []
                        yes_tob_sz = float(yes_levels[-1][1]) if yes_levels else 0.0
                        no_tob_sz = float(no_levels[-1][1]) if no_levels else 0.0
                        self.executor.record_tob(m.ticker, yes_tob_sz, no_tob_sz)
                    except Exception:
                        pass
                    yb_c = int(round(m.yes_bid * 100))
                    ya_c = int(round(m.yes_ask * 100))
                    self.executor.try_fill_against(m.ticker, m.subsector, yb_c, ya_c)
                    # Stamp first-fill spread for PnL bucketing (sub-3c vs wider)
                    if pos.fills and pos.first_fill_spread_c is None:
                        pos.first_fill_spread_c = max(0, ya_c - yb_c)
                    # Aggressive close: take TOB to exit if profitable OR
                    # mid drifted adversely past cutoff.
                    if sub_tuning.close_aggressive_enabled and pos.yes_contracts != 0:
                        self.executor.try_aggressive_close(
                            m.ticker, m.subsector, pos,
                            m.yes_bid, m.yes_ask, m.mid,
                            sub_tuning.min_profit_c, sub_tuning.adverse_cutoff_c,
                        )
                    # Rule C: hold-time auto-close. If position's first fill was
                    # >= max_hold_minutes ago AND we still have inventory, force
                    # close by taking TOB. Targets the 30-180min dead-zone cohort.
                    if sub_tuning.rule_c_enabled and pos.yes_contracts != 0 and pos.fills:
                        try:
                            t_first = datetime.fromisoformat(pos.fills[0].ts.replace("Z","+00:00"))
                            hold_min = (now - t_first).total_seconds() / 60
                            if hold_min >= sub_tuning.max_hold_minutes:
                                self.executor.force_close(
                                    m.ticker, m.subsector, pos,
                                    m.yes_bid, m.yes_ask,
                                    f"rule_c hold={hold_min:.0f}min",
                                )
                        except Exception:
                            pass
                else:
                    self.executor.reconcile_fills(m.ticker, m.subsector)

                # Queue-depth gate: if our bid/ask is AT the TOB (joining, not
                # improving), skip that side if TOB queue is large relative to
                # our size. Prevents dead-queue 1c-spread markets.
                if isinstance(self.executor, PaperExecutor):
                    q_bid_size, q_ask_size = self.executor.tob_at_place.get(m.ticker, (0, 0))
                    max_ratio = sub_tuning.join_queue_max_ratio
                    # Bid side
                    if quote.bid_size > 0 and abs(quote.bid_price_dollars - m.yes_bid) < 0.005:
                        if q_bid_size > max_ratio * max(1, quote.bid_size):
                            quote = type(quote)(
                                bid_price_dollars=quote.bid_price_dollars,
                                ask_price_dollars=quote.ask_price_dollars,
                                bid_size=0, ask_size=quote.ask_size,
                                reservation_dollars=quote.reservation_dollars,
                                spread_cents=quote.spread_cents,
                            )
                    # Ask side
                    if quote.ask_size > 0 and abs(quote.ask_price_dollars - m.yes_ask) < 0.005:
                        if q_ask_size > max_ratio * max(1, quote.ask_size):
                            quote = type(quote)(
                                bid_price_dollars=quote.bid_price_dollars,
                                ask_price_dollars=quote.ask_price_dollars,
                                bid_size=quote.bid_size, ask_size=0,
                                reservation_dollars=quote.reservation_dollars,
                                spread_cents=quote.spread_cents,
                            )

                # Now cancel + repost (rule G suppresses repost only)
                self.executor.cancel_all(m.ticker)

                if sub_halted:
                    pass  # already logged at cycle start; don't spam per-market
                elif rule_g_skip_place:
                    log.info("SKIP G %s: pnl/fill bad after %d fills (existing position still managed)",
                             m.ticker, len(pos.fills))
                elif trend_skip_place:
                    log.info("SKIP TREND %s: |z|>%.1f (mid trending, not reverting)",
                             m.ticker, sub_tuning.trend_z_threshold)
                else:
                    if decision.can_quote_bid and quote.bid_size > 0:
                        intent = OrderIntent(
                            ticker=m.ticker, side="yes", action="buy",
                            count=quote.bid_size,
                            price_cents=int(round(quote.bid_price_dollars * 100)),
                            post_only=True,
                        )
                        self.executor.place_order(intent, m.subsector)
                    if decision.can_quote_ask and quote.ask_size > 0:
                        intent = OrderIntent(
                            ticker=m.ticker, side="yes", action="sell",
                            count=quote.ask_size,
                            price_cents=int(round(quote.ask_price_dollars * 100)),
                            post_only=True,
                        )
                        self.executor.place_order(intent, m.subsector)

                # Intra-cycle save every 60s so fills land on disk even when
                # a single cycle takes 10+ minutes over large universes.
                if time.monotonic() - last_save > 60.0:
                    save_portfolio(self.portfolio, self.state_path)
                    last_save = time.monotonic()

            # 4. Persist state
            save_portfolio(self.portfolio, self.state_path)

            # 5. Status log
            exposure = self.portfolio.total_exposure(mids)
            log.info("cycle %d: markets=%d total_exposure=$%.2f realized_pnl=$%.2f positions=%d",
                     cycle, len(universe), exposure, total_pnl,
                     sum(1 for p in self.portfolio.positions.values() if p.yes_contracts != 0))

            # 6. Sleep
            if duration_seconds is not None and time.monotonic() - t0 >= duration_seconds:
                break
            elapsed = time.monotonic() - cycle_start
            sleep_for = max(0.0, self.tcfg.risk.quote_refresh_seconds - elapsed)
            time.sleep(sleep_for)

        # On exit: cancel everything, save
        log.info("stopping: cancelling all orders")
        self.executor.cancel_all()
        save_portfolio(self.portfolio, self.state_path)
        log.info("done. final realized PnL = $%.2f", self.portfolio.realized_pnl_total())
