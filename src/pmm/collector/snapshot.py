"""Periodic orderbook snapshot collector."""
from __future__ import annotations

import logging
import signal
import time
from dataclasses import dataclass
from typing import Iterable

from pmm.kalshi.client import KalshiAPIError, KalshiClient
from pmm.storage.parquet import OrderbookWriter

log = logging.getLogger(__name__)


@dataclass
class SnapshotCollector:
    client: KalshiClient
    writer: OrderbookWriter
    tickers: list[str]
    interval_s: float = 5.0
    depth: int = 10

    def run(self, duration_s: float | None = None) -> None:
        stop = {"flag": False}

        def _handler(signum, frame):
            log.info("signal %s received, stopping", signum)
            stop["flag"] = True

        signal.signal(signal.SIGINT, _handler)
        signal.signal(signal.SIGTERM, _handler)

        start = time.monotonic()
        cycle = 0
        while not stop["flag"]:
            cycle_start = time.monotonic()
            for ticker in self.tickers:
                if stop["flag"]:
                    break
                try:
                    snap = self.client.get_orderbook(ticker, depth=self.depth)
                    captured_at_ms = int(time.time() * 1000)
                    # Kalshi wraps the book in `orderbook_fp` (dollar strings) or
                    # `orderbook` (integer cents). Prefer the former.
                    book = snap.get("orderbook_fp") or snap.get("orderbook") or snap
                    self.writer.write_snapshot(ticker, book, captured_at_ms)
                except KalshiAPIError as e:
                    log.warning("api error for %s: %s", ticker, e)
                except Exception:
                    log.exception("unexpected error for %s", ticker)

            cycle += 1
            if duration_s is not None and time.monotonic() - start >= duration_s:
                break

            elapsed = time.monotonic() - cycle_start
            sleep_for = max(0.0, self.interval_s - elapsed)
            if sleep_for > 0:
                for _ in range(int(sleep_for * 10)):
                    if stop["flag"]:
                        break
                    time.sleep(0.1)

        self.writer.close()
        log.info("collector stopped after %d cycles", cycle)
