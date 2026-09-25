#!/usr/bin/env python3
"""v2 paper engine entry point. Paper only: there is no order path in pmm.v2.

  env -u PYTHONPATH /opt/local/bin/python3.13 scripts/run_v2.py --arm crypto
  env -u PYTHONPATH /opt/local/bin/python3.13 scripts/run_v2.py --arm niche

State and the fill/settlement record go to research/data/ab/<arm>/ unless
--data-dir says otherwise; point a smoke test somewhere else.
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.config import Config
from pmm.kalshi.client import KalshiClient
from pmm.v2.engine import CRYPTO, NICHE, Engine


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=("crypto", "niche"), required=True)
    ap.add_argument("--data-dir", default=None)
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
    for noisy in ("websockets", "urllib3"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)
    series_path = cfg.data_dir / "series.parquet"
    if not series_path.exists():
        print("error: research/data/series.parquet missing. Run scripts/fast_scan.py first.")
        return 1
    series_df = pd.read_parquet(series_path)
    series_df["subsector"] = series_df.apply(lambda r: classify(r["ticker"] or "", r["title"] or ""), axis=1)
    arm = CRYPTO if args.arm == "crypto" else NICHE
    data = Path(args.data_dir) if args.data_dir else cfg.data_dir / "ab" / arm.name
    asyncio.run(Engine(arm, client, series_df, data).run())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
