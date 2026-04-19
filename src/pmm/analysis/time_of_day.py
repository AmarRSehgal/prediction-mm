"""Hour-of-week heatmaps from snapshot data.

For every ticker, bin snapshots by (day_of_week, hour_of_day_UTC) and compute:
  - realized volatility of mid (std of 1-min returns within the hour)
  - mean spread
  - snapshot count

Used to identify safe vs dangerous windows empirically.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def hour_of_week_stats(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    sub = df[df["ticker"] == ticker].dropna(subset=["mid_cents", "ts"]).copy()
    if sub.empty:
        return pd.DataFrame()
    sub = sub.sort_values("ts")
    sub["minute_bucket"] = sub["ts"].dt.floor("1min")
    per_min = (
        sub.groupby("minute_bucket")
        .agg(mid=("mid_cents", "mean"), spread=("spread_cents", "mean"))
        .reset_index()
    )
    per_min["ret"] = per_min["mid"].diff()
    per_min["dow"] = per_min["minute_bucket"].dt.dayofweek
    per_min["hour"] = per_min["minute_bucket"].dt.hour

    agg = (
        per_min.groupby(["dow", "hour"])
        .agg(
            rv=("ret", lambda x: float(np.sqrt((x**2).sum()))),
            mean_spread=("spread", "mean"),
            n=("mid", "count"),
        )
        .reset_index()
    )
    return agg
