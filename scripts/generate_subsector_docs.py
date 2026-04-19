#!/usr/bin/env python3
"""Generate per-subsector markdown docs.

Reads:
  research/data/sector_scan_series.parquet       # per-series stats (fast scan)
  research/data/market_details.parquet           # per-market depth + trade stats (comprehensive)
  research/data/tte_bucket_summary.parquet       # per-subsector TTE-bucket aggregates
  research/data/subsector_summary_full.parquet   # per-subsector book+trade aggregates

Writes:
  docs/subsectors/<bucket>/<subsector>.md  (one file per subsector with open markets)

Curated content between <!-- KEEP-START --> and <!-- KEEP-END --> is preserved
across runs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.config import Config


PREFIX_TO_FOLDER = {
    "sports": "sports", "weather": "weather", "climate": "weather",
    "eco": "economics", "fin": "financials", "comm": "commodities",
    "crypto": "crypto", "pol": "politics", "companies": "companies",
    "ent": "entertainment", "tech": "tech", "world": "world",
    "rankings": "rankings", "health": "health",
    "collectibles": "misc", "unknown": "misc",
}
KEEP_START = "<!-- KEEP-START -->"
KEEP_END = "<!-- KEEP-END -->"
TTE_ORDER = ["0-15m","15m-1h","1-6h","6-12h","12-24h","1-3d","3-7d","7-30d","30d+"]


def _folder(sub: str) -> str:
    return PREFIX_TO_FOLDER.get(sub.split("_", 1)[0], "misc")


def _extract_keep(text: str) -> str:
    m = re.search(rf"{re.escape(KEEP_START)}(.*?){re.escape(KEEP_END)}", text, re.DOTALL)
    return m.group(1).strip("\n") if m else ""


def _profile(book_agg: dict) -> str:
    spr = book_agg.get("median_spread_c")
    vol = book_agg.get("total_vol_24h", 0)
    depth = (book_agg.get("median_depth_5c_bid", 0) or 0) + (book_agg.get("median_depth_5c_ask", 0) or 0)
    info = abs(book_agg.get("mean_informed") or 0)
    if pd.isna(spr):
        return "Unknown"
    if spr < 3 and vol > 1000:
        return "HFT-saturated"
    if spr >= 8 and vol > 500 and depth >= 20:
        return "Niche opportunity"
    if spr >= 15 and vol < 100:
        return "Wide but dead"
    if info > 0.1:
        return "Toxic flow"
    if spr >= 3 and spr < 8:
        return "Moderate (mixed)"
    return "Mixed / thin"


def render(sub: str, series_rows: pd.DataFrame, mkt_rows: pd.DataFrame | None,
           tte_rows: pd.DataFrame | None, book_agg: dict | None, keep_block: str) -> str:
    top_series = series_rows.sort_values("total_oi", ascending=False).head(10)
    n_series = len(series_rows)
    n_with_mkts = int((series_rows["n_markets"] > 0).sum())
    total_mkts = int(series_rows["n_markets"].sum())
    total_con = int(series_rows["n_contested"].sum())
    total_vol = float(series_rows["total_vol_24h"].sum())
    total_oi = float(series_rows["total_oi"].sum())
    top_spr_med = float(series_rows["top_oi_mean_spread"].median(skipna=True))

    profile = _profile(book_agg or {})

    L: list[str] = []
    L.append(f"# {sub}\n")
    L.append("_Auto-generated. Curated notes (KEEP block) preserved across runs._\n")

    # High-level
    L.append("## Summary")
    L.append("")
    L.append(f"- Series: **{n_series}** ({n_with_mkts} with open markets)")
    L.append(f"- Open markets: **{total_mkts}** ({total_con} contested)")
    L.append(f"- Total 24h volume: **${total_vol:,.0f}**")
    L.append(f"- Total open interest: **{total_oi:,.0f}**")
    L.append(f"- Top-OI mean spread (median across series): **{top_spr_med*100:.1f} cents**" if top_spr_med == top_spr_med else "- Top-OI mean spread: n/a")
    L.append(f"- **MM profile: {profile}**")
    L.append("")

    # Book depth stats (from comprehensive analysis)
    if book_agg is not None and not pd.isna(book_agg.get("median_spread_c", float("nan"))):
        L.append("## Book depth (from comprehensive scan)")
        L.append("")
        L.append(f"- Markets sampled: **{book_agg.get('n_markets', 0):.0f}**")
        L.append(f"- Median spread: **{book_agg['median_spread_c']:.1f}c**")
        L.append(f"- Median TOB bid / ask size: **{book_agg.get('median_tob_bid', 0):.0f} / {book_agg.get('median_tob_ask', 0):.0f}** contracts")
        L.append(f"- Median cumulative depth within 5c of mid — bid: **{book_agg.get('median_depth_5c_bid', 0):.0f}** / ask: **{book_agg.get('median_depth_5c_ask', 0):.0f}** contracts")
        L.append(f"- Median cumulative depth within 10c of mid — bid: **{book_agg.get('median_depth_10c_bid', 0):.0f}** / ask: **{book_agg.get('median_depth_10c_ask', 0):.0f}** contracts")
        L.append(f"- Mean trades per market (last 3000): **{book_agg.get('mean_n_trades', 0):.0f}**")
        L.append(f"- Mean informed-signal proxy: **{book_agg.get('mean_informed', 0):.3f}** (sign(trade) * forward cent-move; >0 = toxic)")
        L.append(f"- Mean abs consecutive-trade move: **{book_agg.get('mean_abs_move_c', 0):.2f}c**")
        L.append("")

    # TTE-bucketed informed flow
    if tte_rows is not None and len(tte_rows):
        L.append("## Informed flow by time-to-expiry")
        L.append("")
        L.append("Trades grouped by how close they occurred to the market's resolution.")
        L.append("Larger `informed_signal_c` (cents) = takers predict direction of next trade.")
        L.append("Larger `mean_abs_move` = more price movement between consecutive trades.\n")
        tte_rows = tte_rows.copy()
        tte_rows["_ord"] = tte_rows["tte_bucket"].map({b: i for i, b in enumerate(TTE_ORDER)})
        tte_rows = tte_rows.sort_values("_ord")
        L.append("| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |")
        L.append("|---|---:|---:|---:|---:|---:|")
        for _, r in tte_rows.iterrows():
            L.append(f"| {r['tte_bucket']} | {r['n_trades']:.0f} | {r['mean_abs_move_c']:.2f} | {r['mean_informed_signal_c']:.3f} | {r['p95_abs_move_c']:.2f} | {r['mean_trade_size']:.1f} |")
        L.append("")

    # Per-market table (top 15 by OI from comprehensive)
    if mkt_rows is not None and len(mkt_rows):
        top = mkt_rows.sort_values("oi", ascending=False).head(15)
        L.append("## Top markets (by OI)")
        L.append("")
        L.append("| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |")
        L.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
        for _, r in top.iterrows():
            mid = r.get("mid_c", 0) or 0
            spr = r.get("spread_c", 0) or 0
            L.append(f"| {r['ticker']} | {str(r.get('subtitle',''))[:40]} | {mid:.0f}c | {spr:.1f}c | {r.get('tob_bid_sz',0):.0f} | {r.get('tob_ask_sz',0):.0f} | {r.get('cum_bid_5c',0):.0f} | {r.get('cum_ask_5c',0):.0f} | {r.get('oi',0):.0f} | ${r.get('vol_24h',0):.0f} | {r.get('tte_now_bucket','')} |")
        L.append("")

    # Top series
    L.append("## Top series by OI")
    L.append("")
    if len(top_series):
        L.append("| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |")
        L.append("|---|---|---|---:|---:|---:|---:|---:|")
        for _, r in top_series.iterrows():
            title = str(r.get("title") or "")[:40].replace("|", "/")
            L.append(f"| {r['series']} | {title} | {r.get('frequency','')} | {r['n_markets']:.0f} | {r['n_contested']:.0f} | ${r['total_vol_24h']:,.0f} | {r['total_oi']:,.0f} | {r.get('top_oi_mean_spread', float('nan'))*100:.1f}c |")
    L.append("")

    # Curated
    L.append("## Curated notes")
    L.append("")
    L.append(KEEP_START)
    if keep_block.strip():
        L.append(keep_block)
    else:
        L.append("<!-- Add market structure, resolution mechanics, time-of-day / TTE patterns, informed-flow analysis, verdict here -->")
        L.append("")
        L.append("### Market structure")
        L.append("- Resolution mechanism:")
        L.append("- Frequency:")
        L.append("- Typical close time:")
        L.append("")
        L.append("### Informed flow profile")
        L.append("- Retail vs pro:")
        L.append("- HFT presence:")
        L.append("- Known asymmetries:")
        L.append("")
        L.append("### Time windows (UTC) / TTE behavior")
        L.append("- Safe:")
        L.append("- Quiet:")
        L.append("- Dangerous:")
        L.append("- Key events:")
        L.append("- TTE pattern: when does informed_signal_c spike?")
        L.append("")
        L.append("### Verdict")
        L.append("- v0 target?")
        L.append("- Notes:")
    L.append(KEEP_END)
    L.append("")
    return "\n".join(L)


def main() -> int:
    cfg = Config.from_env()
    data = cfg.data_dir

    scan_path = data / "sector_scan_series.parquet"
    if not scan_path.exists():
        print("run scripts/fast_scan.py first")
        return 1
    series_df = pd.read_parquet(scan_path)

    mkt_df = pd.read_parquet(data / "market_details.parquet") if (data / "market_details.parquet").exists() else None
    tte_df = pd.read_parquet(data / "tte_bucket_summary.parquet") if (data / "tte_bucket_summary.parquet").exists() else None
    sub_df = pd.read_parquet(data / "subsector_summary_full.parquet") if (data / "subsector_summary_full.parquet").exists() else None

    docs_root = Path.cwd() / "docs" / "subsectors"
    docs_root.mkdir(parents=True, exist_ok=True)

    non_empty = series_df[series_df["n_markets"].fillna(0) > 0]
    subs = sorted(non_empty["subsector"].dropna().unique())

    written = 0
    for sub in subs:
        srows = series_df[series_df["subsector"] == sub]
        folder = _folder(sub)
        stripped = sub.split("_", 1)[1] if "_" in sub else sub
        out_path = docs_root / folder / f"{stripped}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)

        keep = _extract_keep(out_path.read_text()) if out_path.exists() else ""

        mrows = mkt_df[mkt_df["subsector"] == sub] if mkt_df is not None else None
        trows = tte_df[tte_df["subsector"] == sub] if tte_df is not None else None
        bagg = None
        if sub_df is not None:
            row = sub_df[sub_df["subsector"] == sub]
            if len(row):
                bagg = row.iloc[0].to_dict()

        text = render(sub, srows, mrows, trows, bagg, keep)
        out_path.write_text(text)
        written += 1

    print(f"wrote {written} subsector docs")

    # Index
    idx_path = docs_root / "INDEX.md"
    agg = non_empty.groupby("subsector").agg(
        n_series=("series", "count"),
        n_markets=("n_markets", "sum"),
        n_contested=("n_contested", "sum"),
        vol_24h=("total_vol_24h", "sum"),
        top_oi_spread=("top_oi_mean_spread", "median"),
    ).reset_index().sort_values("vol_24h", ascending=False)

    L = ["# Subsector index (auto-generated)\n"]
    L.append(f"Total active subsectors: {len(agg)}\n")
    L.append("| subsector | n_series | n_markets | n_contested | 24h_vol | top_oi_spread_c |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for _, r in agg.iterrows():
        folder = _folder(r["subsector"])
        stripped = r["subsector"].split("_", 1)[1] if "_" in r["subsector"] else r["subsector"]
        link = f"[{r['subsector']}]({folder}/{stripped}.md)"
        L.append(f"| {link} | {r['n_series']:.0f} | {r['n_markets']:.0f} | {r['n_contested']:.0f} | ${r['vol_24h']:,.0f} | {(r['top_oi_spread'] or 0)*100:.1f} |")
    idx_path.write_text("\n".join(L) + "\n")
    print(f"wrote index: {idx_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
