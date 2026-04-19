# Candidate Shortlist (2026-04-18)

First-pass filter after one live sweep of the Kalshi REST API (read-only key).
This is the "what to track first" list. Revise after collecting ~1 week of snapshots.

## Top-level finding

**Daily weather strike ladders (Dallas / SATX / SFO) are already competitively
market-made.** Median spread on contested strikes is **1 cent** (the minimum tick).
Volumes are high (hundreds of K $ / day). HFT MMers are there; a naive
small-MM entry has no edge.

**Commodity daily strike ladders (Brent / Gold / Silver / Copper) are genuinely
under-quoted.** Median spread on contested strikes is **20-35 cents**, moderate
OI (hundreds of contracts), moderate volume (hundreds of $ / day). Wide spreads
give real room for MM edge, at the cost of:
- Underlying-arb risk (CL/GC/SI/HG futures are liquid elsewhere).
- Scheduled news windows (EIA oil inventory, Fed days for gold).

**S&P 500 range (KXINX)** has 60 markets listed but only ~4-7 two-sided. Where
it is quoted, spreads are 1c (HFT again). Skip for v0.

**Deep-illiquid economic monthly markets (PPI, Challenger)** have enormous
spreads (60c+) but near-zero volume — you could *provide* liquidity but the
question is whether anyone trades against you. Possible v0 niche at tiny size.

## Primary watchlist (v0)

Commodity daily strike ladders — top 6 contested strikes per series, refreshed
daily (close time = 21:00 UTC).

| Series     | Series title       | Example contested strikes       | Median spread |
|------------|--------------------|--------------------------------|---------------|
| KXBRENTD   | Brent oil daily    | $88 / 93 / 95 / 95.50 / 99     | 20 cents      |
| KXGOLDD    | Gold daily         | $4604 / 4614 / 4774 / 4844     | 31 cents      |
| KXSILVERD  | Silver daily       | $77.75 / 79 / 80 / 81.25       | 35 cents      |
| KXCOPPERD  | Copper daily       | $5.98 / 6.00 / 6.04 / 6.08     | 33 cents      |

Full strike ladders are written to `research/data/watchlist.parquet`.
Watchlist txt file: `research/data/watchlist.txt`.

## Secondary watchlist (for comparison / control)

- **Weather daily** (3 tickers per series across Dallas/SATX/SFO): to measure
  HFT-saturated baseline against commodity wide-spread case.
- **PPI YoY** (3 tickers): illiquid monthly; quote only in non-release weeks
  at tiny size.
- **Challenger job cuts** (3 tickers): same profile as PPI.

## Time ranges to target (UTC)

For commodity daily contracts resolving at 21:00 UTC:

| Window        | UTC hours | Classification | Why |
|---------------|-----------|----------------|-----|
| Asian session | 00:00-11:00 | **SAFE**       | US/EU commodity futures quiet; retail light |
| EU pre-open   | 11:00-13:00 | QUIET          | Brent ICE volume picks up |
| US cash open  | 13:30-14:30 | DANGEROUS      | NYSE open + equity cross-flow into commodities |
| EIA inv.      | Wed 14:30   | **VERY DANGEROUS** | Weekly crude inventory report; major jump risk for oil |
| Mid-US        | 14:30-18:00 | QUIET / SAFE   | Post-open drift; safe unless macro headline |
| Fed (when on) | 18:00-19:30 | **VERY DANGEROUS** | FOMC statement + Powell presser; kills gold especially |
| Close hour    | 20:00-21:00 | DANGEROUS      | Convergence to settlement; informed flow peaks |

For **weather daily** contracts resolving at 06:00 UTC (midnight local US):

| Window | Classification | Why |
|--------|----------------|-----|
| Contract open (early morning local) | SAFE | Full uncertainty, prior to any obs |
| Mid-morning local | QUIET | Temperature trajectory starting to become clear |
| Afternoon local | DANGEROUS | Max temp typically set or near-set |
| Evening local | VERY DANGEROUS | Max temp known; market converges to 0 or 1 |

Don't quote weather in the last 4 hours of contract life.

## Known dangerous calendar events (coming weeks)

- **CPI release**: monthly, 8:30 ET, Wed 2026-05-13 (next one).
- **NFP / jobs**: monthly, 8:30 ET, Fri 2026-05-01 (first Fri of May).
- **FOMC**: next 2026-05-06.
- **EIA crude inventory**: weekly, Wed 10:30 ET (= 14:30 UTC).
- **OPEC meetings**: announced ad hoc; next regular 2026-06-01.
- **Challenger job cuts release**: first Thu each month, 7:30 ET.
- **PPI release**: monthly, ~8:30 ET.

Maintain this in code as a static JSON; override with RSS/calendar API later.

## Go / no-go gate before writing any quoting logic

Collect 1 week of 10-second snapshots + trade tape on the primary watchlist.
Measure per ticker:

1. **Time-weighted mean spread**. Must be > 8 cents on median to justify MM.
2. **Fill rate proxy** (trade count vs quote presence): we need at least several
   trades per hour in our target window.
3. **Post-trade drift** (1m / 5m): if the market systematically moves against
   fills (adverse selection), subtract that from gross spread to get net edge.
4. **Depth behind TOB**: wall at 0.99 or 0.01 is the MM-of-last-resort
   pattern; we ignore it for quoting but note it for unwind cost.
5. **Book imbalance predictive power**: does BI at TOB predict next-minute
   price? If yes, build into quoting; if no, ignore.

Ship the collector, let it run a week, analyze, decide.
