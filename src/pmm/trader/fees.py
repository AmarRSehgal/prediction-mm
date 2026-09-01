"""Kalshi trading fees.

Source: Kalshi Fee Schedule (kalshi.com/docs/kalshi-fee-schedule.pdf), and the
per-series `fee_type` / `fee_multiplier` fields returned by GET /series.

  taker fee = round_up_to_cent( M       * 0.07   * C * P * (1 - P) )
  maker fee = round_up_to_cent( M_maker * 0.0175 * C * P * (1 - P) )

P is the contract price in dollars, C the contract count, M the series
`fee_multiplier` (observed values: 0, 0.5, 1). M_maker is 0 -- i.e. resting
orders are free -- unless the series `fee_type` is "quadratic_with_maker_fees",
in which case it equals `fee_multiplier`.

Two properties dominate every decision in this repo:

1. **Rounding is per ORDER, up to the whole cent.** A 1-contract taker fill at
   50c costs 2c against a $1 notional, because $0.0175 rounds up to $0.02. Fee
   cost per contract therefore falls sharply with order size; at size 1-3 it is
   brutal.
2. **P*(1-P) peaks at the middle of the book**, which is exactly the price band
   this strategy quotes in (0.15-0.85). There is no cheap corner to hide in.

Consequence: a passive-in / passive-out round trip on a normal series is free,
and a single crossed exit costs ~2c per contract on top of the spread paid.
That is the whole argument against the forced-exit mechanisms.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

TAKER_COEF = 0.07
MAKER_COEF = 0.0175

MAKER_FEE_TYPE = "quadratic_with_maker_fees"


def _round_up_cent(dollars: float) -> float:
    """Kalshi's `round up` -- to the next whole cent, once per order.

    The 1e-9 guard stops a value that is a whole cent in exact arithmetic
    (0.07 * 1 * 0.5 * 0.5 * 4 = 0.07) from being pushed to the next cent by
    float representation error.
    """
    if dollars <= 0:
        return 0.0
    return math.ceil(dollars * 100 - 1e-9) / 100


@dataclass(frozen=True)
class FeeSchedule:
    """Per-series fee parameters, verbatim from the /series payload."""
    fee_type: str = "quadratic"
    fee_multiplier: float = 1.0

    @property
    def maker_multiplier(self) -> float:
        return self.fee_multiplier if self.fee_type == MAKER_FEE_TYPE else 0.0

    @property
    def charges_maker_fees(self) -> bool:
        return self.maker_multiplier > 0

    def taker_fee_dollars(self, price_dollars: float, count: int) -> float:
        return _round_up_cent(
            self.fee_multiplier * TAKER_COEF * count * price_dollars * (1.0 - price_dollars)
        )

    def maker_fee_dollars(self, price_dollars: float, count: int) -> float:
        return _round_up_cent(
            self.maker_multiplier * MAKER_COEF * count * price_dollars * (1.0 - price_dollars)
        )

    def fee_dollars(self, price_dollars: float, count: int, is_taker: bool) -> float:
        if count <= 0:
            return 0.0
        return (self.taker_fee_dollars if is_taker else self.maker_fee_dollars)(price_dollars, count)

    def round_trip_fee_dollars(
        self, price_dollars: float, count: int,
        entry_is_taker: bool = False, exit_is_taker: bool = False,
    ) -> float:
        return (self.fee_dollars(price_dollars, count, entry_is_taker)
                + self.fee_dollars(price_dollars, count, exit_is_taker))

    def min_profitable_spread_cents(
        self, price_dollars: float, count: int,
        entry_is_taker: bool = False, exit_is_taker: bool = False,
    ) -> int:
        """Gross spread (cents, whole) a round trip must capture just to break
        even on fees. Note this is per CONTRACT, so it depends on `count`
        through the per-order rounding: bigger orders amortise the round-up."""
        count = max(1, count)
        total = self.round_trip_fee_dollars(price_dollars, count, entry_is_taker, exit_is_taker)
        return math.ceil(total / count * 100 - 1e-9)


DEFAULT_SCHEDULE = FeeSchedule()


class FeeBook:
    """series ticker -> FeeSchedule, with a conservative default.

    Unknown series fall back to the standard quadratic taker schedule with no
    maker fee. That is the common case (>97% of series as of 2026-08) but it is
    an optimistic default for the ~1% of series that do charge makers, so
    populate the book from a scan wherever it matters.
    """

    def __init__(self, schedules: dict[str, FeeSchedule] | None = None,
                 default: FeeSchedule = DEFAULT_SCHEDULE):
        self._schedules = dict(schedules or {})
        self._default = default

    def __len__(self) -> int:
        return len(self._schedules)

    def get(self, series_ticker: str | None) -> FeeSchedule:
        if not series_ticker:
            return self._default
        return self._schedules.get(series_ticker, self._default)

    def for_market(self, market_ticker: str, series_ticker: str | None = None) -> FeeSchedule:
        """Prefer an explicit series ticker; otherwise take the prefix of the
        market ticker (Kalshi tickers are SERIES-EVENT-STRIKE)."""
        if series_ticker:
            return self.get(series_ticker)
        return self.get(market_ticker.split("-", 1)[0] if market_ticker else None)

    @classmethod
    def from_series_frame(cls, df, ticker_col: str = "ticker") -> "FeeBook":
        """Build from a frame carrying `fee_type` / `fee_multiplier` (written by
        scripts/sector_scan.py). Missing columns yield an empty book rather than
        an exception, so a stale parquet degrades to the default schedule."""
        if df is None or ticker_col not in df.columns:
            return cls()
        if "fee_type" not in df.columns or "fee_multiplier" not in df.columns:
            return cls()
        schedules: dict[str, FeeSchedule] = {}
        for t, ft, fm in zip(df[ticker_col], df["fee_type"], df["fee_multiplier"]):
            if not t:
                continue
            try:
                mult = float(fm)
            except (TypeError, ValueError):
                mult = 1.0
            if mult != mult:  # NaN
                mult = 1.0
            schedules[t] = FeeSchedule(fee_type=str(ft or "quadratic"), fee_multiplier=mult)
        return cls(schedules)
