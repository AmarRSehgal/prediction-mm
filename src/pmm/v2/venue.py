"""v2 paper venue: per-level FIFO queue, ack and cancel latency, tape-driven fills.

Stricter than v1's PaperExecutor on purpose. v1 sets the queue ahead to the
top-of-book size whatever level the order rests at, and fills an order the
instant it is placed. Here:

* an order goes live `ack_s` after it is sent and a cancel lands `cancel_s`
  after it is sent -- fills can arrive in both gaps;
* on going live it queues behind the visible size AT ITS OWN PRICE (zero if it
  improved the touch);
* only prints advance the queue; shrinking visible size caps the queue ahead
  but a cancel is never assumed to have been in front of us.

A stricter venue can only make v2 look worse than v1, so a v2 win survives it.
Maker fees are charged from the series fee book like v1 (zero on most series).
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field

from pmm.v2.stream import KalshiBook, Print

_ids = itertools.count(1)


@dataclass
class Order:
    oid: int
    ticker: str
    side: str
    price_c: int
    size: float
    sent_t: float
    live_t: float
    tactic: str
    fv_c: float
    remaining: float = 0.0
    queue_ahead: float | None = None
    cancel_t: float | None = None

    def __post_init__(self):
        self.remaining = self.size


@dataclass
class VenueFill:
    t: float
    oid: int
    ticker: str
    side: str
    price_c: int
    size: float
    tactic: str
    fv_at_place_c: float
    placed_t: float


@dataclass
class PaperVenue:
    ack_s: float = 0.5
    cancel_s: float = 0.5
    orders: dict[int, Order] = field(default_factory=dict)

    def place(self, t, ticker, side, price_c, size, tactic, fv_c) -> int:
        oid = next(_ids)
        self.orders[oid] = Order(oid, ticker, side, price_c, size, t, t + self.ack_s, tactic, fv_c)
        return oid

    def cancel(self, t: float, oid: int):
        o = self.orders.get(oid)
        if o is not None and o.cancel_t is None:
            o.cancel_t = t + self.cancel_s

    def cancel_ticker(self, t: float, ticker: str):
        for o in list(self.orders.values()):
            if o.ticker == ticker:
                self.cancel(t, o.oid)

    def working(self, ticker: str, side: str) -> Order | None:
        for o in self.orders.values():
            if o.ticker == ticker and o.side == side and o.cancel_t is None:
                return o
        return None

    def pending(self, ticker: str, side: str) -> float:
        return sum(o.remaining for o in self.orders.values() if o.ticker == ticker and o.side == side)

    def advance(self, t: float, books: dict[str, KalshiBook]):
        for oid, o in list(self.orders.items()):
            if o.cancel_t is not None and t >= o.cancel_t:
                del self.orders[oid]
                continue
            b = books.get(o.ticker)
            if t < o.live_t or b is None:
                continue
            visible = b.level_size(o.side, o.price_c)
            if o.queue_ahead is None:
                touch = b.best_bid if o.side == "buy" else b.best_ask
                better = touch is None or (o.price_c > touch if o.side == "buy" else o.price_c < touch)
                o.queue_ahead = 0.0 if better else visible
            else:
                o.queue_ahead = min(o.queue_ahead, visible)

    def on_print(self, pr: Print) -> list[VenueFill]:
        side = "buy" if pr.taker_side == "sell" else "sell"
        left = pr.size
        mine = sorted((o for o in self.orders.values() if o.ticker == pr.ticker and o.side == side
                       and o.queue_ahead is not None and pr.t >= o.live_t),
                      key=lambda o: -o.price_c if side == "buy" else o.price_c)
        fills = []
        for o in mine:
            if left <= 0:
                break
            through = pr.price_c < o.price_c if side == "buy" else pr.price_c > o.price_c
            if not (through or pr.price_c == o.price_c):
                continue
            if not through:
                eat = min(o.queue_ahead, left)
                o.queue_ahead -= eat
                left -= eat
            got = int(min(o.remaining, left) + 1e-9)   # whole contracts; a 0.4 print fills nothing
            if got <= 0:
                continue
            left -= got
            o.remaining -= got
            fills.append(VenueFill(pr.t, o.oid, o.ticker, o.side, o.price_c, got, o.tactic, o.fv_c, o.sent_t))
            if o.remaining <= 1e-9:
                del self.orders[o.oid]
        return fills
