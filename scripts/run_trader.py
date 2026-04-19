#!/usr/bin/env python3
"""Trader entry point.

Default: paper mode. Requires --live flag to place real orders (and a key with
trade scope). Live mode additionally requires user to type 'GO' at the prompt.

Usage:
  python scripts/run_trader.py                  # paper, forever
  python scripts/run_trader.py --duration 3600  # paper, one hour
  python scripts/run_trader.py --live           # LIVE - real orders
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.config import Config
from pmm.kalshi.client import KalshiClient
from pmm.trader.config import TraderConfig
from pmm.trader.runner import TraderRunner


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="REAL ORDERS. Default is paper.")
    ap.add_argument("--duration", type=float, default=None, help="run time in seconds (default forever)")
    ap.add_argument("--capital", type=float, default=100.0, help="starting capital in dollars")
    ap.add_argument("--subsectors", nargs="*", default=None, help="override target subsectors")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )

    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)

    # Load series list; used to map tickers to subsectors
    series_path = cfg.data_dir / "series.parquet"
    if not series_path.exists():
        print("error: research/data/series.parquet missing. Run scripts/fast_scan.py first.")
        return 1
    series_df = pd.read_parquet(series_path)
    series_df["subsector"] = series_df.apply(lambda r: classify(r["ticker"] or "", r["title"] or ""), axis=1)

    tcfg = TraderConfig(dry_run=not args.live)
    # capital override
    if args.capital != tcfg.risk.capital_dollars:
        from dataclasses import replace
        tcfg = replace(tcfg, risk=replace(tcfg.risk, capital_dollars=args.capital))
    if args.subsectors:
        from dataclasses import replace
        tcfg = replace(tcfg, target_subsectors=tuple(args.subsectors))

    if args.live:
        print("=" * 60)
        print("LIVE MODE: real orders will be placed with real money.")
        print(f"  Capital: ${tcfg.risk.capital_dollars:.2f}")
        print(f"  Per-market cap: ${tcfg.risk.capital_dollars * tcfg.risk.per_market_frac:.2f}")
        print(f"  Subsectors: {tcfg.target_subsectors}")
        print(f"  Key ID: {cfg.key_id}")
        print("=" * 60)
        print("Checking account balance...")
        try:
            bal = client.get("/portfolio/balance")
            print(f"  balance: {bal}")
        except Exception as e:
            print(f"  BALANCE CHECK FAILED: {e}")
            print("  (key may not have trade scope)")
            return 2
        confirm = input("Type exactly 'GO' to start live trading: ")
        if confirm != "GO":
            print("aborted.")
            return 3

    state_path = cfg.data_dir / "trader_state" / ("portfolio_live.json" if args.live else "portfolio_paper.json")

    runner = TraderRunner(tcfg=tcfg, client=client, state_path=state_path, series_df=series_df)
    runner.run(duration_seconds=args.duration)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
