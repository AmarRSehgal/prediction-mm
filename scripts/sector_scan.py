#!/usr/bin/env python3
"""Full-universe sector scan.

Walks all Kalshi series, classifies each into a sub-sector, pulls open
markets per series, computes MM-signal stats per series and per sub-sector.

Output:
  research/data/sector_scan_series.parquet   # row-per-series stats
  research/data/sector_scan_subsector.parquet # aggregated by sub-sector
  prints a ranked table to stdout
"""
from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.config import Config
from pmm.kalshi.client import KalshiAPIError, KalshiClient


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    log = logging.getLogger("sector_scan")
    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)

    # ---- 1. all series
    log.info("fetching all series...")
    all_series = []
    cursor = None
    while True:
        kw = {"limit": 1000}
        if cursor:
            kw["cursor"] = cursor
        r = client.list_series(**kw)
        all_series.extend(r.get("series", []))
        cursor = r.get("cursor")
        if not cursor:
            break
    log.info("got %d series", len(all_series))

    series_df = pd.DataFrame([
        {
            "series": s.get("ticker"),
            "title": s.get("title"),
            "category": s.get("category"),
            "frequency": s.get("frequency"),
            "subsector": classify(s.get("ticker") or "", s.get("title") or ""),
        }
        for s in all_series
    ])

    # ---- 2. for each series, fetch open markets (single page, 200 max per series)
    log.info("fetching open markets per series (this takes a few minutes)...")
    rows = []
    t0 = time.time()
    skipped = 0
    for i, s in enumerate(series_df["series"].tolist()):
        if i % 200 == 0:
            log.info("  progress %d / %d (elapsed %.0fs, %d skipped)", i, len(series_df), time.time() - t0, skipped)
        try:
            r = client.list_markets(series_ticker=s, status="open", limit=200)
        except KalshiAPIError:
            skipped += 1
            continue
        except Exception:
            skipped += 1
            continue
        for m in r.get("markets", []) or []:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            rows.append({
                "series": s,
                "ticker": m.get("ticker"),
                "yes_bid": yb,
                "yes_ask": ya,
                "mid": (yb + ya) / 2,
                "spread": ya - yb,
                "vol_24h": float(m.get("volume_24h_fp") or 0),
                "oi": float(m.get("open_interest_fp") or 0),
                "last_price": float(m.get("last_price_dollars") or 0),
            })

    mkt_df = pd.DataFrame(rows)
    log.info("fetched %d open markets across series (skipped %d)", len(mkt_df), skipped)

    # ---- 3. per-series stats
    two = (mkt_df["yes_bid"] > 0) & (mkt_df["yes_ask"] < 1.0) & (mkt_df["yes_bid"] < mkt_df["yes_ask"])
    con = two & (mkt_df["mid"] >= 0.10) & (mkt_df["mid"] <= 0.90)
    mkt_df["is_two_sided"] = two
    mkt_df["is_contested"] = con

    def agg(sub: pd.DataFrame) -> pd.Series:
        con_rows = sub[sub["is_contested"]]
        # Top-OI contested market stats (the REAL signal)
        top_oi = con_rows.sort_values("oi", ascending=False).head(3)
        return pd.Series({
            "n_markets": len(sub),
            "n_two_sided": int(sub["is_two_sided"].sum()),
            "n_contested": len(con_rows),
            "total_oi": float(sub["oi"].sum()),
            "total_vol_24h": float(sub["vol_24h"].sum()),
            "median_spread_contested": float(con_rows["spread"].median()) if len(con_rows) else float("nan"),
            "top_oi_mean_spread": float(top_oi["spread"].mean()) if len(top_oi) else float("nan"),
            "top_oi_median_spread": float(top_oi["spread"].median()) if len(top_oi) else float("nan"),
            "top_oi_total_oi": float(top_oi["oi"].sum()) if len(top_oi) else 0.0,
            "top_oi_total_vol": float(top_oi["vol_24h"].sum()) if len(top_oi) else 0.0,
        })

    per_series = (
        mkt_df.groupby("series").apply(agg, include_groups=False).reset_index()
        if len(mkt_df) else pd.DataFrame(columns=["series"])
    )
    per_series = per_series.merge(series_df[["series", "title", "category", "frequency", "subsector"]], on="series", how="left")
    per_series.to_parquet(cfg.data_dir / "sector_scan_series.parquet")

    # ---- 4. per-subsector aggregation
    if len(per_series):
        def agg_sub(sub):
            return pd.Series({
                "n_series": len(sub),
                "n_series_with_open_markets": int((sub["n_markets"] > 0).sum()),
                "n_markets": int(sub["n_markets"].sum()),
                "n_contested": int(sub["n_contested"].sum()),
                "total_oi": float(sub["total_oi"].sum()),
                "total_vol_24h": float(sub["total_vol_24h"].sum()),
                "median_series_top_oi_spread": float(sub["top_oi_mean_spread"].median(skipna=True)),
                "mean_series_top_oi_spread": float(sub["top_oi_mean_spread"].mean(skipna=True)),
            })
        per_sub = per_series.groupby("subsector").apply(agg_sub, include_groups=False).reset_index()
        per_sub = per_sub.sort_values(["n_contested", "total_vol_24h"], ascending=[False, False])
        per_sub.to_parquet(cfg.data_dir / "sector_scan_subsector.parquet")

        # MM-opportunity score: want HIGH top-oi-spread AND non-trivial volume
        # Dead subsectors have high spread but $0 volume - penalize those
        per_sub["mm_score"] = (
            per_sub["mean_series_top_oi_spread"].fillna(0)
            * (per_sub["total_vol_24h"].clip(upper=50000) / 50000)  # saturation at $50K
        )
        per_sub = per_sub.sort_values("mm_score", ascending=False)

        print(f"\n{'='*120}")
        print("SUB-SECTOR RANKING (by MM opportunity score: spread * log-saturated-volume)")
        print("='*120")
        cols = ["subsector","n_series_with_open_markets","n_markets","n_contested",
                "total_vol_24h","mean_series_top_oi_spread","mm_score"]
        print(per_sub[cols].head(40).to_string(index=False))

        print(f"\n{'='*120}")
        print("DEAD SUB-SECTORS (wide spread but no volume)")
        print("='*120")
        dead = per_sub[(per_sub["mean_series_top_oi_spread"] > 0.2) & (per_sub["total_vol_24h"] < 100)]
        print(dead[cols].head(20).to_string(index=False))

        print(f"\n{'='*120}")
        print("HFT-SATURATED SUB-SECTORS (tight spread and high volume)")
        print("='*120")
        hft = per_sub[(per_sub["mean_series_top_oi_spread"] < 0.03) & (per_sub["total_vol_24h"] > 1000)]
        print(hft[cols].head(20).to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
