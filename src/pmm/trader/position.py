"""Position / PnL tracking.

Per-market inventory, realized/unrealized PnL, fill log. Persisted to disk so
restart is safe.
"""
from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


@dataclass
class Fill:
    ts: str  # iso UTC
    ticker: str
    side: str           # "yes" or "no" (which side we TOOK delivery on)
    action: str         # "buy" or "sell" from our perspective
    count: int
    price_dollars: float  # execution price on the side we took
    order_id: str


@dataclass
class MarketPosition:
    ticker: str
    subsector: str
    yes_contracts: int = 0     # net YES contracts. Negative = short YES (= long NO).
    avg_cost_dollars: float = 0.0  # vwap of yes-side cost basis (sign: buying YES adds positive cost)
    realized_pnl: float = 0.0
    fills: list[Fill] = field(default_factory=list)

    def add_fill(self, fill: Fill) -> None:
        """Update inventory from fill. Convention: all positions tracked in YES-equivalent contracts.
        Buying YES at price p adds to yes_contracts; buying NO at price p subtracts (= selling YES equivalent)."""
        self.fills.append(fill)
        sign = 1 if fill.side == "yes" else -1
        if fill.action == "buy":
            delta = sign * fill.count
            price = fill.price_dollars if fill.side == "yes" else (1 - fill.price_dollars)
        else:
            delta = -sign * fill.count
            price = fill.price_dollars if fill.side == "yes" else (1 - fill.price_dollars)

        # If delta increases absolute inventory, update avg cost; if reduces, realize PnL.
        if self.yes_contracts == 0 or (self.yes_contracts > 0) == (delta > 0):
            # Same direction / opening
            new_qty = self.yes_contracts + delta
            if new_qty != 0:
                self.avg_cost_dollars = (self.avg_cost_dollars * self.yes_contracts + price * delta) / new_qty
            self.yes_contracts = new_qty
        else:
            # Closing / flipping.
            # For a long (direction=+1) closed at price: realized = (price - cost) per contract.
            # For a short (direction=-1) closed at price: realized = (cost - price) per contract
            #   which equals direction * (price - cost) with direction = -1.
            close_qty = min(abs(delta), abs(self.yes_contracts))
            direction = 1 if self.yes_contracts > 0 else -1
            realized_per_contract = direction * (price - self.avg_cost_dollars)
            self.realized_pnl += realized_per_contract * close_qty
            self.yes_contracts += delta
            if self.yes_contracts == 0:
                self.avg_cost_dollars = 0.0
            else:
                # If we flipped direction (closed all and opened new), reset cost basis
                self.avg_cost_dollars = price

    def exposure_dollars(self, mid: float) -> float:
        """Dollar value at risk at current mid."""
        return abs(self.yes_contracts) * abs(mid if self.yes_contracts > 0 else (1 - mid))

    def unrealized_pnl(self, mid: float) -> float:
        if self.yes_contracts == 0:
            return 0.0
        return self.yes_contracts * (mid - self.avg_cost_dollars)


@dataclass
class Portfolio:
    positions: dict[str, MarketPosition] = field(default_factory=dict)
    cash_dollars: float = 100.0
    starting_cash: float = 100.0

    def position(self, ticker: str, subsector: str) -> MarketPosition:
        if ticker not in self.positions:
            self.positions[ticker] = MarketPosition(ticker=ticker, subsector=subsector)
        return self.positions[ticker]

    def realized_pnl_total(self) -> float:
        return sum(p.realized_pnl for p in self.positions.values())

    def total_exposure(self, mids: dict[str, float]) -> float:
        return sum(p.exposure_dollars(mids.get(t, 0.5)) for t, p in self.positions.items())

    def exposure_by_subsector(self, mids: dict[str, float]) -> dict[str, float]:
        out: dict[str, float] = {}
        for t, p in self.positions.items():
            out[p.subsector] = out.get(p.subsector, 0.0) + p.exposure_dollars(mids.get(t, 0.5))
        return out

    def to_json(self) -> dict[str, Any]:
        return {
            "cash_dollars": self.cash_dollars,
            "starting_cash": self.starting_cash,
            "positions": {
                t: {
                    "ticker": p.ticker,
                    "subsector": p.subsector,
                    "yes_contracts": p.yes_contracts,
                    "avg_cost_dollars": p.avg_cost_dollars,
                    "realized_pnl": p.realized_pnl,
                    "fills": [asdict(f) for f in p.fills],
                }
                for t, p in self.positions.items()
            },
        }

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> "Portfolio":
        p = cls(cash_dollars=data.get("cash_dollars", 100.0), starting_cash=data.get("starting_cash", 100.0))
        for t, d in (data.get("positions") or {}).items():
            mp = MarketPosition(
                ticker=d["ticker"], subsector=d["subsector"],
                yes_contracts=d["yes_contracts"], avg_cost_dollars=d["avg_cost_dollars"],
                realized_pnl=d["realized_pnl"],
                fills=[Fill(**f) for f in d.get("fills", [])],
            )
            p.positions[t] = mp
        return p


def save_portfolio(p: Portfolio, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(p.to_json(), indent=2, default=str))


def load_portfolio(path: Path, starting_cash: float = 100.0) -> Portfolio:
    if path.exists():
        try:
            return Portfolio.from_json(json.loads(path.read_text()))
        except Exception as e:
            log.exception("failed to load portfolio from %s: %s", path, e)
    return Portfolio(cash_dollars=starting_cash, starting_cash=starting_cash)
