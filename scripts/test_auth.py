#!/usr/bin/env python3
"""Sanity check: can we authenticate and read from Kalshi?

Hits /exchange/status (authed), then tries /markets with a small limit.
"""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.config import Config
from pmm.kalshi.client import KalshiAPIError, KalshiClient


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    cfg = Config.from_env()
    print(f"base_url: {cfg.base_url}")
    print(f"key_id:   {cfg.key_id}")
    print(f"pem:      {cfg.private_key_path}")

    client = KalshiClient.from_config(cfg)

    try:
        status = client.exchange_status()
        print("\n/exchange/status ->")
        print(json.dumps(status, indent=2))
    except KalshiAPIError as e:
        print(f"\nAUTH FAILED on /exchange/status: {e}")
        return 1

    try:
        markets = client.list_markets(status="open", limit=3)
        print("\n/markets?status=open&limit=3 ->")
        # don't dump entire payload; just counts + first ticker
        items = markets.get("markets", [])
        print(f"returned {len(items)} markets")
        for m in items:
            print(f"  {m.get('ticker'):<40} event={m.get('event_ticker'):<25} "
                  f"last={m.get('last_price')} yes_bid={m.get('yes_bid')} "
                  f"yes_ask={m.get('yes_ask')}")
    except KalshiAPIError as e:
        print(f"\nAUTH FAILED on /markets: {e}")
        return 2

    print("\nauth OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
