#!/usr/bin/env python3
"""launchd entry point for one paper A/B arm, with a size-capped log.

    paper_launch.py baseline | crypto | niche

`baseline` runs v1 from the frozen worktree at tag paper-ab-baseline, through
runpy so not one line of it is changed; this file imports nothing from pmm so
the worktree's copy is the one that loads. v1 logs every order it places, which
is ~100MB a day, so the root logger gets a rotating handler first and v1's own
basicConfig() becomes a no-op.
"""
import logging
import logging.handlers
import runpy
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORKTREE = REPO / ".worktrees" / "baseline"
AB = REPO / "research" / "data" / "ab"

arm = sys.argv[1] if len(sys.argv) > 1 else ""
if arm not in ("baseline", "crypto", "niche"):
    sys.exit("usage: paper_launch.py baseline|crypto|niche")

(REPO / "logs").mkdir(exist_ok=True)
h = logging.handlers.RotatingFileHandler(REPO / "logs" / f"paper_{arm}.log", maxBytes=20_000_000, backupCount=3)
h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s"))
logging.basicConfig(level=logging.INFO, handlers=[h])
for noisy in ("websockets", "urllib3"):
    logging.getLogger(noisy).setLevel(logging.WARNING)

if arm == "baseline":
    if not (WORKTREE / "scripts" / "run_trader.py").exists():
        sys.exit(f"baseline worktree missing: git worktree add --detach {WORKTREE} paper-ab-baseline")
    sys.argv = ["run_trader.py", "--state-path", str(AB / "baseline" / "portfolio.json")]
    runpy.run_path(str(WORKTREE / "scripts" / "run_trader.py"), run_name="__main__")
else:
    sys.argv = ["run_v2.py", "--arm", arm]
    runpy.run_path(str(REPO / "scripts" / "run_v2.py"), run_name="__main__")
