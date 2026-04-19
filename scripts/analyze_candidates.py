#!/usr/bin/env python3
"""Summarize collected snapshots and score markets by MM-ripeness."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.analysis.metrics import load_snapshots
from pmm.analysis.ranking import score_markets
from pmm.analysis.time_of_day import hour_of_week_stats
from pmm.config import Config


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--glob", default=None, help="override parquet glob")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--tod-ticker", default=None, help="dump time-of-day stats for this ticker")
    args = parser.parse_args()

    cfg = Config.from_env()
    glob = args.glob or str(cfg.data_dir / "orderbook" / "*" / "*.parquet")
    print(f"loading from: {glob}")

    df = load_snapshots(glob)
    if df.empty:
        print("no data yet")
        return 1
    print(f"loaded {len(df)} rows for {df['ticker'].nunique()} tickers, "
          f"time range {df['ts'].min()} -> {df['ts'].max()}")

    scored = score_markets(df)
    print(f"\ntop {args.top} by ripeness score:")
    print(scored.head(args.top).to_string(index=False))

    if args.tod_ticker:
        tod = hour_of_week_stats(df, args.tod_ticker)
        print(f"\ntime-of-day stats for {args.tod_ticker}:")
        print(tod.to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
