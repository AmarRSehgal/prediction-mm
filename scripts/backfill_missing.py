#!/usr/bin/env python3
"""Backfill subsectors that were dropped by the fast_scan TARGET_SUBS filter.

Reads missing_series.parquet, pulls markets + orderbook + trades for any open
contested markets, appends to existing market_details.parquet /
market_trades.parquet / subsector_summary_full.parquet / tte_bucket_summary.parquet.
"""
from __future__ import annotations

import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from pmm.analysis.depth_metrics import depth_metrics
from pmm.config import Config
from pmm.kalshi.client import KalshiClient


TTE_EDGES = [
    ("0-15m",       0,       15*60),
    ("15m-1h",      15*60,   60*60),
    ("1-6h",        60*60,   6*3600),
    ("6-12h",       6*3600,  12*3600),
    ("12-24h",      12*3600, 24*3600),
    ("1-3d",        24*3600, 3*24*3600),
    ("3-7d",        3*24*3600, 7*24*3600),
    ("7-30d",       7*24*3600, 30*24*3600),
    ("30d+",        30*24*3600, 10**9),
]


def tte_bucket(s: float) -> str:
    for name, lo, hi in TTE_EDGES:
        if lo <= s < hi:
            return name
    return "past_expiry" if s < 0 else "30d+"


def parse_expiry(ct: str | None):
    if not ct: return None
    try: return datetime.fromisoformat(ct.replace("Z","+00:00"))
    except: return None


def pull_trades(client, ticker, max_pages=1, per_page=1000):
    out = []
    cursor = None
    for _ in range(max_pages):
        kw = {"ticker": ticker, "limit": per_page}
        if cursor: kw["cursor"] = cursor
        try:
            r = client.get_trades(**kw)
        except Exception:
            break
        tr = r.get("trades", []) or []
        out.extend(tr)
        cursor = r.get("cursor")
        if not cursor or not tr: break
    return out


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    log = logging.getLogger("backfill")

    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)
    data = cfg.data_dir

    missing = pd.read_parquet(data / "missing_series.parquet")
    log.info("missing series: %d across %d subsectors", len(missing), missing["subsector"].nunique())

    # Exclude completely unknown bucket unless explicitly asked — too broad
    # but keep non-unknown missing + sample of unknown that has title hints
    include = missing[missing["subsector"] != "unknown"]
    log.info("will scan %d classified-but-missing series", len(include))

    all_mkts = []
    for i, sr in enumerate(include.itertuples()):
        if i % 50 == 0:
            log.info("  %d / %d series", i, len(include))
        try:
            r = client.list_markets(series_ticker=sr.ticker, status="open", limit=200)
        except Exception:
            continue
        for m in r.get("markets", []) or []:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            mid = (yb + ya) / 2
            if yb > 0 and ya < 1.0 and yb < ya and 0.05 <= mid <= 0.95:
                all_mkts.append({
                    "subsector": sr.subsector,
                    "series": sr.ticker,
                    "series_title": sr.title,
                    "category": sr.category,
                    "frequency": sr.frequency,
                    "ticker": m.get("ticker"),
                    "subtitle": (m.get("subtitle") or m.get("yes_sub_title") or "")[:80],
                    "yes_bid": yb, "yes_ask": ya, "mid": mid,
                    "oi": float(m.get("open_interest_fp") or 0),
                    "vol_24h": float(m.get("volume_24h_fp") or 0),
                    "close_time": m.get("close_time"),
                })
    log.info("contested markets found in missing subsectors: %d", len(all_mkts))

    if not all_mkts:
        log.info("nothing to backfill")
        return 0

    mkts_df = pd.DataFrame(all_mkts)
    mkts_df = mkts_df.sort_values(["subsector","oi"], ascending=[True, False]).groupby("subsector").head(200)
    log.info("capped to %d markets (200/subsector)", len(mkts_df))

    rows = []
    trade_rows = []
    for i, m in enumerate(mkts_df.itertuples()):
        if i % 50 == 0:
            log.info("  fetching %d / %d", i, len(mkts_df))
        ticker = m.ticker
        expiry = parse_expiry(m.close_time)
        now = datetime.now(tz=timezone.utc)
        tte_now = (expiry - now).total_seconds() if expiry else float("nan")

        try:
            ob = client.get_orderbook(ticker, depth=50)
            dm = depth_metrics(ob.get("orderbook_fp") or {})
        except Exception:
            dm = {"has_two_sides": False}

        trades = pull_trades(client, ticker, max_pages=1, per_page=1000)
        enr = []
        if trades and expiry:
            for t in trades:
                ct = t.get("created_time")
                try: ts = datetime.fromisoformat(ct.replace("Z","+00:00")) if ct else None
                except: ts = None
                ste = (expiry - ts).total_seconds() if ts else None
                try: yp = float(t.get("yes_price_dollars") or 0)
                except: yp = 0.0
                try: cnt = float(t.get("count_fp") or 0)
                except: cnt = 0.0
                enr.append({
                    "ticker": ticker, "subsector": m.subsector, "series": m.series,
                    "created_time": ct, "ts": ts, "yes_price": yp, "count": cnt,
                    "taker_side": t.get("taker_side"),
                    "seconds_to_expiry": ste,
                    "tte_bucket": tte_bucket(ste) if ste is not None else "unknown",
                })
        trade_rows.extend(enr)

        mean_info, mean_abs, n_trades = float("nan"), float("nan"), 0
        bucket_info = {}
        if enr:
            tdf = pd.DataFrame(enr).dropna(subset=["ts"]).sort_values("ts")
            n_trades = len(tdf)
            if n_trades > 1:
                tdf["next_px"] = tdf["yes_price"].shift(-1)
                tdf["fwd_c"] = (tdf["next_px"] - tdf["yes_price"]) * 100
                def sgn(s):
                    s = str(s or "").lower()
                    return 1 if s == "yes" else (-1 if s == "no" else 0)
                tdf["sign"] = tdf["taker_side"].map(sgn)
                mean_info = float(np.nanmean(tdf["sign"] * tdf["fwd_c"]))
                mean_abs = float(np.nanmean(tdf["fwd_c"].abs()))
                for bname, _, _ in TTE_EDGES:
                    sub = tdf[tdf["tte_bucket"] == bname]
                    if len(sub) >= 5:
                        bucket_info[f"informed_{bname}"] = float(np.nanmean(sub["sign"] * sub["fwd_c"]))
                        bucket_info[f"abs_move_{bname}"] = float(np.nanmean(sub["fwd_c"].abs()))
                        bucket_info[f"n_trades_{bname}"] = int(len(sub))

        rows.append({
            "subsector": m.subsector, "series": m.series, "ticker": ticker,
            "subtitle": m.subtitle, "yes_bid": m.yes_bid, "yes_ask": m.yes_ask, "mid": m.mid,
            "oi": m.oi, "vol_24h": m.vol_24h, "close_time": m.close_time,
            "tte_now_seconds": tte_now,
            "tte_now_bucket": tte_bucket(tte_now) if tte_now == tte_now else "unknown",
            **dm,
            "n_trades_total": n_trades,
            "mean_informed_signal": mean_info,
            "mean_abs_move_c": mean_abs,
            **bucket_info,
        })

    new_mkt = pd.DataFrame(rows)
    new_trades = pd.DataFrame(trade_rows)

    # Merge with existing
    existing_mkt = pd.read_parquet(data / "market_details.parquet") if (data / "market_details.parquet").exists() else pd.DataFrame()
    merged_mkt = pd.concat([existing_mkt, new_mkt], ignore_index=True)
    merged_mkt.to_parquet(data / "market_details.parquet")
    log.info("market_details: %d -> %d rows", len(existing_mkt), len(merged_mkt))

    existing_tr = pd.read_parquet(data / "market_trades.parquet") if (data / "market_trades.parquet").exists() else pd.DataFrame()
    merged_tr = pd.concat([existing_tr, new_trades], ignore_index=True)
    merged_tr.to_parquet(data / "market_trades.parquet")
    log.info("market_trades: %d -> %d rows", len(existing_tr), len(merged_tr))

    # Rebuild per-subsector and TTE aggregates from the merged tables
    two = merged_mkt[merged_mkt["has_two_sides"] == True]
    sub_summary = two.groupby("subsector").agg(
        n_markets=("ticker", "count"),
        median_spread_c=("spread_c", "median"),
        median_tob_bid=("tob_bid_sz", "median"),
        median_tob_ask=("tob_ask_sz", "median"),
        median_depth_5c_of_bid=("depth_5c_of_bid", "median"),
        median_depth_5c_of_ask=("depth_5c_of_ask", "median"),
        median_depth_10c_of_bid=("depth_10c_of_bid", "median"),
        median_depth_10c_of_ask=("depth_10c_of_ask", "median"),
        median_depth_5c_bid=("cum_bid_5c", "median"),
        median_depth_5c_ask=("cum_ask_5c", "median"),
        median_depth_10c_bid=("cum_bid_10c", "median"),
        median_depth_10c_ask=("cum_ask_10c", "median"),
        total_oi=("oi", "sum"),
        total_vol_24h=("vol_24h", "sum"),
        mean_informed=("mean_informed_signal", "mean"),
        mean_abs_move_c=("mean_abs_move_c", "mean"),
        mean_n_trades=("n_trades_total", "mean"),
    ).reset_index().sort_values("total_vol_24h", ascending=False)
    sub_summary.to_parquet(data / "subsector_summary_full.parquet")
    log.info("subsector_summary_full: %d rows", len(sub_summary))

    # TTE buckets
    tte_rows = []
    for (sub, bkt), g in merged_tr.groupby(["subsector","tte_bucket"]):
        if len(g) < 10:
            continue
        g = g.sort_values(["ticker","ts"])
        g["next_px"] = g.groupby("ticker")["yes_price"].shift(-1)
        g["fwd_c"] = (g["next_px"] - g["yes_price"]) * 100
        def sgn(s):
            s = str(s or "").lower()
            return 1 if s == "yes" else (-1 if s == "no" else 0)
        g["sign"] = g["taker_side"].map(sgn)
        tte_rows.append({
            "subsector": sub, "tte_bucket": bkt, "n_trades": len(g),
            "mean_abs_move_c": float(np.nanmean(g["fwd_c"].abs())),
            "mean_informed_signal_c": float(np.nanmean(g["sign"] * g["fwd_c"])),
            "p95_abs_move_c": float(np.nanpercentile(g["fwd_c"].abs().dropna(), 95)) if g["fwd_c"].abs().notna().any() else float("nan"),
            "mean_trade_size": float(g["count"].mean()),
        })
    pd.DataFrame(tte_rows).sort_values(["subsector","tte_bucket"]).to_parquet(data / "tte_bucket_summary.parquet")
    log.info("tte_bucket_summary rebuilt: %d rows", len(tte_rows))

    # Also refresh sector_scan_series with the missing ones
    scan = pd.read_parquet(data / "sector_scan_series.parquet")
    new_scan_rows = []
    for sub, g in new_mkt.groupby("subsector"):
        for series, gg in g.groupby("series"):
            n_mkts = len(gg)
            n_con = int((gg["has_two_sides"] == True).sum())
            total_oi = float(gg["oi"].sum())
            total_vol = float(gg["vol_24h"].sum())
            top_spreads = gg.sort_values("oi", ascending=False).head(3)["spread_c"]
            top_mean = float(top_spreads.mean()) / 100 if len(top_spreads) else float("nan")
            row_title = gg.iloc[0].get("subtitle", "")  # placeholder
            new_scan_rows.append({
                "series": series, "title": row_title,
                "category": None, "frequency": None, "subsector": sub,
                "n_markets": n_mkts, "n_contested": n_con,
                "total_oi": total_oi, "total_vol_24h": total_vol,
                "top_oi_mean_spread": top_mean,
            })
    merged_scan = pd.concat([scan, pd.DataFrame(new_scan_rows)], ignore_index=True)
    merged_scan.to_parquet(data / "sector_scan_series.parquet")
    log.info("sector_scan_series: %d -> %d rows", len(scan), len(merged_scan))

    print("=== BACKFILL DONE ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
