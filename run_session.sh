#!/bin/bash
set -u
# One paper A/B session a day: all three arms for SESSION_S (default 2h) while the
# Mac is awake, then score and publish. launchd fires this hourly; it no-ops once
# today's session is done, so the session lands in the first awake hour of the day.
# Mechanism and gotchas: ~/personal/automation/LAUNCHD.md

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${JOB_PYTHON:-/opt/local/bin/python3.13}"
SESSION_S="${SESSION_S:-7200}"
MARK="$PROJECT_DIR/logs/session_$(date +%F).done"
LOG="$PROJECT_DIR/logs/session.log"
mkdir -p "$PROJECT_DIR/logs"
[ -f "$MARK" ] && exit 0

{
    echo "=== $(date -u '+%Y-%m-%dT%H:%M:%SZ') session start (${SESSION_S}s) ==="
    PIDS=()
    for arm in baseline crypto niche; do
        env -u PYTHONPATH "$PY" "$PROJECT_DIR/scripts/paper_launch.py" "$arm" &
        PIDS+=($!)
    done
    trap 'kill -TERM "${PIDS[@]}" 2>/dev/null' TERM INT
    sleep "$SESSION_S"
    kill -TERM "${PIDS[@]}" 2>/dev/null
    # Shutdown waits out in-flight REST calls; give it a minute, then insist.
    for _ in $(seq 60); do kill -0 "${PIDS[@]}" 2>/dev/null || break; sleep 1; done
    kill -9 "${PIDS[@]}" 2>/dev/null
    wait 2>/dev/null
    echo "arms stopped"
    touch "$MARK"
    find "$PROJECT_DIR/logs" -name 'session_*.done' -mtime +14 -delete
    echo "=== $(date -u '+%Y-%m-%dT%H:%M:%SZ') session end ==="
} >> "$LOG" 2>&1

exec "$PROJECT_DIR/run_report.sh"
