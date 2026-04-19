# weather_temp

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **18** (18 with open markets)
- Open markets: **216** (55 contested)
- Total 24h volume: **$1,906,599**
- Total open interest: **1,600,292**
- Top-OI mean spread (median across series): **2.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **68**
- Median spread: **2.0c**
- Median TOB bid / ask size: **28 / 39** contracts
- Median cumulative depth within 5c of mid — bid: **243** / ask: **216** contracts
- Median cumulative depth within 10c of mid — bid: **588** / ask: **476** contracts
- Mean trades per market (last 3000): **119**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 8116 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXHIGHNY-26APR19-T54 | 53° or below | 44c | 1.0c | 21 | 1 | 180 | 134 | 5915 | $6933 | 1-3d |
| KXHIGHMIA-26APR19-B87.5 | 87° to 88° | 60c | 1.0c | 91 | 1 | 149 | 666 | 4855 | $5768 | 1-3d |
| KXHIGHMIA-26APR19-B85.5 | 85° to 86° | 31c | 1.0c | 33 | 1 | 220 | 59 | 3905 | $6271 | 1-3d |
| KXHIGHTOKC-26APR19-B74.5 | 74° to 75° | 29c | 8.0c | 210 | 211 | 210 | 215 | 3712 | $4418 | 1-3d |
| KXHIGHNY-26APR19-B54.5 | 54° to 55° | 37c | 2.0c | 98 | 1 | 366 | 1 | 3422 | $4037 | 1-3d |
| KXHIGHTOKC-26APR19-B72.5 | 72° to 73° | 44c | 4.0c | 41 | 41 | 242 | 241 | 3342 | $4286 | 1-3d |
| KXHIGHLAX-26APR19-B70.5 | 70° to 71° | 52c | 1.0c | 381 | 50 | 1973 | 258 | 3008 | $3492 | 1-3d |
| KXHIGHAUS-26APR19-B75.5 | 75° to 76° | 43c | 1.0c | 308 | 40 | 627 | 850 | 2930 | $3296 | 1-3d |
| KXHIGHCHI-26APR19-T48 | 47° or below | 12c | 1.0c | 116 | 52 | 564 | 1584 | 2549 | $3134 | 1-3d |
| KXHIGHLAX-26APR19-B68.5 | 68° to 69° | 12c | 1.0c | 23 | 300 | 561 | 398 | 2490 | $3876 | 1-3d |
| KXHIGHMIA-26APR19-T88 | 89° or above | 6c | 1.0c | 16 | 1 | 662 | 5 | 2145 | $3926 | 1-3d |
| KXHIGHLAX-26APR19-B72.5 | 72° to 73° | 24c | 2.0c | 3 | 227 | 581 | 280 | 2141 | $2594 | 1-3d |
| KXHIGHCHI-26APR19-B48.5 | 48° to 49° | 36c | 1.0c | 1248 | 2 | 1476 | 348 | 1862 | $2027 | 1-3d |
| KXHIGHNY-26APR19-B56.5 | 56° to 57° | 15c | 2.0c | 9 | 50 | 9 | 477 | 1802 | $2076 | 1-3d |
| KXHIGHTDC-26APR19-T65 | 64° or below | 64c | 3.0c | 308 | 4 | 308 | 139 | 1726 | $2335 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXHIGHAUS | Highest temperature in Austin | daily | 12 | 2 | $445,355 | 432,558 | 1.0c |
| KXHIGHTDAL | Dallas Maximum Temperature | daily | 12 | 3 | $280,342 | 269,144 | 3.3c |
| KXHIGHNY | Highest temperature in NYC | daily | 12 | 3 | $221,546 | 165,978 | 1.0c |
| KXHIGHLAX | Highest temperature in Los Angeles | daily | 12 | 3 | $215,822 | 152,103 | 1.7c |
| KXHIGHCHI | Highest temperature in Chicago | daily | 12 | 3 | $88,047 | 87,623 | 1.3c |
| KXHIGHMIA | Highest temperature in Miami | daily | 12 | 2 | $88,270 | 74,022 | 1.0c |
| KXHIGHTOKC | Oklahoma City Maximum High Temperature | daily | 12 | 3 | $70,691 | 57,464 | 3.7c |
| KXHIGHTSATX | San Antonio Daily Maximum Temperature | daily | 12 | 3 | $58,346 | 49,989 | 1.7c |
| KXHIGHTSFO | San Francisco High Temperature Daily | daily | 12 | 4 | $61,381 | 41,062 | 3.3c |
| KXHIGHTATL | Atlanta Max Temperature | daily | 12 | 2 | $65,548 | 37,019 | 4.0c |

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
