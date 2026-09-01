"""Kalshi fee model.

The two facts that matter for this strategy, and that these tests pin:
the round-up is per ORDER (so small orders pay a big premium), and the fee
peaks in the middle of the book (which is the only band we quote in).
"""
import math

import pytest

from pmm.trader.fees import DEFAULT_SCHEDULE, FeeBook, FeeSchedule
from pmm.trader.position import Fill, MarketPosition, Portfolio

STD = FeeSchedule()
MAKER = FeeSchedule(fee_type="quadratic_with_maker_fees", fee_multiplier=1.0)
HALF = FeeSchedule(fee_multiplier=0.5)
FREE = FeeSchedule(fee_multiplier=0.0)


def test_taker_fee_matches_the_published_formula():
    # 100 contracts at 50c: 0.07 * 100 * 0.5 * 0.5 = $1.75, the schedule's own
    # worked example and the per-contract maximum.
    assert STD.taker_fee_dollars(0.50, 100) == pytest.approx(1.75)


def test_taker_fee_is_symmetric_about_fifty_cents():
    for p in (0.05, 0.2, 0.35, 0.49):
        assert STD.taker_fee_dollars(p, 100) == pytest.approx(STD.taker_fee_dollars(1 - p, 100))


def test_fee_peaks_at_the_middle_of_the_book():
    fees = [STD.taker_fee_dollars(p / 100, 1000) for p in range(5, 96, 5)]
    assert fees.index(max(fees)) == fees.index(STD.taker_fee_dollars(0.50, 1000))


def test_rounding_is_up_to_the_cent_and_applied_once_per_order():
    # 1 contract at 50c: $0.0175 -> rounds up to a full $0.02, i.e. 2c against
    # a $1 notional. This is the single most important number in the model.
    assert STD.taker_fee_dollars(0.50, 1) == pytest.approx(0.02)
    # Two contracts in ONE order round once: $0.035 -> $0.04, not 2 x $0.02
    # computed independently... which here coincides, so use a size where the
    # per-order round is strictly cheaper than per-contract rounding.
    assert STD.taker_fee_dollars(0.20, 2) == pytest.approx(0.03)
    assert STD.taker_fee_dollars(0.20, 1) * 2 == pytest.approx(0.04)


def test_small_orders_pay_a_large_rounding_premium():
    per_contract = [STD.taker_fee_dollars(0.50, c) / c for c in (1, 2, 5, 20, 100)]
    assert all(a >= b - 1e-12 for a, b in zip(per_contract, per_contract[1:]))
    assert per_contract[0] / per_contract[-1] > 1.1


def test_makers_pay_nothing_on_a_standard_series():
    assert STD.maker_fee_dollars(0.50, 100) == 0.0
    assert not STD.charges_maker_fees


def test_maker_fee_series_charge_a_quarter_of_the_taker_rate():
    assert MAKER.charges_maker_fees
    assert MAKER.maker_fee_dollars(0.50, 100) == pytest.approx(0.4375, abs=0.005)
    assert MAKER.maker_fee_dollars(0.50, 100) < MAKER.taker_fee_dollars(0.50, 100)


def test_fee_multiplier_scales_and_zero_multiplier_is_free():
    # 0.5 * 0.07 * 100 * 0.25 = $0.875, which the per-order round-up takes to $0.88.
    assert HALF.taker_fee_dollars(0.50, 100) == pytest.approx(0.88)
    assert FREE.taker_fee_dollars(0.50, 100) == 0.0
    assert FREE.maker_fee_dollars(0.50, 100) == 0.0


def test_zero_or_negative_count_is_free():
    assert STD.fee_dollars(0.50, 0, is_taker=True) == 0.0
    assert STD.fee_dollars(0.50, -3, is_taker=True) == 0.0


# ---- what the model says about the strategy ----------------------------

def test_a_passive_round_trip_is_free_on_a_standard_series():
    """So the 3c min spread is a defence against adverse selection, not fees."""
    assert STD.round_trip_fee_dollars(0.50, 2) == 0.0
    assert STD.min_profitable_spread_cents(0.50, 2) == 0


def test_a_crossed_exit_costs_about_two_cents_per_contract_mid_band():
    """This is the arithmetic case against rule C / aggressive close: every
    forced exit pays the spread AND ~2c of fee."""
    for count in (1, 2, 3):
        cost_c = STD.taker_fee_dollars(0.50, count) / count * 100
        assert 1.5 <= cost_c <= 2.0
    assert STD.min_profitable_spread_cents(0.50, 2, exit_is_taker=True) == 2


def test_maker_fee_series_need_a_wider_spread_than_the_configured_floor():
    assert MAKER.min_profitable_spread_cents(0.50, 2) >= 1


# ---- fee book ----------------------------------------------------------

def test_fee_book_resolves_by_series_then_by_ticker_prefix():
    book = FeeBook({"KXNFLGAME": MAKER})
    assert book.for_market("KXNFLGAME-26SEP01-DET", "KXNFLGAME") is MAKER
    assert book.for_market("KXNFLGAME-26SEP01-DET") is MAKER
    assert book.for_market("KXWHATEVER-26SEP01-X") is DEFAULT_SCHEDULE


def test_unknown_series_falls_back_to_the_default_schedule():
    assert FeeBook().get("nope") is DEFAULT_SCHEDULE
    assert FeeBook().get(None) is DEFAULT_SCHEDULE


def test_fee_book_from_a_frame_without_fee_columns_is_empty_not_an_error():
    pd = pytest.importorskip("pandas")
    df = pd.DataFrame({"ticker": ["A", "B"], "title": ["a", "b"]})
    assert len(FeeBook.from_series_frame(df)) == 0
    assert FeeBook.from_series_frame(df).get("A") is DEFAULT_SCHEDULE


def test_fee_book_from_a_frame_reads_both_columns():
    pd = pytest.importorskip("pandas")
    df = pd.DataFrame({
        "ticker": ["A", "B"],
        "fee_type": ["quadratic", "quadratic_with_maker_fees"],
        "fee_multiplier": [0.5, 1.0],
    })
    book = FeeBook.from_series_frame(df)
    assert book.get("A") == FeeSchedule("quadratic", 0.5)
    assert book.get("B").charges_maker_fees


def test_fee_book_tolerates_a_nan_multiplier():
    pd = pytest.importorskip("pandas")
    df = pd.DataFrame({"ticker": ["A"], "fee_type": [None], "fee_multiplier": [float("nan")]})
    assert book_mult(FeeBook.from_series_frame(df)) == 1.0


def book_mult(book):
    return book.get("A").fee_multiplier


# ---- fees reach PnL ----------------------------------------------------

def _fill(action, count, price, fee, taker=False):
    return Fill(ts="2026-08-31T00:00:00+00:00", ticker="T", side="yes", action=action,
                count=count, price_dollars=price, order_id="x",
                fee_dollars=fee, is_taker=taker)


def test_fees_are_deducted_from_realized_pnl_and_tracked_separately():
    pos = MarketPosition(ticker="T", subsector="s")
    pos.add_fill(_fill("buy", 2, 0.40, 0.0))
    pos.add_fill(_fill("sell", 2, 0.43, 0.04, taker=True))
    # 3c x 2 contracts = $0.06 gross, less $0.04 of fee.
    assert pos.realized_pnl == pytest.approx(0.02)
    assert pos.fees_paid == pytest.approx(0.04)


def test_a_fee_on_an_opening_fill_hits_pnl_immediately():
    pos = MarketPosition(ticker="T", subsector="s")
    pos.add_fill(_fill("buy", 2, 0.40, 0.01))
    assert pos.yes_contracts == 2
    assert pos.realized_pnl == pytest.approx(-0.01)


def test_fees_survive_the_state_round_trip():
    p = Portfolio()
    pos = p.position("T", "s")
    pos.add_fill(_fill("buy", 2, 0.40, 0.01))
    back = Portfolio.from_json(p.to_json())
    assert back.fees_paid_total() == pytest.approx(0.01)
    assert back.positions["T"].fills[0].fee_dollars == pytest.approx(0.01)


def test_old_state_files_without_fee_fields_still_load():
    legacy = {
        "cash_dollars": 100.0, "starting_cash": 100.0,
        "positions": {"T": {
            "ticker": "T", "subsector": "s", "yes_contracts": 1,
            "avg_cost_dollars": 0.4, "realized_pnl": 0.0,
            "fills": [{"ts": "t", "ticker": "T", "side": "yes", "action": "buy",
                       "count": 1, "price_dollars": 0.4, "order_id": "o"}],
        }},
    }
    p = Portfolio.from_json(legacy)
    assert p.fees_paid_total() == 0.0
    assert p.positions["T"].fills[0].fee_dollars == 0.0
