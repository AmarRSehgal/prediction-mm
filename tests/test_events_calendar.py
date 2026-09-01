"""Events calendar.

The calendar's failure mode is silence: when it goes stale every lookup
returns False and a protective layer disappears without an error anywhere.
These tests cover the shape of the data and the staleness reporting, not the
specific dates -- those are sourced from BLS/BEA/the Fed and will need a
refresh, which `calendar_coverage_days` is what makes visible.
"""
from datetime import datetime, timedelta, timezone

import pytest

from pmm.trader import events_calendar as ec
from pmm.trader.config import TARGET_SUBSECTORS


def test_every_event_is_well_formed():
    for e in ec.EVENTS:
        assert e.start_utc < e.end_utc, e.name
        assert e.subsectors, e.name
        assert e.start_utc.tzinfo is not None and e.end_utc.tzinfo is not None, e.name
        assert e.buffer_before_hours >= 0 and e.buffer_after_hours >= 0, e.name


def test_events_are_sorted():
    starts = [e.start_utc for e in ec.EVENTS]
    assert starts == sorted(starts)


def test_coverage_is_positive_relative_to_the_last_event():
    just_before = ec.latest_event_end() - timedelta(days=1)
    assert ec.calendar_coverage_days(just_before) == pytest.approx(1.0, abs=1e-6)


def test_coverage_goes_negative_once_the_calendar_is_exhausted():
    after = ec.latest_event_end() + timedelta(days=10)
    assert ec.calendar_coverage_days(after) == pytest.approx(-10.0, abs=1e-6)


def test_an_exhausted_calendar_blacks_nothing_out():
    """The reason a stale calendar has to be shouted about at startup."""
    after = ec.latest_event_end() + timedelta(days=1)
    for sub in ec.covered_subsectors():
        assert ec.is_subsector_blacked_out_by_calendar(sub, after) == (False, "")


def test_a_release_blacks_out_its_own_subsectors_and_not_others():
    e = ec.EVENTS[0]
    mid = e.start_utc + (e.end_utc - e.start_utc) / 2
    for sub in e.subsectors:
        blocked, reason = ec.is_subsector_blacked_out_by_calendar(sub, mid)
        assert blocked and e.name in reason
    assert ec.is_subsector_blacked_out_by_calendar("sports_baseball_kbo", mid)[0] is False


def test_buffers_extend_the_window_on_both_sides():
    e = ec.EVENTS[0]
    sub = e.subsectors[0]
    before = e.start_utc - timedelta(hours=e.buffer_before_hours / 2)
    after = e.end_utc + timedelta(hours=e.buffer_after_hours / 2)
    outside = e.start_utc - timedelta(hours=e.buffer_before_hours + 1)
    assert ec.is_subsector_blacked_out_by_calendar(sub, before)[0]
    assert ec.is_subsector_blacked_out_by_calendar(sub, after)[0]
    assert ec.is_subsector_blacked_out_by_calendar(sub, outside)[0] is False


def test_08_30_et_releases_shift_with_daylight_saving():
    """A hardcoded UTC hour would be an hour wrong for half the calendar."""
    releases = [e for e in ec.EVENTS if e.name.startswith("US ")]
    hours = {e.start_utc.hour for e in releases}
    assert hours == {12, 13}, hours


def test_the_calendar_only_names_subsectors_we_actually_trade():
    """Events for a subsector that is not in the target universe are dead
    weight and hide the fact that a live subsector has no coverage."""
    stray = ec.covered_subsectors() - set(TARGET_SUBSECTORS)
    assert not stray, f"calendar covers untraded subsectors: {sorted(stray)}"
