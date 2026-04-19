"""Trader configuration. Deliberately conservative for $100 capital v0."""
from __future__ import annotations

from dataclasses import dataclass, field


# ---- Target universe ----------------------------------------------------
# Based on the comprehensive sweep: subsectors with wide spreads, decent depth,
# low informed-flow magnitude, and predictable schedules.
TARGET_SUBSECTORS: tuple[str, ...] = (
    "sports_baseball_kbo",
    "sports_baseball_npb",
    "sports_cricket_psl",
)

# Price band we will ever quote in — avoid extreme-probability tails.
PRICE_BAND_LOW = 0.15
PRICE_BAND_HIGH = 0.85


# ---- Risk limits (dollars / contracts) ----------------------------------
@dataclass(frozen=True)
class RiskLimits:
    capital_dollars: float = 100.0
    # Fraction of capital that can be exposed at any time
    total_exposure_frac: float = 0.50    # $50 max live exposure
    per_market_frac: float = 0.05        # $5 max per contract-ticker
    per_subsector_frac: float = 0.20     # $20 max per subsector

    # Order sizing (integer contracts)
    default_order_size: int = 2
    max_order_size: int = 3
    max_inventory_per_market: int = 5

    # Quote rules
    min_spread_cents: int = 3            # never quote tighter than 3c
    quote_refresh_seconds: float = 15.0

    # Kill switches
    daily_stop_loss_dollars: float = 10.0
    max_consecutive_adverse_fills: int = 5
    staleness_cutoff_seconds: float = 30.0


# ---- Avellaneda-Stoikov parameters --------------------------------------
@dataclass(frozen=True)
class ASParams:
    gamma: float = 20.0              # high risk aversion for small account
    sigma_floor_c: float = 2.0       # minimum vol estimate in cents
    sigma_window_minutes: int = 30
    inventory_skew_coef: float = 0.02  # additional skew per unit inventory (dollars)


# ---- Schedule / TTE rules ----------------------------------------------
@dataclass(frozen=True)
class ScheduleRules:
    # Don't quote if close is within this many hours. Conservative.
    # For sports we'll exit earlier via game-time detection; this is the floor.
    exit_tte_hours: float = 30.0
    # Reduce size / widen once TTE crosses this; pull at exit_tte_hours.
    widen_tte_hours: float = 48.0
    # Absolute minimum time-since-open before we will quote (stale-market trap)
    min_age_hours: float = 0.5


@dataclass(frozen=True)
class TraderConfig:
    risk: RiskLimits = field(default_factory=RiskLimits)
    as_params: ASParams = field(default_factory=ASParams)
    schedule: ScheduleRules = field(default_factory=ScheduleRules)
    target_subsectors: tuple[str, ...] = TARGET_SUBSECTORS
    dry_run: bool = True             # DEFAULT OFF — live requires explicit flag
