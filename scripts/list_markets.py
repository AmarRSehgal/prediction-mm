#!/usr/bin/env python3
"""Discovery: enumerate open markets, dump to CSV for inspection.

Use to pick candidate markets for the collector. Filters optionally by
series_ticker (e.g. weather) or event_ticker (specific event).

Usage:
  python scripts/list_markets.py                      # all open markets
  python scripts/list_markets.py --series KXHIGHNY    # only HIGHNY series
  python scripts/list_markets.py --out markets.csv
"""
from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.config import Config
from pmm.kalshi.client import KalshiClient


FIELDS = [
    "ticker",
    "event_ticker",
    "series_ticker",
    "title",
    "status",
    "open_time",
    "close_time",
    "expected_expiration_time",
    "last_price",
    "yes_bid",
    "yes_ask",
    "volume",
    "volume_24h",
    "liquidity",
    "open_interest",
    "category",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--series", help="filter by series_ticker")
    parser.add_argument("--event", help="filter by event_ticker")
    parser.add_argument("--status", default="open", choices=["open", "closed", "settled"])
    parser.add_argument("--limit", type=int, default=200, help="per-page limit (max 1000)")
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--out", default=None, help="write CSV to this path")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)

    kwargs: dict = {"status": args.status, "limit": args.limit}
    if args.series:
        kwargs["series_ticker"] = args.series
    if args.event:
        kwargs["event_ticker"] = args.event

    rows = list(client.paginate(client.list_markets, "markets", max_pages=args.max_pages, **kwargs))
    print(f"fetched {len(rows)} markets")

    out_path = Path(args.out) if args.out else cfg.data_dir / "markets_snapshot.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k) for k in FIELDS})
    print(f"wrote {out_path}")

    # Summary by series
    from collections import Counter

    by_series = Counter(r.get("series_ticker") or "(none)" for r in rows)
    print("\ntop series by market count:")
    for s, c in by_series.most_common(15):
        print(f"  {c:5d}  {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
