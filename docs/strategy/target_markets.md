# Target Markets

## Thesis

Edge scales inversely with informed-flow intensity. Target markets where:
- Volume is low enough that HFT MMers have not set up shop.
- Counterparties are mostly hobbyists / noise traders, not quants.
- There is no well-known public model that participants anchor to.
- Resolution mechanics are mechanical / unambiguous (reduces headline-risk adverse selection).

## Candidates, ranked by tractability for a small MM

### 1. Weather / climate (Kalshi)
Temperature, snowfall, hurricane counts, precipitation.
- Informed flow: narrow — a few meteorology-literate participants.
- Noise: high — hobbyists, retail.
- Resolution: mechanical (NOAA observations).
- Dangerous windows: GFS / ECMWF model runs (00z / 06z / 12z / 18z UTC), observation times.
- **Best v0 candidate.**

### 2. Economic data releases (Kalshi) — in the *quiet* periods only
CPI, NFP / jobs, GDP, Fed decisions, retail sales, PPI.
- Informed flow: spikes near release, near zero otherwise.
- Strategy: MM only in between-release quiet periods; pull entirely in the ~2h window around scheduled release and for several minutes after.
- Requires a reliable economic calendar.

### 3. Long-dated niche politics
Mid-term local races, non-US elections, cabinet appointments, specific legislation passage.
- Informed flow: thin (local political insiders).
- Noise: moderate — politically engaged retail.
- Avoid: headline US national races.

### 4. Entertainment / culture
Oscars, Emmys, box office, album chart positions, TV ratings.
- Informed flow: very low.
- Noise: vibes-based retail.
- Caution: some categories (box office opening weekends) have sharp scheduled releases — treat like economic data.

### 5. Science / tech milestones
"Will X release by Y", "Will SpaceX launch Z in Q1".
- Informed flow: moderate (tech Twitter is loud but not always informed).
- Noise: high.
- Caution: single-tweet events can jump prices hard.

## Categories to avoid in v0

- **Headline US political markets** (presidential, major Senate / House). Deeply informed flow. Public models everywhere.
- **Sports** (NFL, NBA, MLB). Professional models. Injury / lineup news causes constant jumps.
- **Markets with Metaculus or 538 public predictions**. Participants anchor to these; you are competing against a free consensus.
- **Crypto price-level markets** if the underlying has a liquid spot market. Arbers will eat your edge.

## Selection process for Phase 1 data collection

For each candidate, pull 1-2 weeks of orderbook + trade data and compute:
- Time-averaged spread (bps and absolute).
- Mean / median book depth at TOB.
- Trade frequency (trades per hour).
- Trade size distribution.
- Price impact per trade.
- Cancel-to-fill ratio at TOB.
- Quote-update rate.
- Informed-flow proxies:
  - % of trades that predict next-1h direction.
  - Large-trade follow-through (do 95th-percentile trades get continuation?).
  - Post-trade drift conditional on trade side.

Go / no-go rubric (draft, refine with data):
- Median spread > expected adverse-selection cost after fees.
- Trade frequency > threshold (need turnover; quoting a market with 2 trades/day is not MM).
- Informed flow proxies below threshold.
- No existing tight MMer quoting continuously (check quote-update patterns).
