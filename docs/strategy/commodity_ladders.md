# Commodity Strike Ladders — design note

**Status: not built. This is a design note, not a plan of record.**

README thesis point 5 (exploit correlation structure between related contracts)
is the largest unbuilt piece of the original design, and adjacent strikes on a
commodity ladder are its most tractable instance. This note records why, what
the previous attempt got wrong, and what the fee model now lets us say
quantitatively — so that whoever picks it up starts from the arithmetic rather
than from the thesis.

## Why this direction and not more of the same

Everything the bot does today is a bet that a two-sided quote earns more from
uninformed flow than it loses to informed flow. That is a bet about the
*counterparty*, and a sharper counterparty simply wins it. The live-book survey
in `scripts/sector_scan.py` is the reason to doubt we are the sharper one: in a
369-market sample of the current target universe, 55% of the markets carrying
any 24h volume had a 1c spread, and only 5% were 3c or wider. Where there is
flow the book is already made; where the book is wide there is no flow.

A no-arb bound between adjacent strikes is a different kind of edge. `P(X > 68)
>= P(X > 69)` is not a forecast — it is true at resolution regardless of who is
on the other side. A counterparty cannot be right about it. That is worth more
than a better volatility estimate.

## What killed commodities the first time

`comm_energy` lost $13.34 in a single session (2026-04-21) and the commodity
subsectors were cut from `TARGET_SUBSECTORS`. The cause was **the absence of
this feature, not a reason to avoid it**: the bot quoted each strike as an
independent market, so a trending underlying walked up the ladder and filled
the passive ask on every strike in sequence. Eight independent short deltas on
the same underlying is one large short delta, and nothing in `risk.py` counts
it that way — `per_subsector_frac` caps dollars in a subsector, not net delta
on an underlying.

So the ladder work has a prerequisite that is worth doing on its own merits:

**Per-underlying net delta accounting.** Positions must aggregate by
(underlying, expiry), not by ticker. Until they do, any ladder strategy has an
uncapped directional position hiding inside a set of individually capped ones.

## What the fee model now settles

`pmm.trader.fees` gives the arithmetic the earlier framing lacked. A ladder
arbitrage is two legs, and a violation you have to *take* costs a taker fee on
each (`ceil(0.07 * C * P * (1-P))`, rounded up per order):

| leg price | round-trip taker fee, both legs |
|---|---|
| 50c | 4.0c / contract (3.6c at size 10+) |
| 30c or 70c | 3.0c / contract |
| 20c or 80c | 2.4c / contract |

**A monotonicity violation smaller than ~3-4c per contract is not tradeable as
a taker.** That is a hard gate, and it should be the first thing measured: if
the observed violation distribution on Kalshi commodity ladders sits below it,
the taker version of this idea is dead before any code is written.

The maker version does not pay that. A passive round trip on a standard series
is free (0.03c/contract measured across 5,708 recorded passive fills). So the
economically live form of the idea is **not** arb-taking; it is *quoting the
ladder as one instrument*: fit a CDF across the strikes, quote each strike
against the fitted curve rather than against its own mid, and let the no-arb
bound be a constraint on the quote set instead of a signal to cross.

## Order of work, if it is picked up

1. **Measure the violation distribution.** For a month of commodity ladders,
   how often is `P(>K)` below `P(>K+1)`, by how much, for how long, and at what
   size? Compare against the 3-4c taker gate above. This is a research question
   answerable from `sector_scan_markets.parquet` plus an orderbook collection
   run; it needs no trading code and it can kill the idea cheaply.
2. **Per-underlying delta accounting** in `position.py` / `risk.py`. Required
   regardless, and it is what would have prevented the comm_energy loss.
3. **A ladder-aware quoter** that fits a monotone CDF to the strikes and derives
   each strike's reservation price from the fit. This subsumes the current
   per-market `compute_quote`; it should be a sibling, not a rewrite.
4. Only then, an arb-taker for violations that clear the fee gate.

Steps 1 and 2 are independently useful. Step 3 is the actual thesis. Do not
re-enable the commodity subsectors before step 2 lands — the last time they ran
without it they lost money in exactly the way this note describes.
