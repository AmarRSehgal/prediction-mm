"""v2 quoting: an edge curve in cents around a fair value, not a clipped AS spread.

What v1 got wrong, from its own paper record (README, "What the loss actually
is"): every exit that crossed the spread lost, and the only profitable path --
passive round trips -- was 32 of ~478 closes. So v2:

* never takes. There is no flatten and no forced close anywhere; the reducing
  side's required edge goes to zero and then negative as inventory grows, so
  the book quotes through fair value to get out, and otherwise holds to
  resolution;
* centres on a fair value that is not the touch mid (see fairvalue.py);
* demands an edge that covers fees, adverse selection and the days of capital
  a position locks up, instead of a fixed minimum spread.

All prices are YES cents. Inventory is signed YES contracts.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

TWO_SIDED, QUIET, REDUCE_ONLY = "two_sided", "quiet", "reduce_only"


@dataclass(frozen=True)
class EdgeParams:
    order_size: int = 2
    q_max: int = 5
    k_base_c: float = 1.5       # at flat inventory: adverse selection plus a cushion
    k_vol: float = 0.5          # multiple of the fair value's typical move
    k_skew_c: float = 3.0       # shift at |q| = 1; reducing side crosses FV at q = base/skew
    k_day_c: float = 0.05       # capital lockup, per day to resolution, on a ~50c contract
    quiet_mult: float = 1.5     # widen the base in QUIET windows
    band_lo_c: int = 15         # never ADD outside this band; reducing may go anywhere
    band_hi_c: int = 85

    def check(self):
        if self.order_size <= 0 or self.q_max < self.order_size:
            raise ValueError("q_max must hold at least one order")
        if self.k_skew_c <= 0 or self.k_base_c < 0:
            raise ValueError("k_skew_c must be > 0 and k_base_c >= 0")
        if not 0 < self.k_base_c / self.k_skew_c < 1:
            raise ValueError("reducing side must cross fair value inside |q| < 1")
        if not 0 < self.band_lo_c < self.band_hi_c < 100:
            raise ValueError("band must sit inside (0, 100)")


@dataclass(frozen=True)
class Quote:
    side: str
    price_c: int
    size: int
    tactic: str     # improve | join | rest
    edge_c: float


def required_edge(q_side: float, sigma_c: float, days: float, mode: str, p: EdgeParams) -> float:
    base = p.k_base_c * (p.quiet_mult if mode == QUIET else 1.0)
    x = max(-1.0, min(1.0, q_side))
    return base + p.k_vol * sigma_c + p.k_day_c * max(days, 0.0) + p.k_skew_c * x


def desired_quotes(fv_c: float, sigma_c: float, position: int, q_eff: float,
                   best_bid: int, best_ask: int, days: float, mode: str,
                   p: EdgeParams) -> tuple[Quote | None, Quote | None]:
    """Both passive quotes. `q_eff` is the inventory ratio used for skew; it may
    carry correlated exposure from sibling markets, not just this one.

    Price = the least aggressive of {edge-curve limit rounded away from FV, one
    tick better than the touch, one tick off the far side}. Improving by exactly
    one tick takes first place in the queue without giving away more edge than
    the curve asked for.
    """
    out: list[Quote | None] = []
    size_scale = 0.5 if mode == QUIET else 1.0
    for side, s in (("buy", 1), ("sell", -1)):
        adds = s * position >= 0
        if mode == REDUCE_ONLY and adds:
            out.append(None)
            continue
        e = required_edge(s * q_eff, sigma_c, days, mode, p)
        if side == "buy":
            price = min(math.floor(fv_c - e + 1e-9), best_bid + 1, best_ask - 1)
            room = p.q_max - position
        else:
            price = max(math.ceil(fv_c + e - 1e-9), best_ask - 1, best_bid + 1)
            room = p.q_max + position
        size = min(max(1, int(p.order_size * size_scale)), room)
        if not adds:
            size = min(size, abs(position))
        in_band = p.band_lo_c <= price <= p.band_hi_c if adds else 1 <= price <= 99
        if size <= 0 or not in_band:
            out.append(None)
            continue
        touch = best_bid if side == "buy" else best_ask
        tactic = "join" if price == touch else ("improve" if s * (price - touch) > 0 else "rest")
        out.append(Quote(side, price, size, tactic, s * (fv_c - price)))
    return out[0], out[1]
