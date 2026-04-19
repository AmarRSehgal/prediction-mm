"""Append-mode parquet writers partitioned by (date, ticker).

Simple approach: for each (date, ticker) open a ParquetWriter. Rotate at midnight
UTC. Callers must close writers explicitly on shutdown.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

log = logging.getLogger(__name__)


def _today_utc() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


@dataclass
class _Rotating:
    data_dir: Path
    kind: str  # "orderbook" or "trades"
    _writers: dict[tuple[str, str], pq.ParquetWriter] = field(default_factory=dict)

    def _path(self, date_str: str, ticker: str) -> Path:
        return self.data_dir / self.kind / date_str / f"{ticker}.parquet"

    def _writer_for(self, date_str: str, ticker: str, schema: pa.Schema) -> pq.ParquetWriter:
        key = (date_str, ticker)
        if key not in self._writers:
            path = self._path(date_str, ticker)
            path.parent.mkdir(parents=True, exist_ok=True)
            # If file exists, we need to append; pyarrow ParquetWriter doesn't natively
            # append, so we write new files with a suffix per process session.
            if path.exists():
                ts = datetime.now(tz=timezone.utc).strftime("%H%M%S")
                path = path.with_suffix(f".{ts}.parquet")
            self._writers[key] = pq.ParquetWriter(path, schema)
        return self._writers[key]

    def close(self) -> None:
        for writer in self._writers.values():
            try:
                writer.close()
            except Exception:
                log.exception("failed to close parquet writer")
        self._writers.clear()


class OrderbookWriter(_Rotating):
    """Writes orderbook snapshots. Each row is one snapshot with serialized levels."""

    def __init__(self, data_dir: Path) -> None:
        super().__init__(data_dir=data_dir, kind="orderbook")

    def write_snapshot(self, ticker: str, snapshot: dict[str, Any], captured_at_ms: int) -> None:
        """snapshot is the raw `orderbook_fp` dict from Kalshi (keys: yes_dollars, no_dollars).
        Each is a list of [price_str_dollars, size_str] pairs sorted ascending in price
        (last entry = best bid on that side)."""
        yes_raw = snapshot.get("yes_dollars") or snapshot.get("yes") or []
        no_raw = snapshot.get("no_dollars") or snapshot.get("no") or []

        def norm(levels):
            # tolerate str or numeric inputs
            return [[float(p), float(s)] for p, s in levels]

        yes = norm(yes_raw)
        no = norm(no_raw)

        yes_bid = yes[-1] if yes else [None, None]
        no_bid = no[-1] if no else [None, None]
        yes_ask = (1.0 - no_bid[0]) if no_bid[0] is not None else None

        row = {
            "captured_at_ms": captured_at_ms,
            "ticker": ticker,
            "yes_levels": yes,
            "no_levels": no,
            "yes_bid_dollars": yes_bid[0],
            "yes_bid_size": yes_bid[1],
            "yes_ask_dollars": yes_ask,
            "yes_ask_size": no_bid[1],
            "yes_depth_total": sum(s for _, s in yes),
            "no_depth_total": sum(s for _, s in no),
        }
        df = pd.DataFrame([row])
        table = pa.Table.from_pandas(df, preserve_index=False)
        w = self._writer_for(_today_utc(), ticker, table.schema)
        w.write_table(table)


class TradesWriter(_Rotating):
    def __init__(self, data_dir: Path) -> None:
        super().__init__(data_dir=data_dir, kind="trades")

    def write_trades(self, ticker: str, trades: list[dict[str, Any]]) -> None:
        if not trades:
            return
        df = pd.DataFrame(trades)
        df["ticker"] = ticker
        table = pa.Table.from_pandas(df, preserve_index=False)
        w = self._writer_for(_today_utc(), ticker, table.schema)
        w.write_table(table)
