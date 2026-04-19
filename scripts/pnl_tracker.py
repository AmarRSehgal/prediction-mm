#!/usr/bin/env python3
"""Poll portfolio_paper.json and append a PnL snapshot to a CSV every minute.

Writes: research/data/trader_state/pnl_timeseries.csv
Columns: ts_utc, realized_pnl, total_exposure_dollars, n_positions_open, n_markets_tracked, n_fills_total
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pmm.config import Config


def snapshot(state_path: Path, mids_hint: dict[str, float] | None = None) -> dict:
    if not state_path.exists():
        return {"realized_pnl": 0.0, "total_exposure": 0.0, "n_pos": 0, "n_tracked": 0, "n_fills": 0}
    try:
        data = json.loads(state_path.read_text())
    except Exception:
        return {"realized_pnl": 0.0, "total_exposure": 0.0, "n_pos": 0, "n_tracked": 0, "n_fills": 0}
    positions = data.get("positions") or {}
    realized = sum(p.get("realized_pnl", 0.0) for p in positions.values())
    # Exposure approx: abs(yes_contracts) * 0.50 as rough mid proxy if no live mids
    exposure = sum(abs(p.get("yes_contracts", 0)) * (mids_hint.get(t, 0.50) if mids_hint else 0.50)
                   for t, p in positions.items())
    n_pos = sum(1 for p in positions.values() if p.get("yes_contracts", 0) != 0)
    n_fills = sum(len(p.get("fills", [])) for p in positions.values())
    return {
        "realized_pnl": realized,
        "total_exposure": exposure,
        "n_pos": n_pos,
        "n_tracked": len(positions),
        "n_fills": n_fills,
    }


def main() -> int:
    cfg = Config.from_env()
    state_path = cfg.data_dir / "trader_state" / "portfolio_paper.json"
    csv_path = cfg.data_dir / "trader_state" / "pnl_timeseries.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not csv_path.exists()

    with open(csv_path, "a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["ts_utc", "realized_pnl", "total_exposure", "n_positions_open", "n_markets_tracked", "n_fills_total"])
        while True:
            s = snapshot(state_path)
            ts = datetime.now(tz=timezone.utc).isoformat()
            w.writerow([ts, f"{s['realized_pnl']:.4f}", f"{s['total_exposure']:.2f}", s["n_pos"], s["n_tracked"], s["n_fills"]])
            f.flush()
            time.sleep(60)


if __name__ == "__main__":
    raise SystemExit(main())
