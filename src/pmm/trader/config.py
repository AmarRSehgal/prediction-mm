"""Trader configuration. Sunday test: broad universe, ~$5 per market."""
from __future__ import annotations

from dataclasses import dataclass, field


# ---- Target universe ----------------------------------------------------
# Broad curated list of subsectors with wide spreads + moderate+ depth + low
# toxicity, per the overnight sector scan. Explicitly excludes HFT-saturated
# and playoff-heavy subsectors (see docs/subsectors/INDEX.md for rationale).
TARGET_SUBSECTORS: tuple[str, ...] = (
    # Sports (niche / wide-spread)
    "sports_baseball_kbo",
    "sports_baseball_npb",
    "sports_baseball_us",
    "sports_cricket_ipl",
    "sports_cricket_psl",
    "sports_cricket_odi",
    "sports_cricket_t20_misc",
    "sports_soccer_mls",
    # "sports_tennis_challenger" — removed: match-start times not in tickers,
    # can't do game-window EXIT, continuous live-play bleed. Re-add only after
    # fetching ATP/WTA schedule directly.
    "sports_basketball_cba",
    "sports_basketball_acb",
    "sports_combat",
    "sports_esports_valorant",
    "sports_esports_cs2",
    "sports_esports_dota",
    "sports_golf",     # reinstated with strict 2.5c realized-vol gate (see subsector_tuning)
    # Commodities — dropped after Monday test: strike-ladder correlation
    # trap on trending underlyings. comm_energy alone lost -$13.34 (session
    # 2). MM model bets on mean-reversion; oil/grains/metals trend intraday
    # and our passive asks can't chase fast enough (see analysis 2026-04-21).
    # comm_gold and comm_precious_other were profitable; re-add only with
    # per-underlying delta caps and trend gating.
    # "comm_energy",
    # "comm_gold",
    # "comm_precious_other",
    # "comm_metals_industrial",
    # "comm_agri",
    # Economics (wide spreads; quiet windows between releases)
    "eco_cpi",
    "eco_ppi",
    "eco_jobs",
    "eco_fed",
    "eco_gdp",
    # Entertainment (surprise wide-spread finds)
    "ent_music",
    "ent_awards",
    "ent_tv_reality",
    # Politics (niche / slow-moving)
    "pol_fiscal",
    "pol_confirmation",
    # Companies / tech
    "companies_earnings",
    "companies_ipo",
    "tech_ev_tesla",
    "tech_space",
    # World / geopolitics
    "world_mideast",
)

# Price band we will ever quote in — avoid extreme-probability tails.
PRICE_BAND_LOW = 0.15
PRICE_BAND_HIGH = 0.85


# ---- Risk limits (dollars / contracts) ----------------------------------
@dataclass(frozen=True)
class RiskLimits:
    # Monday-night session #2: $10 per market across ~388-market universe.
    # Account sized to be exactly enough ($3,880 = 388 * $10) with no cushion
    # (total_exposure_frac = 1.0).
    capital_dollars: float = 3880.0

    total_exposure_frac: float = 1.0     # allow full deployment
    per_subsector_frac: float = 0.10     # $388 per subsector (~38 markets cap)
    per_market_frac: float = 0.002577    # $10 per market at $3880 capital

    # Order sizing (integer contracts)
    default_order_size: int = 2
    max_order_size: int = 3
    max_inventory_per_market: int = 5

    # Quote rules: sub-3c experiment was -$3.20 over 53 fills on today's
    # Monday session; reverting to 3c floor. Both 1c and 2c buckets lost.
    min_spread_cents: int = 3
    quote_refresh_seconds: float = 15.0

    # Kill switches - scale with capital: 5% of $3880 = $194
    daily_stop_loss_dollars: float = 194.0
    max_consecutive_adverse_fills: int = 5
    staleness_cutoff_seconds: float = 30.0


# ---- Avellaneda-Stoikov parameters --------------------------------------
@dataclass(frozen=True)
class ASParams:
    gamma: float = 20.0
    sigma_floor_c: float = 2.0
    sigma_window_minutes: int = 30
    inventory_skew_coef: float = 0.02


# ---- Schedule / TTE rules ----------------------------------------------
@dataclass(frozen=True)
class ScheduleRules:
    exit_tte_hours: float = 30.0
    widen_tte_hours: float = 48.0
    min_age_hours: float = 0.5


@dataclass(frozen=True)
class TraderConfig:
    risk: RiskLimits = field(default_factory=RiskLimits)
    as_params: ASParams = field(default_factory=ASParams)
    schedule: ScheduleRules = field(default_factory=ScheduleRules)
    target_subsectors: tuple[str, ...] = TARGET_SUBSECTORS
    dry_run: bool = True
