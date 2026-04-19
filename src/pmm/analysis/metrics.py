"""Per-market metrics from collected orderbook snapshots.

Kalshi orderbook format (per `yes` / `no`):
  Each side is a list of [price_cents, size], sorted ascending in price.
  The LAST entry is the best (highest price someone is willing to pay) on that side.

For YES contract:
  best_yes_bid = last entry in `yes` side (bid to buy YES)
  best_yes_ask = 100 - last entry in `no` side (inverse; since a NO bid at 55
                 implies willingness to sell YES at 45)

So the YES-side two-sided market is:
  yes_bid_cents = yes[-1][0]
  yes_ask_cents = 100 - no[-1][0]
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


@dataclass
class MarketMetrics:
    ticker: str
    n_snapshots: int
    mean_spread_cents: float
    median_spread_cents: float
    mean_mid_cents: float
    mean_yes_bid_size: float
    mean_yes_ask_size: float
    pct_time_in_band_5_95: float
    pct_time_both_sides_quoted: float


def derive_tob(row: dict[str, Any]) -> dict[str, Any]:
    """Works with rows written by OrderbookWriter (post-fix schema).
    Falls back to deriving from yes_levels / no_levels (dollars) if needed."""
    out = {
        "yes_bid_cents": None,
        "yes_bid_size": None,
        "yes_ask_cents": None,
        "yes_ask_size": None,
    }
    if "yes_bid_dollars" in row and row.get("yes_bid_dollars") is not None:
        out["yes_bid_cents"] = row["yes_bid_dollars"] * 100
        out["yes_bid_size"] = row.get("yes_bid_size")
    if "yes_ask_dollars" in row and row.get("yes_ask_dollars") is not None:
        out["yes_ask_cents"] = row["yes_ask_dollars"] * 100
        out["yes_ask_size"] = row.get("yes_ask_size")

    if out["yes_bid_cents"] is None or out["yes_ask_cents"] is None:
        yes = row.get("yes_levels") or []
        no = row.get("no_levels") or []
        if yes:
            out["yes_bid_cents"] = yes[-1][0] * 100
            out["yes_bid_size"] = yes[-1][1]
        if no:
            out["yes_ask_cents"] = (1.0 - no[-1][0]) * 100
            out["yes_ask_size"] = no[-1][1]

    if out["yes_bid_cents"] is not None and out["yes_ask_cents"] is not None:
        out["spread_cents"] = out["yes_ask_cents"] - out["yes_bid_cents"]
        out["mid_cents"] = (out["yes_ask_cents"] + out["yes_bid_cents"]) / 2
    else:
        out["spread_cents"] = None
        out["mid_cents"] = None
    return out


def load_snapshots(parquet_glob: str) -> pd.DataFrame:
    import glob

    frames = [pd.read_parquet(p) for p in glob.glob(parquet_glob)]
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    tob = df.apply(derive_tob, axis=1, result_type="expand")
    df = pd.concat([df, tob], axis=1)
    df["ts"] = pd.to_datetime(df["captured_at_ms"], unit="ms", utc=True)
    return df


def compute_market_metrics(df: pd.DataFrame, ticker: str) -> MarketMetrics:
    sub = df[df["ticker"] == ticker]
    n = len(sub)
    if n == 0:
        return MarketMetrics(ticker, 0, 0, 0, 0, 0, 0, 0, 0)
    both = sub.dropna(subset=["yes_bid_cents", "yes_ask_cents"])
    in_band = both[(both["mid_cents"] >= 5) & (both["mid_cents"] <= 95)]
    return MarketMetrics(
        ticker=ticker,
        n_snapshots=n,
        mean_spread_cents=float(both["spread_cents"].mean()) if len(both) else 0.0,
        median_spread_cents=float(both["spread_cents"].median()) if len(both) else 0.0,
        mean_mid_cents=float(both["mid_cents"].mean()) if len(both) else 0.0,
        mean_yes_bid_size=float(both["yes_bid_size"].mean()) if len(both) else 0.0,
        mean_yes_ask_size=float(both["yes_ask_size"].mean()) if len(both) else 0.0,
        pct_time_in_band_5_95=len(in_band) / n if n else 0.0,
        pct_time_both_sides_quoted=len(both) / n if n else 0.0,
    )
