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

    def _install_signals(self):
        def _h(signum, frame):
            log.info("signal %s received, stopping", signum)
            self._stop = True
        signal.signal(signal.SIGINT, _h)
        signal.signal(signal.SIGTERM, _h)

    def flatten_market(self, ticker: str, subsector: str, mid: float) -> None:
        """Cross the spread to exit inventory if we can't MM our way out."""
        pos = self.portfolio.position(ticker, subsector)
        qty = pos.yes_contracts
        if qty == 0:
            return
        if isinstance(self.executor, PaperExecutor):
            log.info("PAPER FLATTEN %s inv=%d at mid $%.2f (skipping real execution)", ticker, qty, mid)
            return
        # Live: place a marketable limit at the far side
        if qty > 0:
            # Sell YES at bid
            intent = OrderIntent(ticker=ticker, side="yes", action="sell",
                                 count=abs(qty), price_cents=max(1, int(mid * 100) - 2), post_only=False)
        else:
            # Buy YES at ask
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

            # 1. Universe
            try:
                universe = discover_markets(
                    self.client, self.tcfg.target_subsectors, self.series_df,
                )
            except Exception:
                log.exception("universe discovery failed")
                time.sleep(self.tcfg.risk.quote_refresh_seconds)
                continue

            mids = {m.ticker: m.mid for m in universe}
            now = datetime.now(tz=timezone.utc)

            # 2. Kill switch check
            total_pnl = self.portfolio.realized_pnl_total()
            killed = total_pnl <= -self.tcfg.risk.daily_stop_loss_dollars
            if killed:
                log.warning("KILL SWITCH: realized PnL %.2f <= -%.2f", total_pnl, self.tcfg.risk.daily_stop_loss_dollars)

            # 3. Per-market processing
            for m in universe:
                win = compute_window(
                    m.ticker, m.subsector, m.close_time, now,
                    exit_tte_hours=self.tcfg.schedule.exit_tte_hours,
                    widen_tte_hours=self.tcfg.schedule.widen_tte_hours,
                    min_age_hours=self.tcfg.schedule.min_age_hours,
                )
                pos = self.portfolio.position(m.ticker, m.subsector)

                # Exit / closed: cancel and flatten
                if win.state in ("EXIT", "CLOSED"):
                    self.executor.cancel_all(m.ticker)
                    if pos.yes_contracts != 0 and win.state == "EXIT":
                        self.flatten_market(m.ticker, m.subsector, m.mid)
                    continue

                # Risk assessment
                decision = assess_market(self.portfolio, m.ticker, m.subsector, m.mid, mids,
                                         self.tcfg.risk, kill=killed)

                # Compute quote
                sigma_c = _sigma_cents_proxy(m.subsector)
                # For QUIET, widen via shortened TTE fraction
                tte_hours_to_exit = (win.exit_at - now).total_seconds() / 3600 if win.exit_at else 12.0
                if win.state == "QUIET":
                    tte_hours_to_exit = min(tte_hours_to_exit, 6.0)  # force tighter/widened reservation

                quote = compute_quote(
                    mid_dollars=m.mid,
                    inventory_contracts=pos.yes_contracts,
                    tte_hours_to_exit=max(tte_hours_to_exit, 1.0),
                    current_bid_dollars=m.yes_bid,
                    current_ask_dollars=m.yes_ask,
                    sigma_cents=sigma_c,
                    order_size=decision.max_order_size,
                    params=self.tcfg.as_params,
                    min_spread_cents=self.tcfg.risk.min_spread_cents,
                )

                # Cancel-then-post cycle
                self.executor.cancel_all(m.ticker)

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

                # Fill simulation / reconciliation
                if isinstance(self.executor, PaperExecutor):
                    # Fetch TOB sizes to estimate queue position (via orderbook call).
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
                else:
                    self.executor.reconcile_fills(m.ticker, m.subsector)

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
