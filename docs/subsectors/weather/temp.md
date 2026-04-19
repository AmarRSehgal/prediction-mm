# weather_temp

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **18** (18 with open markets)
- Open markets: **216** (54 contested)
- Total 24h volume: **$1,947,337**
- Total open interest: **1,687,420**
- Top-OI mean spread (median across series): **2.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **73**
- Median spread: **2.0c**
- Median TOB bid / ask size: **23 / 13** contracts
- Median depth within 5c of best bid / ask — **285 / 202** contracts
- Median depth within 10c of best bid / ask — **757 / 444** contracts
- Median depth within 5c of midpoint — bid: **196** / ask: **99** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **145**
- Mean informed-signal proxy: **-0.399** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.56c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 12-24h | 406 | 2.11 | -0.776 | 8.00 | 6.8 |
| 1-3d | 10536 | 1.60 | -0.364 | 7.00 | 14.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXHIGHNY-26APR19-T54 | 53° or below | 55c | 2.0c | 50 | 500 | 327 | 776 | 396 | 998 | 6405 | $7651 | 12-24h |
| KXHIGHMIA-26APR19-B87.5 | 87° to 88° | 55c | 2.0c | 18 | 21 | 282 | 476 | 847 | 1497 | 5359 | $6436 | 12-24h |
| KXHIGHTDC-26APR19-T65 | 64° or below | nanc | nanc | nan | nan | nan | nan | nan | nan | 4467 | $6245 | 12-24h |
| KXHIGHNY-26APR19-B54.5 | 54° to 55° | 36c | 4.0c | 110 | 18 | 524 | 161 | 534 | 788 | 4377 | $5021 | 12-24h |
| KXHIGHMIA-26APR19-B85.5 | 85° to 86° | 37c | 4.0c | 32 | 1 | 293 | 118 | 293 | 121 | 4321 | $6578 | 12-24h |
| KXHIGHAUS-26APR19-B75.5 | 75° to 76° | 18c | 5.0c | 106 | 1 | 146 | 1 | 529 | 449 | 3991 | $5209 | 1-3d |
| KXHIGHLAX-26APR19-B70.5 | 70° to 71° | 52c | 2.0c | 85 | 37 | 1508 | 726 | 1919 | 2088 | 3739 | $4237 | 1-3d |
| KXHIGHTOKC-26APR19-B74.5 | 74° to 75° | 30c | 11.0c | 7 | 7 | 80 | 181 | 128 | 305 | 3714 | $4633 | 1-3d |
| KXHIGHTOKC-26APR19-B72.5 | 72° to 73° | 44c | 7.0c | 288 | 8 | 288 | 286 | 437 | 508 | 3478 | $4452 | 1-3d |
| KXHIGHLAX-26APR19-B68.5 | 68° to 69° | 12c | 1.0c | 1 | 85 | 1647 | 388 | 6794 | 753 | 3226 | $4614 | 1-3d |
| KXHIGHLAX-26APR19-T68 | 67° or below | 6c | 2.0c | 26 | 70 | 4436 | 1007 | 4436 | 1217 | 2906 | $3336 | 1-3d |
| KXHIGHCHI-26APR19-T48 | 47° or below | 10c | 1.0c | 8 | 443 | 758 | 699 | 4270 | 714 | 2543 | $3295 | 1-3d |
| KXHIGHCHI-26APR19-B52.5 | 52° to 53° | 26c | 1.0c | 7 | 50 | 371 | 345 | 382 | 722 | 2393 | $3291 | 1-3d |
| KXHIGHLAX-26APR19-B72.5 | 72° to 73° | 24c | 1.0c | 13 | 206 | 357 | 746 | 757 | 1050 | 2284 | $2810 | 1-3d |
| KXHIGHMIA-26APR19-T88 | 89° or above | 11c | 4.0c | 2 | 53 | 350 | 473 | 3363 | 1284 | 2263 | $4295 | 12-24h |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXHIGHAUS | Highest temperature in Austin | daily | 12 | 2 | $448,862 | 442,934 | 1.0c |
| KXHIGHTDAL | Dallas Maximum Temperature | daily | 12 | 3 | $281,924 | 278,316 | 1.0c |
| KXHIGHNY | Highest temperature in NYC | daily | 12 | 3 | $232,194 | 180,528 | 1.3c |
| KXHIGHLAX | Highest temperature in Los Angeles | daily | 12 | 3 | $233,421 | 170,828 | 1.3c |
| KXHIGHCHI | Highest temperature in Chicago | daily | 12 | 4 | $82,866 | 92,886 | 1.0c |
| KXHIGHMIA | Highest temperature in Miami | daily | 12 | 3 | $91,181 | 78,489 | 2.3c |
| KXHIGHTOKC | Oklahoma City Maximum High Temperature | daily | 12 | 3 | $70,710 | 59,664 | 5.0c |
| KXHIGHTSATX | San Antonio Daily Maximum Temperature | daily | 12 | 3 | $54,381 | 50,701 | 3.3c |
| KXHIGHTATL | Atlanta Max Temperature | daily | 12 | 3 | $72,419 | 43,905 | 11.0c |
| KXHIGHTSFO | San Francisco High Temperature Daily | daily | 12 | 4 | $62,760 | 42,435 | 3.0c |

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
