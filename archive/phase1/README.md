# Paper A/B, phase 1 (2026-09-25 to 2026-10-29)

v1 (frozen at tag `paper-ab-baseline`) against the v2 engine on Kalshi, before the aggro
close. In this phase v2 quoted its reducing side only as far as the edge curve allowed, so
a small position could rest off the touch and was otherwise held to resolution. Phase 2
(from 2026-10-30) adds the aggro close to every v2 arm and starts all arms from flat.

| file | what it is |
|---|---|
| `report.json` | the final scored report, markouts included, exactly as `scripts/ab_report.py` produced it on 2026-10-29 |
| `report.txt` | that run's console table |
| `data.tar.xz` | the raw record: `ab/<arm>/portfolio.json`, `fills.jsonl`, `settlements.jsonl` for every arm, and `ab/daily.jsonl` |

Days 2026-10-02..24 and 2026-10-29 are declared downtime (`~/personal/automation/downtime.json`)
and excluded from the per-day statistics. Positions still open on 2026-10-29 are marked to
mid in `report.json`; they were never settled in this record.

To re-score it, or score it a different way:

    mkdir -p /tmp/phase1 && tar -xJf archive/phase1/data.tar.xz -C /tmp/phase1
    PMM_DATA_DIR=/tmp/phase1 env -u PYTHONPATH /opt/local/bin/python3.13 scripts/ab_report.py \
        --no-markouts --date 2026-10-29 --output /tmp/phase1/report.json

`ab_report.py` writes the `--date` row into the extracted `daily.jsonl`, which is why it
runs against a copy. Phase 2's code carries phase-2 labels (`PHASE`, `started`); the
numbers it computes from these files are phase 1's.
