"""v2 engine pieces: book, edge curve, placement, paper venue, crypto fair value."""
import math

import pytest

from pmm.v2.fairvalue import Anchor, p_above, prob_sigma_c, twap_t_eff
from pmm.v2.quote import QUIET, REDUCE_ONLY, TWO_SIDED, EdgeParams, close_quote, desired_quotes, required_edge
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


def test_sleepwatch(monkeypatch):
    from pmm import sleepwatch
    clock = {"wall": 0.0, "mono": 0.0}
    monkeypatch.setattr(sleepwatch.time, "time", lambda: clock["wall"])
    monkeypatch.setattr(sleepwatch.time, "monotonic", lambda: clock["mono"])
    w = sleepwatch.SleepWatch()
    clock["wall"] += 3600; clock["mono"] += 1
    assert w.check() == pytest.approx(3599.0)
    clock["wall"] += 10; clock["mono"] += 10
    assert w.check() == 0.0


def _engine(tmp_path, cfgs):
    import pandas as pd
    from pmm.v2.engine import Engine
    return Engine(cfgs, None, pd.DataFrame(), tmp_path)


def test_ladder_arms_differ_only_in_latency(tmp_path):
    from dataclasses import replace
    from pmm.v2.engine import CRYPTO_LADDER
    e = _engine(tmp_path, CRYPTO_LADDER)
    assert [a.cfg.latency_s for a in e.arms] == [0.0, 0.125, 0.25, 0.375, 0.5]
    assert all((tmp_path / a.cfg.name).is_dir() for a in e.arms)
    bad = (CRYPTO_LADDER[0], replace(CRYPTO_LADDER[1], step_s=2.0))
    with pytest.raises(ValueError):
        _engine(tmp_path, bad)


def test_one_print_fills_the_fast_rung_not_the_slow_one(tmp_path):
    from datetime import datetime, timedelta, timezone
    from pmm.v2.engine import CRYPTO_LADDER, Mkt
    e = _engine(tmp_path, (CRYPTO_LADDER[0], CRYPTO_LADDER[-1]))
    t = "KXBTCD-X-T1"
    e.mkts[t] = Mkt(t, "crypto_btc", "KXBTCD", "KXBTCD-X", datetime.now(timezone.utc) + timedelta(hours=2))
    b = book()
    e.stream.books[t] = b
    for arm in e.arms:
        arm.venue.place(0.0, t, "sell", 44, 3, "improve", 42.0)
        arm.venue.advance(0.0, e.stream.books)
    e._on_print(Print(0.2, t, "buy", 44, 5.0))
    fast, slow = e.arms
    assert fast.portfolio.positions[t].yes_contracts == -3
    assert t not in slow.portfolio.positions


AGGRO = EdgeParams(aggro_close=True)


def test_aggro_close_joins_the_touch_with_the_whole_position():
    """A small long the edge curve would rest off the touch is offered at the best ask, all of it."""
    plain_bid, _ = desired_quotes(50.0, 0.0, 1, 0.2, 45, 55, 1.0, TWO_SIDED, P)
    bid, ask = desired_quotes(50.0, 0.0, 1, 0.2, 45, 55, 1.0, TWO_SIDED, AGGRO)
    assert (ask.side, ask.price_c, ask.size, ask.tactic) == ("sell", 55, 1, "join")
    assert bid == plain_bid                                                  # adding side unchanged
    bid, ask = desired_quotes(50.0, 0.0, -3, -0.6, 45, 55, 1.0, REDUCE_ONLY, AGGRO)
    assert (bid.side, bid.price_c, bid.size) == ("buy", 45, 3) and ask is None


def test_aggro_close_never_crosses_and_is_off_when_flat():
    assert close_quote(0, 45, 55) is None
    assert close_quote(2, 55, 55) is None                                    # locked book: nothing to join
    q = close_quote(2, 45, 55)
    assert q.price_c == 55 and q.side == "sell"                              # the ask, never the bid


def test_aggro_arm_keeps_its_close_through_a_fair_value_gate(tmp_path):
    from datetime import datetime, timedelta, timezone
    from pmm.trader.position import Fill
    from dataclasses import replace
    from pmm.v2.engine import NICHE, Mkt
    plain_cfg = replace(NICHE, name="v2_niche_plain", edge=replace(NICHE.edge, aggro_close=False))
    e = _engine(tmp_path, (plain_cfg, NICHE))
    t = "KXX-E-T1"
    e.mkts[t] = Mkt(t, "weather", "KXX", "KXX-E", datetime.now(timezone.utc) + timedelta(days=2))
    e.stream.books[t] = book(yes=((40, 10.0),), no=((50, 10.0),))         # bid 40, ask 50
    for arm in e.arms:
        arm.portfolio.position(t, "weather").add_fill(
            Fill(ts="2026-10-29T00:00:00Z", ticker=t, side="yes", action="buy", count=2,
                 price_dollars=0.42, fee_dollars=0.0, order_id="o1"))
    e._pull(e.mkts[t], 0.0, "fv_gap", e.stream.books[t])
    plain, aggro = e.arms
    assert plain.venue.working(t, "sell") is None
    w = aggro.venue.working(t, "sell")
    assert w is not None and (w.price_c, w.size) == (50, 2)


def test_phase2_arms_all_carry_the_aggro_close():
    from pmm.v2.engine import CRYPTO, CRYPTO_LADDER, NICHE, NICHE_LADDER
    assert all(a.edge.aggro_close for a in (NICHE, CRYPTO, *NICHE_LADDER, *CRYPTO_LADDER))
