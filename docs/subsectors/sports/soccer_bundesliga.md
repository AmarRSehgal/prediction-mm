# sports_soccer_bundesliga

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **149** (94 contested)
- Total 24h volume: **$190,179**
- Total open interest: **410,334**
- Top-OI mean spread (median across series): **1.7 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **99**
- Median spread: **3.0c**
- Median TOB bid / ask size: **656 / 298** contracts
- Median depth within 5c of best bid / ask — **11838 / 11529** contracts
- Median depth within 10c of best bid / ask — **13004 / 12164** contracts
- Median depth within 5c of midpoint — bid: **11223** / ask: **10890** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **20**
- Mean informed-signal proxy: **-0.911** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1586 | 0.47 | -0.225 | 2.00 | 175.2 |
| 30d+ | 433 | 3.77 | -1.207 | 16.00 | 56.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBUNDESLIGAGAME-26APR19BMUVFB-BMU | Bayern Munich | 70c | 1.0c | 324 | 71243 | 203527 | 267797 | 208523 | 268040 | 198724 | $166582 | 7-30d |
| KXBUNDESLIGATOP4-26-LEV | Leverkusen | 22c | 35.0c | 4 | 24 | 1452 | 24 | 1452 | 744 | 16330 | $13 | 7-30d |
| KXBUNDESLIGASPREAD-26APR19BMUVFB-BMU1 | Bayern Munich wins by over 1.5 goals | 50c | 1.0c | 1266 | 11449 | 20543 | 24375 | 26223 | 24875 | 8610 | $5293 | 7-30d |
| KXBUNDESLIGAGAME-26APR19SCFFCH-SCF | Freiburg | 57c | 1.0c | 16892 | 3500 | 245869 | 252580 | 246369 | 253642 | 3687 | $3043 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMUVFB-VFB | Stuttgart | 15c | 1.0c | 745 | 15161 | 271917 | 246517 | 282329 | 247417 | 3124 | $1441 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMGM05-TIE | Tie | 27c | 2.0c | 8875 | 26962 | 371464 | 251622 | 371964 | 251682 | 2228 | $2205 | 7-30d |
| KXBUNDESLIGA2GAME-26APR19SCHPMU-SCH | Schalke | 64c | 1.0c | 40 | 4552 | 1827 | 10998 | 12327 | 10998 | 2218 | $1814 | 7-30d |
| KXBUNDESLIGATOP4-26-TSG | Hoffenheim | 17c | 10.0c | 100 | 116 | 100 | 417 | 350 | 417 | 1996 | $21 | 7-30d |
| KXBUNDESLIGATOTAL-26APR19BMUVFB-3 | Over 3.5 goals scored | 60c | 1.0c | 275 | 12563 | 16116 | 19538 | 22116 | 19718 | 1626 | $1891 | 7-30d |
| KXBUNDESLIGAGAME-26APR19SCFFCH-TIE | Tie | 22c | 1.0c | 4957 | 3672 | 413490 | 242367 | 415750 | 244370 | 1580 | $2045 | 7-30d |
| KXBUNDESLIGATOP4-26-RBL | Leipzig | 61c | 76.0c | 1 | 678 | 1 | 678 | 1 | 678 | 1505 | $10 | 7-30d |
| KXBUNDESLIGASPREAD-26APR19BMUVFB-BMU2 | Bayern Munich wins by over 2.5 goals | 30c | 2.0c | 1297 | 19477 | 33033 | 31377 | 33193 | 31777 | 1486 | $424 | 7-30d |
| KXBUNDESLIGA2GAME-26APR19EBSBSC-BSC | Hertha | 44c | 1.0c | 1 | 600 | 6437 | 10856 | 11937 | 11756 | 1447 | $1353 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMUVFB-TIE | Tie | 17c | 1.0c | 675 | 4654 | 319568 | 236557 | 324043 | 237557 | 1328 | $524 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMGM05-M05 | Mainz | 31c | 1.0c | 3532 | 21380 | 156288 | 211766 | 156288 | 211766 | 1247 | $875 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBUNDESLIGAGAME | Bundesliga Game | custom | 36 | 36 | $177,053 | 211,580 | 1.0c |
| KXBUNDESLIGA | BUNDESLIGA | annual | 18 | 0 | $1,007 | 143,416 | nanc |
| KXBUNDESLIGATOP4 | Bundesliga Top 4 Finishers | annual | 18 | 4 | $44 | 22,105 | 37.3c |
| KXBUNDESLIGARELEGATION | Bundesliga Relegation | annual | 18 | 2 | $21 | 13,954 | 47.0c |
| KXBUNDESLIGASPREAD | Bundesliga Spread | custom | 12 | 6 | $5,649 | 11,048 | 1.0c |
| KXBUNDESLIGA2GAME | Bundesliga 2 Game | custom | 9 | 9 | $2,865 | 4,340 | 1.3c |
| KXBUNDESLIGATOTAL | Bundesliga Total | one_off | 12 | 11 | $2,937 | 3,252 | 1.3c |
| KXBUNDESLIGABTTS | Bundesliga BTTS | custom | 3 | 3 | $316 | 316 | 1.7c |
| KXBUNDESLIGA1H | Bundesliga First Half Winner | custom | 9 | 9 | $204 | 255 | 2.3c |
| KXBBLGAME | Bundesliga Basketball Game | custom | 14 | 14 | $84 | 68 | 5.3c |

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
