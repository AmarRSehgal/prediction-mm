"""Market selection: pull every contested open market in target subsectors."""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone

import pandas as pd

from pmm.analysis.taxonomy import classify
from pmm.kalshi.client import KalshiClient

log = logging.getLogger(__name__)

# Ticker-pattern blacklist (idea 4, 2026-04-22). MENTION-style markets
# behave like correlated strike ladders within a single event: a word being
# said resolves ALL mention contracts simultaneously, and our improving
# quotes can't react fast enough. Observed -$6.36 on baseball_us alone
# during Tuesday MLB evening play. Also blocking FEDMENTION by extension.
BLACKLISTED_TICKER_PATTERNS: tuple[re.Pattern, ...] = (
    re.compile(r"^KX[A-Z]*MENTION"),
)


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
    max_hours_to_close: float = 720.0,  # 30 days
    max_per_subsector: int = 0,  # 0 = no cap; trade everything
) -> list[MarketInfo]:
    """Return every open contested market whose subsector is in target_subsectors."""
    series_df = series_df.copy()
    if "subsector" not in series_df.columns:
        series_df["subsector"] = series_df.apply(
            lambda r: classify(r["ticker"] or "", r["title"] or ""), axis=1
        )
    targets = series_df[series_df["subsector"].isin(target_subsectors)]
    # Pre-filter to series known to have recent open markets (from sector_scan).
    # This cuts API load 5-10x vs scanning every series in every subsector.
    try:
        import os
        scan_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "data", "sector_scan_series.parquet")
        scan_path = os.path.abspath(scan_path)
        if os.path.exists(scan_path):
            scan = pd.read_parquet(scan_path)
            active_series = set(scan[scan["n_contested"].fillna(0) > 0]["series"].tolist())
            before = len(targets)
            targets = targets[targets["ticker"].isin(active_series)]
            log.info("universe: %d target-sub series scanned down to %d with known open markets", before, len(targets))
        else:
            log.info("universe: %d target-sub series to scan (no scan cache)", len(targets))
    except Exception as e:
        log.warning("series pre-filter failed: %s — scanning all", e)
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
            tk = m.get("ticker") or ""
            if any(pat.match(tk) for pat in BLACKLISTED_TICKER_PATTERNS):
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
    # Cap disabled when max_per_subsector == 0. Trade everything worth trading;
    # realized-vol gate + calendar + inventory caps limit actual exposure.
    if max_per_subsector > 0:
        from pmm.trader.subsector_tuning import get as get_tuning
        by_sub: dict[str, list[MarketInfo]] = {}
        for m in out:
            by_sub.setdefault(m.subsector, []).append(m)
        trimmed: list[MarketInfo] = []
        for sub, lst in by_sub.items():
            cap = get_tuning(sub).max_markets
            lst.sort(key=lambda x: x.oi, reverse=True)
            trimmed.extend(lst[:cap])
        out = trimmed
    log.info("universe: %d contested markets in target subsectors", len(out))
    return out
