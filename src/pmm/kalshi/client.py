"""Read-only Kalshi REST client.

Scoped deliberately to read endpoints. No order-placing methods exist in this
file on purpose. If you find yourself wanting to add one, stop and reconsider
the phase of the project first.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

import requests

from pmm.config import Config
from pmm.kalshi.auth import KalshiSigner

log = logging.getLogger(__name__)


class KalshiAPIError(RuntimeError):
    def __init__(self, status_code: int, body: str, path: str):
        super().__init__(f"Kalshi API {status_code} on {path}: {body[:500]}")
        self.status_code = status_code
        self.body = body
        self.path = path


@dataclass
class KalshiClient:
    base_url: str
    signer: KalshiSigner
    session: requests.Session
    min_interval_s: float = 0.1
    _last_request_ts: float = 0.0

    @classmethod
    def from_config(cls, cfg: Config) -> "KalshiClient":
        signer = KalshiSigner.from_pem_file(cfg.key_id, cfg.private_key_path)
        return cls(
            base_url=cfg.base_url,
            signer=signer,
            session=requests.Session(),
        )

    def _sign_path(self, url: str) -> str:
        # Kalshi signs the path portion of the URL only (excluding query).
        parsed = urlparse(url)
        return parsed.path

    def _rate_limit(self) -> None:
        elapsed = time.monotonic() - self._last_request_ts
        if elapsed < self.min_interval_s:
            time.sleep(self.min_interval_s - elapsed)
        self._last_request_ts = time.monotonic()

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        headers = self.signer.sign("GET", self._sign_path(url))
        headers["Accept"] = "application/json"
        self._rate_limit()
        resp = self.session.get(url, headers=headers, params=params, timeout=15)
        if resp.status_code >= 400:
            raise KalshiAPIError(resp.status_code, resp.text, path)
        return resp.json()

    # ---- Read endpoints ---------------------------------------------------

    def exchange_status(self) -> dict[str, Any]:
        return self.get("/exchange/status")

    def list_series(self, **params: Any) -> dict[str, Any]:
        return self.get("/series", params=params)

    def list_events(self, **params: Any) -> dict[str, Any]:
        return self.get("/events", params=params)

    def list_markets(self, **params: Any) -> dict[str, Any]:
        """Common params: status (open|closed|settled), series_ticker, event_ticker, limit, cursor."""
        return self.get("/markets", params=params)

    def get_market(self, ticker: str) -> dict[str, Any]:
        return self.get(f"/markets/{ticker}")

    def get_orderbook(self, ticker: str, depth: int = 10) -> dict[str, Any]:
        return self.get(f"/markets/{ticker}/orderbook", params={"depth": depth})

    def get_trades(self, **params: Any) -> dict[str, Any]:
        """Trade history. Params include ticker, limit, cursor, min_ts, max_ts."""
        return self.get("/markets/trades", params=params)

    # ---- Pagination helper ------------------------------------------------

    def paginate(self, fn, collection_key: str, max_pages: int = 50, **kwargs):
        """Iterate through a paginated endpoint. `fn` is a bound method returning dict with
        `cursor` and `collection_key` fields. Yields individual items."""
        cursor = None
        pages = 0
        while pages < max_pages:
            call_kwargs = dict(kwargs)
            if cursor:
                call_kwargs["cursor"] = cursor
            page = fn(**call_kwargs)
            items = page.get(collection_key, [])
            for item in items:
                yield item
            cursor = page.get("cursor")
            pages += 1
            if not cursor:
                return
