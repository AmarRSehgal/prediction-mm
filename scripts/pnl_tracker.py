#!/usr/bin/env python3
"""PnL time-series tracker with per-subsector rollup.

Writes two CSVs every 60s:
  research/data/trader_state/pnl_timeseries.csv        — portfolio totals
  research/data/trader_state/pnl_by_subsector.csv      — per-subsector rollup
"""
from __future__ import annotations

import csv
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pmm.config import Config


def snapshot(state_path: Path) -> tuple[dict, dict]:
    if not state_path.exists():
        return ({"realized_pnl": 0, "deployed": 0, "open": 0, "tracked": 0, "fills": 0}, {})
    try:
        data = json.loads(state_path.read_text())
    except Exception:
        return ({"realized_pnl": 0, "deployed": 0, "open": 0, "tracked": 0, "fills": 0}, {})

    positions = data.get("positions") or {}
    totals = {
        "realized_pnl": sum(p.get("realized_pnl", 0.0) for p in positions.values()),
        # "deployed" = capital currently tied up in live inventory (approx.)
        "deployed": sum(
            abs(p.get("yes_contracts", 0)) * (p.get("avg_cost_dollars", 0.5) or 0.5)
            for p in positions.values()
        ),
        "open": sum(1 for p in positions.values() if p.get("yes_contracts", 0) != 0),
        "tracked": len(positions),
        "fills": sum(len(p.get("fills", [])) for p in positions.values()),
    }

    by_sub = defaultdict(lambda: {"realized_pnl": 0, "deployed": 0, "open": 0, "tracked": 0, "fills": 0})
    for p in positions.values():
        sub = p.get("subsector") or "unknown"
        by_sub[sub]["realized_pnl"] += p.get("realized_pnl", 0.0)
        by_sub[sub]["deployed"] += abs(p.get("yes_contracts", 0)) * (p.get("avg_cost_dollars", 0.5) or 0.5)
        if p.get("yes_contracts", 0) != 0:
            by_sub[sub]["open"] += 1
        by_sub[sub]["tracked"] += 1
        by_sub[sub]["fills"] += len(p.get("fills", []))
    return totals, dict(by_sub)


def main() -> int:
    cfg = Config.from_env()
    state_path = cfg.data_dir / "trader_state" / "portfolio_paper.json"
    total_csv = cfg.data_dir / "trader_state" / "pnl_timeseries.csv"
    sub_csv = cfg.data_dir / "trader_state" / "pnl_by_subsector.csv"
    total_csv.parent.mkdir(parents=True, exist_ok=True)

    write_header_total = not total_csv.exists()
    write_header_sub = not sub_csv.exists()

    with open(total_csv, "a", newline="") as f_total, open(sub_csv, "a", newline="") as f_sub:
        w_total = csv.writer(f_total)
        w_sub = csv.writer(f_sub)
        if write_header_total:
            w_total.writerow(["ts_utc", "realized_pnl", "deployed_capital", "n_open_positions", "n_markets_tracked", "n_fills_total"])
        if write_header_sub:
            w_sub.writerow(["ts_utc", "subsector", "realized_pnl", "deployed_capital", "n_open", "n_tracked", "n_fills"])
        while True:
            totals, by_sub = snapshot(state_path)
            ts = datetime.now(tz=timezone.utc).isoformat()
            w_total.writerow([ts, f"{totals['realized_pnl']:.4f}", f"{totals['deployed']:.2f}",
                              totals["open"], totals["tracked"], totals["fills"]])
            for sub, s in sorted(by_sub.items()):
                w_sub.writerow([ts, sub, f"{s['realized_pnl']:.4f}", f"{s['deployed']:.2f}",
                                s["open"], s["tracked"], s["fills"]])
            f_total.flush()
            f_sub.flush()
            time.sleep(60)


if __name__ == "__main__":
    raise SystemExit(main())
