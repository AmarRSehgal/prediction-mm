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

# A market is only worth quoting if the book is at least this wide -- below it
# there is no room to post a two-sided quote at RiskLimits.min_spread_cents.
MIN_QUOTABLE_SPREAD = 0.03


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
            # Fee parameters are per-series and only obtainable here. The fee
            # book (pmm.trader.fees) is built off these two columns.
            "fee_type": s.get("fee_type") or "quadratic",
            "fee_multiplier": float(s.get("fee_multiplier") if s.get("fee_multiplier") is not None else 1.0),
            "subsector": classify(s.get("ticker") or "", s.get("title") or ""),
        }
        for s in all_series
    ])

    # series.parquet is what run_trader.py loads to map ticker -> subsector.
    # Nothing else in the repo wrote it, so it had gone stale by 4 months.
    (
        series_df.rename(columns={"series": "ticker"})
        [["ticker", "title", "category", "frequency", "fee_type", "fee_multiplier", "subsector"]]
        .to_parquet(cfg.data_dir / "series.parquet")
    )

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
    # The joint condition is what actually matters and neither half predicts it:
    # a market only pays if the book is wide enough to quote inside AND there is
    # flow to fill against. Most contested Kalshi markets have one or the other.
    mkt_df["is_quotable"] = con & (mkt_df["spread"] >= MIN_QUOTABLE_SPREAD - 1e-9)
    mkt_df["has_flow"] = con & (mkt_df["vol_24h"] > 0)
    mkt_df["is_tradeable"] = mkt_df["is_quotable"] & mkt_df["has_flow"]
    # Keep the raw per-market rows so this question can be re-asked without
    # another hour of API calls.
    mkt_df.to_parquet(cfg.data_dir / "sector_scan_markets.parquet")

    def agg(sub: pd.DataFrame) -> pd.Series:
        con_rows = sub[sub["is_contested"]]
        # Top-OI contested market stats (the REAL signal)
        top_oi = con_rows.sort_values("oi", ascending=False).head(3)
        flow_rows = sub[sub["has_flow"]]
        trade_rows = sub[sub["is_tradeable"]]
        return pd.Series({
            "n_markets": len(sub),
            "n_two_sided": int(sub["is_two_sided"].sum()),
            "n_contested": len(con_rows),
            "n_quotable": int(sub["is_quotable"].sum()),
            "n_flow": len(flow_rows),
            "n_tradeable": int(sub["is_tradeable"].sum()),
            "vol_24h_tradeable": float(trade_rows["vol_24h"].sum()),
            "median_spread_flow": float(flow_rows["spread"].median()) if len(flow_rows) else float("nan"),
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
    per_series = per_series.merge(
        series_df[["series", "title", "category", "frequency", "fee_type", "fee_multiplier", "subsector"]],
        on="series", how="left",
    )
    per_series.to_parquet(cfg.data_dir / "sector_scan_series.parquet")

    # ---- 4. per-subsector aggregation
    if len(per_series):
        def agg_sub(sub):
            return pd.Series({
                "n_series": len(sub),
                "n_series_with_open_markets": int((sub["n_markets"] > 0).sum()),
                "n_markets": int(sub["n_markets"].sum()),
                "n_contested": int(sub["n_contested"].sum()),
                "n_quotable": int(sub["n_quotable"].sum()),
                "n_flow": int(sub["n_flow"].sum()),
                "n_tradeable": int(sub["n_tradeable"].sum()),
                "vol_24h_tradeable": float(sub["vol_24h_tradeable"].sum()),
                "median_spread_flow": float(sub["median_spread_flow"].median(skipna=True)),
                "total_oi": float(sub["total_oi"].sum()),
                "total_vol_24h": float(sub["total_vol_24h"].sum()),
                "median_series_top_oi_spread": float(sub["top_oi_mean_spread"].median(skipna=True)),
                "mean_series_top_oi_spread": float(sub["top_oi_mean_spread"].mean(skipna=True)),
            })
        per_sub = per_series.groupby("subsector").apply(agg_sub, include_groups=False).reset_index()
        per_sub = per_sub.sort_values(["n_contested", "total_vol_24h"], ascending=[False, False])
        per_sub.to_parquet(cfg.data_dir / "sector_scan_subsector.parquet")

        # MM-opportunity score. The old score was mean spread * saturated
        # volume across ALL contested markets, which happily rewarded a
        # subsector whose wide markets are dead and whose live markets are 1c.
        # Score the markets that are BOTH quotable and traded, or nothing.
        per_sub["tradeable_frac"] = per_sub["n_tradeable"] / per_sub["n_contested"].replace(0, float("nan"))
        per_sub["mm_score"] = (
            per_sub["n_tradeable"]
            * per_sub["median_spread_flow"].fillna(0)
            * (per_sub["vol_24h_tradeable"].clip(upper=50000) / 50000)
        )
        per_sub = per_sub.sort_values("mm_score", ascending=False)

        cols = ["subsector", "n_contested", "n_quotable", "n_flow", "n_tradeable",
                "tradeable_frac", "median_spread_flow", "vol_24h_tradeable", "mm_score"]
        print(f"\n{'='*130}")
        print(f"SUB-SECTOR RANKING -- markets that are BOTH >= {MIN_QUOTABLE_SPREAD*100:.0f}c wide AND have 24h volume")
        print("=" * 130)
        print(per_sub[cols].head(45).to_string(index=False))

        print(f"\n{'='*130}")
        print("DEAD (wide spreads, no flow: n_quotable high, n_tradeable ~0)")
        print("=" * 130)
        dead = per_sub[(per_sub["n_quotable"] >= 10) & (per_sub["n_tradeable"] <= 1)]
        print(dead[cols].head(25).to_string(index=False))

        print(f"\n{'='*130}")
        print("PICKED OVER (flow exists but the book is tighter than we can quote)")
        print("=" * 130)
        picked = per_sub[(per_sub["n_flow"] >= 10) & (per_sub["tradeable_frac"] < 0.15)]
        print(picked.sort_values("n_flow", ascending=False)[cols].head(25).to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
