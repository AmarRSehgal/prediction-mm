#!/usr/bin/env python3
"""PnL / account-value time-series tracker.

Writes:
  research/data/trader_state/pnl_timeseries.csv
    ts_utc, account_value, realized_pnl, unrealized_pnl, cash_tied_up, n_open, n_tracked, n_fills
  research/data/trader_state/pnl_by_subsector.csv
    ts_utc, subsector, account_value_contrib, realized_pnl, unrealized_pnl, cash_tied_up, n_open, n_tracked, n_fills

Account value definition:
  account_value = starting_cash + realized_pnl + unrealized_pnl
  unrealized_pnl per position = yes_contracts * (last_observed_mid - avg_cost)
  (works for both long and short positions; signs align)

The trader writes last_mid_dollars on every cycle. If it stalls or a position
hasn't been re-observed in a while, that field goes stale — but it's still
closer to reality than ignoring unrealized altogether.
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
        return ({"starting": 1000, "account_value": 1000, "realized": 0, "unrealized": 0,
                 "cash_tied": 0, "open": 0, "tracked": 0, "fills": 0}, {})
    try:
        data = json.loads(state_path.read_text())
    except Exception:
        return ({"starting": 1000, "account_value": 1000, "realized": 0, "unrealized": 0,
                 "cash_tied": 0, "open": 0, "tracked": 0, "fills": 0}, {})

    positions = data.get("positions") or {}
    starting = float(data.get("starting_cash", 1000))

    realized = sum(float(p.get("realized_pnl", 0.0)) for p in positions.values())
    unrealized = 0.0
    cash_tied = 0.0
    n_open = 0
    n_fills = 0
    by_sub = defaultdict(lambda: {"realized": 0, "unrealized": 0, "cash_tied": 0, "open": 0, "tracked": 0, "fills": 0})

    for pos in positions.values():
        qty = int(pos.get("yes_contracts", 0))
        cost = float(pos.get("avg_cost_dollars", 0.0))
        mid = float(pos.get("last_mid_dollars", 0.5))
        rpnl = float(pos.get("realized_pnl", 0.0))
        sub = pos.get("subsector", "unknown")
        fills = len(pos.get("fills", []))

        n_fills += fills
        upnl = qty * (mid - cost)
        unrealized += upnl
        if qty > 0:
            ct = qty * cost
        elif qty < 0:
            ct = -qty * (1 - cost)
        else:
            ct = 0.0
        cash_tied += ct
        if qty != 0:
            n_open += 1

        by_sub[sub]["realized"] += rpnl
        by_sub[sub]["unrealized"] += upnl
        by_sub[sub]["cash_tied"] += ct
        by_sub[sub]["open"] += 1 if qty != 0 else 0
        by_sub[sub]["tracked"] += 1
        by_sub[sub]["fills"] += fills

    account_value = starting + realized + unrealized

    totals = {
        "starting": starting,
        "account_value": account_value,
        "realized": realized,
        "unrealized": unrealized,
        "cash_tied": cash_tied,
        "open": n_open,
        "tracked": len(positions),
        "fills": n_fills,
    }
    return totals, dict(by_sub)


def main() -> int:
    cfg = Config.from_env()
    state_path = cfg.data_dir / "trader_state" / "portfolio_paper.json"
    total_csv = cfg.data_dir / "trader_state" / "pnl_timeseries.csv"
    sub_csv = cfg.data_dir / "trader_state" / "pnl_by_subsector.csv"
    total_csv.parent.mkdir(parents=True, exist_ok=True)

    write_header_total = not total_csv.exists() or total_csv.stat().st_size == 0
    write_header_sub = not sub_csv.exists() or sub_csv.stat().st_size == 0

    with open(total_csv, "a", newline="") as f_total, open(sub_csv, "a", newline="") as f_sub:
        w_total = csv.writer(f_total)
        w_sub = csv.writer(f_sub)
        if write_header_total:
            w_total.writerow(["ts_utc", "account_value", "realized_pnl", "unrealized_pnl",
                              "cash_tied_up", "n_open_positions", "n_markets_tracked", "n_fills_total"])
        if write_header_sub:
            w_sub.writerow(["ts_utc", "subsector", "realized_pnl", "unrealized_pnl",
                            "cash_tied_up", "n_open", "n_tracked", "n_fills"])
        while True:
            totals, by_sub = snapshot(state_path)
            ts = datetime.now(tz=timezone.utc).isoformat()
            w_total.writerow([ts,
                              f"{totals['account_value']:.4f}",
                              f"{totals['realized']:.4f}",
                              f"{totals['unrealized']:.4f}",
                              f"{totals['cash_tied']:.2f}",
                              totals["open"], totals["tracked"], totals["fills"]])
            for sub, s in sorted(by_sub.items()):
                w_sub.writerow([ts, sub,
                                f"{s['realized']:.4f}",
                                f"{s['unrealized']:.4f}",
                                f"{s['cash_tied']:.2f}",
                                s["open"], s["tracked"], s["fills"]])
            f_total.flush()
            f_sub.flush()
            time.sleep(60)


if __name__ == "__main__":
    raise SystemExit(main())
