"""Known-event blackout calendar.

During these windows we do NOT quote markets in the listed subsectors.

Keep this file dumb -- schedules and the two predicates over them, nothing
else. The runner calls `is_subsector_blacked_out_by_calendar`, and shouts at
startup when `calendar_coverage_days` has run out (a stale calendar is
otherwise a silent no-op: every check just returns False and one of the three
protective layers is simply gone).

The per-market realized-vol gate in runner.py is a separate, dynamic layer
that catches what the calendar misses. The calendar's job is the opposite one:
stand down BEFORE a scheduled shock, while the book still looks calm.

Sources, refreshed 2026-09-01 (the previous contents expired 2026-05-24):
  Employment Situation  bls.gov/schedule/news_release/empsit.htm
  CPI                   bls.gov/schedule/news_release/cpi.htm
  PPI                   bls.gov/schedule/news_release/ppi.htm
  GDP                   bea.gov/news/schedule
  FOMC                  federalreserve.gov/monetarypolicy/fomccalendars.htm

All four statistical releases are 08:30 America/New_York; the FOMC statement
is 14:00 with the press conference at 14:30. Times are declared in ET and
converted here, so the November DST change is handled rather than hardcoded.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


@dataclass(frozen=True)
class Event:
    name: str
    subsectors: tuple[str, ...]
    start_utc: datetime
    end_utc: datetime
    buffer_before_hours: float = 6.0
    buffer_after_hours: float = 2.0


def _et(y: int, m: int, d: int, h: int = 0, mi: int = 0) -> datetime:
    """An America/New_York wall-clock time, as UTC."""
    return datetime(y, m, d, h, mi, tzinfo=ET).astimezone(timezone.utc)


# ---- US statistical releases (08:30 ET) ---------------------------------
# (month, day) in 2026. Release shock plus follow-through; the 1h lead buffer
# covers pre-release positioning.

_RELEASES: tuple[tuple[str, tuple[str, ...], tuple[tuple[int, int], ...]], ...] = (
    ("US Employment Situation", ("eco_jobs", "eco_fed"),
     ((9, 4), (10, 2), (11, 6), (12, 4))),
    ("US CPI", ("eco_cpi", "eco_fed"),
     ((9, 11), (10, 14), (11, 10), (12, 10))),
    ("US PPI", ("eco_ppi", "eco_fed"),
     ((9, 10), (10, 15), (11, 13), (12, 15))),
    ("US GDP", ("eco_gdp", "eco_fed"),
     ((9, 30), (10, 29), (11, 25), (12, 23))),
)

# FOMC: (month, day of the DECISION -- the second day of each meeting).
# Sep 15-16, Oct 27-28, Dec 8-9; Sep and Dec also carry an SEP.
_FOMC_DECISIONS: tuple[tuple[int, int], ...] = ((9, 16), (10, 28), (12, 9))

# Subsectors whose pricing moves off the macro tape even though they are not
# themselves economic markets. Kept narrow on purpose -- a blackout that
# covers everything is the same as no blackout. Empty while the commodity
# subsectors are out of TARGET_SUBSECTORS; re-add ("comm_gold",
# "comm_precious_other") alongside the commodity-ladder work, since gold and
# silver are the ones that actually trade the macro tape.
_MACRO_SPILLOVER: tuple[str, ...] = ()


def _build_events() -> list[Event]:
    out: list[Event] = []
    for name, subsectors, days in _RELEASES:
        for month, day in days:
            start = _et(2026, month, day, 8, 30)
            out.append(Event(
                name=f"{name} {month:02d}-{day:02d}",
                subsectors=subsectors + _MACRO_SPILLOVER,
                start_utc=start,
                end_utc=start + timedelta(hours=3),
                buffer_before_hours=1.0,
                buffer_after_hours=1.0,
            ))
    for month, day in _FOMC_DECISIONS:
        start = _et(2026, month, day, 14, 0)
        out.append(Event(
            name=f"FOMC decision + presser {month:02d}-{day:02d}",
            subsectors=("eco_fed", "eco_cpi", "eco_gdp", "eco_jobs") + _MACRO_SPILLOVER,
            start_utc=start,
            end_utc=start + timedelta(hours=2),
            buffer_before_hours=3.0,
            buffer_after_hours=2.0,
        ))
    out.sort(key=lambda e: e.start_utc)
    return out


EVENTS: list[Event] = _build_events()


def latest_event_end() -> datetime:
    """End of the last event on the calendar. Used to detect a stale calendar."""
    return max(e.end_utc for e in EVENTS)


def calendar_coverage_days(now: datetime) -> float:
    """Days of forward coverage left. <= 0 means the calendar is exhausted and
    is_subsector_blacked_out_by_calendar can only ever return False."""
    return (latest_event_end() - now).total_seconds() / 86400


def covered_subsectors() -> set[str]:
    """Every subsector any event mentions. A subsector NOT in here gets no
    calendar protection at all, which is worth knowing before trading it."""
    return {s for e in EVENTS for s in e.subsectors}


def active_events_for(now: datetime, subsector: str) -> list[Event]:
    """Return all events currently active for this subsector (incl. buffers)."""
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
