# Safe vs Dangerous Time Windows

## Core idea

Every prediction market has time periods when material information is unlikely to arrive (**safe windows**) and time periods when it is likely (**dangerous windows**). Quoting naively through dangerous windows is a direct donation to informed flow.

The strategy is:
1. Build a per-market **event calendar** of known / probable information releases.
2. Classify every hour of the week as safe, quiet, or dangerous.
3. Quote only in safe windows. Widen in quiet. Pull entirely in dangerous.
4. Continuously validate the classification against realized post-window price moves and trade toxicity.

## Dangerous window taxonomy

### Scheduled, known-time
- **Economic data releases**: CPI, PPI, NFP, GDP, retail sales, FOMC statements, Fed minutes, Powell pressers. All have exact release times (typically 8:30 ET, 10:00 ET, 14:00 ET for Fed).
- **Weather model runs**: GFS at 00z / 06z / 12z / 18z; ECMWF at 00z / 12z. Observation releases (METAR, hourly).
- **Earnings / corporate announcements** (if relevant).
- **Sports**: game start, halftime, quarters, post-game.
- **Entertainment releases**: Oscar nominations / ceremony time, box office reporting (Monday / Sunday), ratings releases.

### Scheduled, loose-time
- **Debates** (date known, within a 2-3h window).
- **Speeches** (date known, time announced day-of).
- **Polling releases** (often Sunday evenings for weekend polls).
- **Regulatory decisions** (day known, sometimes not exact time).

### Unscheduled
- Breaking news, tweets, wire reports.
- Impossible to predict, but *frequency* is estimable per market. Markets with high unscheduled news rate (politics, crypto) should carry a permanent spread widening.

## Safe window patterns by market type

### Weather (Kalshi)
- **Safe**: mid-afternoon UTC (between model runs), overnight local time for the target city.
- **Dangerous**: the hour after each model run (00z, 06z, 12z, 18z), and the hours approaching resolution.
- **Very dangerous**: if resolution is "high temp today at LGA", the morning observation period is dangerous.

### Economic data
- **Safe**: any day with no scheduled release for the relevant series. Midweek afternoons.
- **Dangerous**: the 2h window surrounding release, plus 15-60min after (revision noise, repositioning).
- **Very dangerous**: Fed days — widen or pull for the full day.

### Entertainment
- **Safe**: most of the contract's lifetime.
- **Dangerous**: the actual event (ceremony, release weekend). Often the final few hours before resolution.
- **Quiet but suspicious**: announcement days (nomination announcements, trailer drops).

### Niche politics
- **Safe**: non-campaign periods, non-debate weeks.
- **Dangerous**: debate nights, primary / election days, endorsement news cycles.

## Operationalization

Three pieces needed:

1. **Event calendar data source.** Economic data: Trading Economics API, or scrape BLS / BEA schedules. Weather: NOAA model-run schedule is fixed. Entertainment: manually curated. Political: manual + news API.

2. **Window state machine** per market. States:
   - `SAFE`: quote normally with AS parameters.
   - `QUIET`: widen spread, reduce size, maintain quoting.
   - `DANGEROUS`: pull all quotes; optionally maintain far-out "safety" quotes at [0.01, 0.99] for protection.
   - `POST_EVENT_COOLDOWN`: quotes pulled for N minutes after release while new equilibrium forms. Return to `SAFE` only after realized vol returns to baseline.

3. **Continuous validation.** For every window:
   - Measure post-window price change vs pre-window.
   - Measure trade toxicity (did takers during this window predict the post-window direction?).
   - Upgrade / downgrade window classifications as data accumulates.

## Proxies to measure window danger from data alone

If event calendars are incomplete, can detect windows empirically:
- **Realized vol by time-of-day / day-of-week** (per market). Histogram of 1-min realized vol; find hours with elevated baseline.
- **Trade intensity** (trades per minute, histogram by hour).
- **Quote update frequency** (is the rest of the market revising quotes rapidly during this hour?).
- **Post-trade price drift** (does a trade in this window predict direction more strongly than average?).

Markets with high values on these proxies should have that time-of-day permanently classified as quiet or dangerous, even without a known event cause.

## Phase 1 deliverable

Per candidate market category, produce a heatmap: hour-of-week vs realized-vol and trade-toxicity. This directly feeds the window state machine in Phase 3.
