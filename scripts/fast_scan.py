#!/usr/bin/env python3
"""Fast targeted scan: only subsectors we care about, not all 9734 series."""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.config import Config
from pmm.kalshi.client import KalshiClient


TARGET_SUBS = {
    "sports_baseball_us","sports_baseball_kbo","sports_baseball_npb",
    "sports_cricket","sports_rugby",
    "sports_tennis_challenger","sports_tennis_itf","sports_tennis_grandslam",
    "sports_esports","sports_darts","sports_squash","sports_motor",
    "sports_nfl","sports_nba","sports_wnba","sports_nhl",
    "sports_soccer_mls","sports_soccer_ligamx","sports_soccer_epl","sports_soccer_laliga",
    "sports_soccer_seriea","sports_soccer_bundesliga","sports_soccer_ligue1",
    "sports_soccer_eredivisie","sports_soccer_jleague","sports_soccer_kleague",
    "sports_soccer_belgian","sports_soccer_polish","sports_soccer_ucl",
    "sports_basketball_acb","sports_basketball_cba","sports_basketball_italy_lega",
    "sports_ncaabball","sports_ncaafootball","sports_golf","sports_combat","sports_olympics",
    "weather_temp","weather_snow","weather_rain","weather_disaster","weather_climate",
    "eco_cpi","eco_ppi","eco_jobs","eco_gdp","eco_fed","eco_ratedecisions","eco_realestate_retail","eco_macro_misc",
    "fin_equity_indices","fin_rates","fin_fx","fin_misc",
    "comm_energy","comm_gold","comm_precious_other","comm_metals_industrial","comm_agri",
    "crypto_btc","crypto_eth","crypto_sol","crypto_meme","crypto_misc",
    "pol_race","pol_primary","pol_figures","pol_confirmation","pol_events","pol_fiscal","pol_exotic","pol_religion",
    "ent_awards","ent_movie_ratings","ent_movie_box","ent_music","ent_tv_reality","ent_wrestling","ent_media",
    "tech_ai","tech_space","tech_ev_tesla",
    "world_royalty","world_mideast","world_russia_ukraine","world_china","world_northkorea",
    "companies_earnings","companies_ma","companies_ipo","companies_execs",
    "health_misc",
    "rankings_misc",
}


def main() -> int:
    cfg = Config.from_env()
    client = KalshiClient.from_config(cfg)
    data_dir = cfg.data_dir

    series_df = pd.read_parquet(data_dir / "series.parquet")
    series_df["subsector"] = series_df.apply(lambda r: classify(r["ticker"] or "", r["title"] or ""), axis=1)

    candidates = series_df[series_df["subsector"].isin(TARGET_SUBS)].copy()
    print(f"{len(candidates)} series in target subsectors across {candidates['subsector'].nunique()} subsectors", flush=True)

    rows = []
    t0 = time.time()
    for i, sr in enumerate(candidates.itertuples()):
        if i % 100 == 0:
            print(f"  {i} / {len(candidates)}, elapsed {time.time()-t0:.0f}s", flush=True)
        try:
            r = client.list_markets(series_ticker=sr.ticker, status="open", limit=200)
            mkts = r.get("markets", []) or []
        except Exception:
            continue
        if not mkts:
            continue
        con = 0
        total_oi = 0.0
        total_vol = 0.0
        top_spreads = []
        for m in mkts:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            oi = float(m.get("open_interest_fp") or 0)
            vol = float(m.get("volume_24h_fp") or 0)
            total_oi += oi
            total_vol += vol
            if yb > 0 and ya < 1.0 and yb < ya and 0.10 <= (yb + ya) / 2 <= 0.90:
                con += 1
                top_spreads.append((oi, ya - yb))
        top_spreads.sort(reverse=True)
        top_oi_mean_spread = sum(s for _, s in top_spreads[:3]) / min(3, len(top_spreads)) if top_spreads else float("nan")
        rows.append({
            "series": sr.ticker, "title": sr.title,
            "category": sr.category, "frequency": sr.frequency, "subsector": sr.subsector,
            "n_markets": len(mkts), "n_contested": con,
            "total_oi": total_oi, "total_vol_24h": total_vol,
            "top_oi_mean_spread": top_oi_mean_spread,
        })

    df = pd.DataFrame(rows)
    df.to_parquet(data_dir / "sector_scan_series.parquet")
    print(f"\nsaved {len(df)} active series", flush=True)
    print(f"across {df['subsector'].nunique()} subsectors", flush=True)

    print("\nTop subsectors by contested markets:")
    print(df.groupby("subsector").agg(
        n_series=("series","count"),
        n_contested=("n_contested","sum"),
        total_vol=("total_vol_24h","sum"),
        top_oi_spread=("top_oi_mean_spread","mean"),
    ).sort_values("n_contested", ascending=False).head(30).to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
