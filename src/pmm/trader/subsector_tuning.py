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
    # Skip markets whose close_time is within this many hours. Catches
    # tournament-in-progress and settlement-pending windows for multi-day
    # events (golf, tennis grand slams). 0 = disabled.
    skip_if_close_within_hours: float = 0.0
    # When a side of our quote is AT the TOB (joining, not improving), skip
    # it if the existing TOB queue > this many contracts per contract we'd
    # post (so multiplier, not absolute). Default 20 -> at order_size=2 we
    # skip if TOB > 40 contracts.
    join_queue_max_ratio: float = 20.0
    # Aggressive close: after a fill on this subsector, each cycle check
    # whether we can take the real TOB to exit at entry_cost + min_profit_c.
    # If adverse mid drift >= adverse_cutoff_c against us, close anyway to
    # cap the loss rather than bleed passively (see design 2026-04-21).
    close_aggressive_enabled: bool = False
    min_profit_c: int = 1          # require this much profit to close
    adverse_cutoff_c: int = 3      # override: force close if mid drift worse
    # Rule G: per-market cumulative pnl/fill tracking. If a market has had
    # >= min_fills_for_pnl_check fills and its (realized + unrealized) / fills
    # is worse than min_pnl_per_fill, stop placing new quotes on it. Adapts
    # to "bad markets" that consistently bleed. Offline-validated +$1.03 on
    # non-comm Monday subset; +$2.26 including commodities.
    rule_g_enabled: bool = True
    min_fills_for_pnl_check: int = 3
    min_pnl_per_fill: float = -0.05
    # Rule C: hold-time auto-close. Offline analysis on Monday (2026-04-21):
    # positions held 30-180min had 17-37% winrate and negative avg PnL (the
    # "dead zone"). 0-30min cohort had 75-83% winrate and positive PnL. So
    # force-close any position held >= max_hold_minutes by taking real TOB.
    # Existing position gets closed once; no new quotes until it lands.
    rule_c_enabled: bool = True
    max_hold_minutes: float = 30.0
    # Pre-game blackout (idea 1): hours before game_start to go to EXIT state.
    # Default 2h; raise for subsectors where informed flow arrives earlier.
    # Tuesday session showed cs2 bled -$5 while positions built up 6h before
    # game start. Raising to 8-12h for live-play-heavy sports.
    pre_game_blackout_hours: float = 2.0
    # Trend detector (idea C, 2026-04-22): z-score of current mid vs recent
    # mid history. If |z| > threshold AND we have enough samples, the market
    # is trending not mean-reverting — skip placing. Existing position still
    # gets managed. Helps on step-event markets (ent_music, MLB live games).
    trend_detector_enabled: bool = True
    trend_min_samples: int = 10        # need at least N mid observations
    trend_z_threshold: float = 2.0     # |z| > 2.0 = trending
    # Subsector drawdown halt (2026-04-22): if cumulative realized+unrealized
    # for this subsector drops below halt_subsector_drawdown_dollars, stop
    # placing new quotes across ALL markets in the subsector. Existing
    # positions still get managed. Wednesday overnight ent_music -$12 would
    # have been capped at -$3 under this.
    halt_subsector_drawdown_dollars: float = -3.0


TUNING: dict[str, SubsectorTuning] = {
    # Low-toxicity niches — wider queue tolerance (more flow, queue moves fast)
    "sports_baseball_kbo": SubsectorTuning(gamma=10.0, max_markets=30, max_recent_vol_c=3.0, join_queue_max_ratio=50.0,
                                             close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_baseball_npb": SubsectorTuning(gamma=10.0, max_markets=30, max_recent_vol_c=3.0, join_queue_max_ratio=50.0,
                                             close_aggressive_enabled=True, adverse_cutoff_c=4),
    # sports_cricket_psl: bleed -$1.58 Monday session. Wider adverse_cutoff to
    # allow for game-event variance, but aggressive close on profit.
    "sports_cricket_psl":  SubsectorTuning(gamma=12.0, max_markets=30, max_recent_vol_c=3.0, join_queue_max_ratio=50.0,
                                             close_aggressive_enabled=True, adverse_cutoff_c=5),
    "sports_tennis_challenger": SubsectorTuning(gamma=12.0, max_markets=30, max_recent_vol_c=3.0, join_queue_max_ratio=50.0),

    # Moderate: standard gamma, more markets. Sports have stable mids between
    # events -> aggressive close scalps each passive fill.
    # baseball_us: Tuesday session -$6.36 loss primarily from MLB mention
    # markets (now blacklisted by ticker) + live-game flow. Bumping to 8h
    # pre-game blackout for remaining positions.
    "sports_baseball_us":  SubsectorTuning(gamma=20.0, max_markets=40,
                                            close_aggressive_enabled=True, adverse_cutoff_c=4,
                                            pre_game_blackout_hours=8.0),
    "sports_cricket_ipl":  SubsectorTuning(gamma=20.0, max_markets=20,
                                            close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_cricket_odi":  SubsectorTuning(gamma=15.0, max_markets=20,
                                            close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_cricket_t20_misc": SubsectorTuning(gamma=18.0, max_markets=20,
                                                close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_soccer_mls":   SubsectorTuning(gamma=20.0, max_markets=30,
                                            close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_basketball_cba": SubsectorTuning(gamma=18.0, max_markets=20,
                                              close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_basketball_acb": SubsectorTuning(gamma=18.0, max_markets=20,
                                              close_aggressive_enabled=True, adverse_cutoff_c=4),
    "sports_golf":         SubsectorTuning(gamma=18.0, max_markets=30,
                                            close_aggressive_enabled=True, adverse_cutoff_c=4),
    # Esports: same-day live-match risk is high even with game-time parser —
    # only trade markets closing >6h out so we're not caught in-progress.
    # Aggressive close with wider adverse_cutoff (5c) — game events produce
    # larger mid jumps, 3c would be too trigger-happy.
    "sports_esports_valorant": SubsectorTuning(
        gamma=22.0, max_markets=20, max_recent_vol_c=3.0,
        skip_if_close_within_hours=6.0,
        close_aggressive_enabled=True, adverse_cutoff_c=5,
        pre_game_blackout_hours=12.0,
    ),
    "sports_esports_cs2":  SubsectorTuning(
        gamma=22.0, max_markets=20, max_recent_vol_c=3.0,
        skip_if_close_within_hours=6.0,
        close_aggressive_enabled=True, adverse_cutoff_c=5,
        pre_game_blackout_hours=12.0,
    ),
    "sports_esports_dota": SubsectorTuning(
        gamma=22.0, max_markets=20, max_recent_vol_c=3.0,
        skip_if_close_within_hours=6.0,
        close_aggressive_enabled=True, adverse_cutoff_c=5,
        pre_game_blackout_hours=12.0,
    ),

    # High toxicity / large moves -> higher gamma (wider/safer)
    "sports_combat":       SubsectorTuning(gamma=35.0, max_markets=15, max_recent_vol_c=5.0),

    # Multi-day tournament sports. Golf tournaments (PGA, LPGA, European,
    # Challenge, LIV, etc.) happen most weekends. Weekday blackout was too
    # coarse. Instead: skip if close_time is within 48h (catches
    # tournament-in-progress AND just-finished-pending-settlement windows).
    # Mon-Wed of tournament week typically have all markets closing 96h+ out,
    # so are unblocked.
    "sports_golf":         SubsectorTuning(
        gamma=25.0, max_markets=20, max_recent_vol_c=2.5,
        skip_if_close_within_hours=48.0,
    ),
    "sports_golf_tgl":     SubsectorTuning(
        gamma=25.0, max_markets=15, max_recent_vol_c=2.5,
        skip_if_close_within_hours=48.0,
    ),

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
    # ent_music: Billboard Hot 100 & Spotify charts refresh Tuesdays; big
    # step-moves on TOPSONG/BBCHART/RANKLIST markets then. Blackout all of
    # Tuesday UTC (chart-refresh day). Also tighten gamma + vol gate —
    # chart-ranking markets jump discretely, not smoothly, so vol-gate
    # catches nothing between moves. Aggressive close with tight cutoff (3c)
    # since step jumps are usually larger than that threshold.
    "ent_music":           SubsectorTuning(
        gamma=22.0, max_markets=25, max_recent_vol_c=2.5,
        blackout_utc_dow=(1,),  # 0=Mon, 1=Tue
        close_aggressive_enabled=True, adverse_cutoff_c=3,
    ),
    "ent_awards":          SubsectorTuning(gamma=18.0, max_markets=30,
                                             close_aggressive_enabled=True, adverse_cutoff_c=3),
    "ent_tv_reality":      SubsectorTuning(gamma=18.0, max_markets=15,
                                             close_aggressive_enabled=True, adverse_cutoff_c=3),

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
