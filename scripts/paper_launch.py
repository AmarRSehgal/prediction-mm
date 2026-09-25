#!/usr/bin/env python3
"""launchd entry point for one paper A/B arm, with a size-capped log.

    paper_launch.py baseline | crypto | niche

`baseline` runs v1 from the frozen worktree at tag paper-ab-baseline, through
runpy so not one line of it is changed; this file imports nothing from pmm so
the worktree's copy is the one that loads. v1 logs every order it places, which
is ~100MB a day, so the root logger gets a rotating handler first and v1's own
basicConfig() becomes a no-op. See guard_baseline_against_sleep for laptop sleep.
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

WOKE_EXIT = 75   # session.py restarts an arm that exits


def guard_baseline_against_sleep(state_path: Path):
    """Harness, not strategy: v1's code is untouched.

    v1 keeps its paper orders and its universe cache (timed on the monotonic clock,
    which stops while the lid is closed) across a sleep, so on wake it would match
    orders against every print made while asleep and flatten at hours-old mids --
    fills no running system could have had. So the first paper-venue or flatten
    call after a sleep saves the portfolio and exits, and session.py restarts v1
    clean: the same thing as the process having been killed at sleep and started
    on wake, which v1's own restart path already handles.
    """
    import os
    sys.path.insert(0, str(WORKTREE / "src"))
    from pmm.trader import executor, runner
    from pmm.trader.position import save_portfolio
    sys.path.insert(0, str(REPO / "src" / "pmm"))
    from sleepwatch import SleepWatch
    sys.path.pop(0)
    watch = SleepWatch()

    def wrap(cls, name, portfolio_of):
        original = getattr(cls, name)

        def guarded(self, *a, **kw):
            slept = watch.check()
            if slept:
                save_portfolio(portfolio_of(self), state_path)
                logging.getLogger("paper_launch").warning(
                    "woke after %.0fs asleep: saved state, restarting v1 clean", slept)
                logging.shutdown()
                os._exit(WOKE_EXIT)
            return original(self, *a, **kw)
        setattr(cls, name, guarded)

    for name in ("try_fill_against", "place_order", "cancel_all"):
        wrap(executor.PaperExecutor, name, lambda ex: ex.portfolio)
    wrap(runner.TraderRunner, "flatten_market", lambda r: r.portfolio)


if arm == "baseline":
    if not (WORKTREE / "scripts" / "run_trader.py").exists():
        sys.exit(f"baseline worktree missing: git worktree add --detach {WORKTREE} paper-ab-baseline")
    state = AB / "baseline" / "portfolio.json"
    guard_baseline_against_sleep(state)
    sys.argv = ["run_trader.py", "--state-path", str(state)]
    runpy.run_path(str(WORKTREE / "scripts" / "run_trader.py"), run_name="__main__")
else:
    sys.argv = ["run_v2.py", "--arm", arm]
    runpy.run_path(str(REPO / "scripts" / "run_v2.py"), run_name="__main__")
