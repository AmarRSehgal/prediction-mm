"""Orderbook depth and informed-flow metrics.

Per-orderbook:
  - spread_c, mid_c
  - TOB size (both sides)
  - Cumulative depth within [1c, 3c, 5c, 10c] of mid
  - Total book depth
  - Book imbalance at TOB and within bands
  - Wall ratio (max level size / mean level size)
  - Number of levels populated

Per trade history:
  - Trade intensity by UTC hour-of-week
  - Mean / p95 trade size
  - Consecutive-trade drift (sign of next trade agreeing with this one = informed signal)
  - Post-trade-drift to mid proxy (if we have follow-up orderbook)
  - "Dangerous window" detection: hours with elevated realized vol + trade count
"""
from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def parse_book(ob_fp: dict[str, Any]) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Returns (yes_levels, no_levels) each as (price_dollars, size) sorted ascending.
    Last entry on each side is the best (= highest price someone will pay)."""
    yes = [(float(p), float(s)) for p, s in (ob_fp.get("yes_dollars") or [])]
    no = [(float(p), float(s)) for p, s in (ob_fp.get("no_dollars") or [])]
    return yes, no


def depth_metrics(ob_fp: dict[str, Any]) -> dict[str, Any]:
    """Compute depth metrics for a single orderbook snapshot.

    Convention: we analyze the YES-contract two-sided market.
      yes_bid = best yes level (last entry of yes side)
      yes_ask = 1 - best no level (last entry of no side)
    Depth on the ask side comes from the NO book; we map NO prices to YES-ask prices.
    """
    yes, no = parse_book(ob_fp)
    if not yes or not no:
        return {"has_two_sides": False}

    yes_bid_price, yes_bid_sz = yes[-1]
    no_bid_price, no_bid_sz = no[-1]
    yes_ask_price = 1.0 - no_bid_price

    if yes_bid_price >= yes_ask_price:
        # Crossed or touching — not two-sided
        return {"has_two_sides": False}

    mid = (yes_bid_price + yes_ask_price) / 2
    spread = yes_ask_price - yes_bid_price

    # YES-ask prices are derived from NO bids:  yes_ask_at_level = 1 - no_price
    # The NO ladder is ascending in no_price => the corresponding YES-ask ladder is
    # descending from (1 - no_lowest) down to (1 - no_best_bid = yes_ask_price).
    yes_asks = [(1.0 - p, s) for p, s in no]  # (yes_ask_price_equivalent, size)

    def cum_bid_within(delta: float) -> float:
        return sum(s for p, s in yes if p >= mid - delta)

    def cum_ask_within(delta: float) -> float:
        return sum(s for p, s in yes_asks if p <= mid + delta)

    bands = [0.01, 0.03, 0.05, 0.10]
    cum_bid = {f"cum_bid_{int(b*100)}c": cum_bid_within(b) for b in bands}
    cum_ask = {f"cum_ask_{int(b*100)}c": cum_ask_within(b) for b in bands}

    # Bid/ask-relative depth (more useful when spread > 10c — most of the book
    # sits far from mid but close to the best quote on its own side).
    def cum_bid_from_best(delta: float) -> float:
        return sum(s for p, s in yes if p >= yes_bid_price - delta)

    def cum_ask_from_best(delta: float) -> float:
        return sum(s for p, s in yes_asks if p <= yes_ask_price + delta)

    bid_rel = {f"depth_{int(b*100)}c_of_bid": cum_bid_from_best(b) for b in bands}
    ask_rel = {f"depth_{int(b*100)}c_of_ask": cum_ask_from_best(b) for b in bands}

    total_bid = sum(s for _, s in yes)
    total_ask = sum(s for _, s in yes_asks)

    bid_sizes = [s for _, s in yes]
    ask_sizes = [s for _, s in yes_asks]
    wall_bid = (max(bid_sizes) / (sum(bid_sizes)/len(bid_sizes))) if bid_sizes else 0
    wall_ask = (max(ask_sizes) / (sum(ask_sizes)/len(ask_sizes))) if ask_sizes else 0

    # Imbalance at TOB (yes_bid_sz vs no_bid_sz = yes_ask_sz)
    denom = yes_bid_sz + no_bid_sz
    tob_imbalance = (yes_bid_sz - no_bid_sz) / denom if denom else 0.0

    return {
        "has_two_sides": True,
        "yes_bid_c": yes_bid_price * 100,
        "yes_ask_c": yes_ask_price * 100,
        "mid_c": mid * 100,
        "spread_c": spread * 100,
        "tob_bid_sz": yes_bid_sz,
        "tob_ask_sz": no_bid_sz,
        "tob_imbalance": tob_imbalance,
        **cum_bid,
        **cum_ask,
        **bid_rel,
        **ask_rel,
        "total_bid_depth": total_bid,
        "total_ask_depth": total_ask,
        "wall_bid_ratio": wall_bid,
        "wall_ask_ratio": wall_ask,
        "n_bid_levels": len(yes),
        "n_ask_levels": len(no),
    }


def trade_metrics(trades: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute informed-flow proxies from a list of trades.

    Kalshi trade schema (as returned by /markets/trades):
      trade_id, ticker, count, created_time (ISO), yes_price (dollars), no_price, taker_side
    """
    if not trades:
        return {"n_trades": 0}

    df = pd.DataFrame(trades)
    if "created_time" in df.columns:
        df["ts"] = pd.to_datetime(df["created_time"], utc=True, errors="coerce")
    df = df.dropna(subset=["ts"]).sort_values("ts").reset_index(drop=True)

    # Normalize price to yes-side dollars
    def price(row):
        if "yes_price" in row and row.get("yes_price") is not None:
            try:
                return float(row["yes_price"]) / (100 if float(row["yes_price"]) > 1.5 else 1)
            except Exception:
                return np.nan
        return np.nan

    df["yes_px"] = df.apply(price, axis=1)
    df["size"] = pd.to_numeric(df.get("count", 0), errors="coerce").fillna(0)

    # Signed direction: +1 if taker bought YES, -1 if bought NO
    def side_sign(s):
        s = str(s).lower() if s is not None else ""
        if s == "yes": return 1
        if s == "no": return -1
        return 0
    df["sign"] = df.get("taker_side", pd.Series([None]*len(df))).map(side_sign)

    # Consecutive-trade price change (informed-flow proxy)
    df["next_px"] = df["yes_px"].shift(-1)
    df["fwd_move_1"] = df["next_px"] - df["yes_px"]
    # Informed metric: mean(sign * fwd_move). Positive => trades predict next direction.
    informed_signal = float(np.nanmean(df["sign"] * df["fwd_move_1"]))

    # Time-of-day distribution (UTC hour-of-week: 0 = Monday 0:00 UTC .. 167 = Sunday 23:00)
    df["how"] = df["ts"].dt.dayofweek * 24 + df["ts"].dt.hour
    how_counts = df["how"].value_counts().sort_index()
    how_realized_vol = df.groupby("how")["yes_px"].apply(lambda x: float(x.diff().abs().sum())).sort_index()

    n = len(df)
    return {
        "n_trades": n,
        "first_trade": str(df["ts"].iloc[0]),
        "last_trade": str(df["ts"].iloc[-1]),
        "trade_duration_h": float((df["ts"].iloc[-1] - df["ts"].iloc[0]).total_seconds() / 3600) if n > 1 else 0.0,
        "mean_size": float(df["size"].mean()),
        "p95_size": float(df["size"].quantile(0.95)) if n >= 20 else float(df["size"].max()),
        "informed_signal": informed_signal,
        "mean_abs_consecutive_move_c": float(df["fwd_move_1"].abs().mean() * 100),
        "hourofweek_trade_counts": how_counts.to_dict(),
        "hourofweek_realized_vol": how_realized_vol.to_dict(),
        "top_3_active_hours_utc": how_counts.nlargest(3).index.tolist(),
        "top_3_vol_hours_utc": how_realized_vol.nlargest(3).index.tolist(),
    }
