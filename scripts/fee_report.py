#!/usr/bin/env python3
"""Kalshi fee model: reference table + retro-scoring of the paper sessions.

The paper record in this repo was accumulated with NO fee model at all, so
every PnL number it produced is optimistic. This re-prices the recorded fills
under the real schedule and reports what fees would have cost.

Fill classification (the recorded state predates the `is_taker` field):
  order_id `paper-<uuid>`     -> a resting virtual order         -> MAKER
  order_id `paper-flatten-*`  -> simulated cross at EXIT         -> TAKER
  order_id FORCE_CLOSE        -> rule C hold-time exit           -> TAKER
  order_id AGG_CLOSE          -> aggressive close                -> TAKER

Usage:
  python scripts/fee_report.py                 # table + all sessions
  python scripts/fee_report.py --table-only
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.config import Config
from pmm.trader.fees import DEFAULT_SCHEDULE, FeeBook, FeeSchedule

TAKER_PREFIXES = ("paper-flatten-", "FORCE_CLOSE", "AGG_CLOSE")


def classify(order_id: str) -> str:
    oid = order_id or ""
    for pre in TAKER_PREFIXES:
        if oid.startswith(pre):
            return pre.rstrip("-")
    return "passive"


def load_fee_book(data_dir: Path) -> FeeBook:
    path = data_dir / "series.parquet"
    if not path.exists():
        return FeeBook()
    try:
        import pandas as pd
        return FeeBook.from_series_frame(pd.read_parquet(path))
    except Exception as e:
        print(f"  (fee book unavailable: {e}; using default schedule)")
        return FeeBook()


def print_table() -> None:
    print("=" * 78)
    print("TAKER FEE, cents per contract  --  ceil(0.07 * C * P * (1-P)) / C, per ORDER")
    print("=" * 78)
    sizes = (1, 2, 3, 5, 10, 50, 100)
    print(f"{'price':>7} " + "".join(f"{('C=' + str(c)):>8}" for c in sizes))
    for p_c in (15, 20, 30, 40, 50, 60, 70, 80, 85):
        p = p_c / 100
        row = "".join(f"{DEFAULT_SCHEDULE.taker_fee_dollars(p, c) / c * 100:8.2f}" for c in sizes)
        print(f"{p_c:>6}c " + row)
    print()
    print("Makers pay 0 on a standard series. On `quadratic_with_maker_fees`")
    print("series the maker rate is 0.0175 (a quarter of taker), same rounding:")
    maker = FeeSchedule("quadratic_with_maker_fees", 1.0)
    print(f"{'price':>7} " + "".join(f"{('C=' + str(c)):>8}" for c in sizes))
    for p_c in (20, 35, 50, 65, 80):
        p = p_c / 100
        row = "".join(f"{maker.maker_fee_dollars(p, c) / c * 100:8.2f}" for c in sizes)
        print(f"{p_c:>6}c " + row)
    print()
    print("Read this as the round-trip cost floor:")
    for size in (1, 2, 3):
        pp = DEFAULT_SCHEDULE.min_profitable_spread_cents(0.5, size)
        pt = DEFAULT_SCHEDULE.min_profitable_spread_cents(0.5, size, exit_is_taker=True)
        tt = DEFAULT_SCHEDULE.min_profitable_spread_cents(0.5, size, True, True)
        print(f"  size {size} @ 50c: passive/passive {pp}c | passive/crossed {pt}c | crossed/crossed {tt}c")
    print()


def score_session(path: Path, book: FeeBook) -> dict:
    data = json.loads(path.read_text())
    by_path: dict[str, dict] = defaultdict(lambda: {"n": 0, "contracts": 0, "fee": 0.0})
    gross = 0.0
    for pos in (data.get("positions") or {}).values():
        gross += float(pos.get("realized_pnl") or 0.0)
        for f in pos.get("fills") or []:
            kind = classify(f.get("order_id", ""))
            count = int(f.get("count") or 0)
            price = float(f.get("price_dollars") or 0.0)
            sched = book.for_market(f.get("ticker") or "")
            fee = sched.fee_dollars(price, count, is_taker=(kind != "passive"))
            b = by_path[kind]
            b["n"] += 1
            b["contracts"] += count
            b["fee"] += fee
    total_fee = sum(b["fee"] for b in by_path.values())
    return {"gross": gross, "fee": total_fee, "by_path": dict(by_path)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table-only", action="store_true")
    args = ap.parse_args()

    print_table()
    if args.table_only:
        return 0

    cfg = Config.from_env()
    book = load_fee_book(cfg.data_dir)
    print(f"fee book: {len(book)} series with explicit schedules "
          f"(everything else uses the standard quadratic, no maker fee)")
    print()

    state_dir = cfg.data_dir / "trader_state"
    files = sorted(state_dir.glob("portfolio_paper*.json"))
    if not files:
        print(f"no paper sessions under {state_dir}")
        return 0

    print("=" * 96)
    print("PAPER SESSIONS RE-PRICED WITH FEES")
    print("=" * 96)
    print(f"{'session':<44}{'gross':>10}{'fees':>10}{'net':>10}{'fills':>8}{'%eaten':>9}")
    tot_g = tot_f = 0.0
    all_paths: dict[str, dict] = defaultdict(lambda: {"n": 0, "contracts": 0, "fee": 0.0})
    for f in files:
        r = score_session(f, book)
        n = sum(b["n"] for b in r["by_path"].values())
        net = r["gross"] - r["fee"]
        eaten = (r["fee"] / abs(r["gross"]) * 100) if r["gross"] else float("nan")
        print(f"{f.name[:44]:<44}{r['gross']:>10.2f}{r['fee']:>10.2f}{net:>10.2f}{n:>8}{eaten:>8.0f}%")
        tot_g += r["gross"]
        tot_f += r["fee"]
        for k, b in r["by_path"].items():
            for key in ("n", "contracts", "fee"):
                all_paths[k][key] += b[key]
    print("-" * 96)
    print(f"{'TOTAL':<44}{tot_g:>10.2f}{tot_f:>10.2f}{tot_g - tot_f:>10.2f}")
    print()
    print("Fees by exit path (all sessions):")
    print(f"  {'path':<16}{'fills':>8}{'contracts':>12}{'fee $':>10}{'c/contract':>12}")
    for k, b in sorted(all_paths.items(), key=lambda kv: -kv[1]["fee"]):
        per = (b["fee"] / b["contracts"] * 100) if b["contracts"] else 0.0
        print(f"  {k:<16}{b['n']:>8}{b['contracts']:>12}{b['fee']:>10.2f}{per:>12.2f}")
    print()
    print("Passive fills cost nothing; every cent above is a crossed exit. Note the")
    print("sessions double-count: portfolio_paper.json is the running state, the")
    print("dated files are its snapshots, so the TOTAL overstates. Compare columns,")
    print("not the sum.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
