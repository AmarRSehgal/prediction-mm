"""Position accounting: the ledger everything else is measured against.

If add_fill is wrong, every PnL number in the repo is wrong, so this is the
first thing worth pinning down.
"""
from pmm.trader.position import Fill, MarketPosition, Portfolio


def _fill(action, count, price, side="yes"):
    return Fill(ts="2026-01-01T00:00:00+00:00", ticker="T", side=side,
                action=action, count=count, price_dollars=price, order_id="x")


def test_long_round_trip_realizes_the_spread():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("buy", 2, 0.40))
    assert p.yes_contracts == 2
    assert p.avg_cost_dollars == 0.40
    p.add_fill(_fill("sell", 2, 0.43))
    assert p.yes_contracts == 0
    assert abs(p.realized_pnl - 0.06) < 1e-12  # 2 contracts * 3c
    assert p.avg_cost_dollars == 0.0


def test_short_round_trip_realizes_the_spread():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("sell", 2, 0.43))
    assert p.yes_contracts == -2
    p.add_fill(_fill("buy", 2, 0.40))
    assert p.yes_contracts == 0
    assert abs(p.realized_pnl - 0.06) < 1e-12


def test_vwap_accumulates_on_same_side_adds():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("buy", 1, 0.40))
    p.add_fill(_fill("buy", 3, 0.50))
    assert p.yes_contracts == 4
    assert abs(p.avg_cost_dollars - 0.475) < 1e-12


def test_no_side_fill_is_tracked_as_yes_equivalent():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("buy", 2, 0.60, side="no"))
    assert p.yes_contracts == -2          # long NO == short YES
    assert abs(p.avg_cost_dollars - 0.40) < 1e-12  # 1 - 0.60


def test_flip_realizes_the_closed_leg_and_rebases_cost():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("buy", 2, 0.40))
    p.add_fill(_fill("sell", 5, 0.45))    # close 2, open 3 short
    assert p.yes_contracts == -3
    assert abs(p.realized_pnl - 0.10) < 1e-12  # 2 * 5c
    assert p.avg_cost_dollars == 0.45


def test_unrealized_and_cash_tied_signs():
    p = MarketPosition(ticker="T", subsector="s")
    p.add_fill(_fill("buy", 4, 0.30))
    assert abs(p.unrealized_pnl(0.35) - 0.20) < 1e-12
    assert abs(p.cash_tied_up() - 1.20) < 1e-12
    q = MarketPosition(ticker="U", subsector="s")
    q.add_fill(_fill("sell", 4, 0.30))
    assert abs(q.unrealized_pnl(0.25) - 0.20) < 1e-12
    assert abs(q.cash_tied_up() - 2.80) < 1e-12  # long NO at 70c


def test_portfolio_roundtrips_through_json():
    pf = Portfolio(cash_dollars=100.0, starting_cash=100.0)
    pos = pf.position("T", "sub_a")
    pos.add_fill(_fill("buy", 2, 0.40))
    pos.first_fill_spread_c = 4
    back = Portfolio.from_json(pf.to_json())
    got = back.positions["T"]
    assert got.yes_contracts == 2
    assert got.first_fill_spread_c == 4
    assert len(got.fills) == 1
