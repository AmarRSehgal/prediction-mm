"""Quote generation. Simple AS-flavored reservation-price + spread logic,
adapted for prediction-market bounded [0,1] prices.

Given:
  mid (dollars in [0,1])
  sigma_c (cents)
  inventory (contracts, positive = long YES)
  TTE (hours to exit, NOT to close)

Reservation price:
  r = mid - inventory * gamma * sigma^2 * TTE_fraction
  where TTE_fraction = TTE_hours / 24 capped at [0, 1]

Spread:
  s = gamma * sigma^2 * TTE_fraction + base_microstructure_spread

  base_microstructure_spread is capped at min_spread_cents (never tighter).

Bid / ask:
  bid = clip(r - s/2, PRICE_BAND_LOW, PRICE_BAND_HIGH)
  ask = clip(r + s/2, PRICE_BAND_LOW, PRICE_BAND_HIGH)

Ensure bid < ask and bid is >= current best bid + tick (post-only-friendly).
"""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass

from pmm.trader.config import ASParams, PRICE_BAND_HIGH, PRICE_BAND_LOW

log = logging.getLogger(__name__)


@dataclass
class Quote:
    bid_price_dollars: float
    ask_price_dollars: float
    bid_size: int
    ask_size: int
    reservation_dollars: float
    spread_cents: float


def compute_quote(
    mid_dollars: float,
    inventory_contracts: int,
    tte_hours_to_exit: float,
    current_bid_dollars: float | None,
    current_ask_dollars: float | None,
    sigma_cents: float,
    order_size: int,
    params: ASParams,
    min_spread_cents: int = 3,
    max_spread_cents: int = 30,
) -> Quote:
    """Symmetric AS-flavored quote around an inventory-adjusted reservation price,
    clipped INSIDE the current market's TOB so we actually get in line for fills.

    Key v0 rule: **we always post inside-or-at the existing spread**. If AS says
    wider than TOB, we clip to (current_bid + 1c, current_ask - 1c). If AS says
    tighter than 1c (sub-tick), we skip quoting.
    """
    tte_frac_spread = max(0.0, min(tte_hours_to_exit / 24.0, 1.0))  # cap at 1-day horizon
    tte_frac_skew = max(0.0, min(tte_hours_to_exit / 24.0, 2.0))

    sigma_d = max(sigma_cents, params.sigma_floor_c) / 100.0

    # Inventory skew (dollars)
    inv_skew_d = inventory_contracts * params.inventory_skew_coef
    # Intensify as time-to-exit shrinks (more urgent to flatten)
    inv_skew_d *= 1.0 + (2.0 - tte_frac_skew) * 0.5
    r = mid_dollars - inv_skew_d

    # AS-style spread
    as_spread_d = (
        params.gamma * (sigma_d ** 2) * max(tte_frac_spread, 0.25)
        + (2.0 / params.gamma) * math.log(1 + params.gamma / 40)
    )
    as_spread_d = max(as_spread_d, min_spread_cents / 100.0)
    as_spread_d = min(as_spread_d, max_spread_cents / 100.0)

    raw_bid = r - as_spread_d / 2
    raw_ask = r + as_spread_d / 2

    # ---- Clip INSIDE the existing spread ----------------------------------
    # A MM bid must improve on (or match) current_bid to get priority.
    # A MM ask must improve on (or match) current_ask.
    # If our raw quote is outside the existing TOB, bring it inside by 1c.
    bid = raw_bid
    ask = raw_ask
    if current_bid_dollars is not None and current_ask_dollars is not None and current_bid_dollars < current_ask_dollars:
        # Only post where there's a spread to be inside of
        min_bid_inside = current_bid_dollars + 0.01
        max_bid_inside = current_ask_dollars - 0.01  # can't cross
        min_ask_inside = current_bid_dollars + 0.01
        max_ask_inside = current_ask_dollars - 0.01
        bid = max(bid, min_bid_inside)
        bid = min(bid, max_bid_inside)
        ask = min(ask, max_ask_inside)
        ask = max(ask, min_ask_inside)
    elif current_bid_dollars is not None:
        bid = max(bid, current_bid_dollars + 0.01)
    elif current_ask_dollars is not None:
        ask = min(ask, current_ask_dollars - 0.01)

    # Hard price-band clip
    bid = max(PRICE_BAND_LOW, bid)
    ask = min(PRICE_BAND_HIGH, ask)

    # Round to cents
    bid_c = round(bid * 100) / 100
    ask_c = round(ask * 100) / 100

    # Size adjustments based on inventory
    bid_size = order_size
    ask_size = order_size
    if inventory_contracts >= 3:
        bid_size = max(0, order_size - 1)
    if inventory_contracts <= -3:
        ask_size = max(0, order_size - 1)

    # Degenerate / sub-tick spread -> skip quoting the side that would be worse than TOB
    if ask_c - bid_c < 0.01:
        return Quote(bid_c, ask_c, 0, 0, r, (ask_c - bid_c) * 100)

    # JOIN vs IMPROVE: if AS bid is below current TOB bid, that means AS wants
    # a wider spread than the market. Instead of skipping, JOIN the TOB bid —
    # we still capture the spread if flow crosses us (second in queue behind
    # existing maker). Same logic on ask.
    if current_bid_dollars is not None and bid_c < current_bid_dollars:
        bid_c = round(current_bid_dollars * 100) / 100  # match TOB
    if current_ask_dollars is not None and ask_c > current_ask_dollars:
        ask_c = round(current_ask_dollars * 100) / 100
    # Final safety: we must never cross
    if current_ask_dollars is not None and bid_c >= current_ask_dollars:
        bid_c = round((current_ask_dollars - 0.01) * 100) / 100
        if bid_c <= 0:
            bid_size = 0
    if current_bid_dollars is not None and ask_c <= current_bid_dollars:
        ask_c = round((current_bid_dollars + 0.01) * 100) / 100
        if ask_c >= 1.0:
            ask_size = 0

    return Quote(
        bid_price_dollars=bid_c,
        ask_price_dollars=ask_c,
        bid_size=bid_size,
        ask_size=ask_size,
        reservation_dollars=r,
        spread_cents=(ask_c - bid_c) * 100,
    )
