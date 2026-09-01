"""Per-market trading schedule: when we may quote, when we must exit.

For sports, price-discovery happens during the game, NOT at close_time (markets
may settle 1-3 days after the game). So the dangerous window is game-relative.

Heuristics (conservative):
  KBO  — game start encoded in ticker as HHMM UTC. Exit 2h before game start.
  NPB  — game start parsed from ticker when present; default to 10:00 UTC (JST evening).
  IPL / PSL — game start time not always in ticker; assume 14:00 UTC.
  Commodities — exit 2h before close_time.
  Fallback: exit exit_tte_hours before close.

Even with game-time parsing, the 30h-before-close floor from ScheduleRules still
applies as a safety net.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

log = logging.getLogger(__name__)


# ---- Ticker parsers -----------------------------------------------------

_KBO_RE = re.compile(r"KXKBOGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})")
_NPB_RE = re.compile(r"KXNPBGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
_IPL_RE = re.compile(r"KXIPLGAME-(\d{2})([A-Z]{3})(\d{2})")
_PSL_RE = re.compile(r"KXPSLGAME-(\d{2})([A-Z]{3})(\d{2})")
# Esports: KXVALORANTGAME-26APR191400ATTAXDOR-..., time encoded as HHMM
_VAL_RE = re.compile(r"KXVALORANT(?:GAME|MAP)-(\d{2})([A-Z]{3})(\d{2})(\d{4})")
_CS2_RE = re.compile(r"KXCS2GAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})")
_DOTA_RE = re.compile(r"KXDOTA2(?:MAP|GAME)-(\d{2})([A-Z]{3})(\d{2})(\d{4})")
_R6_RE = re.compile(r"KXR6GAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
_OW_RE = re.compile(r"KXOWGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
# Cricket ODI / T20 match
_CRICK_ODI_RE = re.compile(r"KXCRICKETODIMATCH-(\d{2})([A-Z]{3})(\d{2})")
_CRICK_T20_RE = re.compile(r"KXT20MATCH-(\d{2})([A-Z]{3})(\d{2})")
_CRICK_T20I_RE = re.compile(r"KXCRICKETT20IMATCH-(\d{2})([A-Z]{3})(\d{2})")
# Tennis: match time often not in ticker; fallback to 12:00 UTC (avg)
_TENNIS_RE = re.compile(r"KXATPCHALLENGERMATCH-(\d{2})([A-Z]{3})(\d{2})")
_TENNIS_ATP_RE = re.compile(r"KXATPMATCH-(\d{2})([A-Z]{3})(\d{2})")
_TENNIS_WTA_CH_RE = re.compile(r"KXWTACHALLENGERMATCH-(\d{2})([A-Z]{3})(\d{2})")
_TENNIS_WTA_RE = re.compile(r"KXWTAMATCH-(\d{2})([A-Z]{3})(\d{2})")
_TENNIS_ITF_RE = re.compile(r"KXITFMATCH-(\d{2})([A-Z]{3})(\d{2})")
# Basketball ACB / CBA — game start time varies; conservative 12:00 UTC
_ACB_RE = re.compile(r"KXACBGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
_CBA_RE = re.compile(r"KXCBAGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
# Soccer MLS
_MLS_RE = re.compile(r"KXMLSGAME-(\d{2})([A-Z]{3})(\d{2})(\d{4})?")
# Combat
_UFC_RE = re.compile(r"KX[A-Z]*UFC[A-Z]*-(\d{2})([A-Z]{3})(\d{2})")

_MONTHS = {
    "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
    "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12,
}


def _parse_yyMMMddHHMM(m, default_hhmm: tuple[int, int] = (12, 0)) -> datetime:
    groups = m.groups()
    yy, mon, dd = groups[:3]
    hhmm = groups[3] if len(groups) > 3 else None
    y = 2000 + int(yy); mo = _MONTHS[mon]; d = int(dd)
    if hhmm:
        hh = int(hhmm[:2]); mm = int(hhmm[2:])
    else:
        hh, mm = default_hhmm
    return datetime(y, mo, d, hh, mm, tzinfo=timezone.utc)


def parse_game_start_utc(ticker: str, close_time: datetime | None) -> datetime | None:
    """Extract game start in UTC from ticker, fallback to subsector default.
    Returns None if cannot determine."""
    # Order matters: more-specific patterns first.
    for pat, default in [
        (_KBO_RE, (5, 30)),
        (_NPB_RE, (10, 0)),
        (_IPL_RE, (14, 0)),
        (_PSL_RE, (15, 0)),
        (_VAL_RE, (12, 0)),
        (_CS2_RE, (12, 0)),
        (_DOTA_RE, (12, 0)),
        (_R6_RE, (12, 0)),
        (_OW_RE, (18, 0)),
        (_CRICK_T20I_RE, (12, 0)),
        (_CRICK_T20_RE, (12, 0)),
        (_CRICK_ODI_RE, (8, 0)),
        (_TENNIS_RE, (12, 0)),
        (_TENNIS_ATP_RE, (12, 0)),
        (_TENNIS_WTA_CH_RE, (12, 0)),
        (_TENNIS_WTA_RE, (12, 0)),
        (_TENNIS_ITF_RE, (12, 0)),
        (_ACB_RE, (18, 0)),
        (_CBA_RE, (11, 0)),  # CBA = China Basketball, 11 UTC = 19 Beijing
        (_MLS_RE, (23, 0)),
        (_UFC_RE, (2, 0)),   # UFC main cards ~22-02 UTC
    ]:
        m = pat.match(ticker)
        if m:
            return _parse_yyMMMddHHMM(m, default_hhmm=default)
    return None


@dataclass
class Window:
    state: str   # "SAFE" | "QUIET" | "EXIT" | "CLOSED"
    reason: str
    exit_at: datetime | None


def compute_window(
    ticker: str,
    subsector: str,
    close_time: datetime | None,
    now: datetime,
    exit_tte_hours: float = 30.0,
    widen_tte_hours: float = 48.0,
    min_age_hours: float = 0.5,
    market_open_time: datetime | None = None,
) -> Window:
    """Classify the current moment for the given market.

    Rules:
      1. If close_time <= now => CLOSED.
      2. If market_open_time too recent => EXIT (let it settle).
      3. If in 'game window' for sports: EXIT.
      4. If TTE to close <= exit_tte_hours: EXIT.
      5. If TTE to close <= widen_tte_hours: QUIET.
      6. Else: SAFE.
    """
    if close_time is not None and now >= close_time:
        return Window("CLOSED", "close_time reached", close_time)

    if market_open_time is not None:
        if (now - market_open_time).total_seconds() < min_age_hours * 3600:
            return Window("EXIT", "market too young", None)

    # Sports game-window rule. Pre-game blackout hours is per-subsector
    # (default 2h, bumped to 8-12h for live-flow heavy sports after
    # Tuesday 2026-04-22 session).
    if subsector.startswith("sports_"):
        game_start = parse_game_start_utc(ticker, close_time)
        if game_start is not None:
            from pmm.trader.subsector_tuning import get as get_tuning
            buffer_h = get_tuning(subsector).pre_game_blackout_hours
            game_exit = game_start - timedelta(hours=buffer_h)
            if now >= game_exit:
                return Window("EXIT", f"within {buffer_h:.0f}h of game start ({game_start.isoformat()})", game_exit)
            hours_to_exit = (game_exit - now).total_seconds() / 3600
            if hours_to_exit < 6:
                return Window("QUIET", f"{hours_to_exit:.1f}h to game-exit", game_exit)
            return Window("SAFE", f"{hours_to_exit:.1f}h to game-exit", game_exit)

    # Generic TTE-based rule
    if close_time is None:
        return Window("EXIT", "no close_time", None)
    tte_h = (close_time - now).total_seconds() / 3600
    if tte_h <= exit_tte_hours:
        return Window("EXIT", f"TTE {tte_h:.1f}h <= exit_tte {exit_tte_hours}h", close_time - timedelta(hours=exit_tte_hours))
    if tte_h <= widen_tte_hours:
        return Window("QUIET", f"TTE {tte_h:.1f}h <= widen_tte {widen_tte_hours}h", close_time - timedelta(hours=exit_tte_hours))
    return Window("SAFE", f"TTE {tte_h:.1f}h", close_time - timedelta(hours=exit_tte_hours))
