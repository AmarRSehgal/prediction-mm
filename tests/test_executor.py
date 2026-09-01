"""PaperExecutor: fill matching and the fee-aware exit economics.

The point of these is the arithmetic the strategy lives or dies on -- a
passive round trip keeps its gross spread, and any crossed exit gives back the
spread plus ~2c of taker fee per contract.
"""
from datetime import datetime, timedelta, timezone

import pytest

from pmm.trader.executor import OrderIntent, PaperExecutor
from pmm.trader.fees import FeeBook, FeeSchedule
from pmm.trader.position import Portfolio

TICKER = "KXTEST-26SEP01-A"


class FakeClient:
    """Serves a fixed trade tape to PaperExecutor.try_fill_against."""

    def __init__(self, trades):
        self.trades = trades

    def get_trades(self, **kwargs):
        return {"trades": self.trades}


def _trade(ts, yes_price, count, taker_side):
    return {"created_time": ts.isoformat().replace("+00:00", "Z"),
            "yes_price_dollars": f"{yes_price:.4f}", "count_fp": f"{count:.2f}",
            "taker_side": taker_side}


def _executor(trades, fee_book=None):
    p = Portfolio()
    ex = PaperExecutor(portfolio=p, client=FakeClient(trades),
                       fee_book=fee_book or FeeBook())
    return p, ex


def test_a_yes_bid_fills_when_a_no_taker_crosses_it():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.40, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    fills = ex.try_fill_against(TICKER, "s", 40, 43)
    assert len(fills) == 1 and fills[0].count == 2
    assert p.position(TICKER, "s").yes_contracts == 2


def test_a_trade_that_does_not_reach_our_price_does_not_fill_us():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.41, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    assert ex.try_fill_against(TICKER, "s", 40, 43) == []


def test_a_taker_on_our_own_side_does_not_fill_us():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.40, 10, "yes")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    assert ex.try_fill_against(TICKER, "s", 40, 43) == []


def test_a_trade_older_than_our_order_does_not_fill_us():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now - timedelta(minutes=5), 0.40, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    assert ex.try_fill_against(TICKER, "s", 40, 43) == []


def test_the_same_trade_is_not_replayed_into_a_second_fill():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.40, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    assert len(ex.try_fill_against(TICKER, "s", 40, 43)) == 1
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    assert ex.try_fill_against(TICKER, "s", 40, 43) == []


# ---- the economics -----------------------------------------------------

def test_a_passive_round_trip_keeps_its_whole_gross_spread():
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([
        _trade(now + timedelta(seconds=5), 0.40, 10, "no"),    # hits our bid
        _trade(now + timedelta(seconds=6), 0.43, 10, "yes"),   # lifts our ask
    ])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    ex.place_order(OrderIntent(TICKER, "yes", "sell", 2, 43), "s")
    ex.try_fill_against(TICKER, "s", 40, 43)
    pos = p.position(TICKER, "s")
    assert pos.yes_contracts == 0
    assert pos.fees_paid == 0.0
    assert pos.realized_pnl == pytest.approx(0.06)   # 3c x 2 contracts, no fee


def test_force_closing_the_same_position_gives_back_the_spread_and_the_fee():
    """Same entry as above, exited by crossing instead of by a passive fill."""
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.40, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    ex.try_fill_against(TICKER, "s", 40, 43)
    pos = p.position(TICKER, "s")
    ex.force_close(TICKER, "s", pos, yes_bid_d=0.40, yes_ask_d=0.43, reason="test")
    assert pos.yes_contracts == 0
    # Flat on price (bought and sold at 40c) but 4c down on the taker fee.
    assert pos.fees_paid == pytest.approx(0.04)
    assert pos.realized_pnl == pytest.approx(-0.04)


def test_maker_fee_series_charge_the_passive_round_trip_too():
    now = datetime.now(tz=timezone.utc)
    book = FeeBook({"KXTEST": FeeSchedule("quadratic_with_maker_fees", 1.0)})
    p, ex = _executor([
        _trade(now + timedelta(seconds=5), 0.40, 10, "no"),
        _trade(now + timedelta(seconds=6), 0.43, 10, "yes"),
    ], fee_book=book)
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    ex.place_order(OrderIntent(TICKER, "yes", "sell", 2, 43), "s")
    ex.try_fill_against(TICKER, "s", 40, 43)
    pos = p.position(TICKER, "s")
    assert pos.fees_paid > 0
    assert pos.realized_pnl < 0.06


def test_aggressive_close_will_not_take_a_profit_that_the_fee_eats():
    """1c of edge does not cover a 2c/contract taker fee. Before the fee model
    this closed and booked a net loss as a 'profit'."""
    now = datetime.now(tz=timezone.utc)
    p, ex = _executor([_trade(now + timedelta(seconds=5), 0.40, 10, "no")])
    ex.record_tob(TICKER, 0.0, 0.0)
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    ex.try_fill_against(TICKER, "s", 40, 43)
    pos = p.position(TICKER, "s")
    assert ex.try_aggressive_close(TICKER, "s", pos, 0.41, 0.44, 0.425,
                                   min_profit_c=1, adverse_cutoff_c=50) is None
    assert pos.yes_contracts == 2
    # 5c of edge does clear it.
    assert ex.try_aggressive_close(TICKER, "s", pos, 0.45, 0.48, 0.465,
                                   min_profit_c=1, adverse_cutoff_c=50) is not None
    assert pos.realized_pnl > 0


def test_cancel_all_is_scoped_to_one_ticker():
    p, ex = _executor([])
    ex.place_order(OrderIntent(TICKER, "yes", "buy", 2, 40), "s")
    ex.place_order(OrderIntent("OTHER-X", "yes", "buy", 2, 40), "s")
    assert ex.cancel_all(TICKER) == 1
    assert len(ex.open_orders) == 1
    assert ex.cancel_all() == 1
    assert ex.open_orders == {}
