# weather_temp

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration._

## Curated notes

<!-- KEEP-START -->

### Market structure
- Series: KXHIGHTDAL, KXHIGHTSATX, KXHIGHTSFO, HIGHCHI, KXTEMPNYCH (hourly), etc.
- Resolution: NOAA / official airport observations (LGA, JFK, LAX, SFO, DAL, ORD, etc.).
- Frequency: daily (max temp at city X for day Y) and hourly directional.
- Structure:
  - Daily strike ladder: "high above 70F", "high above 71F", ... binary per strike.
  - Range markets: "high between 70F-71F" as single contract.
- Close time: 06:00 UTC for daily (= ~midnight local US time).

### Informed flow profile
- **Retail + weather hobbyists + a few quant weather MMers (HFT-like).**
- **HFT presence: HIGH on active daily markets.** Spreads are 1-2c on Dallas / SATX /
  SFO contested strikes during most of the day.
- The weather-MM niche was filled years ago on Kalshi by quant firms who fit
  distributional models over forecast ensembles.
- Informed flow sources:
  - GFS / ECMWF model runs (00z/06z/12z/18z) - models revise, price moves.
  - Observations throughout the day (METAR hourly reports).

### Time windows (UTC)
- Contracts resolve at 06:00 UTC. The trading day evolves through:
- **SAFE** (early contract life): 12:00-15:00 UTC the day before. Full uncertainty on
  tomorrow's temp; but HFT MMers still tight.
- **QUIET**: 15:00-23:00 UTC the day before. Evening model runs provide information.
- **DANGEROUS**: the day of, as temp observations accumulate.
- **VERY DANGEROUS**: afternoon local time on the resolution day (max temp set).
- **Pull entirely**: last 4 hours before resolution. Markets converge to 0 or 1.

### Correlation / basket structure
- Strike ladder = monotone CDF — same structure as commodities.
- Adjacent cities: correlated (Dallas + SATX both hot when TX heat dome; LAX + SFO
  sometimes anticorrelated because of marine layer).
- Temp markets at the same city for different days are independent ex ante but update
  jointly when ECMWF releases.

### Verdict
- **v0 target: NO.**
- Why not:
  - Daily weather markets are HFT-saturated (1-2c spreads on contested strikes).
  - We have no edge vs established weather-MM quants.
- What would change this:
  - Weather markets on lesser-covered cities (Denver, Austin, Miami, Columbus, Boston)
    MIGHT have wider spreads. Sweep shows the major cities are tight; smaller ones need
    a closer look.
  - Hourly directional markets (KXTEMPNYCH, KXTEMPLAXH) may have different dynamics
    and could be re-evaluated.
  - Off-peak seasonal (snowfall monthly) may be less competitive.

<!-- KEEP-END -->
