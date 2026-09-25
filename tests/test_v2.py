"""v2 engine pieces: book, edge curve, placement, paper venue, crypto fair value."""
import math

import pytest

from pmm.v2.fairvalue import Anchor, p_above, prob_sigma_c, twap_t_eff
from pmm.v2.quote import QUIET, REDUCE_ONLY, TWO_SIDED, EdgeParams, desired_quotes, required_edge
from pmm.v2.stream import KalshiBook, Print
from pmm.v2.venue import PaperVenue

P = EdgeParams()


def book(yes=((40, 10.0),), no=((50, 10.0),), t=0.0):
    b = KalshiBook()
    b.snapshot({"yes_dollars_fp": [[p / 100, s] for p, s in yes],
                "no_dollars_fp": [[p / 100, s] for p, s in no]}, t)
    return b


def test_book_maps_no_bids_to_yes_asks():
    b = book(yes=((40, 10.0), (39, 5.0)), no=((55, 7.0),))
    assert (b.best_bid, b.best_ask, b.mid_c) == (40, 45, 42.5)
    assert b.level_size("sell", 45) == 7.0 and b.level_size("buy", 39) == 5.0
    b.delta({"side": "no", "price_dollars": "0.55", "delta_fp": "-7"}, 1.0)
    assert b.best_ask is None and b.mid_c is None


def test_impact_mid_resists_a_small_top_order():
    b = book(yes=((45, 1.0), (40, 50.0)), no=((50, 50.0),))
    assert b.mid_c == 47.5
    assert b.impact_mid(20.0) < 46.0


def test_check_rejects_a_curve_that_never_crosses():
    P.check()
    with pytest.raises(ValueError):
        EdgeParams(k_base_c=4.0, k_skew_c=3.0).check()


def test_one_cent_book_sits_out_at_flat():
    """v1 joined both sides of a 1c book for zero gross edge. v2 does not."""
    bid, ask = desired_quotes(50.5, 0.0, 0, 0.0, 50, 51, 2.0, TWO_SIDED, P)
    assert bid is None or 50.5 - bid.price_c >= required_edge(0, 0, 2.0, TWO_SIDED, P)
    assert ask is None or ask.price_c - 50.5 >= required_edge(0, 0, 2.0, TWO_SIDED, P)


def test_inventory_skews_instead_of_silencing():
    """v1 dropped both quotes when long. v2 keeps working the exit, through FV if needed."""
    bid, ask = desired_quotes(50.0, 0.0, 4, 0.8, 45, 55, 1.0, TWO_SIDED, P)
    assert ask is not None and ask.price_c <= 54
    assert ask.size <= 4


def test_reduce_only_never_adds():
    for pos in (-3, 0, 3):
        bid, ask = desired_quotes(50.0, 0.0, pos, pos / 5, 40, 60, 1.0, REDUCE_ONLY, P)
        if pos >= 0:
            assert bid is None
        if pos <= 0:
            assert ask is None
    _, ask = desired_quotes(50.0, 0.0, 3, 0.6, 40, 60, 1.0, REDUCE_ONLY, P)
    assert ask is not None and ask.size <= 3


def test_quiet_is_wider_and_smaller():
    b2, _ = desired_quotes(50.0, 0.0, 0, 0.0, 30, 70, 1.0, TWO_SIDED, P)
    bq, _ = desired_quotes(50.0, 0.0, 0, 0.0, 30, 70, 1.0, QUIET, P)
    assert bq.price_c <= b2.price_c and bq.size <= b2.size


def test_days_to_resolution_cost_widens():
    near, _ = desired_quotes(50.0, 0.0, 0, 0.0, 48, 60, 0.5, TWO_SIDED, P)
    far, _ = desired_quotes(50.0, 0.0, 0, 0.0, 48, 60, 60.0, TWO_SIDED, P)
    assert far.price_c < near.price_c


@pytest.mark.parametrize("fv,pos,bb,ba,sig,mode", [(50.0, 0, 44, 56, 0.4, TWO_SIDED),
                                                   (63.2, 2, 58, 66, 1.0, QUIET),
                                                   (37.0, -3, 30, 41, 0.0, REDUCE_ONLY)])
def test_sell_mirrors_buy(fv, pos, bb, ba, sig, mode):
    q = pos / P.q_max
    bid, ask = desired_quotes(fv, sig, pos, q, bb, ba, 1.0, mode, P)
    mbid, mask = desired_quotes(100 - fv, sig, -pos, -q, 100 - ba, 100 - bb, 1.0, mode, P)
    for a, m in ((bid, mask), (ask, mbid)):
        assert (a is None) == (m is None)
        if a:
            assert (a.price_c, a.size, a.tactic) == (100 - m.price_c, m.size, m.tactic)
            assert math.isclose(a.edge_c, m.edge_c)


def test_venue_queues_behind_its_own_level_not_the_touch():
    b = book(yes=((40, 100.0), (38, 3.0)), no=((55, 10.0),))
    v = PaperVenue(ack_s=0.0)
    v.place(0.0, "T", "buy", 38, 2, "rest", 41.0)
    v.advance(0.0, {"T": b})
    fills = v.on_print(Print(0.1, "T", "sell", 38, 4.0))
    assert sum(f.size for f in fills) == 1


def test_venue_ignores_prints_before_ack_and_fills_through():
    b = book()
    v = PaperVenue(ack_s=0.5)
    v.place(0.0, "T", "sell", 44, 2, "improve", 42.0)
    v.advance(0.2, {"T": b})
    assert v.on_print(Print(0.3, "T", "buy", 44, 5.0)) == []
    v.advance(0.6, {"T": b})
    assert sum(f.size for f in v.on_print(Print(0.7, "T", "buy", 49, 5.0))) == 2


def test_venue_does_not_fill_fractional_prints():
    v, b = PaperVenue(ack_s=0.0), book()
    v.place(0.0, "T", "sell", 44, 2, "improve", 42.0)
    v.advance(0.0, {"T": b})
    assert v.on_print(Print(0.1, "T", "buy", 44, 0.4)) == []


def test_twap_reduces_time_inside_the_averaging_window():
    assert twap_t_eff(600) == 540 + 20
    assert twap_t_eff(30) == 10


def test_p_above_is_a_probability_and_monotone():
    lo, hi = p_above(99_000, 100_000, 3600, 0.4), p_above(101_000, 100_000, 3600, 0.4)
    assert 0 < lo < 0.5 < hi < 1
    assert prob_sigma_c(100_000, 100_000, 3600, 0.4, 10) > prob_sigma_c(103_000, 100_000, 3600, 0.4, 10)


def test_anchor_keeps_kalshi_level():
    a = Anchor(half_life_s=60, seed_s=10)
    for t in range(20):
        a.update(float(t), 0.30, 0.40)
    assert a.value(0.40) == pytest.approx(0.30, abs=1e-6)
    assert a.value(0.45) > 0.30
