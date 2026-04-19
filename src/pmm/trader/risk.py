"""Risk limit enforcement + kill switches."""
from __future__ import annotations

import logging
from dataclasses import dataclass

from pmm.trader.config import RiskLimits
from pmm.trader.position import Portfolio

log = logging.getLogger(__name__)


@dataclass
class RiskDecision:
    can_quote_bid: bool
    can_quote_ask: bool
    max_order_size: int
    reason: str


def assess_market(
    portfolio: Portfolio,
    ticker: str,
    subsector: str,
    mid: float,
    mids: dict[str, float],
    limits: RiskLimits,
    kill: bool = False,
) -> RiskDecision:
    """Decide if we may place bid / ask quotes in this market, and at what size."""
    if kill:
        return RiskDecision(False, False, 0, "killswitch tripped")

    pos = portfolio.position(ticker, subsector)

    # Per-market dollar cap
    total_exp = portfolio.total_exposure(mids)
    sub_exp = portfolio.exposure_by_subsector(mids).get(subsector, 0.0)
    mkt_exp = pos.exposure_dollars(mid)

    cap_total = limits.capital_dollars * limits.total_exposure_frac
    cap_sub = limits.capital_dollars * limits.per_subsector_frac
    cap_mkt = limits.capital_dollars * limits.per_market_frac

    can_grow_bid = True
    can_grow_ask = True
    reasons: list[str] = []

    if total_exp >= cap_total:
        can_grow_bid = can_grow_ask = False
        reasons.append(f"total_exposure ${total_exp:.2f} >= ${cap_total:.2f}")
    if sub_exp >= cap_sub:
        can_grow_bid = can_grow_ask = False
        reasons.append(f"subsector_exposure ${sub_exp:.2f} >= ${cap_sub:.2f}")
    if mkt_exp >= cap_mkt:
        can_grow_bid = can_grow_ask = False
        reasons.append(f"market_exposure ${mkt_exp:.2f} >= ${cap_mkt:.2f}")

    # Inventory cap (contracts)
    if pos.yes_contracts >= limits.max_inventory_per_market:
        can_grow_bid = False
        reasons.append("long inventory capped")
    if pos.yes_contracts <= -limits.max_inventory_per_market:
        can_grow_ask = False
        reasons.append("short inventory capped")

    # Order size: reduce toward caps
    headroom_mkt = max(0.0, cap_mkt - mkt_exp)
    contracts_fit = int(headroom_mkt / max(mid, 1e-3))
    size = min(limits.default_order_size, max(1, contracts_fit))
    if size < 1:
        can_grow_bid = can_grow_ask = False
        reasons.append("zero sizing after caps")

    return RiskDecision(
        can_quote_bid=can_grow_bid,
        can_quote_ask=can_grow_ask,
        max_order_size=size,
        reason="; ".join(reasons) if reasons else "ok",
    )
