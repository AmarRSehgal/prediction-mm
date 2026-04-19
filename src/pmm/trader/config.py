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
    "sports_tennis_challenger",
    "sports_basketball_cba",
    "sports_basketball_acb",
    "sports_combat",
    "sports_esports_valorant",
    "sports_esports_cs2",
    "sports_esports_dota",
    # sports_golf: REMOVED — in-tournament player-prop markets lost $8.45 when
    # flattened at current TOB. Top-N of 100-player field = asymmetric payoff.
    # Only safe off-tournament, and then flow is near zero.
    # Commodities
    "comm_energy",
    "comm_gold",
    "comm_precious_other",
    "comm_metals_industrial",
    "comm_agri",
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
    # Nominal capital for display; fractions below are set so that effectively
    # the only binding constraint is the per-market cap of $5.
    capital_dollars: float = 1000.0

    # Effectively disable total / per-subsector caps for the Sunday test —
    # we want to see deployed capital grow organically.
    total_exposure_frac: float = 100.0   # disable
    per_subsector_frac: float = 100.0    # disable
    per_market_frac: float = 0.005       # = $5 per market

    # Order sizing (integer contracts)
    default_order_size: int = 2
    max_order_size: int = 3
    max_inventory_per_market: int = 5

    # Quote rules
    min_spread_cents: int = 3
    quote_refresh_seconds: float = 15.0

    # Kill switches
    daily_stop_loss_dollars: float = 50.0
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
