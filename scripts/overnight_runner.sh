#!/usr/bin/env bash
# Auto-restart wrapper. Runs paper trader in a loop; if it dies, restart up
# to 5 times. Exit cleanly after a total of --total-hours.

set -u
cd "$(dirname "$0")/.."

TOTAL_HOURS="${1:-10}"
MAX_RESTARTS="${2:-5}"
DEADLINE=$(( $(date +%s) + TOTAL_HOURS * 3600 ))

restarts=0
while (( $(date +%s) < DEADLINE )); do
  remaining=$(( DEADLINE - $(date +%s) ))
  echo "[$(date -u +%FT%TZ)] starting trader, remaining=${remaining}s, restart=${restarts}/${MAX_RESTARTS}"
  .venv/bin/python scripts/run_trader.py --duration "${remaining}" >> logs/overnight_trader.log 2>&1
  rc=$?
  echo "[$(date -u +%FT%TZ)] trader exited rc=${rc}"
  # Always restart until deadline; clean-exit is still a restart trigger.
  restarts=$(( restarts + 1 ))
  if (( restarts > MAX_RESTARTS )); then
    echo "[$(date -u +%FT%TZ)] giving up after ${MAX_RESTARTS} restarts"
    break
  fi
  sleep 10
done
echo "[$(date -u +%FT%TZ)] overnight wrapper done"
