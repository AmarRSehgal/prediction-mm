#!/usr/bin/env python3
"""One-shot status tick.

Reads current portfolio state + trader log, compares against last tick's
snapshot (stored in trader_state/last_tick.json), prints deltas, updates
snapshot.

Output fields: fills_delta, flatten_delta, skip_delta, account_value, realized,
unrealized, open, deployed — plus the deltas since the last tick.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pmm.config import Config


def count_log_events(log_path: Path) -> dict[str, int]:
    counts = {"fills": 0, "flatten": 0, "skip_vol": 0, "errors": 0}
    if not log_path.exists():
        return counts
    with open(log_path, "r", errors="replace") as f:
        for line in f:
            if "PAPER FILL" in line:
                counts["fills"] += 1
            elif "PAPER FLATTEN" in line:
                counts["flatten"] += 1
            elif "SKIP " in line and "recent vol" in line:
                counts["skip_vol"] += 1
            elif re.search(r"Traceback|ERROR|Exception", line):
                counts["errors"] += 1
    return counts


def portfolio_snapshot(state_path: Path) -> dict:
    if not state_path.exists():
        return {"account_value": 3880, "realized": 0, "unrealized": 0,
                "cash_tied": 0, "open": 0, "tracked": 0, "fills": 0,
                "best_sub": [], "worst_sub": [],
                "bucket_sub3c": {"realized": 0.0, "unrealized": 0.0, "fills": 0, "open": 0, "tracked": 0},
                "bucket_ge3c": {"realized": 0.0, "unrealized": 0.0, "fills": 0, "open": 0, "tracked": 0}}
    data = json.loads(state_path.read_text())
    positions = data.get("positions") or {}
    starting = float(data.get("starting_cash", 3880))

    realized = 0.0
    unrealized = 0.0
    cash_tied = 0.0
    n_open = 0
    n_fills = 0
    fees = 0.0
    by_sub_net = defaultdict(float)
    # Spread-bucket split: positions whose first fill came at TOB spread < 3c
    # vs >= 3c. Lets us evaluate the 1c-min-spread change in isolation.
    bucket_sub3c = {"realized": 0.0, "unrealized": 0.0, "fills": 0, "open": 0, "tracked": 0}
    bucket_ge3c  = {"realized": 0.0, "unrealized": 0.0, "fills": 0, "open": 0, "tracked": 0}
    bucket_unkn  = {"realized": 0.0, "unrealized": 0.0, "fills": 0, "open": 0, "tracked": 0}
    for pos in positions.values():
        qty = int(pos.get("yes_contracts", 0))
        cost = float(pos.get("avg_cost_dollars", 0.0))
        mid = float(pos.get("last_mid_dollars", 0.5))
        r = float(pos.get("realized_pnl", 0.0))
        fees += float(pos.get("fees_paid", 0.0))
        u = qty * (mid - cost)
        realized += r
        unrealized += u
        ct = qty * cost if qty > 0 else -qty * (1 - cost) if qty < 0 else 0
        cash_tied += ct
        if qty != 0:
            n_open += 1
        f = len(pos.get("fills", []))
        n_fills += f
        by_sub_net[pos.get("subsector", "unknown")] += r + u
        sp = pos.get("first_fill_spread_c")
        if sp is None:
            b = bucket_unkn
        elif sp < 3:
            b = bucket_sub3c
        else:
            b = bucket_ge3c
        b["realized"] += r
        b["unrealized"] += u
        b["fills"] += f
        b["tracked"] += 1
        if qty != 0:
            b["open"] += 1

    sorted_sub = sorted(by_sub_net.items(), key=lambda x: x[1], reverse=True)
    return {
        "account_value": starting + realized + unrealized,
        "realized": realized,
        "unrealized": unrealized,
        "fees": fees,
        "cash_tied": cash_tied,
        "open": n_open,
        "tracked": len(positions),
        "fills": n_fills,
        "best_sub": sorted_sub[:3],
        "worst_sub": sorted_sub[-3:] if len(sorted_sub) > 3 else [],
        "bucket_sub3c": bucket_sub3c,
        "bucket_ge3c": bucket_ge3c,
    }


def main() -> int:
    cfg = Config.from_env()
    state_path = cfg.data_dir / "trader_state" / "portfolio_paper.json"
    log_path = Path.home() / "personal" / "prediction-mm" / "logs" / "overnight_trader.log"
    tick_path = cfg.data_dir / "trader_state" / "last_tick.json"

    prev = {}
    if tick_path.exists():
        try:
            prev = json.loads(tick_path.read_text())
        except Exception:
            prev = {}

    snap = portfolio_snapshot(state_path)
    log_counts = count_log_events(log_path)
    now_iso = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")

    curr = {
        "ts": now_iso,
        "account_value": snap["account_value"],
        "realized": snap["realized"],
        "unrealized": snap["unrealized"],
        "fees": snap["fees"],
        "cash_tied": snap["cash_tied"],
        "open": snap["open"],
        "tracked": snap["tracked"],
        "fills_total": snap["fills"],
        "log_fills": log_counts["fills"],
        "log_flatten": log_counts["flatten"],
        "log_skip": log_counts["skip_vol"],
        "log_errors": log_counts["errors"],
    }

    def delta(k, fmt="{:+d}"):
        if k not in prev: return "n/a"
        d = curr[k] - prev[k]
        if isinstance(d, float): return f"{d:+.4f}"
        return fmt.format(d)

    print(f"=== tick {now_iso} ===")
    print(f"  account_value   ${curr['account_value']:.2f}  (delta ${(curr['account_value']-prev.get('account_value',curr['account_value'])):+.4f})")
    print(f"  realized        ${curr['realized']:+.2f}  (delta ${(curr['realized']-prev.get('realized',curr['realized'])):+.4f})")
    print(f"  unrealized      ${curr['unrealized']:+.2f}  (delta ${(curr['unrealized']-prev.get('unrealized',curr['unrealized'])):+.4f})")
    print(f"  fees paid       ${curr['fees']:.4f}  (delta ${(curr['fees']-prev.get('fees',curr['fees'])):+.4f})  [realized is NET of these]")
    print(f"  cash tied up    ${curr['cash_tied']:.2f}  (delta ${(curr['cash_tied']-prev.get('cash_tied',curr['cash_tied'])):+.2f})")
    print(f"  open positions  {curr['open']}  (delta {delta('open')})")
    print(f"  fills (state)   {curr['fills_total']}  (delta {delta('fills_total')})")
    print(f"  fills (log)     {curr['log_fills']}  (delta {delta('log_fills')})")
    print(f"  flatten events  {curr['log_flatten']}  (delta {delta('log_flatten')})")
    print(f"  SKIP-vol events {curr['log_skip']}  (delta {delta('log_skip')})")
    print(f"  errors          {curr['log_errors']}  (delta {delta('log_errors')})")
    print()
    b1 = snap["bucket_sub3c"]
    b2 = snap["bucket_ge3c"]
    print(f"  sub-3c spread    net ${b1['realized']+b1['unrealized']:+.4f}  (r={b1['realized']:+.3f}  u={b1['unrealized']:+.3f})  fills={b1['fills']}  open={b1['open']}/{b1['tracked']}")
    print(f"  >=3c spread      net ${b2['realized']+b2['unrealized']:+.4f}  (r={b2['realized']:+.3f}  u={b2['unrealized']:+.3f})  fills={b2['fills']}  open={b2['open']}/{b2['tracked']}")
    print()
    print("  TOP 3 subsectors by net PnL:")
    for s, net in snap["best_sub"]:
        print(f"    {s:<30} ${net:+.4f}")
    if snap["worst_sub"]:
        print("  BOTTOM 3:")
        for s, net in snap["worst_sub"]:
            print(f"    {s:<30} ${net:+.4f}")

    # Persist
    tick_path.parent.mkdir(parents=True, exist_ok=True)
    tick_path.write_text(json.dumps(curr, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
