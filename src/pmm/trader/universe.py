"""Market selection: pull every contested open market in target subsectors."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.kalshi.client import KalshiClient

log = logging.getLogger(__name__)


@dataclass
class MarketInfo:
    ticker: str
    subsector: str
    series: str
    subtitle: str
    close_time: datetime | None
    yes_bid: float
    yes_ask: float
    mid: float
    vol_24h: float
    oi: float


def _parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def discover_markets(
    client: KalshiClient,
    target_subsectors: tuple[str, ...],
    series_df: pd.DataFrame,
    price_band: tuple[float, float] = (0.15, 0.85),
    max_hours_to_close: float = 168.0,
    max_per_subsector: int = 10,
) -> list[MarketInfo]:
    """Return every open contested market whose subsector is in target_subsectors."""
    series_df = series_df.copy()
    if "subsector" not in series_df.columns:
        series_df["subsector"] = series_df.apply(
            lambda r: classify(r["ticker"] or "", r["title"] or ""), axis=1
        )
    targets = series_df[series_df["subsector"].isin(target_subsectors)]
    log.info("universe: %d target-sub series to scan", len(targets))

    out: list[MarketInfo] = []
    lo, hi = price_band
    now = datetime.now(tz=timezone.utc)
    for sr in targets.itertuples():
        try:
            r = client.list_markets(series_ticker=sr.ticker, status="open", limit=200)
        except Exception as e:
            log.warning("list_markets failed for %s: %s", sr.ticker, e)
            continue
        for m in r.get("markets", []) or []:
            yb = float(m.get("yes_bid_dollars") or 0)
            ya = float(m.get("yes_ask_dollars") or 0)
            mid = (yb + ya) / 2
            if not (yb > 0 and ya < 1.0 and yb < ya):
                continue
            if not (lo <= mid <= hi):
                continue
            ct = _parse_dt(m.get("close_time"))
            if ct is None:
                continue
            hrs = (ct - now).total_seconds() / 3600
            if hrs <= 0 or hrs > max_hours_to_close:
                continue
            out.append(MarketInfo(
                ticker=m.get("ticker"),
                subsector=sr.subsector,
                series=sr.ticker,
                subtitle=(m.get("subtitle") or m.get("yes_sub_title") or "")[:80],
                close_time=ct,
                yes_bid=yb, yes_ask=ya, mid=mid,
                vol_24h=float(m.get("volume_24h_fp") or 0),
                oi=float(m.get("open_interest_fp") or 0),
            ))
    # Cap per subsector to avoid API-rate overruns
    if max_per_subsector > 0:
        by_sub: dict[str, list[MarketInfo]] = {}
        for m in out:
            by_sub.setdefault(m.subsector, []).append(m)
        trimmed: list[MarketInfo] = []
        for sub, lst in by_sub.items():
            lst.sort(key=lambda x: x.oi, reverse=True)
            trimmed.extend(lst[:max_per_subsector])
        out = trimmed
    log.info("universe: %d contested markets in target subsectors", len(out))
    return out
