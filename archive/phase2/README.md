# Paper A/B, phase 2 (2026-10-30 to 2026-11-02)

v1 (frozen, unchanged) against the v2 engine on Kalshi with an aggro close at all times: any
v2 position rested in full at the touch on the closing side, through every fair-value gate,
never crossing. Stopped after 3 scored days because v2 tripped its own kill criterion
(negative realized PnL per resolved contract). v1 lost at its phase-1 rate (-$1.98/day), v2
lost far more (niche -$7.72/day, crypto -$41.87/day): the rule gave away the +5.5c (niche)
/ +1.8c (crypto) that phase-1 exits earned, and flattening faster tripled turnover on
entries that were already adversely selected. Phase 3 (from 2026-11-03) quotes normally and
unwinds only near the close.

| file | what it is |
|---|---|
| `report.json` | the final scored report, markouts included, as `scripts/ab_report.py` produced it on 2026-11-02 |
| `report.txt` | that run's console table |
| `data.tar.xz` | the raw record: `ab/<arm>/portfolio.json`, `fills.jsonl`, `settlements.jsonl` for every arm, and `ab/daily.jsonl` |

2026-10-30's first session had no prior row, so the per-day series starts on 10-31.

To re-score it:

    mkdir -p /tmp/phase2 && tar -xJf archive/phase2/data.tar.xz -C /tmp/phase2
    PMM_DATA_DIR=/tmp/phase2 env -u PYTHONPATH /opt/local/bin/python3.13 scripts/ab_report.py \
        --no-markouts --date 2026-11-02 --output /tmp/phase2/report.json

Later code carries its own phase labels; the numbers it computes from these files are phase 2's.
