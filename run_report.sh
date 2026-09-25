#!/bin/bash
set -u
# Daily: score the paper A/B and publish it to the website.
# Mechanism and gotchas: ~/personal/automation/LAUNCHD.md

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${JOB_PYTHON:-/opt/local/bin/python3.13}"
SITE="${WEBSITE_DIR:-$HOME/personal/website}"
OUT="$PROJECT_DIR/web/kalshi_mm_paper.json"
LOG="$PROJECT_DIR/logs/report.log"
mkdir -p "$PROJECT_DIR/logs" "$PROJECT_DIR/web"

notify() { /usr/bin/osascript -e "display notification \"$1\" with title \"prediction-mm\"" 2>/dev/null; }

{
    echo "=== $(date -u '+%Y-%m-%dT%H:%M:%SZ') report start ==="
    if env -u PYTHONPATH "$PY" "$PROJECT_DIR/scripts/ab_report.py" --output "$OUT" \
        && env -u PYTHONPATH "$PY" "$SITE/.github/scripts/validate_predictions.py" kalshi_mm_paper "$OUT"; then
        cp "$OUT" "$SITE/predictions/kalshi_mm_paper.json"
        git -C "$SITE" add predictions/kalshi_mm_paper.json
        if git -C "$SITE" diff --cached --quiet -- predictions/kalshi_mm_paper.json; then
            echo "no change to publish"
        elif git -C "$SITE" commit -q -m "kalshi-mm paper A/B: $(date -u +%Y-%m-%d)" -- predictions/kalshi_mm_paper.json \
            && git -C "$SITE" push -q origin HEAD; then
            echo "published"
        else
            echo "publish FAILED"; notify "paper A/B publish failed - see logs/report.log"
        fi
    else
        echo "report FAILED"; notify "paper A/B report failed - see logs/report.log"
    fi
    # Silence is the failure a daemon has: say so if an arm stopped writing status.
    for arm in baseline v2_niche v2_crypto; do
        f="$PROJECT_DIR/research/data/ab/$arm/portfolio.json"
        [ "$arm" != baseline ] && f="$PROJECT_DIR/research/data/ab/$arm/status.json"
        if [ ! -f "$f" ] || [ $(( $(date +%s) - $(stat -f %m "$f") )) -gt 7200 ]; then
            echo "STALE: $arm has not written $f in 2h"; notify "paper arm $arm is not running"
        fi
    done
    echo "=== $(date -u '+%Y-%m-%dT%H:%M:%SZ') report end ==="
} >> "$LOG" 2>&1
exit 0
