"""Quote generation invariants.

Several of these tests pin CURRENT behaviour that is arguably wrong (see the
xfail-style comments). They exist so a future change to the quoter is a
deliberate, visible decision rather than a silent one.
"""
from pmm.trader.config import ASParams
from pmm.trader.quoter import compute_quote

P = ASParams()


def q(bid, ask, inv=0, size=2, min_spread=3, tte=12.0):
    return compute_quote(
        mid_dollars=(bid + ask) / 2, inventory_contracts=inv,
        tte_hours_to_exit=tte, current_bid_dollars=bid, current_ask_dollars=ask,
        sigma_cents=5.0, order_size=size, params=P, min_spread_cents=min_spread,
    )


def test_never_crosses_the_book():
    for bid, ask in [(0.40, 0.43), (0.40, 0.45), (0.30, 0.50), (0.20, 0.80), (0.45, 0.46)]:
        r = q(bid, ask)
        if r.bid_size:
            assert r.bid_price_dollars < ask, (bid, ask)
        if r.ask_size:
            assert r.ask_price_dollars > bid, (bid, ask)


def test_two_cent_book_produces_no_quote():
    r = q(0.40, 0.42)
    assert r.bid_size == 0 and r.ask_size == 0


def test_inventory_skews_the_reservation_price_against_adding():
    flat = q(0.30, 0.50, inv=0).reservation_dollars
    long_ = q(0.30, 0.50, inv=4).reservation_dollars
    short = q(0.30, 0.50, inv=-4).reservation_dollars
    assert long_ < flat < short


def test_long_inventory_shrinks_the_bid_size():
    # Small inventory still quotes, with a reduced bid.
    assert q(0.30, 0.50, inv=3, size=2).bid_size == 1


def test_quotes_are_whole_cents():
    for bid, ask in [(0.31, 0.49), (0.22, 0.77), (0.40, 0.45)]:
        r = q(bid, ask)
        assert abs(round(r.bid_price_dollars * 100) - r.bid_price_dollars * 100) < 1e-9
        assert abs(round(r.ask_price_dollars * 100) - r.ask_price_dollars * 100) < 1e-9


# ---- Pinned known-bad behaviour ----------------------------------------

def test_KNOWN_BUG_min_spread_cents_is_not_enforced_on_the_posted_quote():
    """min_spread_cents is applied to the AS spread and then thrown away by the
    inside-the-TOB clip. On a 3c book we post a 1c spread despite asking for 3c.

    This is the single biggest suspected cause of the paper bleed: max 1c of
    gross capture against multi-cent adverse selection. Change the quoter and
    this test should be updated, not deleted.
    """
    r = q(0.40, 0.43, min_spread=3)
    assert (r.bid_price_dollars, r.ask_price_dollars) == (0.41, 0.42)
    assert round(r.spread_cents) == 1


def test_KNOWN_BUG_one_cent_book_makes_us_join_both_sides_for_zero_edge():
    """On a 1c-wide book the inside-clip inverts and we end up quoting exactly
    the existing TOB on both sides: zero gross spread, full adverse selection.
    Only the queue-depth gate in runner.py stops this, and only when the queue
    is deep."""
    r = q(0.45, 0.46)
    assert (r.bid_price_dollars, r.ask_price_dollars) == (0.45, 0.46)
    assert r.bid_size > 0 and r.ask_size > 0


def test_KNOWN_BUG_join_tob_branch_is_unreachable():
    """The 'JOIN vs IMPROVE' block can never fire on a normal book, because the
    earlier clip has already forced bid >= tob_bid + 1c and ask <= tob_ask - 1c.
    Verified across a wide sweep of books and AS widths."""
    for bid_c in range(16, 80, 3):
        for w in range(3, 40, 3):
            bid, ask = bid_c / 100, (bid_c + w) / 100
            if ask >= 0.85:
                continue
            r = q(bid, ask)
            if r.bid_size:
                assert r.bid_price_dollars > bid
            if r.ask_size:
                assert r.ask_price_dollars < ask


def test_KNOWN_BUG_real_inventory_silences_the_quoter_instead_of_skewing_it():
    """Inventory skew moves the reservation price, but the inside-the-TOB clip
    then drags both sides back to the same cent, so the quote is dropped.

    Net effect: exactly when we hold inventory and most want to lean on the
    offer to work out of it, we stop quoting altogether and the position can
    only be exited by crossing the spread. This is why the forced-exit
    mechanisms (rule C / aggressive close) looked necessary in the first place
    -- they are treating a symptom of this bug.
    """
    r = q(0.30, 0.50, inv=4, size=2)
    assert r.bid_size == 0 and r.ask_size == 0
    assert r.bid_price_dollars == r.ask_price_dollars
