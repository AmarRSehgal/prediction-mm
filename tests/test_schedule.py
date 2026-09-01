"""Game-window scheduling. The golf post-mortem and every subsequent sports
loss traces back to quoting inside a live event, so the parsers matter.
"""
from datetime import datetime, timedelta, timezone

from pmm.trader.schedule import compute_window, parse_game_start_utc

UTC = timezone.utc


def test_parses_time_from_ticker_when_present():
    got = parse_game_start_utc("KXKBOGAME-26APR190530ABCDEF", None)
    assert got == datetime(2026, 4, 19, 5, 30, tzinfo=UTC)


def test_falls_back_to_a_subsector_default_hour():
    got = parse_game_start_utc("KXIPLGAME-26APR19ABCDEF", None)
    assert got == datetime(2026, 4, 19, 14, 0, tzinfo=UTC)


def test_unknown_sport_has_no_game_time():
    assert parse_game_start_utc("KXSOMETHINGELSE-26APR19", None) is None


def test_exit_inside_the_pre_game_blackout():
    start = datetime(2026, 4, 19, 14, 0, tzinfo=UTC)
    w = compute_window("KXIPLGAME-26APR19ABC", "sports_cricket_ipl",
                       close_time=start + timedelta(hours=6), now=start - timedelta(hours=1))
    assert w.state == "EXIT"


def test_safe_well_before_the_game():
    start = datetime(2026, 4, 19, 14, 0, tzinfo=UTC)
    w = compute_window("KXIPLGAME-26APR19ABC", "sports_cricket_ipl",
                       close_time=start + timedelta(hours=6), now=start - timedelta(hours=20))
    assert w.state == "SAFE"


def test_closed_after_close_time():
    now = datetime(2026, 4, 19, 14, 0, tzinfo=UTC)
    w = compute_window("X", "eco_cpi", close_time=now - timedelta(hours=1), now=now)
    assert w.state == "CLOSED"


def test_generic_tte_ladder_for_non_sports():
    now = datetime(2026, 4, 19, 0, 0, tzinfo=UTC)
    assert compute_window("X", "eco_cpi", now + timedelta(hours=20), now).state == "EXIT"
    assert compute_window("X", "eco_cpi", now + timedelta(hours=40), now).state == "QUIET"
    assert compute_window("X", "eco_cpi", now + timedelta(hours=100), now).state == "SAFE"


def test_GAP_no_nfl_or_nba_game_time_parser():
    """sports_nfl / sports_nba exist in the taxonomy but have no ticker parser
    and no entry in subsector_tuning, so an NFL/NBA market would fall through
    to the generic close-time ladder with NO game-window protection at all.

    Adding either subsector to TARGET_SUBSECTORS before fixing this would quote
    straight through kickoff. This test is the tripwire.
    """
    assert parse_game_start_utc("KXNFLGAME-26SEP14SEAARI", None) is None
    assert parse_game_start_utc("KXNBAGAME-26OCT21BOSNYK", None) is None

    now = datetime(2026, 9, 14, 12, 0, tzinfo=UTC)     # 5h before a 17:00 kickoff
    kickoff = datetime(2026, 9, 14, 17, 0, tzinfo=UTC)
    w = compute_window("KXNFLGAME-26SEP14SEAARI", "sports_nfl",
                       close_time=kickoff + timedelta(hours=4), now=now)
    assert w.state == "EXIT"  # only because close_time is <30h away, not because of the game

    # Same market a week out: quoting freely straight through the injury-report
    # and line-move window with no game awareness whatsoever.
    w2 = compute_window("KXNFLGAME-26SEP14SEAARI", "sports_nfl",
                        close_time=kickoff + timedelta(hours=4), now=now - timedelta(days=7))
    assert w2.state == "SAFE"
