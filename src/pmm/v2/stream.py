"""Kalshi websocket: pushed order books and the trade tape for a set of tickers.

v1 polls REST once per market per 15s cycle, three calls a market, so it sees a
book up to a cycle stale and shares a 10 req/s budget with everything else. The
v2 engine subscribes to `orderbook_delta` and `trade` instead and uses REST only
for universe discovery and settlement.

Kalshi books are two bid ladders: YES bids and NO bids. A NO bid at c is a YES
ask at 100 - c. Prices are integer cents; sizes are floats (the API sends
fractional `_fp` counts).
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass
from typing import Callable, Iterable

import websockets

from pmm.kalshi.client import KalshiClient

log = logging.getLogger(__name__)

WS_PATH = "/trade-api/ws/v2"


def _c(price: str | float) -> int:
    return int(round(float(price) * 100))


class KalshiBook:
    def __init__(self):
        self.yes: dict[int, float] = {}
        self.no: dict[int, float] = {}
        self.updated = 0.0

    def snapshot(self, msg: dict, t: float):
        self.yes = {_c(p): float(s) for p, s in msg.get("yes_dollars_fp") or [] if float(s) > 0}
        self.no = {_c(p): float(s) for p, s in msg.get("no_dollars_fp") or [] if float(s) > 0}
        self.updated = t

    def delta(self, msg: dict, t: float):
        side = self.yes if msg.get("side") == "yes" else self.no
        c = _c(msg["price_dollars"])
        s = side.get(c, 0.0) + float(msg["delta_fp"])
        if s > 1e-9:
            side[c] = s
        else:
            side.pop(c, None)
        self.updated = t

    @property
    def best_bid(self) -> int | None:
        return max(self.yes) if self.yes else None

    @property
    def best_ask(self) -> int | None:
        return 100 - max(self.no) if self.no else None

    @property
    def mid_c(self) -> float | None:
        b, a = self.best_bid, self.best_ask
        if b is None or a is None or b >= a:
            return None
        return (b + a) / 2.0

    def level_size(self, side: str, price_c: int) -> float:
        """Visible size a YES `side` order at `price_c` would queue behind."""
        return self.yes.get(price_c, 0.0) if side == "buy" else self.no.get(100 - price_c, 0.0)

    def impact_mid(self, depth: float) -> float | None:
        """Average of the VWAPs to sell and to buy `depth` contracts.

        Less jumpy than the touch: pulling one small order at the best bid moves
        the plain mid a full half-tick and moves this by a fraction of that. Where
        a side is thinner than `depth` the whole side is used.
        """
        def vwap(levels: Iterable[tuple[int, float]]) -> float | None:
            got = cost = 0.0
            for px, sz in levels:
                take = min(sz, depth - got)
                got += take
                cost += take * px
                if got >= depth:
                    break
            return cost / got if got > 0 else None
        bid = vwap(sorted(self.yes.items(), reverse=True))
        ask = vwap((100 - p, s) for p, s in sorted(self.no.items(), reverse=True))
        if bid is None or ask is None or bid >= ask:
            return self.mid_c
        return (bid + ask) / 2.0


@dataclass
class Print:
    t: float
    ticker: str
    taker_side: str   # "buy" | "sell", in YES terms
    price_c: int      # YES price
    size: float


class KalshiStream:
    def __init__(self, client: KalshiClient, on_trade: Callable[[Print], None]):
        self.client = client
        self.on_trade = on_trade
        self.books: dict[str, KalshiBook] = {}
        self.tickers: tuple[str, ...] = ()
        self.connected_at = 0.0
        self.last_msg = 0.0
        self.gaps = 0
        self._resubscribe = asyncio.Event()
        self._stop = False

    def set_tickers(self, tickers: Iterable[str]):
        new = tuple(sorted(set(tickers)))
        if new != self.tickers:
            self.tickers = new
            self._resubscribe.set()

    def stop(self):
        self._stop = True
        self._resubscribe.set()

    def _url_headers(self) -> tuple[str, dict]:
        host = self.client.base_url.split("/trade-api")[0].replace("https://", "wss://")
        return host + WS_PATH, self.client.signer.sign("GET", WS_PATH)

    def _handle(self, m: dict, seqs: dict[int, int], now: float) -> bool:
        """Apply one message. False means a sequence gap: the books are unsafe."""
        typ = m.get("type")
        sid, seq = m.get("sid"), m.get("seq")
        if sid is not None and seq is not None:
            if sid in seqs and seq != seqs[sid] + 1:
                return False
            seqs[sid] = seq
        msg = m.get("msg") or {}
        if typ == "orderbook_snapshot":
            self.books.setdefault(msg["market_ticker"], KalshiBook()).snapshot(msg, now)
        elif typ == "orderbook_delta":
            b = self.books.get(msg["market_ticker"])
            if b is not None:
                b.delta(msg, now)
        elif typ == "trade":
            # taker_side "yes": the taker bought YES and lifted YES asks.
            side = "buy" if msg.get("taker_side") == "yes" else "sell"
            self.on_trade(Print(t=now, ticker=msg["market_ticker"], taker_side=side,
                                price_c=_c(msg["yes_price_dollars"]), size=float(msg["count_fp"])))
        elif typ == "error":
            log.warning("ws error: %s", m)
        return True

    async def run(self):
        backoff = 1.0
        while not self._stop:
            if not self.tickers:
                self._resubscribe.clear()
                await self._resubscribe.wait()
                continue
            url, headers = self._url_headers()
            try:
                async with websockets.connect(url, additional_headers=headers, ping_interval=10,
                                              ping_timeout=10, max_size=None, open_timeout=15) as ws:
                    self._resubscribe.clear()
                    self.books = {}
                    await ws.send(json.dumps({"id": 1, "cmd": "subscribe", "params": {
                        "channels": ["orderbook_delta", "trade"], "market_tickers": list(self.tickers)}}))
                    self.connected_at = time.time()
                    backoff = 1.0
                    seqs: dict[int, int] = {}
                    while not self._resubscribe.is_set():
                        try:
                            raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
                        except asyncio.TimeoutError:
                            continue
                        now = time.time()
                        self.last_msg = now
                        if not self._handle(json.loads(raw), seqs, now):
                            self.gaps += 1
                            log.warning("sequence gap; resubscribing (%d so far)", self.gaps)
                            break
            except asyncio.CancelledError:
                raise
            except Exception as e:
                log.warning("kalshi ws: %s; reconnect in %.0fs", e, backoff)
                self.books = {}
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 60.0)
