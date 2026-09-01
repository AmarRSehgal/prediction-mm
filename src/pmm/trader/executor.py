"""Order executors.

PaperExecutor — simulates fills against the current orderbook. Default.
LiveExecutor  — real Kalshi order endpoints. Requires read-write API key.
"""
from __future__ import annotations

import logging
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from pmm.kalshi.client import KalshiClient
from pmm.trader.position import Fill, Portfolio

log = logging.getLogger(__name__)


@dataclass
class OrderIntent:
    ticker: str
    side: str        # "yes" | "no"
    action: str      # "buy" | "sell"
    count: int
    price_cents: int  # price on the `side` in integer cents
    post_only: bool = True


@dataclass
class PlacedOrder:
    order_id: str
    intent: OrderIntent
    placed_ts: datetime
    filled_count: int = 0


# ---- Paper executor ----------------------------------------------------

@dataclass
class PaperExecutor:
    """Live paper executor using trade-match fills.

    Virtual orders are recorded but not placed with Kalshi. Every cycle we pull
    the most-recent trades for each ticker we have orders in, and check:
      - Did a trade happen at or through our virtual price?
      - Was the taker on the side that would cross us?
      - Was the trade size large enough to consume the book ahead of us?
    If all yes, we count the fill at our price.
    """
    portfolio: Portfolio
    client: "KalshiClient | None" = None  # injected for trade lookup
    open_orders: dict[str, PlacedOrder] = field(default_factory=dict)
    # Per-ticker last-trade-ts we've processed, to avoid duplicate fills
    last_trade_ts: dict[str, datetime] = field(default_factory=dict)
    # Per-ticker last observed TOB sizes (ahead-of-us proxy) captured at place time
    tob_at_place: dict[str, tuple[float, float]] = field(default_factory=dict)

    def cancel_all(self, ticker: str | None = None) -> int:
        to_drop = [oid for oid, o in self.open_orders.items() if ticker is None or o.intent.ticker == ticker]
        for oid in to_drop:
            del self.open_orders[oid]
        return len(to_drop)

    def place_order(self, intent: OrderIntent, subsector: str) -> PlacedOrder:
        order_id = f"paper-{uuid.uuid4()}"
        po = PlacedOrder(order_id=order_id, intent=intent, placed_ts=datetime.now(tz=timezone.utc))
        self.open_orders[order_id] = po
        log.info("PAPER placed %s %s %d @ %dc (%s)",
                 intent.action, intent.side, intent.count, intent.price_cents, intent.ticker)
        return po

    def record_tob(self, ticker: str, yes_bid_size: float, yes_ask_size: float) -> None:
        """Called by runner with the TOB sizes observed at quote time.
        Used later as 'queue ahead' proxy when matching trades."""
        self.tob_at_place[ticker] = (yes_bid_size, yes_ask_size)

    def try_fill_against(self, ticker: str, subsector: str,
                         current_yes_bid_c: int, current_yes_ask_c: int) -> list[Fill]:
        """Match open virtual orders in this ticker against actual trades since last
        check. Uses queue-position approximation: we are 'behind' the TOB size that
        was there when we placed, and need an aggressor large enough to sweep past."""
        if self.client is None:
            return []

        try:
            resp = self.client.get_trades(ticker=ticker, limit=50)
        except Exception as e:
            log.warning("paper trade fetch failed %s: %s", ticker, e)
            return []
        trades = resp.get("trades", []) or []
        if not trades:
            return []

        # Trades come newest-first; sort ascending so we process chronologically
        parsed = []
        for t in trades:
            ct = t.get("created_time")
            try:
                ts = datetime.fromisoformat(ct.replace("Z", "+00:00")) if ct else None
            except Exception:
                ts = None
            if ts is None:
                continue
            try:
                yp = float(t.get("yes_price_dollars") or 0)
                sz = float(t.get("count_fp") or 0)
            except Exception:
                continue
            parsed.append((ts, yp, sz, t.get("taker_side")))
        parsed.sort(key=lambda x: x[0])

        last_seen = self.last_trade_ts.get(ticker)
        queue_bid, queue_ask = self.tob_at_place.get(ticker, (0.0, 0.0))
        # If any of our open orders is IMPROVING on the real TOB (bid > real
        # yes_bid, or ask < real yes_ask), we become the new TOB on that side
        # and there are zero contracts ahead of us. Without this, improving
        # quotes inherit the 51-100 queue of the level they jumped, and
        # paper fills never happen.
        cur_bid_d = current_yes_bid_c / 100.0
        cur_ask_d = current_yes_ask_c / 100.0
        for po in self.open_orders.values():
            if po.intent.ticker != ticker:
                continue
            p = po.intent.price_cents / 100.0
            if po.intent.action == "buy" and po.intent.side == "yes" and p > cur_bid_d:
                queue_bid = 0.0
            if po.intent.action == "sell" and po.intent.side == "yes" and p < cur_ask_d:
                queue_ask = 0.0
        fills: list[Fill] = []

        for ts, yp, sz, taker in parsed:
            if last_seen is not None and ts <= last_seen:
                continue
            # Trades that happened AFTER our place
            for po in list(self.open_orders.values()):
                if po.intent.ticker != ticker:
                    continue
                if ts < po.placed_ts:
                    continue
                our_price = po.intent.price_cents / 100.0
                action = po.intent.action
                side = po.intent.side

                if action == "buy" and side == "yes":
                    # We're a YES bid; a NO taker (selling YES) crosses us.
                    if taker == "no" and yp <= our_price:
                        # Queue: aggressor must exceed book-ahead to reach us.
                        if sz > queue_bid:
                            got = min(int(sz - queue_bid), po.intent.count)
                            if got > 0:
                                fills.append(self._execute(po, our_price, subsector, fill_size=got))
                                queue_bid = 0  # we got priority subsequently
                        else:
                            queue_bid = max(0.0, queue_bid - sz)
                elif action == "sell" and side == "yes":
                    # We're a YES ask; a YES taker (buying YES) crosses us.
                    if taker == "yes" and yp >= our_price:
                        if sz > queue_ask:
                            got = min(int(sz - queue_ask), po.intent.count)
                            if got > 0:
                                fills.append(self._execute(po, our_price, subsector, fill_size=got))
                                queue_ask = 0
                        else:
                            queue_ask = max(0.0, queue_ask - sz)
            last_seen = ts

        if last_seen is not None:
            self.last_trade_ts[ticker] = last_seen
        # Update our queue estimate after processing
        self.tob_at_place[ticker] = (queue_bid, queue_ask)
        return fills

    def _execute(self, po: PlacedOrder, price_dollars: float, subsector: str, fill_size: int) -> Fill:
        now = datetime.now(tz=timezone.utc).isoformat()
        fill = Fill(
            ts=now, ticker=po.intent.ticker, side=po.intent.side, action=po.intent.action,
            count=fill_size, price_dollars=price_dollars, order_id=po.order_id,
        )
        pos = self.portfolio.position(po.intent.ticker, subsector)
        pos.add_fill(fill)
        po.filled_count += fill_size
        log.info("PAPER FILL %s %s %d @ $%.2f (%s) -> inv=%d realized=$%.2f",
                 po.intent.action, po.intent.side, fill_size, price_dollars,
                 po.intent.ticker, pos.yes_contracts, pos.realized_pnl)
        if po.filled_count >= po.intent.count:
            self.open_orders.pop(po.order_id, None)
        return fill

    def force_close(self, ticker: str, subsector: str, pos,
                     yes_bid_d: float, yes_ask_d: float, reason: str) -> Fill | None:
        """Unconditional close at real TOB. Used by rule C (hold-time) and
        similar forced-exit mechanisms. Paper-sim only."""
        if pos.yes_contracts == 0:
            return None
        if yes_bid_d <= 0 or yes_ask_d <= 0:
            return None
        direction = 1 if pos.yes_contracts > 0 else -1
        qty = abs(pos.yes_contracts)
        exit_price = yes_bid_d if direction == 1 else yes_ask_d
        action = "sell" if direction == 1 else "buy"
        fill = Fill(
            ts=datetime.now(tz=timezone.utc).isoformat(),
            ticker=ticker, side="yes", action=action,
            count=qty, price_dollars=exit_price, order_id="FORCE_CLOSE",
        )
        pos.add_fill(fill)
        log.info("FORCE CLOSE %s %d @ $%.2f [%s] cost=$%.2f realized=$%+.2f (%s)",
                 action, qty, exit_price, ticker, pos.avg_cost_dollars,
                 pos.realized_pnl, reason)
        return fill

    def try_aggressive_close(self, ticker: str, subsector: str, pos,
                              yes_bid_d: float, yes_ask_d: float, mid: float,
                              min_profit_c: int, adverse_cutoff_c: int) -> Fill | None:
        """Close position by taking the real TOB if we can lock in profit OR
        the mid has drifted adversely past the cutoff. Paper-sim only."""
        if pos.yes_contracts == 0:
            return None
        if yes_bid_d <= 0 or yes_ask_d <= 0:
            return None
        direction = 1 if pos.yes_contracts > 0 else -1
        qty = abs(pos.yes_contracts)
        entry_cost = pos.avg_cost_dollars
        if direction == 1:
            # Long YES: sell at real yes_bid
            exit_price = yes_bid_d
            profitable = exit_price >= entry_cost + min_profit_c / 100.0
            drift = mid - entry_cost  # positive = favorable
        else:
            # Short YES: buy back at real yes_ask
            exit_price = yes_ask_d
            profitable = exit_price <= entry_cost - min_profit_c / 100.0
            drift = entry_cost - mid  # positive = favorable
        adverse_override = drift <= -adverse_cutoff_c / 100.0
        if not (profitable or adverse_override):
            return None
        action = "sell" if direction == 1 else "buy"
        fill = Fill(
            ts=datetime.now(tz=timezone.utc).isoformat(),
            ticker=ticker, side="yes", action=action,
            count=qty, price_dollars=exit_price, order_id="AGG_CLOSE",
        )
        pos.add_fill(fill)
        reason = "profit" if profitable else "adverse"
        log.info("AGG CLOSE %s %d @ $%.2f [%s] mid=$%.2f cost=$%.2f drift=$%+.3f realized=$%+.2f (%s)",
                 action, qty, exit_price, ticker, mid, entry_cost, drift,
                 pos.realized_pnl, reason)
        return fill


# ---- Live executor (real Kalshi write API) ---------------------------

@dataclass
class LiveExecutor:
    """Real Kalshi order placement. Requires the KalshiClient's key to have trade scope."""
    client: KalshiClient
    portfolio: Portfolio
    open_orders: dict[str, PlacedOrder] = field(default_factory=dict)

    def get_balance(self) -> dict[str, Any]:
        return self.client.get("/portfolio/balance")

    def list_positions(self, ticker: str | None = None) -> dict[str, Any]:
        params = {"ticker": ticker} if ticker else None
        return self.client.get("/portfolio/positions", params=params)

    def list_open_orders(self, ticker: str | None = None) -> dict[str, Any]:
        params = {"status": "resting"}
        if ticker:
            params["ticker"] = ticker
        return self.client.get("/portfolio/orders", params=params)

    def cancel_all(self, ticker: str | None = None) -> int:
        """Cancel all our resting orders (optionally for one ticker)."""
        resp = self.list_open_orders(ticker)
        orders = resp.get("orders", []) or []
        cancelled = 0
        for o in orders:
            order_id = o.get("order_id")
            if not order_id:
                continue
            try:
                # Kalshi DELETE /portfolio/orders/{id}
                # KalshiClient doesn't have .delete(); fall back to requests via session
                path = f"/portfolio/orders/{order_id}"
                url = f"{self.client.base_url}{path}"
                headers = self.client.signer.sign("DELETE", self.client._sign_path(url))
                headers["Accept"] = "application/json"
                self.client._rate_limit()
                r = self.client.session.delete(url, headers=headers, timeout=15)
                if r.status_code < 300:
                    cancelled += 1
                    self.open_orders.pop(order_id, None)
                else:
                    log.warning("cancel %s failed: %s %s", order_id, r.status_code, r.text[:200])
            except Exception as e:
                log.exception("cancel exception: %s", e)
        return cancelled

    def place_order(self, intent: OrderIntent, subsector: str) -> PlacedOrder | None:
        """POST /portfolio/orders. Body matches Kalshi schema."""
        client_order_id = str(uuid.uuid4())
        body: dict[str, Any] = {
            "ticker": intent.ticker,
            "client_order_id": client_order_id,
            "side": intent.side,
            "action": intent.action,
            "type": "limit",
            "count": intent.count,
            "post_only": intent.post_only,
        }
        if intent.side == "yes":
            body["yes_price"] = intent.price_cents
        else:
            body["no_price"] = intent.price_cents
        try:
            path = "/portfolio/orders"
            url = f"{self.client.base_url}{path}"
            headers = self.client.signer.sign("POST", self.client._sign_path(url))
            headers["Content-Type"] = "application/json"
            headers["Accept"] = "application/json"
            self.client._rate_limit()
            r = self.client.session.post(url, json=body, headers=headers, timeout=15)
            if r.status_code >= 400:
                log.warning("place_order rejected: %s %s", r.status_code, r.text[:300])
                return None
            data = r.json() or {}
            order_id = (data.get("order") or {}).get("order_id") or data.get("order_id")
            po = PlacedOrder(order_id=order_id, intent=intent, placed_ts=datetime.now(tz=timezone.utc))
            self.open_orders[order_id] = po
            log.info("LIVE placed %s %s %d @ %dc (%s) id=%s",
                     intent.action, intent.side, intent.count, intent.price_cents, intent.ticker, order_id)
            return po
        except Exception as e:
            log.exception("place_order exception: %s", e)
            return None

    def reconcile_fills(self, ticker: str, subsector: str) -> list[Fill]:
        """Poll trades list for fills that match our order ids."""
        # Kalshi: GET /portfolio/fills?ticker=
        try:
            resp = self.client.get("/portfolio/fills", params={"ticker": ticker, "limit": 100})
        except Exception as e:
            log.exception("list fills failed: %s", e)
            return []
        fills_out = []
        for f in resp.get("fills", []) or []:
            oid = f.get("order_id")
            if not oid or oid not in self.open_orders:
                continue
            po = self.open_orders[oid]
            count = int(f.get("count") or 0)
            price_c = int(f.get("yes_price") or 0) if po.intent.side == "yes" else int(f.get("no_price") or 0)
            fill = Fill(
                ts=f.get("created_time", datetime.now(tz=timezone.utc).isoformat()),
                ticker=ticker, side=po.intent.side, action=po.intent.action,
                count=count, price_dollars=price_c / 100.0, order_id=oid,
            )
            self.portfolio.position(ticker, subsector).add_fill(fill)
            fills_out.append(fill)
            po.filled_count += count
            if po.filled_count >= po.intent.count:
                self.open_orders.pop(oid, None)
        return fills_out
