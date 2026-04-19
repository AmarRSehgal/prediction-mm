"""Per-subsector tuning: gamma, market cap, blackout hours.

Derived from the overnight sector scan + TTE analysis. Key principles:
- Low informed-flow magnitude → lower gamma (tighter quotes, more fills).
- High informed-flow magnitude → higher gamma (safer).
- Scheduled release windows / market opens / closes → blackout hours (UTC).

Defaults kick in for any subsector not listed.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SubsectorTuning:
    gamma: float = 20.0            # AS risk aversion
    max_markets: int = 20          # cap in universe selection
    # UTC hours (0-23) where we SKIP quoting entirely
    blackout_utc_hours: tuple[int, ...] = ()
    # UTC days of week (0=Mon, 6=Sun) where we skip (0-indexed)
    blackout_utc_dow: tuple[int, ...] = ()
    # Dynamic: skip market if realized abs-move per trade in last hour
    # exceeds this (in cents). Detects price-discovery / info-release
    # regardless of schedule. Lower for quieter subsectors.
    max_recent_vol_c: float = 4.0  # default: skip if > 4c mean abs move / trade


TUNING: dict[str, SubsectorTuning] = {
    # Low-toxicity, wide spreads, predictable game schedule -> tighter gamma
    "sports_baseball_kbo": SubsectorTuning(gamma=10.0, max_markets=30, max_recent_vol_c=3.0),
    "sports_baseball_npb": SubsectorTuning(gamma=10.0, max_markets=30, max_recent_vol_c=3.0),
    "sports_cricket_psl":  SubsectorTuning(gamma=12.0, max_markets=30, max_recent_vol_c=3.0),
    "sports_tennis_challenger": SubsectorTuning(gamma=12.0, max_markets=30, max_recent_vol_c=3.0),

    # Moderate: standard gamma, more markets
    "sports_baseball_us":  SubsectorTuning(gamma=20.0, max_markets=40),
    "sports_cricket_ipl":  SubsectorTuning(gamma=20.0, max_markets=20),
    "sports_cricket_odi":  SubsectorTuning(gamma=15.0, max_markets=20),
    "sports_cricket_t20_misc": SubsectorTuning(gamma=18.0, max_markets=20),
    "sports_soccer_mls":   SubsectorTuning(gamma=20.0, max_markets=30),
    "sports_basketball_cba": SubsectorTuning(gamma=18.0, max_markets=20),
    "sports_basketball_acb": SubsectorTuning(gamma=18.0, max_markets=20),
    "sports_golf":         SubsectorTuning(gamma=18.0, max_markets=30),
    "sports_esports_valorant": SubsectorTuning(gamma=20.0, max_markets=25),
    "sports_esports_cs2":  SubsectorTuning(gamma=20.0, max_markets=25),
    "sports_esports_dota": SubsectorTuning(gamma=18.0, max_markets=20),

    # High toxicity / large moves -> higher gamma (wider/safer)
    "sports_combat":       SubsectorTuning(gamma=35.0, max_markets=15, max_recent_vol_c=5.0),

    # Multi-day tournament sports — reinstate with STRICT vol gate.
    # During inactive weeks, vol is low; during tournament, vol explodes.
    # 2.5c threshold will keep us out during the event.
    "sports_golf":         SubsectorTuning(gamma=25.0, max_markets=20, max_recent_vol_c=2.5),
    "sports_golf_tgl":     SubsectorTuning(gamma=25.0, max_markets=15, max_recent_vol_c=2.5),

    # Commodities: blackout US equity open + close-hour + EIA time
    "comm_energy":         SubsectorTuning(
        gamma=20.0, max_markets=30,
        # EIA Wed 14:30 UTC, US open ~13:30, close hour 20-21.
        blackout_utc_hours=(13, 14, 20),
    ),
    "comm_gold":           SubsectorTuning(
        gamma=18.0, max_markets=25,
        # US data-release window (13:30), FOMC (18:00-19:30), close 20:00.
        blackout_utc_hours=(13, 14, 18, 19, 20),
    ),
    "comm_precious_other": SubsectorTuning(
        gamma=20.0, max_markets=25,
        blackout_utc_hours=(13, 14, 20),
    ),
    "comm_metals_industrial": SubsectorTuning(
        gamma=22.0, max_markets=25,
        # China session-sensitive; blackout SHFE open-ish window.
        blackout_utc_hours=(1, 2, 13, 14),
    ),
    "comm_agri":           SubsectorTuning(
        gamma=20.0, max_markets=25,
        # USDA reports typically 12:00 UTC.
        blackout_utc_hours=(12, 13),
    ),

    # Economics: release times are 13:30 UTC for most US series.
    # Blackout conservative window around it + FOMC.
    "eco_cpi":             SubsectorTuning(
        gamma=25.0, max_markets=20,
        blackout_utc_hours=(13, 14, 15),  # release + 2h cooldown
    ),
    "eco_ppi":             SubsectorTuning(
        gamma=25.0, max_markets=20,
        blackout_utc_hours=(13, 14, 15),
    ),
    "eco_jobs":            SubsectorTuning(
        gamma=30.0, max_markets=15,
        # NFP release 13:30 UTC Fridays; also ADP 12:15 Wed. Be paranoid.
        blackout_utc_hours=(12, 13, 14, 15),
    ),
    "eco_fed":             SubsectorTuning(
        gamma=30.0, max_markets=15,
        blackout_utc_hours=(17, 18, 19, 20),  # FOMC window
    ),
    "eco_gdp":             SubsectorTuning(
        gamma=22.0, max_markets=15,
        blackout_utc_hours=(13, 14, 15),
    ),

    # Entertainment
    "ent_music":           SubsectorTuning(gamma=15.0, max_markets=40),
    "ent_awards":          SubsectorTuning(gamma=18.0, max_markets=30),
    "ent_tv_reality":      SubsectorTuning(gamma=18.0, max_markets=15),

    # Politics (low-hour-sensitivity)
    "pol_fiscal":          SubsectorTuning(gamma=18.0, max_markets=20),
    "pol_confirmation":    SubsectorTuning(gamma=18.0, max_markets=20),

    # Companies / tech
    "companies_earnings":  SubsectorTuning(
        gamma=20.0, max_markets=25,
        # Earnings after-market hours: 20:00-21:00 UTC common
        blackout_utc_hours=(20, 21, 22),
    ),
    "companies_ipo":       SubsectorTuning(gamma=20.0, max_markets=25),
    "tech_ev_tesla":       SubsectorTuning(
        gamma=18.0, max_markets=15,
        blackout_utc_hours=(20, 21, 22),  # TSLA earnings / AMC moves
    ),
    "tech_space":          SubsectorTuning(gamma=18.0, max_markets=15),

    # Geopolitics
    "world_mideast":       SubsectorTuning(gamma=25.0, max_markets=15),
}


def get(subsector: str) -> SubsectorTuning:
    return TUNING.get(subsector, SubsectorTuning())


def is_in_blackout(subsector: str, utc_hour: int, utc_dow: int | None = None) -> bool:
    t = get(subsector)
    if utc_hour in t.blackout_utc_hours:
        return True
    if utc_dow is not None and utc_dow in t.blackout_utc_dow:
        return True
    return False
