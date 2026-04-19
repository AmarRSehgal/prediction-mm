"""Known-event blackout calendar.

During these windows, we DO NOT quote markets in the listed subsectors.
Buffers: default 6h before start, 2h after end (overridable per event).

Sources of dates (added 2026-04-19):
- PGA Tour 2026 schedule (ESPN, PGA Tour, Wikipedia)
- UFC 2026 schedule (CBS Sports, UFC.com, Yahoo Sports)
- BLS / WH / Fed releases (standard monthly cadence + FOMC calendar)
- Tesla Q1 2026 earnings (Tesla IR, IG)

Keep this file dumb — just data. Runner checks `is_market_in_event_window`.

NOTE: the per-market realized-vol gate (see runner.py) is a separate,
dynamic layer that catches things the calendar misses.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(frozen=True)
class Event:
    name: str
    subsectors: tuple[str, ...]
    start_utc: datetime
    end_utc: datetime
    buffer_before_hours: float = 6.0
    buffer_after_hours: float = 2.0


def _dt(y: int, m: int, d: int, h: int = 0, mi: int = 0) -> datetime:
    return datetime(y, m, d, h, mi, tzinfo=timezone.utc)


# ---- PGA Tour 2026 (Apr 20 - May 10) --------------------------------------
# Rounds play Thu-Sun typical, ~12:00-22:00 UTC per day.
# Market reacts each day during play. Blackout during play hours on tournament days.
# Simplification: block Thu 12:00 UTC -> Sun 23:00 UTC.

EVENTS: list[Event] = [
    Event(
        name="PGA RBC Heritage (past, kept as doc)",
        subsectors=("sports_golf",),
        start_utc=_dt(2026, 4, 16, 12, 0),  # Thu
        end_utc=_dt(2026, 4, 19, 23, 0),    # Sun
    ),
    Event(
        name="PGA Zurich Classic of New Orleans",
        subsectors=("sports_golf",),
        start_utc=_dt(2026, 4, 23, 12, 0),
        end_utc=_dt(2026, 4, 26, 23, 0),
    ),
    Event(
        name="PGA Miami Championship / CJ Cup Byron Nelson week",
        subsectors=("sports_golf",),
        start_utc=_dt(2026, 4, 30, 12, 0),
        end_utc=_dt(2026, 5, 3, 23, 0),
    ),
    Event(
        name="PGA Truist Championship + Myrtle Beach Classic",
        subsectors=("sports_golf",),
        start_utc=_dt(2026, 5, 7, 12, 0),
        end_utc=_dt(2026, 5, 10, 23, 0),
    ),

    # ---- UFC numbered events (PPVs) + Fight Nights with known dates -------
    Event(
        name="UFC Fight Night Perth AU",
        subsectors=("sports_combat",),
        start_utc=_dt(2026, 5, 2, 8, 0),    # Sat morning UTC (Perth evening)
        end_utc=_dt(2026, 5, 2, 14, 0),
    ),
    Event(
        name="UFC 328 Prochazka vs Ulberg",
        subsectors=("sports_combat",),
        start_utc=_dt(2026, 5, 9, 22, 0),   # Sat evening US
        end_utc=_dt(2026, 5, 10, 6, 0),     # Sun morning UTC
    ),

    # ---- Earnings ---------------------------------------------------------
    Event(
        name="Tesla Q1 2026 earnings",
        subsectors=("tech_ev_tesla", "companies_earnings"),
        start_utc=_dt(2026, 4, 22, 20, 0),  # blackout from 4pm ET the day of
        end_utc=_dt(2026, 4, 23, 14, 0),    # through next-day US open
        buffer_before_hours=4.0,
    ),

    # ---- Economic releases (US) -------------------------------------------
    # NFP first Friday of each month, 13:30 UTC
    Event(
        name="US NFP / Jobs Report - May release",
        subsectors=("eco_jobs", "eco_fed"),
        start_utc=_dt(2026, 5, 1, 13, 0),
        end_utc=_dt(2026, 5, 1, 16, 0),
    ),
    # CPI typically 2nd week of month, Wednesday 13:30 UTC (8:30 ET)
    Event(
        name="US CPI - May release",
        subsectors=("eco_cpi", "eco_fed", "comm_gold"),
        start_utc=_dt(2026, 5, 13, 13, 0),
        end_utc=_dt(2026, 5, 13, 16, 0),
    ),
    Event(
        name="US PPI - May release",
        subsectors=("eco_ppi", "eco_fed"),
        start_utc=_dt(2026, 5, 14, 13, 0),
        end_utc=_dt(2026, 5, 14, 16, 0),
    ),
    # FOMC April meeting (Apr 28-29), May meeting typically mid-June
    Event(
        name="FOMC April meeting + presser",
        subsectors=("eco_fed", "eco_cpi", "comm_gold", "tech_ev_tesla"),
        start_utc=_dt(2026, 4, 28, 14, 0),
        end_utc=_dt(2026, 4, 29, 21, 0),
        buffer_before_hours=2.0,
    ),

    # ---- Tennis majors (French Open) --------------------------------------
    # Roland-Garros: May 24 - June 7, 2026. Outside our window but add early.
    Event(
        name="Roland-Garros qualifying week",
        subsectors=("sports_tennis_challenger",),
        start_utc=_dt(2026, 5, 18, 8, 0),
        end_utc=_dt(2026, 5, 24, 22, 0),
    ),
]


def active_events_for(now: datetime, subsector: str) -> list[Event]:
    """Return all events currently active for this subsector (including buffers)."""
    out = []
    for e in EVENTS:
        if subsector not in e.subsectors:
            continue
        start = e.start_utc - timedelta(hours=e.buffer_before_hours)
        end = e.end_utc + timedelta(hours=e.buffer_after_hours)
        if start <= now <= end:
            out.append(e)
    return out


def is_subsector_blacked_out_by_calendar(subsector: str, now: datetime) -> tuple[bool, str]:
    """Convenience: True + reason string if any event is active."""
    active = active_events_for(now, subsector)
    if active:
        names = "; ".join(e.name for e in active)
        return True, f"calendar: {names}"
    return False, ""
