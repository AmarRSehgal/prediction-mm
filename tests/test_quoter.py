"""Quote generation invariants.

These pin the post-fix contract of the quoter. The v0 quoter clipped every
quote to strictly inside the top of book, which discarded `min_spread_cents`
and silenced the quoter whenever inventory skew pulled the two sides onto the
same cent; the tests that used to pin those defects are now written as the
positive behaviour that replaced them.
"""
from dataclasses import replace

import pytest

from pmm.trader.config import ASParams, PRICE_BAND_HIGH, PRICE_BAND_LOW
from pmm.trader.quoter import compute_quote

P = ASParams()

# A parameterisation whose desired spread is narrow enough to fit inside a
# small book, used to exercise the join-the-TOB regime.
TIGHT = replace(P, gamma=2.0, sigma_floor_c=0.5, k_order_arrival=4000.0)


def q(bid, ask, inv=0, size=2, min_spread=3, tte=12.0, params=P, sigma=5.0):
    return compute_quote(
        mid_dollars=(bid + ask) / 2, inventory_contracts=inv,
        tte_hours_to_exit=tte, current_bid_dollars=bid, current_ask_dollars=ask,
        sigma_cents=sigma, order_size=size, params=params, min_spread_cents=min_spread,
    )


BOOKS = [(0.40, 0.43), (0.40, 0.45), (0.30, 0.50), (0.20, 0.80), (0.45, 0.46), (0.40, 0.42)]


def test_never_crosses_the_book():
    for bid, ask in BOOKS:
        r = q(bid, ask)
        if r.bid_size:
            assert r.bid_price_dollars < ask, (bid, ask)
        if r.ask_size:
            assert r.ask_price_dollars > bid, (bid, ask)


def test_never_posts_worse_than_the_top_of_book():
    """A resting order behind the TOB is a quote we are not really making.
    Every live side must be at or better than the corresponding TOB price."""
    for bid, ask in BOOKS:
        for inv in (-4, -2, 0, 2, 4):
            r = q(bid, ask, inv=inv)
            if r.bid_size:
                assert r.bid_price_dollars >= bid - 1e-9, (bid, ask, inv)
            if r.ask_size:
                assert r.ask_price_dollars <= ask + 1e-9, (bid, ask, inv)


def test_quotes_are_whole_cents():
    for bid, ask in [(0.31, 0.49), (0.22, 0.77), (0.40, 0.45)]:
        r = q(bid, ask)
        assert abs(round(r.bid_price_dollars * 100) - r.bid_price_dollars * 100) < 1e-9
        assert abs(round(r.ask_price_dollars * 100) - r.ask_price_dollars * 100) < 1e-9


def test_inventory_skews_the_reservation_price_against_adding():
    flat = q(0.30, 0.50, inv=0).reservation_dollars
    long_ = q(0.30, 0.50, inv=4).reservation_dollars
    short = q(0.30, 0.50, inv=-4).reservation_dollars
    assert long_ < flat < short


# ---- min_spread_cents is enforced on the POSTED quote -------------------

@pytest.mark.parametrize("min_spread", [2, 3, 4, 5])
def test_posted_spread_is_never_tighter_than_min_spread(min_spread):
    for bid_c in range(16, 82):
        for w in range(1, 20):
            ask_c = bid_c + w
            if ask_c > 84:
                continue
            for inv in (-4, 0, 4):
                r = q(bid_c / 100, ask_c / 100, inv=inv, min_spread=min_spread)
                if r.bid_size and r.ask_size:
                    assert r.spread_cents >= min_spread, (bid_c, ask_c, inv, min_spread)


def test_book_tighter_than_min_spread_is_sat_out():
    """This is the whole purpose of the parameter. v0 posted a 1c spread into
    a 3c book; a 1c book made it join both sides for zero edge."""
    for bid_c, ask_c in [(45, 46), (40, 42), (30, 31)]:
        r = q(bid_c / 100, ask_c / 100, min_spread=3)
        assert r.bid_size == 0 and r.ask_size == 0, (bid_c, ask_c)


def test_a_book_exactly_min_spread_wide_is_joined_not_narrowed():
    """When the desired spread fits, we take the whole book rather than
    stepping inside it and halving our own edge."""
    r = q(0.40, 0.43, min_spread=3, params=TIGHT)
    assert r.bid_size > 0 and r.ask_size > 0
    assert (r.bid_price_dollars, r.ask_price_dollars) == (0.40, 0.43)
    assert r.spread_cents == 3


def test_wide_book_is_quoted_inside_at_the_desired_spread():
    r = q(0.30, 0.50, min_spread=3)
    assert r.bid_size > 0 and r.ask_size > 0
    assert 0.30 < r.bid_price_dollars < r.ask_price_dollars < 0.50


# ---- inventory skews the quote instead of silencing it -----------------

def test_long_inventory_keeps_the_ask_live_and_stands_the_bid_down():
    """v0 dropped BOTH sides here, which is what made the forced-exit hacks
    (rule C / aggressive close) look necessary: with no live ask, inventory
    could only ever be exited by crossing the spread."""
    r = q(0.30, 0.50, inv=4, size=2)
    assert r.ask_size > 0, "must keep offering while long"
    assert r.bid_size == 0, "must not keep adding while long"
    assert r.ask_price_dollars < 0.50, "the offer should work inside the book"


def test_short_inventory_keeps_the_bid_live_and_stands_the_ask_down():
    r = q(0.30, 0.50, inv=-4, size=2)
    assert r.bid_size > 0
    assert r.ask_size == 0
    assert r.bid_price_dollars > 0.30


def test_inventory_never_silences_both_sides_on_a_quotable_book():
    for inv in range(-5, 6):
        r = q(0.30, 0.50, inv=inv, size=2)
        assert r.bid_size > 0 or r.ask_size > 0, inv


def test_exit_side_gets_more_aggressive_as_inventory_grows():
    asks = [q(0.30, 0.50, inv=i).ask_price_dollars for i in (1, 2, 3, 4)]
    assert asks == sorted(asks, reverse=True)
    assert asks[0] > asks[-1]


def test_large_inventory_shrinks_the_size_on_the_adding_side():
    # Book chosen so the bid survives the skew and we can observe the size cut.
    r = q(0.20, 0.50, inv=3, size=2)
    assert r.bid_size == 1


# ---- price band --------------------------------------------------------

def test_sides_outside_the_price_band_are_suppressed_not_clamped():
    """Clamping a quote back into the band pushes it to a MORE aggressive
    price, which is the opposite of what the band is for."""
    r = q(PRICE_BAND_LOW + 0.005, PRICE_BAND_LOW + 0.045, min_spread=3, params=TIGHT)
    assert r.bid_size == 0 or r.bid_price_dollars >= PRICE_BAND_LOW - 1e-9
    r = q(PRICE_BAND_HIGH - 0.045, PRICE_BAND_HIGH + 0.005, min_spread=3, params=TIGHT)
    assert r.ask_size == 0 or r.ask_price_dollars <= PRICE_BAND_HIGH + 1e-9


# ---- missing top of book ------------------------------------------------

def test_quotes_with_no_top_of_book_at_all():
    r = compute_quote(
        mid_dollars=0.50, inventory_contracts=0, tte_hours_to_exit=12.0,
        current_bid_dollars=None, current_ask_dollars=None, sigma_cents=5.0,
        order_size=2, params=P, min_spread_cents=3,
    )
    assert r.bid_size > 0 and r.ask_size > 0
    assert r.spread_cents >= 3


# ---- calibration surface ------------------------------------------------

def test_k_order_arrival_is_load_bearing():
    """The desired spread is dominated by the (2/gamma)*ln(1+gamma/k) term,
    not by volatility. This was a bare `40` inline in the old quoter and it is
    uncalibrated -- the test exists so that is visible rather than buried."""
    wide = q(0.20, 0.80, params=replace(P, k_order_arrival=40.0)).spread_cents
    tight = q(0.20, 0.80, params=replace(P, k_order_arrival=4000.0)).spread_cents
    assert wide > tight
