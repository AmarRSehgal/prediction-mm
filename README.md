# prediction-mm

A Kalshi market-making bot built around an Avellaneda-Stoikov reservation
price, plus the research that picks which of Kalshi's ~13,700 series are worth
quoting at all.

## Status (2026-08-31)

**Paper only. Not profitable. Do not go live.**

Eight paper sessions ran 2026-04-19 through 2026-04-23. Every session but one
lost money, and the sessions were consistent enough that the losses are
structural rather than variance:

| session | start capital | fills | net PnL |
|---|---:|---:|---:|
| overnight (toy) | $100 | 10 | -$0.03 |
| sunday_day | $1,000 | 314 | -$8.10 |
| sunday_night | $10,000 | 315 | -$24.15 |
| monday_1c_test | $10,000 | 575 | **+$0.17** |
| monday_night_3c | $3,880 | 743 | -$12.26 |
| tuesday | $3,880 | 538 | -$22.48 |
| wed | $3,880 | 875 | -$33.21 |
| final (Apr 22-23) | $3,880 | 1,008 | -$30.80 |

Roughly **-$130 across ~4,400 paper fills**. Nothing has run since 2026-04-23.

### What the loss actually is

Breaking the final session's round trips down by the fill that *closed* them:

| closing fill | n | total | mean |
|---|---:|---:|---:|
| FORCE_CLOSE (rule C, 30-min timer) | 404 | -$25.21 | -6.2c |
| AGG_CLOSE (aggressive close) | 35 | -$7.49 | -21.4c |
| paper-flatten | 7 | -$0.32 | -4.6c |
| **passive (a quote actually got hit)** | **32** | **+$1.55** | **+4.8c** |

Passive round trips - the actual market-making business - were the only
profitable exit path, in this and both other sessions that ran that code. Every
other path crosses the spread. Both forced-exit mechanisms are now disabled by
default.

That leaves the real problem: only 32 of ~478 closes were passive. The quoter
has three defects that explain why (all pinned by `test_KNOWN_BUG_*` tests):

1. **`min_spread_cents` is not enforced on the posted quote.** The AS spread
   respects it and then the inside-the-TOB clip discards it. On a 3c book the
   bot posts a 1c spread - at most 1c of gross capture against multi-cent
   adverse selection.
2. **On a 1c book the clip inverts** and the bot joins both sides of the TOB
   for zero gross edge.
3. **Real inventory silences the quoter instead of skewing it.** The skewed
   reservation price gets clipped back until bid and ask land on the same cent
   and the quote is dropped - so a position can only be exited by crossing.
   This is what made the forced-exit mechanisms look necessary.

There is also **no fee model anywhere in the repo**. Kalshi's fee is material
relative to a 1-3c capture, so every PnL number above is optimistic.

## Layout

```
src/pmm/
  config.py                 env-driven config; key path, base URL, data dir
  kalshi/
    auth.py                 RSA-PSS request signing
    client.py               READ-ONLY REST client (no order methods, on purpose)
  analysis/
    taxonomy.py             ticker/title -> one of ~105 subsectors
    depth_metrics.py        book-shape stats
    metrics.py, ranking.py, time_of_day.py
  collector/snapshot.py     orderbook snapshot collection
  storage/parquet.py        parquet IO
  trader/
    runner.py               main loop: universe -> window -> quote -> risk -> execute
    quoter.py               AS reservation price + spread
    risk.py                 exposure / inventory caps, kill switch
    position.py             per-market inventory, realized/unrealized PnL
    executor.py             PaperExecutor (trade-match sim) + LiveExecutor
    universe.py             market discovery, price band, ticker blacklist
    schedule.py             game-window / TTE state machine
    subsector_tuning.py     per-subsector gamma, blackouts, gates
    events_calendar.py      known tournaments / earnings / macro releases
    config.py               target subsectors, risk limits, AS params
scripts/                    entry points (see below)
tests/                      unit tests (pytest)
docs/
  theory/                   MM fundamentals, orderbook reading, AS deep dive
  strategy/                 target markets, safe windows, correlation structure
  venues/                   Kalshi vs Polymarket vs Manifold
  subsectors/               auto-generated per-subsector stat sheets (~105)
  trader_guide.md           operational guide
```

## Running it

Use the real system python, not a work virtualenv:

```bash
cd ~/personal/prediction-mm
alias pmmpy='env -u PYTHONPATH /opt/local/bin/python3.13'

pmmpy scripts/test_auth.py              # read-only auth smoke test
pmmpy scripts/sector_scan.py            # full universe scan (~13.7k series, ~1h)
pmmpy scripts/fast_scan.py              # quicker series pull
pmmpy scripts/collect_snapshots.py      # orderbook snapshots
pmmpy scripts/run_trader.py --duration 3600   # PAPER, one hour
pmmpy scripts/status_tick.py            # one-shot status of the paper portfolio
pmmpy -m pytest tests/ -q               # unit tests
```

`scripts/pnl_tracker.py` is a daemon: it appends a row per minute forever and
never exits. Import `snapshot()` from it for a one-shot read instead.

### Live mode

`scripts/run_trader.py --live` places **real orders with real money**. It
requires the `--live` flag, a key with trade scope, and typing `GO` at a
prompt. `TraderConfig.dry_run` defaults to `True` and `LiveExecutor` is
unreachable without the flag.

Given the record above, live is not a sensible next step. Before it ever is:
the quoter defects need fixing, a fee model needs adding, and a session needs
to be positive on passive round trips alone.

Known live-mode bugs (paper mode is unaffected, but fix before live):
- `LiveExecutor.reconcile_fills` re-adds the same fill every cycle while an
  order is partially filled - there is no dedup on fill id.
- `TraderRunner.flatten_market` claims to cross the spread but prices off
  `mid +/- 2c` and ignores the `yes_bid`/`yes_ask` it is handed, so it can rest
  passively instead of flattening.
- The daily stop loss trips on realized PnL only and ignores mark-to-market.

## Thesis

1. **Target illiquid / inefficient markets** where informed flow is minimal.
   Avoid headline politics and anything with a public model.
2. **Be time-aware.** Every market has safe windows and dangerous ones
   (scheduled releases, live game play). Quote in the former, pull in the
   latter. This is `schedule.py` + `events_calendar.py` + per-subsector
   blackouts.
3. **Avoid extreme probabilities** (outside roughly [0.15, 0.85]): tick size
   dominates and resolution risk fat-tails.
4. **Derive risk parameters from data**, not theory defaults - hence
   `docs/subsectors/`.
5. **Exploit correlation structure** between related contracts (adjacent
   strikes, headline vs core, win vs vote-share). **Not built.** The bot treats
   every market as independent, which is exactly why commodities were dropped
   after a strike-ladder correlation loss. This is the largest unbuilt piece of
   the original thesis.

## Lessons paid for

- **1-of-N player props are not two-sided MM territory** (golf, 2026-04-19,
  -$8.45). ~30 players compete for N places; each "Top 20" binary looks
  independent and mean-reverting until the leaderboard settles and 70% go to
  1c while 30% go to 99c.
- **Correlated strike ladders on a trending underlying** lose the same way
  (comm_energy, -$13.34). Passive asks cannot chase a trend.
- **Simultaneous-resolve markets** (`KX*MENTION`) resolve every contract in the
  event at once; blacklisted by ticker pattern.
- **Forcing an exit to control hold time converts adverse selection into a
  guaranteed spread payment.** The cure was worse than the disease.

## Ground rules

- No API keys in the repo. Ever. `.gitignore` is strict; keys live in
  `~/.midpoint/.claude/prediction_mm_keys/`.
- Paper before live. Small before big.
- Never run with `--live` casually. The prompt exists for a reason.
