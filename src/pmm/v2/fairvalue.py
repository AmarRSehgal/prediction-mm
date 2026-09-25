"""v2 fair values.

niche   Depth-weighted mid of the Kalshi book itself. These markets have no
        faster venue, so this is the best available and it is a weak one --
        the niche arm exists to measure what the engine changes are worth on
        v1's own universe, not because a book-mid fair value is expected to win.

crypto  Kalshi's hourly BTC/ETH "above K" markets are cash-or-nothing calls
        on the 60-second average of CF Benchmarks' RTI before the close.
        Binance spot leads that index, so:
            model  = P(avg_60s > K) under GBM with the TWAP's reduced variance
            FV     = sigmoid(EW[logit kalshi mid] + logit(model) - EW[logit model])
        i.e. the Kalshi level, moved by the Binance-implied change. The anchor
        absorbs the USDT/USD basis and whatever the model gets wrong about
        level, and keeps the part that leads.
"""
from __future__ import annotations

import asyncio
import json
import logging
import math
import time

import requests
import websockets

log = logging.getLogger(__name__)

SECONDS_PER_YEAR = 365.25 * 24 * 3600
BINANCE_WS = "wss://stream.binance.com:9443/stream?streams="
BINANCE_REST = "https://api.binance.com/api/v3/klines"


def norm_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2))


def logit(p: float) -> float:
    p = min(max(p, 0.01), 0.99)
    return math.log(p / (1 - p))


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def twap_t_eff(tau_s: float, lookback_s: float = 60.0) -> float:
    """Driftless GBM: the average over the last L seconds has variance sigma^2*L/3."""
    before = max(tau_s - lookback_s, 0.0)
    return before + min(tau_s, lookback_s) / 3.0


def p_above(S: float, K: float, t_eff_s: float, sigma: float) -> float:
    if t_eff_s <= 0 or sigma <= 0:
        return 1.0 if S > K else 0.0
    T = t_eff_s / SECONDS_PER_YEAR
    d2 = (math.log(S / K) - 0.5 * sigma ** 2 * T) / (sigma * math.sqrt(T))
    return norm_cdf(d2)


class EWVar:
    """EW variance of a series' changes, irregular time steps, half-life in seconds."""

    def __init__(self, half_life_s: float, floor: float):
        self.h, self.floor = half_life_s, floor
        self.var: float | None = None
        self.last: float | None = None
        self.last_t: float | None = None

    def update(self, t: float, x: float):
        if self.last is not None:
            a = 1 - 0.5 ** ((t - self.last_t) / self.h)
            d2 = (x - self.last) ** 2
            self.var = d2 if self.var is None else self.var + a * (d2 - self.var)
        self.last, self.last_t = x, t

    @property
    def sigma(self) -> float:
        return max(math.sqrt(self.var) if self.var else 0.0, self.floor)


class Anchor:
    def __init__(self, half_life_s: float = 120.0, seed_s: float = 30.0):
        self.h, self.seed_s = half_life_s, seed_s
        self.a_mkt = self.a_model = None
        self.first_t = self.last_t = None

    def update(self, t: float, mid_p: float, model_p: float):
        lm, lo = logit(mid_p), logit(model_p)
        if self.a_mkt is None:
            self.a_mkt, self.a_model, self.first_t, self.last_t = lm, lo, t, t
            return
        a = 1 - 0.5 ** (max(t - self.last_t, 0.0) / self.h)
        self.a_mkt += a * (lm - self.a_mkt)
        self.a_model += a * (lo - self.a_model)
        self.last_t = t

    def value(self, model_p: float) -> float | None:
        if self.a_mkt is None or self.last_t - self.first_t < self.seed_s:
            return None
        return sigmoid(self.a_mkt + logit(model_p) - self.a_model)


class SpotVol:
    """Annualised EWMA vol of 1-minute log returns, seeded from REST klines."""

    def __init__(self, symbol: str, half_life_bars: int = 60, bump: float = 1.25):
        self.symbol, self.bump = symbol, bump
        self.alpha = 1 - 0.5 ** (1 / half_life_bars)
        self.var: float | None = None
        self.bar_start = 0
        self.bar_close = 0.0
        self.last_close = 0.0
        self.bars = 0

    def seed(self):
        r = requests.get(BINANCE_REST, params={"symbol": self.symbol, "interval": "1m", "limit": 240},
                         timeout=10)
        r.raise_for_status()
        for k in r.json()[:-1]:
            self._close_bar(float(k[4]))
        self.bar_start = int(time.time()) // 60 * 60

    def _close_bar(self, close: float):
        if self.last_close > 0:
            r2 = math.log(close / self.last_close) ** 2
            self.var = r2 if self.var is None else self.var + self.alpha * (r2 - self.var)
            self.bars += 1
        self.last_close = close

    def on_price(self, px: float, t: float):
        b = int(t) // 60 * 60
        if self.bar_start and b > self.bar_start and self.bar_close > 0:
            self._close_bar(self.bar_close)
        self.bar_start = b
        self.bar_close = px

    @property
    def ready(self) -> bool:
        return self.bars >= 60

    @property
    def annual(self) -> float:
        """Bumped: 1-minute realised vol understates the jumps an hour can hold."""
        return math.sqrt((self.var or 0.0) * 525_960) * self.bump


class BinanceSpot:
    """Pushed best bid/offer mids for a few symbols, feeding a SpotVol each."""

    def __init__(self, symbols: tuple[str, ...]):
        self.symbols = symbols
        self.mid: dict[str, float] = {}
        self.updated: dict[str, float] = {}
        self.vol = {s: SpotVol(s) for s in symbols}
        self._stop = False

    def seed(self):
        for v in self.vol.values():
            v.seed()

    def stop(self):
        self._stop = True

    async def run(self):
        url = BINANCE_WS + "/".join(f"{s.lower()}@bookTicker" for s in self.symbols)
        backoff = 1.0
        while not self._stop:
            try:
                async with websockets.connect(url, ping_interval=20, ping_timeout=10) as ws:
                    backoff = 1.0
                    async for raw in ws:
                        d = json.loads(raw).get("data") or {}
                        sym = d.get("s")
                        if sym not in self.vol:
                            continue
                        now = time.time()
                        m = (float(d["b"]) + float(d["a"])) / 2
                        self.mid[sym], self.updated[sym] = m, now
                        self.vol[sym].on_price(m, now)
                        if self._stop:
                            return
            except asyncio.CancelledError:
                raise
            except Exception as e:
                log.warning("binance ws: %s; reconnect in %.0fs", e, backoff)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30.0)


def prob_sigma_c(S: float, K: float, t_eff_s: float, sigma: float, horizon_s: float) -> float:
    """Typical move of the YES probability, in cents, over `horizon_s`."""
    if S <= 0 or t_eff_s <= 0 or sigma <= 0:
        return 0.0
    h = sigma * math.sqrt(horizon_s / SECONDS_PER_YEAR)
    return abs(p_above(S * math.exp(h), K, t_eff_s, sigma) - p_above(S * math.exp(-h), K, t_eff_s, sigma)) * 50
