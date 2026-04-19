#!/usr/bin/env python3
"""Collect orderbook snapshots for a set of tickers.

Usage:
  python scripts/collect_snapshots.py --tickers T1 T2 T3 --interval 5 --duration 3600
  python scripts/collect_snapshots.py --tickers-file tickers.txt
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.collector.snapshot import SnapshotCollector
from pmm.config import Config
from pmm.kalshi.client import KalshiClient
from pmm.storage.parquet import OrderbookWriter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tickers", nargs="*", default=[])
    parser.add_argument("--tickers-file", default=None)
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument("--duration", type=float, default=None, help="seconds to run, None=forever")
    parser.add_argument("--depth", type=int, default=10)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    cfg = Config.from_env()

    tickers = list(args.tickers)
    if args.tickers_file:
        tickers.extend(
            line.strip()
            for line in Path(args.tickers_file).read_text().splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    if not tickers:
        parser.error("no tickers provided")

    client = KalshiClient.from_config(cfg)
    writer = OrderbookWriter(cfg.data_dir)
    collector = SnapshotCollector(
        client=client,
        writer=writer,
        tickers=tickers,
        interval_s=args.interval,
        depth=args.depth,
    )
    print(f"collecting {len(tickers)} tickers at {args.interval}s, writing to {cfg.data_dir}")
    collector.run(duration_s=args.duration)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
