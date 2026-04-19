# sports_soccer_ucl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **12** (12 with open markets)
- Open markets: **66** (47 contested)
- Total 24h volume: **$297,685**
- Total open interest: **4,848,690**
- Top-OI mean spread (median across series): **3.1 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **50**
- Median spread: **2.0c**
- Median TOB bid / ask size: **240 / 174** contracts
- Median cumulative depth within 5c of mid — bid: **1197** / ask: **1151** contracts
- Median cumulative depth within 10c of mid — bid: **2520** / ask: **2270** contracts
- Mean trades per market (last 3000): **802**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 8161 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 31961 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXUCL-26-BMU | Bayern Munich | 35c | 2.0c | 90835 | 330251 | 325362 | 420369 | 934198 | $37319 | 30d+ |
| KXUCL-26-ARS | Arsenal | 29c | 1.0c | 2734 | 161786 | 252434 | 410876 | 772647 | $29517 | 30d+ |
| KXUCL-26-PSG | PSG | 26c | 1.0c | 5522 | 19237 | 259097 | 284382 | 676780 | $24185 | 30d+ |
| KXUCL-26-ATM | Atletico | 12c | 1.0c | 4076 | 90945 | 93483 | 164162 | 651983 | $10733 | 30d+ |
| KXUSAIRANAGREEMENT-27-26MAY | Before May | 20c | 1.0c | 2252 | 0 | 4001 | 1549 | 396203 | $37607 | 7-30d |
| KXREACTOR-26DEC31 | By Dec 31, 2026 | 27c | 1.4c | 41 | 38 | 3917 | 4673 | 210235 | $2061 | 30d+ |
| KXUSAIRANAGREEMENT-27-26JUN | Before June | 43c | 1.0c | 1670 | 171 | 3476 | 1066 | 191386 | $18522 | 30d+ |
| KXUSAIRANAGREEMENT-27 | Before 2027 | 76c | 1.0c | 2283 | 1198 | 5083 | 4557 | 170635 | $14296 | 30d+ |
| KXUSAIRANAGREEMENT-27-26AUG | Before August | 62c | 1.0c | 50 | 2 | 5760 | 903 | 158676 | $13764 | 30d+ |
| KXUCLGAME-26APR29ATMARS-ATM | Atletico | 33c | 2.0c | 665 | 82 | 45539 | 177046 | 119700 | $12100 | 7-30d |
| KXUCLGAME-26APR28PSGBMU-PSG | PSG | 43c | 1.0c | 426 | 39113 | 47017 | 196251 | 106862 | $12177 | 7-30d |
| KXUCLGAME-26APR28PSGBMU-BMU | Bayern Munich | 34c | 2.0c | 364 | 34342 | 52248 | 168518 | 80310 | $23085 | 7-30d |
| KXCRITICALITY-26AUG-VALAR | Valar Atomics | 72c | 5.0c | 16 | 522 | 34 | 522 | 39021 | $17 | 30d+ |
| KXUSAIRANAGREEMENT-27-26JUL | Before July | 52c | 1.0c | 10 | 21 | 709 | 1029 | 32475 | $10435 | 30d+ |
| KXTEAMSINUCL-26-BMUATM | Bayern vs Atletico | 22c | 3.0c | 322 | 5 | 1470 | 12919 | 28722 | $6098 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUCL | UEFA Champions League | custom | 4 | 4 | $102,217 | 3,033,741 | 1.3c |
| KXUSAIRANAGREEMENT | US Iran nuclear deal | custom | 8 | 8 | $106,220 | 975,753 | 1.0c |
| KXUCLGAME | UEFA Champions League Game | custom | 9 | 9 | $61,139 | 334,829 | 2.0c |
| KXREACTOR | US grants license for new nuclear reacto | custom | 1 | 1 | $2,143 | 210,231 | 0.3c |
| KXTEAMSINUCL | Champions League Final Matchup | custom | 4 | 4 | $20,626 | 94,056 | 3.0c |
| KXCRITICALITY | Nuclear power criticality | custom | 10 | 7 | $1,195 | 81,457 | 6.0c |
| KXUCLFINALIST | UCL Advance to the Finals | annual | 4 | 4 | $2,256 | 77,460 | 1.3c |
| KXLEADERUCLGOALS | UCL Top Goalscorer | annual | 9 | 2 | $1,500 | 19,175 | 6.0c |
| KXFUSION | Nuclear fusion | custom | 3 | 3 | $133 | 16,683 | 3.2c |
| KXDATACENTER | Data center nuclear | custom | 1 | 1 | $27 | 3,544 | 5.0c |

## Curated notes

<!-- KEEP-START -->
<!-- Add market structure, resolution mechanics, time-of-day / TTE patterns, informed-flow analysis, verdict here -->

### Market structure
- Resolution mechanism:
- Frequency:
- Typical close time:

### Informed flow profile
- Retail vs pro:
- HFT presence:
- Known asymmetries:

### Time windows (UTC) / TTE behavior
- Safe:
- Quiet:
- Dangerous:
- Key events:
- TTE pattern: when does informed_signal_c spike?

### Verdict
- v0 target?
- Notes:
<!-- KEEP-END -->
