"""Risk-limit enforcement. The only thing standing between a config typo and a
real-money position, so the caps get tested even though the bot is paper-only.
"""
from dataclasses import replace

from pmm.trader.config import RiskLimits
from pmm.trader.position import Fill, Portfolio
from pmm.trader.risk import assess_market

LIMITS = RiskLimits()


def _pf(ticker="T", sub="s", qty=0, price=0.50):
    pf = Portfolio(cash_dollars=LIMITS.capital_dollars, starting_cash=LIMITS.capital_dollars)
    pos = pf.position(ticker, sub)
    if qty:
        pos.add_fill(Fill(ts="2026-01-01T00:00:00+00:00", ticker=ticker, side="yes",
                          action="buy" if qty > 0 else "sell", count=abs(qty),
                          price_dollars=price, order_id="x"))
    return pf


def test_killswitch_blocks_both_sides():
    d = assess_market(_pf(), "T", "s", 0.5, {"T": 0.5}, LIMITS, kill=True)
    assert not d.can_quote_bid and not d.can_quote_ask and d.max_order_size == 0


def test_flat_book_allows_both_sides():
    d = assess_market(_pf(), "T", "s", 0.5, {"T": 0.5}, LIMITS)
    assert d.can_quote_bid and d.can_quote_ask
    assert d.reason == "ok"


def test_long_inventory_cap_blocks_the_bid_only():
    pf = _pf(qty=LIMITS.max_inventory_per_market)
    d = assess_market(pf, "T", "s", 0.5, {"T": 0.5}, LIMITS)
    assert not d.can_quote_bid
    assert d.can_quote_ask
    assert "long inventory capped" in d.reason


def test_short_inventory_cap_blocks_the_ask_only():
    pf = _pf(qty=-LIMITS.max_inventory_per_market)
    d = assess_market(pf, "T", "s", 0.5, {"T": 0.5}, LIMITS)
    assert d.can_quote_bid
    assert not d.can_quote_ask


def test_per_market_dollar_cap_blocks_growth():
    tiny = replace(LIMITS, per_market_frac=0.00001)  # ~4c per market
    pf = _pf(qty=2)
    d = assess_market(pf, "T", "s", 0.5, {"T": 0.5}, tiny)
    assert not d.can_quote_bid and not d.can_quote_ask
    assert "market_exposure" in d.reason


def test_total_exposure_cap_blocks_growth():
    tiny = replace(LIMITS, total_exposure_frac=0.0000001)
    pf = _pf(qty=2)
    d = assess_market(pf, "T", "s", 0.5, {"T": 0.5}, tiny)
    assert not d.can_quote_bid and not d.can_quote_ask
    assert "total_exposure" in d.reason


def test_KNOWN_BUG_order_size_never_falls_below_one_contract():
    """`size = min(default, max(1, contracts_fit))` floors at 1, so a market
    with zero dollar headroom is still sized for one contract and the
    'zero sizing after caps' branch is unreachable. The can_quote_* flags do
    stop the order today, so this is a latent hazard rather than a live leak --
    but any future caller that trusts max_order_size alone would overshoot the
    per-market cap by one contract."""
    tiny = replace(LIMITS, per_market_frac=0.0)
    d = assess_market(_pf(), "T", "s", 0.5, {"T": 0.5}, tiny)
    assert d.max_order_size == 1
    assert "zero sizing after caps" not in d.reason


def test_KNOWN_BUG_killswitch_ignores_unrealized_pnl():
    """runner.py trips the daily stop on realized PnL only, so an account can
    sit on an arbitrarily large mark-to-market drawdown without the kill switch
    firing. Paper sessions realized their losses quickly so this never bit,
    but it is the wrong invariant for live."""
    pf = _pf(qty=5, price=0.90)
    assert pf.realized_pnl_total() == 0.0
    assert pf.positions["T"].unrealized_pnl(0.10) < -3.0
