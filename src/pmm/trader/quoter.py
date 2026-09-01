"""Quote generation. AS-flavored reservation-price + spread logic, adapted for
prediction-market bounded [0,1] prices and integer-cent ticks.

Reservation price
-----------------
    r = mid - inventory * inventory_skew_coef * urgency

Desired spread (Avellaneda-Stoikov)
-----------------------------------
    s = gamma * sigma^2 * TTE_frac  +  (2 / gamma) * ln(1 + gamma / k)

`k` is the order-arrival decay. It is NOT calibrated -- see ASParams.

The passive band
----------------
The v0 quoter clipped every quote to (tob_bid + 1c, tob_ask - 1c). That threw
`min_spread_cents` away: on a 3c book it posted a 1c spread, and when inventory
skew pushed the two sides together the clip collapsed them onto the same cent
and the quote was dropped entirely -- so holding inventory SILENCED the quoter
at exactly the moment it should have been leaning on one side to work out of
the position. Both defects are fixed here by replacing that clip with:

    bid in [tob_bid, tob_ask - min_spread]      posted only if r-side wants >= tob_bid
    ask in [tob_bid + min_spread, tob_ask]      posted only if r-side wants <= tob_ask

Properties that fall out of it:

* We never post *worse* than the top of book, and never cross it.
* The posted spread is always >= min_spread_cents. A book tighter than
  min_spread_cents has no admissible quote, so we sit it out -- which is the
  whole point of having the parameter.
* Joining the TOB on both sides is allowed (that is the book-spread ==
  min_spread case) but zero-edge joins on a 1c book are not.
* Each side is independent. Inventory skew therefore SKEWS: when we are long,
  the AS bid falls below the TOB bid so the bid goes quiet while the ask stays
  live and moves inside the book. The quoter is never silenced by inventory.
"""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass

from pmm.trader.config import ASParams, PRICE_BAND_HIGH, PRICE_BAND_LOW

log = logging.getLogger(__name__)

# Exchange price bounds in whole cents. 0 and 100 are settled values, not quotes.
MIN_TICK_C = 1
MAX_TICK_C = 99


@dataclass
class Quote:
    bid_price_dollars: float
    ask_price_dollars: float
    bid_size: int
    ask_size: int
    reservation_dollars: float
    spread_cents: float


def _clamp(v: int, lo: int | None, hi: int | None) -> int:
    if lo is not None:
        v = max(v, lo)
    if hi is not None:
        v = min(v, hi)
    return v


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
    """Two-sided passive quote. Either side may be suppressed independently
    (size 0) when the AS price for that side is worse than the top of book."""
    min_spread_cents = max(1, int(min_spread_cents))
    order_size = max(0, int(order_size))

    tte_frac_spread = max(0.0, min(tte_hours_to_exit / 24.0, 1.0))
    tte_frac_skew = max(0.0, min(tte_hours_to_exit / 24.0, 2.0))

    sigma_d = max(sigma_cents, params.sigma_floor_c) / 100.0

    # Inventory skew (dollars), intensified as time-to-exit shrinks.
    inv_skew_d = inventory_contracts * params.inventory_skew_coef
    inv_skew_d *= 1.0 + (2.0 - tte_frac_skew) * 0.5
    r = mid_dollars - inv_skew_d

    as_spread_d = (
        params.gamma * (sigma_d ** 2) * max(tte_frac_spread, 0.25)
        + (2.0 / params.gamma) * math.log(1 + params.gamma / params.k_order_arrival)
    )
    spread_c = as_spread_d * 100.0
    spread_c = min(max(spread_c, float(min_spread_cents)), float(max_spread_cents))

    r_c = r * 100.0
    bid_c = math.floor(r_c - spread_c / 2 + 0.5)
    ask_c = math.floor(r_c + spread_c / 2 + 0.5)

    # Rounding can shave a cent off the target; widen away from the side we
    # want filled (when long we want the ask kept close, so widen the bid down).
    short = min_spread_cents - (ask_c - bid_c)
    if short > 0:
        if inventory_contracts > 0:
            bid_c -= short
        elif inventory_contracts < 0:
            ask_c += short
        else:
            ask_c += (short + 1) // 2
            bid_c -= short // 2

    tob_bid_c = None if current_bid_dollars is None else int(round(current_bid_dollars * 100))
    tob_ask_c = None if current_ask_dollars is None else int(round(current_ask_dollars * 100))

    bid_live = True
    ask_live = True

    if tob_bid_c is not None and tob_ask_c is not None:
        if tob_ask_c - tob_bid_c < min_spread_cents:
            # No admissible passive quote exists: any pair inside this book is
            # tighter than our cost floor. Includes locked / crossed books.
            bid_live = ask_live = False
        else:
            # Post a side only if AS is willing to trade at least at the TOB
            # price. Otherwise that side goes quiet and the other keeps working.
            bid_live = bid_c >= tob_bid_c
            ask_live = ask_c <= tob_ask_c
            bid_c = _clamp(bid_c, tob_bid_c, tob_ask_c - min_spread_cents)
            ask_c = _clamp(ask_c, tob_bid_c + min_spread_cents, tob_ask_c)
    elif tob_bid_c is not None:
        bid_live = bid_c >= tob_bid_c
        bid_c = max(bid_c, tob_bid_c)
        ask_c = max(ask_c, tob_bid_c + min_spread_cents)
    elif tob_ask_c is not None:
        ask_live = ask_c <= tob_ask_c
        ask_c = min(ask_c, tob_ask_c)
        bid_c = min(bid_c, tob_ask_c - min_spread_cents)

    # Never quote outside the probability band we are willing to hold, and
    # never outside the exchange's own bounds. Suppress the side rather than
    # clamping the price -- clamping would push us to a MORE aggressive price.
    band_lo_c = int(round(PRICE_BAND_LOW * 100))
    band_hi_c = int(round(PRICE_BAND_HIGH * 100))
    if bid_c < max(MIN_TICK_C, band_lo_c):
        bid_live = False
    if ask_c > min(MAX_TICK_C, band_hi_c):
        ask_live = False

    bid_size = order_size if bid_live else 0
    ask_size = order_size if ask_live else 0
    if inventory_contracts >= 3:
        bid_size = max(0, bid_size - 1)
    if inventory_contracts <= -3:
        ask_size = max(0, ask_size - 1)

    return Quote(
        bid_price_dollars=bid_c / 100.0,
        ask_price_dollars=ask_c / 100.0,
        bid_size=bid_size,
        ask_size=ask_size,
        reservation_dollars=r,
        spread_cents=float(ask_c - bid_c),
    )
