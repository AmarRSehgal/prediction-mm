"""MM-ripeness scoring from collected metrics.

Heuristic first-pass score. This is explicitly NOT a fit model; it is a
filter to shortlist markets for deeper study. Refine with data.

Ripeness = product of:
  - spread_factor: wider is better for MM, but only up to some cap
  - liquidity_factor: need *some* size on book to quote meaningfully
  - band_factor: % of time in [0.05, 0.95] (avoid extreme-price markets)
  - two_sided_factor: % of time both sides are quoted
  - stability_factor: low turnover in TOB is good (fewer sniping HFTs)
"""
from __future__ import annotations

import math

import pandas as pd

from pmm.analysis.metrics import compute_market_metrics


def score_markets(df: pd.DataFrame) -> pd.DataFrame:
    tickers = sorted(df["ticker"].unique())
    rows = []
    for t in tickers:
        m = compute_market_metrics(df, t)
        # 1-cent spreads are the minimum tick; anything <=1 is HFT-saturated.
        # Beyond ~10 cents (10% price spread at mid=0.50) is wide enough to be
        # interesting but also suggests very low activity.
        spread = m.mean_spread_cents
        spread_factor = max(0.0, min(1.0, (spread - 1) / 5))  # peaks around 6c
        liq_factor = 1 - math.exp(-m.mean_yes_bid_size / 50)  # saturates at ~50 contracts
        rows.append(
            {
                "ticker": t,
                "n": m.n_snapshots,
                "spread_c": round(spread, 2),
                "mid_c": round(m.mean_mid_cents, 1),
                "bid_sz": round(m.mean_yes_bid_size, 1),
                "ask_sz": round(m.mean_yes_ask_size, 1),
                "pct_in_band": round(m.pct_time_in_band_5_95, 3),
                "pct_two_sided": round(m.pct_time_both_sides_quoted, 3),
                "score": round(
                    spread_factor
                    * liq_factor
                    * m.pct_time_in_band_5_95
                    * m.pct_time_both_sides_quoted,
                    4,
                ),
            }
        )
    out = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
    return out
