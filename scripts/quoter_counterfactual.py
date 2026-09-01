#!/usr/bin/env python3
"""What the fixed quoter and the fee model do to the recorded paper sessions.

Two questions, one cheap and one expensive:

  1. Which recorded markets would the fixed quoter REFUSE to quote at all?
     `first_fill_spread_c` records the TOB spread at our first fill in each
     market, which is exactly the input the refuse/quote decision turns on, so
     this half is a clean filter -- no simulation, no assumption.

  2. What would we have made on the markets it still quotes?
     Only answerable by replaying the tape against a quoter that posts at
     DIFFERENT prices, which this does not do. The passive line below is the
     PnL of the fills we actually got at the old (too tight) prices; a wider
     quote fills less often and captures more per fill. Read it as a sign and
     an order of magnitude, not a forecast.

Fees are applied per the real schedule; the recorded state predates the fee
model, so every number here is worse than the one in the session logs.

Usage:  python scripts/quoter_counterfactual.py [--state PATH]
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.config import Config
from pmm.trader.config import ASParams, RiskLimits
from pmm.trader.fees import FeeBook
from pmm.trader.position import Fill, MarketPosition
from pmm.trader.quoter import compute_quote

EXIT_PATHS = ("FORCE_CLOSE", "AGG_CLOSE", "paper-flatten")


def exit_path(order_id: str) -> str:
    for p in EXIT_PATHS:
        if order_id.startswith(p):
            return p
    return "passive"


def would_quote(spread_c: int, mid: float, params: ASParams, min_spread_c: int) -> bool:
    """Reconstruct a book of the recorded width around the recorded price and
    ask the real quoter whether it would post two-sided."""
    bid = round(mid - spread_c / 200, 2)
    ask = round(bid + spread_c / 100, 2)
    if bid <= 0 or ask >= 1:
        return False
    q = compute_quote(
        mid_dollars=(bid + ask) / 2, inventory_contracts=0, tte_hours_to_exit=12.0,
        current_bid_dollars=bid, current_ask_dollars=ask, sigma_cents=5.0,
        order_size=2, params=params, min_spread_cents=min_spread_c,
    )
    return bool(q.bid_size and q.ask_size)


def replay(positions, book: FeeBook, keep) -> tuple[int, dict]:
    """Re-run each kept position's fills through MarketPosition with fees, and
    attribute each realized-PnL step to the fill that caused it."""
    agg: dict[str, dict] = collections.defaultdict(lambda: {"n": 0, "pnl": 0.0})
    n_markets = 0
    for pos in positions:
        fills = pos.get("fills") or []
        if not fills or not keep(pos, fills):
            continue
        n_markets += 1
        mp = MarketPosition(ticker=pos["ticker"], subsector=pos["subsector"])
        sched = book.for_market(pos["ticker"])
        for f in fills:
            path = exit_path(f["order_id"])
            is_taker = path != "passive"
            price, count = float(f["price_dollars"]), int(f["count"])
            before = mp.realized_pnl
            mp.add_fill(Fill(
                ts=f["ts"], ticker=f["ticker"], side=f["side"], action=f["action"],
                count=count, price_dollars=price, order_id=f["order_id"],
                fee_dollars=sched.fee_dollars(price, count, is_taker), is_taker=is_taker,
            ))
            a = agg[path]
            a["n"] += 1
            a["pnl"] += mp.realized_pnl - before
    return n_markets, dict(agg)


def show(label: str, n_markets: int, agg: dict) -> float:
    total = sum(a["pnl"] for a in agg.values())
    fills = sum(a["n"] for a in agg.values())
    print(f"\n{label}  ({n_markets} markets, {fills} fills)")
    print(f"  {'exit path':<16}{'fills':>7}{'net PnL':>11}{'per fill':>11}")
    for path, a in sorted(agg.items(), key=lambda kv: kv[1]["pnl"]):
        print(f"  {path:<16}{a['n']:>7}{a['pnl']:>11.2f}{a['pnl'] / a['n'] * 100:>10.1f}c")
    print(f"  {'TOTAL':<16}{fills:>7}{total:>11.2f}")
    return total


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", default=None)
    args = ap.parse_args()

    cfg = Config.from_env()
    state = Path(args.state) if args.state else cfg.data_dir / "trader_state" / "portfolio_paper.json"
    data = json.loads(state.read_text())
    positions = list((data.get("positions") or {}).values())

    book = FeeBook()
    series_path = cfg.data_dir / "series.parquet"
    if series_path.exists():
        try:
            import pandas as pd
            book = FeeBook.from_series_frame(pd.read_parquet(series_path))
        except Exception:
            pass

    params, min_spread_c = ASParams(), RiskLimits().min_spread_cents
    print(f"state: {state}")
    print(f"quoter: gamma={params.gamma} k={params.k_order_arrival} "
          f"sigma_floor={params.sigma_floor_c}c min_spread={min_spread_c}c")

    def quotable(pos, fills):
        sp = pos.get("first_fill_spread_c")
        return (sp is not None and sp >= min_spread_c
                and would_quote(sp, float(fills[0]["price_dollars"]), params, min_spread_c))

    all_total = show("ALL recorded markets, fees applied", *replay(positions, book, lambda p, f: True))
    keep_total = show("Markets the FIXED quoter would still quote",
                      *replay(positions, book, quotable))
    drop_total = show("Markets the FIXED quoter now REFUSES",
                      *replay(positions, book, lambda p, f: not quotable(p, f)))

    print()
    print(f"Refusing the un-quotable books removes {drop_total:.2f} of the {all_total:.2f}.")
    print("On what is left, every forced/crossed exit line above is a mechanism that")
    print("is now disabled by default; the passive line is the only one that survives")
    print("both changes -- and per the header, it is a sign, not a forecast.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
