#!/usr/bin/env python3
"""Score the Kalshi paper A/B: v1 (frozen at tag paper-ab-baseline) against v2.

    baseline   v1 exactly as it lost ~$130 in April, run from a git worktree
    v2_niche   v2 engine on v1's own universe
    v2_crypto  v2 engine on hourly BTC/ETH strikes, Binance-anchored fair value

The arms trade different markets, so the paired unit is the DAY: every run
appends each arm's total PnL (realized + mark-to-mid, net of fees) to
daily.jsonl, and day-over-day differences are compared on the same days.
Alongside that, per resolved contract and by exit path -- the table that showed
v1's losses were all in its forced exits -- and 5m / 60m markouts computed the
same way for every arm from Kalshi's 1-minute candles.

    env -u PYTHONPATH /opt/local/bin/python3.13 scripts/ab_report.py
    env -u PYTHONPATH /opt/local/bin/python3.13 scripts/ab_report.py --output web/kalshi_mm_paper.json
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pmm.config import Config
from pmm.kalshi.client import KalshiClient
from pmm.trader.position import Fill, MarketPosition, load_portfolio

MIN_DAYS = 14
MIN_CONTRACTS = 200
BOOT = 2000
ARMS = {
    "baseline": ("control", "v1 unchanged: Avellaneda-Stoikov quotes around the touch mid on niche "
                            "markets, crossing the spread to flatten before game windows and closes."),
    "v2_niche": ("treatment", "v2 engine on the same universe: edge curve around a depth-weighted mid, "
                              "never crosses, reduce-only instead of flatten, holds to resolution."),
    "v2_crypto": ("treatment", "v2 engine on hourly BTC/ETH strike ladders, fair value from Binance "
                               "anchored to the Kalshi book, exposure netted across strikes."),
}
KILL = [f"A treatment whose realized expectancy per resolved contract is negative after {MIN_CONTRACTS} "
        "contracts is stopped.",
        "Any aggregate exposure breach, or a position held into a resolution rule nobody read, stops "
        "that arm until fixed.",
        "Written before the first v2 paper fill (2026-09-25); not moved after seeing results."]
CAVEATS = [
    "Paper fills. v2's venue is stricter than v1's: v2 queues behind the size at its own price and "
    "waits 0.5s for acks and cancels; v1 queues behind the top of book and fills instantly. "
    "That bias works against v2.",
    "v1 marks open inventory at the last mid it saw; v2 holds to resolution and settles at 0 or 100.",
    "Days lost to the laptop sleeping are lost for every arm at once.",
]


def exit_kind(order_id: str) -> str:
    if order_id == "SETTLE":
        return "settled"
    if order_id.startswith("paper-flatten") or order_id in ("FORCE_CLOSE", "AGG_CLOSE"):
        return "crossed"
    return "passive"


def boot_ci(xs, seed=7):
    if len(xs) < 2:
        return None
    rng = random.Random(seed)
    n = len(xs)
    m = sorted(sum(xs[rng.randrange(n)] for _ in range(n)) / n for _ in range(BOOT))
    return [round(m[int(0.025 * BOOT)], 4), round(m[int(0.975 * BOOT)], 4)]


def candles(client, ticker: str, t0: int, t1: int) -> dict[int, float]:
    """minute end ts -> mid cents, from Kalshi's 1-minute candles."""
    series = ticker.split("-", 1)[0]
    out: dict[int, float] = {}
    start = t0
    while start < t1:
        end = min(t1, start + 4000 * 60)
        try:
            r = client.get(f"/series/{series}/markets/{ticker}/candlesticks",
                           params={"start_ts": start, "end_ts": end, "period_interval": 1})
        except Exception:
            break
        for c in r.get("candlesticks") or []:
            b = float((c.get("yes_bid") or {}).get("close_dollars") or 0)
            a = float((c.get("yes_ask") or {}).get("close_dollars") or 0)
            if 0 < b < a < 1:
                out[int(c["end_period_ts"])] = (a + b) * 50
        start = end
    return out


def mid_at(series: dict[int, float], t: float) -> float | None:
    k = (int(t) // 60 + 1) * 60
    for probe in (k, k + 60, k - 60):
        if probe in series:
            return series[probe]
    return None


def score_arm(name: str, pf_path: Path, client, with_markouts: bool) -> dict:
    pf = load_portfolio(pf_path, starting_cash=0.0)
    by_exit = defaultdict(lambda: [0, 0.0])
    closed_contracts = 0
    per_market: list[float] = []
    fills = contracts = 0
    fees = mtm = 0.0
    mk = defaultdict(list)
    for t, pos in pf.positions.items():
        replay = MarketPosition(ticker=t, subsector=pos.subsector)
        for f in pos.fills:
            prev, before = replay.yes_contracts, replay.realized_pnl
            replay.add_fill(f)
            if f.order_id != "SETTLE":
                fills += 1
                contracts += f.count
            fees += f.fee_dollars
            reducing = prev != 0 and (prev > 0) != (replay.yes_contracts - prev > 0)
            if reducing:
                closed = min(abs(prev), f.count)
                k = exit_kind(f.order_id)
                by_exit[k][0] += closed
                by_exit[k][1] += replay.realized_pnl - before      # net of this fill's fee
                closed_contracts += closed
        m = pos.realized_pnl + pos.unrealized_pnl(pos.last_mid_dollars)
        mtm += pos.unrealized_pnl(pos.last_mid_dollars)
        per_market.append(m)
        if with_markouts and pos.fills:
            ts = [datetime.fromisoformat(f.ts.replace("Z", "+00:00")).timestamp() for f in pos.fills
                  if f.order_id != "SETTLE"]
            if ts:
                series = candles(client, t, int(min(ts)) - 120, int(min(max(ts) + 3700, time.time())))
                for f, tf in zip((f for f in pos.fills if f.order_id != "SETTLE"), ts):
                    s = 1 if f.action == "buy" else -1
                    for h in (300, 3600):
                        mid = mid_at(series, tf + h)
                        if mid is not None and tf + h < time.time():
                            mk[str(h)].append(s * (mid - f.price_dollars * 100))
    total = sum(per_market)
    realized = pf.realized_pnl_total()
    passive = by_exit.get("passive", [0])[0]
    exits = {k: {"contracts": v[0], "pnl": round(v[1], 2),
                 "per_contract_c": round(100 * v[1] / v[0], 2) if v[0] else None} for k, v in by_exit.items()}
    return {
        "name": name, "role": ARMS[name][0], "description": ARMS[name][1],
        "fills": fills, "size": contracts, "markets": len(pf.positions),
        "pnl": round(total, 2), "realized": round(realized, 2), "mtm": round(mtm, 2), "fees": round(fees, 2),
        "pnl_per_size_c": round(100 * total / contracts, 3) if contracts else None,
        "resolved_contracts": closed_contracts,
        "realized_per_resolved_c": round(100 * sum(v[1] for v in by_exit.values()) / closed_contracts, 3)
        if closed_contracts else None,
        "passive_exit_share": round(passive / closed_contracts, 3) if closed_contracts else None,
        "exits": exits,
        "per_market_pnl_ci": boot_ci(per_market),
        "markouts_c": {h: round(sum(v) / len(v), 3) for h, v in mk.items() if v} or None,
    }


def build(data: Path, client, with_markouts: bool = True) -> dict:
    arms = [score_arm(a, data / a / "portfolio.json", client, with_markouts) for a in ARMS]
    daily_path = data / "daily.jsonl"
    today = datetime.now(timezone.utc).date().isoformat()
    rows = [json.loads(x) for x in daily_path.read_text().splitlines()] if daily_path.exists() else []
    rows = [r for r in rows if r["date"] != today] + [{"date": today, **{a["name"]: a["pnl"] for a in arms}}]
    daily_path.write_text("".join(json.dumps(r) + "\n" for r in rows))
    deltas = {a: [(r1[a] - r0[a]) for r0, r1 in zip(rows, rows[1:]) if a in r0 and a in r1] for a in ARMS}
    for a in arms:
        d = deltas[a["name"]]
        a["units"] = len(d)
        a["pnl_per_unit"] = round(sum(d) / len(d), 3) if d else None
        a["pnl_per_unit_ci"] = boot_ci(d)
    comps = []
    for t in ("v2_niche", "v2_crypto"):
        diff = [x - y for x, y in zip(deltas[t], deltas["baseline"])]
        ci = boot_ci(diff)
        n = len(diff)
        verdict = ("collecting" if n < MIN_DAYS or ci is None else
                   "better" if ci[0] > 0 else "worse" if ci[1] < 0 else "indistinguishable")
        comps.append({"treatment": t, "control": "baseline", "metric": "pnl_per_day",
                      "diff": round(sum(diff) / n, 3) if n else None, "ci": ci, "verdict": verdict})
    n_days = len(rows) - 1
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "experiment": "Kalshi market making: v1 against the v2 engine",
        "venue": "Kalshi", "paper": True, "started": "2026-09-25",
        "unit": "day", "min_units_for_verdict": MIN_DAYS,
        "status": "verdict" if n_days >= MIN_DAYS else "collecting",
        "headline": headline(n_days, arms, comps),
        "arms": arms, "comparisons": comps, "kill_criteria": KILL, "caveats": CAVEATS,
    }


def headline(n_days, arms, comps) -> str:
    base = next(a for a in arms if a["name"] == "baseline")
    if n_days < MIN_DAYS:
        bits = [f"{a['name']} {a['pnl']:+.2f} over {a['fills']} fills" for a in arms]
        return (f"Collecting: day {n_days} of {MIN_DAYS} before the arms are scored against each other. "
                f"Running totals, not results: {'; '.join(bits)}.")
    parts = []
    for c in comps:
        lo, hi = c["ci"]
        parts.append(f"{c['treatment']} {c['verdict']} than v1 ({c['diff']:+.2f}/day, 95% CI {lo:+.2f} to {hi:+.2f})")
    return f"After {n_days} days: " + "; ".join(parts) + f". v1 itself: {base['pnl']:+.2f}."


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    ap.add_argument("--no-markouts", action="store_true", help="skip the candle fetch (fast, offline-ish)")
    a = ap.parse_args()
    cfg = Config.from_env()
    doc = build(cfg.data_dir / "ab", KalshiClient.from_config(cfg), not a.no_markouts)
    print(doc["headline"])
    for r in doc["arms"]:
        print(f"  {r['name']:10} fills={r['fills']:5} pnl={r['pnl']:+8.2f} realized={r['realized']:+8.2f} "
              f"resolved={r['resolved_contracts']} passive={r['passive_exit_share']} exits={r['exits']} "
              f"markouts={r['markouts_c']}")
    if a.output:
        Path(a.output).parent.mkdir(parents=True, exist_ok=True)
        Path(a.output).write_text(json.dumps(doc, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
