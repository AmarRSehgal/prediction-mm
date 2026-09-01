#!/usr/bin/env python3
"""Deep-dive per subsector: orderbook depth + informed-flow from trade history.

For each subsector with open markets:
  - pick top-3 series by contested-market count x total_oi
  - per series, pick top-3 markets by OI
  - pull current orderbook (depth=50)
  - pull last 500 trades
  - compute depth and trade metrics
  - aggregate to subsector

Output:
  research/data/subsector_depth_markets.parquet
  research/data/subsector_depth_summary.parquet
"""
from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.analysis.depth_metrics import depth_metrics, trade_metrics
from pmm.config import Config
from pmm.kalshi.client import KalshiClient


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    log = logging.getLogger("depth_analysis")

    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)

    scan_path = cfg.data_dir / "sector_scan_series.parquet"
    if not scan_path.exists():
        log.error("sector scan output missing at %s - run scripts/sector_scan.py first", scan_path)
        return 1

    series_df = pd.read_parquet(scan_path)
    log.info("loaded %d series from sector scan", len(series_df))

    active_subs = (
        series_df[(series_df["n_markets"].fillna(0) > 0) & (series_df["n_contested"].fillna(0) > 0)]
        .copy()
    )
    active_subs["rank_score"] = active_subs["n_contested"] * (active_subs["total_oi"].fillna(0) + 1).pipe(lambda s: s.pow(0.5))
    log.info("%d series with contested markets across %d subsectors",
             len(active_subs), active_subs["subsector"].nunique())

    # Top-3 series per subsector
    top_series_per_sub = (
        active_subs.sort_values(["subsector", "rank_score"], ascending=[True, False])
        .groupby("subsector")
        .head(3)
    )
    log.info("selected %d series across %d subsectors for deep dive",
             len(top_series_per_sub), top_series_per_sub["subsector"].nunique())

    rows = []
    t0 = time.time()
    processed = 0
    for _, srow in top_series_per_sub.iterrows():
        series = srow["series"]
        sub = srow["subsector"]
        try:
            mkts = client.list_markets(series_ticker=series, status="open", limit=200).get("markets", []) or []
        except Exception as e:
            log.warning("list_markets failed for %s: %s", series, e)
            continue

        # top-3 by OI, contested only
        viable = []
        for m in mkts:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            mid = (yb + ya) / 2
            if yb > 0 and ya < 1.0 and yb < ya and 0.05 <= mid <= 0.95:
                viable.append({
                    "ticker": m.get("ticker"),
                    "oi": float(m.get("open_interest_fp") or 0),
                    "vol_24h": float(m.get("volume_24h_fp") or 0),
                    "yes_bid": yb, "yes_ask": ya, "mid": mid,
                    "close_time": m.get("close_time"),
                    "subtitle": (m.get("subtitle") or "")[:50],
                })
        viable.sort(key=lambda r: r["oi"], reverse=True)
        viable = viable[:3]

        for mrow in viable:
            ticker = mrow["ticker"]
            try:
                ob = client.get_orderbook(ticker, depth=50)
                dm = depth_metrics(ob.get("orderbook_fp") or {})
            except Exception as e:
                log.warning("orderbook failed for %s: %s", ticker, e)
                dm = {"has_two_sides": False}

            try:
                tresp = client.get_trades(ticker=ticker, limit=1000)
                trades = tresp.get("trades", [])
                tm = trade_metrics(trades)
            except Exception as e:
                log.warning("trades failed for %s: %s", ticker, e)
                tm = {"n_trades": 0}

            rows.append({
                "subsector": sub,
                "series": series,
                "series_title": srow.get("title"),
                "category": srow.get("category"),
                "frequency": srow.get("frequency"),
                "ticker": ticker,
                "subtitle": mrow["subtitle"],
                "oi": mrow["oi"],
                "vol_24h": mrow["vol_24h"],
                "close_time": mrow["close_time"],
                **dm,
                **{k: (json.dumps(v) if isinstance(v, dict) else v) for k, v in tm.items()},
            })
            processed += 1
            if processed % 50 == 0:
                log.info("processed %d markets, elapsed %.0fs", processed, time.time() - t0)

    df = pd.DataFrame(rows)
    df.to_parquet(cfg.data_dir / "subsector_depth_markets.parquet")
    log.info("wrote %d market rows to subsector_depth_markets.parquet", len(df))

    # Per-subsector aggregation
    if len(df):
        def agg(sub_rows):
            two = sub_rows[sub_rows["has_two_sides"] == True]
            if len(two) == 0:
                return pd.Series({"n_markets_sampled": len(sub_rows)})
            return pd.Series({
                "n_markets_sampled": len(sub_rows),
                "n_two_sided": len(two),
                "median_spread_c": float(two["spread_c"].median()),
                "mean_spread_c": float(two["spread_c"].mean()),
                "median_tob_bid_sz": float(two["tob_bid_sz"].median()),
                "median_tob_ask_sz": float(two["tob_ask_sz"].median()),
                "median_depth_within_5c_bid": float(two.get("cum_bid_5c", pd.Series([0])).median()),
                "median_depth_within_5c_ask": float(two.get("cum_ask_5c", pd.Series([0])).median()),
                "median_total_bid_depth": float(two["total_bid_depth"].median()),
                "median_total_ask_depth": float(two["total_ask_depth"].median()),
                "median_wall_ratio": float(two[["wall_bid_ratio","wall_ask_ratio"]].stack().median()),
                "mean_informed_signal": float(two.get("informed_signal", pd.Series(dtype=float)).mean(skipna=True)),
                "mean_abs_move_c": float(two.get("mean_abs_consecutive_move_c", pd.Series(dtype=float)).mean(skipna=True)),
                "mean_trades_per_market": float(two.get("n_trades", pd.Series(dtype=float)).mean(skipna=True)),
                "total_oi": float(two["oi"].sum()),
                "total_vol_24h": float(two["vol_24h"].sum()),
            })

        per_sub = df.groupby("subsector").apply(agg, include_groups=False).reset_index()
        per_sub.to_parquet(cfg.data_dir / "subsector_depth_summary.parquet")

        # MM-ripeness composite: wider spread x meaningful depth x modest informed signal x some volume
        def score(r):
            if pd.isna(r.get("median_spread_c")):
                return 0.0
            spread_score = min(r["median_spread_c"] / 20, 2.0)  # saturate at 20c = 2.0
            depth_bid = r.get("median_depth_within_5c_bid") or 0
            depth_ask = r.get("median_depth_within_5c_ask") or 0
            depth_score = min((depth_bid + depth_ask) / 200, 1.0)  # saturate at 200 contracts
            vol_score = min(r.get("total_vol_24h", 0) / 10000, 1.0)
            # informed_signal: >0.002 = toxic; <0.0005 = low info; penalize toxicity
            info = abs(r.get("mean_informed_signal") or 0)
            info_penalty = max(0, 1 - info / 0.005)
            return float(spread_score * depth_score * vol_score * info_penalty)

        per_sub["mm_score"] = per_sub.apply(score, axis=1)
        per_sub = per_sub.sort_values("mm_score", ascending=False)
        print("\n=== subsector ranking by MM-ripeness (spread x depth x vol x non-toxic) ===\n")
        cols = ["subsector", "n_markets_sampled", "n_two_sided",
                "median_spread_c", "median_depth_within_5c_bid", "median_depth_within_5c_ask",
                "mean_informed_signal", "mean_abs_move_c", "total_vol_24h", "mm_score"]
        print(per_sub[cols].head(30).to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
