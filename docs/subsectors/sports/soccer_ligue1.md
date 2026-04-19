# sports_soccer_ligue1

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **159** (101 contested)
- Total 24h volume: **$24,981**
- Total open interest: **237,558**
- Top-OI mean spread (median across series): **2.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **108**
- Median spread: **2.0c**
- Median TOB bid / ask size: **566 / 484** contracts
- Median cumulative depth within 5c of mid — bid: **3113** / ask: **3545** contracts
- Median cumulative depth within 10c of mid — bid: **4109** / ask: **8112** contracts
- Mean trades per market (last 3000): **8**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 695 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 138 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLIGUE1GAME-26APR19ASMAUX-AUX | Auxerre | 16c | 1.0c | 967 | 3506 | 219355 | 142171 | 7770 | $7834 | 7-30d |
| KXLIGUE1RELEGATION-26-AUX | Auxerre | 43c | 74.0c | 100 | 100 | 0 | 0 | 6752 | $0 | 30d+ |
| KXLIGUE1TOP4-26-OM | Marseille | 60c | 65.0c | 100 | 179 | 0 | 0 | 5512 | $31 | 7-30d |
| KXLIGUE1GAME-26APR19PSGOL-OL | Lyon | 9c | 1.0c | 4891 | 3506 | 380306 | 178748 | 5203 | $4125 | 7-30d |
| KXLIGUE1GAME-26APR19PSGOL-PSG | PSG | 74c | 1.0c | 4703 | 463 | 242010 | 257132 | 5077 | $2720 | 7-30d |
| KXLIGUE1GAME-26APR19RCSREN-REN | Stade Rennais | 40c | 1.0c | 19314 | 3500 | 209976 | 190274 | 3188 | $3305 | 7-30d |
| KXLIGUE1GAME-26APR19ASMAUX-ASM | Monaco | 64c | 1.0c | 40 | 5131 | 55813 | 224372 | 2500 | $1664 | 7-30d |
| KXLIGUE1GAME-26APR19FCMPAR-PAR | Paris | 45c | 2.0c | 5948 | 6518 | 157386 | 49807 | 2200 | $1113 | 7-30d |
| KXLIGUE1GAME-26APR22PSGFCN-FCN | Nantes | 7c | 2.0c | 250 | 3949 | 44195 | 22235 | 2007 | $1992 | 7-30d |
| KXLIGUE1SPREAD-26APR19PSGOL-PSG1 | PSG wins by over 1.5 goals | 52c | 1.0c | 565 | 456 | 2687 | 9123 | 1759 | $1651 | 7-30d |
| KXLIGUE1GAME-26APR19RCSREN-RCS | Strasbourg Alsace | 34c | 1.0c | 293 | 10664 | 148826 | 177828 | 1719 | $924 | 7-30d |
| KXLIGUE1GAME-26APR19FCNSTB-STB | Stade Brest | 31c | 1.0c | 3500 | 452 | 165077 | 194989 | 1187 | $590 | 7-30d |
| KXLIGUE1GAME-26APR19FCMPAR-TIE | Tie | 27c | 2.0c | 14132 | 4275 | 230566 | 234793 | 936 | $919 | 7-30d |
| KXLIGUE1GAME-26APR19PSGOL-TIE | Tie | 16c | 1.0c | 454 | 5500 | 396907 | 213393 | 622 | $607 | 7-30d |
| KXLIGUE1GAME-26APR22PSGFCN-PSG | PSG | 82c | 1.0c | 554 | 1470 | 5187 | 22503 | 546 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLIGUE1 | LIGUE 1 | annual | 18 | 0 | $1,381 | 181,512 | nanc |
| KXLIGUE1GAME | Ligue 1 Game | custom | 45 | 43 | $22,863 | 30,172 | 1.3c |
| KXLIGUE1TOP4 | Ligue 1 Top 4 Finishers | annual | 18 | 6 | $39 | 12,079 | 41.7c |
| KXLIGUE1RELEGATION | Ligue 1 Relegation | annual | 18 | 2 | $3 | 11,283 | 66.0c |
| KXLIGUE1SPREAD | Ligue 1 Spread | custom | 20 | 10 | $207 | 1,713 | 2.3c |
| KXLIGUE1TOTAL | Ligue 1 Total | custom | 20 | 20 | $484 | 789 | 2.0c |
| KXLIGUE1BTTS | Ligue 1 BTTS | custom | 5 | 5 | $0 | 8 | 2.0c |
| KXLIGUE11H | Ligue 1 First Half Winner | custom | 15 | 15 | $3 | 3 | 6.7c |

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
