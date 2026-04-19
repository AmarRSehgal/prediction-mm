# sports_soccer_bundesliga

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **149** (95 contested)
- Total 24h volume: **$172,849**
- Total open interest: **389,823**
- Top-OI mean spread (median across series): **2.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **99**
- Median spread: **3.0c**
- Median TOB bid / ask size: **570 / 384** contracts
- Median cumulative depth within 5c of mid — bid: **11158** / ask: **11474** contracts
- Median cumulative depth within 10c of mid — bid: **12046** / ask: **12355** contracts
- Mean trades per market (last 3000): **18**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1336 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 433 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBUNDESLIGAGAME-26APR19BMUVFB-BMU | Bayern Munich | 70c | 1.0c | 3520 | 44424 | 252967 | 287457 | 189552 | $159345 | 7-30d |
| KXBUNDESLIGATOP4-26-LEV | Leverkusen | 19c | 28.0c | 34 | 100 | 0 | 0 | 16330 | $13 | 7-30d |
| KXBUNDESLIGASPREAD-26APR19BMUVFB-BMU1 | Bayern Munich wins by over 1.5 goals | 50c | 1.0c | 275 | 1812 | 13942 | 14108 | 7443 | $4271 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMUVFB-VFB | Stuttgart | 15c | 1.0c | 745 | 15675 | 298074 | 226869 | 2958 | $1194 | 7-30d |
| KXBUNDESLIGAGAME-26APR19SCFFCH-SCF | Freiburg | 58c | 1.0c | 3500 | 14768 | 272032 | 172356 | 2093 | $1491 | 7-30d |
| KXBUNDESLIGATOP4-26-TSG | Hoffenheim | 18c | 11.0c | 100 | 440 | 0 | 0 | 1996 | $21 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMGM05-TIE | Tie | 27c | 2.0c | 12129 | 6982 | 336010 | 251162 | 1895 | $1858 | 7-30d |
| KXBUNDESLIGATOP4-26-RBL | Leipzig | 61c | 74.0c | 100 | 2000 | 0 | 0 | 1505 | $10 | 7-30d |
| KXBUNDESLIGAGAME-26APR19SCFFCH-TIE | Tie | 22c | 1.0c | 5192 | 3514 | 424749 | 236755 | 1505 | $1970 | 7-30d |
| KXBUNDESLIGASPREAD-26APR19BMUVFB-BMU2 | Bayern Munich wins by over 2.5 goals | 30c | 1.0c | 887 | 2040 | 14609 | 14690 | 1327 | $321 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMUVFB-TIE | Tie | 16c | 2.0c | 30728 | 4691 | 331767 | 219346 | 1225 | $448 | 7-30d |
| KXBUNDESLIGA2GAME-26APR19SCHPMU-SCH | Schalke | 64c | 1.0c | 40 | 5543 | 1533 | 11489 | 920 | $736 | 7-30d |
| KXBUNDESLIGAGAME-26APR19BMGM05-M05 | Mainz | 32c | 2.0c | 4756 | 26878 | 275494 | 198176 | 801 | $458 | 7-30d |
| KXBUNDESLIGARELEGATION-26-STP | St. Pauli | 38c | 22.0c | 500 | 3 | 0 | 0 | 742 | $5 | 7-30d |
| KXBUNDESLIGA2GAME-26APR19EBSBSC-BSC | Hertha | 45c | 2.0c | 430 | 5355 | 11766 | 11826 | 700 | $659 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBUNDESLIGAGAME | Bundesliga Game | custom | 36 | 36 | $166,411 | 199,551 | 1.3c |
| KXBUNDESLIGA | BUNDESLIGA | annual | 18 | 0 | $1,007 | 143,416 | nanc |
| KXBUNDESLIGATOP4 | Bundesliga Top 4 Finishers | annual | 18 | 4 | $44 | 22,105 | 30.0c |
| KXBUNDESLIGARELEGATION | Bundesliga Relegation | annual | 18 | 3 | $23 | 13,954 | 40.7c |
| KXBUNDESLIGASPREAD | Bundesliga Spread | custom | 12 | 6 | $2,692 | 7,723 | 1.3c |
| KXBUNDESLIGA2GAME | Bundesliga 2 Game | custom | 9 | 9 | $1,830 | 1,906 | 1.7c |
| KXBUNDESLIGATOTAL | Bundesliga Total | one_off | 12 | 11 | $603 | 888 | 1.7c |
| KXBUNDESLIGA1H | Bundesliga First Half Winner | custom | 9 | 9 | $185 | 227 | 2.7c |
| KXBBLGAME | Bundesliga Basketball Game | custom | 14 | 14 | $53 | 52 | 7.7c |
| KXBUNDESLIGABTTS | Bundesliga BTTS | custom | 3 | 3 | $1 | 1 | 2.3c |

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
