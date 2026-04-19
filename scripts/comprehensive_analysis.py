#!/usr/bin/env python3
"""Comprehensive per-subsector analysis.

For EVERY contested market across target subsectors:
  - pull orderbook (depth=50) -> depth metrics
  - pull trade history (paginated to ~2000 trades) -> informed-flow metrics
  - compute time-to-expiry (TTE) for each trade
  - bin trades by TTE bucket, compute per-bucket metrics

Output:
  research/data/market_details.parquet       # row-per-market with snapshot metrics
  research/data/market_trades.parquet         # all trades (for per-market reanalysis)
  research/data/tte_bucket_summary.parquet    # per-subsector + per-TTE-bucket metrics

This is a long-running job (~10-20 min depending on market count).
"""
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from pmm.analysis.depth_metrics import depth_metrics
from pmm.config import Config
from pmm.kalshi.client import KalshiAPIError, KalshiClient


# Time-to-expiry (seconds) bucket edges
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


def tte_bucket(seconds_to_expiry: float) -> str:
    for name, lo, hi in TTE_EDGES:
        if lo <= seconds_to_expiry < hi:
            return name
    return "past_expiry" if seconds_to_expiry < 0 else "30d+"


def parse_expiry(close_time: str | None) -> datetime | None:
    if not close_time:
        return None
    try:
        ts = close_time.replace("Z", "+00:00")
        return datetime.fromisoformat(ts)
    except Exception:
        return None


def pull_all_trades(client: KalshiClient, ticker: str, max_pages: int = 3, per_page: int = 1000) -> list[dict]:
    """Paginate through trade history. Default: up to 3000 trades per market."""
    out = []
    cursor = None
    for _ in range(max_pages):
        kw = {"ticker": ticker, "limit": per_page}
        if cursor:
            kw["cursor"] = cursor
        try:
            r = client.get_trades(**kw)
        except KalshiAPIError:
            break
        except Exception:
            break
        tr = r.get("trades", []) or []
        out.extend(tr)
        cursor = r.get("cursor")
        if not cursor or not tr:
            break
    return out


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    log = logging.getLogger("comprehensive")

    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)
    data_dir = cfg.data_dir

    scan_path = data_dir / "sector_scan_series.parquet"
    if not scan_path.exists():
        log.error("run scripts/fast_scan.py first")
        return 1

    series_df = pd.read_parquet(scan_path)
    target = series_df[series_df["n_contested"].fillna(0) > 0].copy()
    log.info("%d series with contested markets across %d subsectors",
             len(target), target["subsector"].nunique())

    # Collect all contested markets (no sampling)
    log.info("listing all contested markets per series...")
    all_mkts = []
    for i, sr in enumerate(target.itertuples()):
        if i % 50 == 0:
            log.info("  %d / %d series listed", i, len(target))
        try:
            r = client.list_markets(series_ticker=sr.series, status="open", limit=200)
        except Exception as e:
            log.warning("list markets err for %s: %s", sr.series, e)
            continue
        for m in r.get("markets", []) or []:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            mid = (yb + ya) / 2
            if yb > 0 and ya < 1.0 and yb < ya and 0.05 <= mid <= 0.95:
                all_mkts.append({
                    "subsector": sr.subsector,
                    "series": sr.series,
                    "series_title": sr.title,
                    "category": sr.category,
                    "frequency": sr.frequency,
                    "ticker": m.get("ticker"),
                    "subtitle": (m.get("subtitle") or m.get("yes_sub_title") or "")[:80],
                    "yes_bid": yb, "yes_ask": ya, "mid": mid,
                    "oi": float(m.get("open_interest_fp") or 0),
                    "vol_24h": float(m.get("volume_24h_fp") or 0),
                    "vol_total": float(m.get("volume_fp") or 0),
                    "close_time": m.get("close_time"),
                    "expected_expiration_time": m.get("expected_expiration_time"),
                    "expiration_time": m.get("expiration_time"),
                    "last_price": float(m.get("last_price_dollars") or 0),
                })
    log.info("total contested markets: %d", len(all_mkts))

    if not all_mkts:
        return 0

    # Rank within each subsector, cap if huge. We aim for every contested
    # market but cap huge sports subsectors at 200 to keep runtime bounded.
    mkts_df = pd.DataFrame(all_mkts)
    before = len(mkts_df)
    mkts_df = mkts_df.sort_values(["subsector","oi"], ascending=[True, False]).groupby("subsector").head(200)
    log.info("capped per-subsector at 200 markets: %d -> %d", before, len(mkts_df))

    # ---- pull orderbook + trades for every market
    market_rows = []
    all_trade_rows = []
    t0 = time.time()
    for i, m in enumerate(mkts_df.itertuples()):
        if i % 25 == 0:
            log.info("  %d / %d markets, elapsed %.0fs", i, len(mkts_df), time.time() - t0)
        ticker = m.ticker

        expiry = parse_expiry(m.close_time)
        now = datetime.now(tz=timezone.utc)
        tte_now = (expiry - now).total_seconds() if expiry else float("nan")

        # Orderbook
        try:
            ob = client.get_orderbook(ticker, depth=50)
            dm = depth_metrics(ob.get("orderbook_fp") or {})
        except Exception:
            dm = {"has_two_sides": False}

        # Trades (paginated)
        trades = pull_all_trades(client, ticker, max_pages=3, per_page=1000)
        trades_enriched = []
        if trades and expiry:
            for t in trades:
                ct = t.get("created_time")
                try:
                    ts = datetime.fromisoformat(ct.replace("Z", "+00:00")) if ct else None
                except Exception:
                    ts = None
                seconds_to_expiry_at_trade = (expiry - ts).total_seconds() if ts else None
                trades_enriched.append({
                    "ticker": ticker,
                    "subsector": m.subsector,
                    "series": m.series,
                    "created_time": ct,
                    "ts": ts,
                    "yes_price": float(t.get("yes_price") or 0),
                    "count": float(t.get("count") or 0),
                    "taker_side": t.get("taker_side"),
                    "seconds_to_expiry": seconds_to_expiry_at_trade,
                    "tte_bucket": tte_bucket(seconds_to_expiry_at_trade) if seconds_to_expiry_at_trade is not None else "unknown",
                })
        all_trade_rows.extend(trades_enriched)

        # Trade-based summary stats for this market
        if trades_enriched:
            tdf = pd.DataFrame(trades_enriched).dropna(subset=["ts"]).sort_values("ts")
            n_trades = len(tdf)
            if n_trades > 1:
                tdf["next_px"] = tdf["yes_price"].shift(-1)
                tdf["fwd_move_c"] = (tdf["next_px"] - tdf["yes_price"])
                # Kalshi yes_price may be stored as cents int (e.g. 55) or dollars (0.55);
                # heuristic: if max > 1.5, treat as cents; else dollars scale to cents
                price_scale = 1.0 if tdf["yes_price"].max() > 1.5 else 100.0
                tdf["fwd_move_c"] = tdf["fwd_move_c"] * price_scale
                # Signed informed signal per trade
                def side_sign(s):
                    s = str(s or "").lower()
                    if s == "yes": return 1
                    if s == "no": return -1
                    return 0
                tdf["sign"] = tdf["taker_side"].map(side_sign)
                tdf["informed_px_move"] = tdf["sign"] * tdf["fwd_move_c"]

                mean_informed = float(np.nanmean(tdf["informed_px_move"]))
                mean_abs_move = float(np.nanmean(tdf["fwd_move_c"].abs()))
                median_abs_move = float(np.nanmedian(tdf["fwd_move_c"].abs()))

                # Per-TTE bucket means
                bucket_info = {}
                for bname, _, _ in TTE_EDGES:
                    sub = tdf[tdf["tte_bucket"] == bname]
                    if len(sub) >= 5:
                        bucket_info[f"informed_{bname}"] = float(np.nanmean(sub["informed_px_move"]))
                        bucket_info[f"abs_move_{bname}"] = float(np.nanmean(sub["fwd_move_c"].abs()))
                        bucket_info[f"n_trades_{bname}"] = int(len(sub))
            else:
                mean_informed = mean_abs_move = median_abs_move = float("nan")
                bucket_info = {}
        else:
            n_trades = 0
            mean_informed = mean_abs_move = median_abs_move = float("nan")
            bucket_info = {}

        market_rows.append({
            "subsector": m.subsector,
            "series": m.series,
            "ticker": ticker,
            "subtitle": m.subtitle,
            "yes_bid": m.yes_bid, "yes_ask": m.yes_ask, "mid": m.mid,
            "oi": m.oi, "vol_24h": m.vol_24h,
            "close_time": m.close_time,
            "tte_now_seconds": tte_now,
            "tte_now_bucket": tte_bucket(tte_now) if tte_now == tte_now else "unknown",
            **dm,
            "n_trades_total": n_trades,
            "mean_informed_signal": mean_informed,
            "mean_abs_move_c": mean_abs_move,
            "median_abs_move_c": median_abs_move,
            **bucket_info,
        })

    mkt_df = pd.DataFrame(market_rows)
    mkt_df.to_parquet(data_dir / "market_details.parquet")
    log.info("wrote %d market rows to market_details.parquet", len(mkt_df))

    trade_df = pd.DataFrame(all_trade_rows)
    if len(trade_df):
        trade_df.to_parquet(data_dir / "market_trades.parquet")
        log.info("wrote %d trade rows to market_trades.parquet", len(trade_df))

    # ---- aggregate per-subsector + per-TTE-bucket
    rows = []
    if len(trade_df):
        trade_df["tte_bucket"] = trade_df["tte_bucket"].fillna("unknown")
        for (sub, bkt), g in trade_df.groupby(["subsector", "tte_bucket"]):
            if len(g) < 10:
                continue
            # price scale
            scale = 1.0 if g["yes_price"].max() > 1.5 else 100.0
            g = g.sort_values(["ticker", "ts"])
            g["next_px"] = g.groupby("ticker")["yes_price"].shift(-1)
            g["fwd_c"] = (g["next_px"] - g["yes_price"]) * scale

            def sgn(s):
                s = str(s or "").lower()
                if s == "yes": return 1
                if s == "no": return -1
                return 0
            g["sign"] = g["taker_side"].map(sgn)
            rows.append({
                "subsector": sub,
                "tte_bucket": bkt,
                "n_trades": len(g),
                "mean_abs_move_c": float(np.nanmean(g["fwd_c"].abs())),
                "mean_informed_signal_c": float(np.nanmean(g["sign"] * g["fwd_c"])),
                "p95_abs_move_c": float(np.nanpercentile(g["fwd_c"].abs().dropna(), 95)) if g["fwd_c"].abs().notna().any() else float("nan"),
                "mean_trade_size": float(g["count"].mean()),
            })
        tte_df = pd.DataFrame(rows).sort_values(["subsector", "tte_bucket"])
        tte_df.to_parquet(data_dir / "tte_bucket_summary.parquet")
        log.info("wrote %d TTE bucket summaries", len(tte_df))

    # Per-subsector book summary
    if len(mkt_df):
        two = mkt_df[mkt_df["has_two_sides"] == True]
        sub_summary = two.groupby("subsector").agg(
            n_markets=("ticker", "count"),
            median_spread_c=("spread_c", "median"),
            median_tob_bid=("tob_bid_sz", "median"),
            median_tob_ask=("tob_ask_sz", "median"),
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
        sub_summary.to_parquet(data_dir / "subsector_summary_full.parquet")
        print("\n=== per-subsector book+trade summary ===\n")
        print(sub_summary.to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
