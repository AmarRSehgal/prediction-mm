# sports_soccer_ligue1

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **8** (8 with open markets)
- Open markets: **159** (99 contested)
- Total 24h volume: **$41,444**
- Total open interest: **254,136**
- Top-OI mean spread (median across series): **2.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **108**
- Median spread: **2.0c**
- Median TOB bid / ask size: **783 / 572** contracts
- Median depth within 5c of best bid / ask — **8402 / 11783** contracts
- Median depth within 10c of best bid / ask — **13299 / 11944** contracts
- Median depth within 5c of midpoint — bid: **7076** / ask: **11722** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **9**
- Mean informed-signal proxy: **-1.787** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.61c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 842 | 0.63 | -0.248 | 2.00 | 83.0 |
| 30d+ | 138 | 5.52 | -3.246 | 33.95 | 41.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLIGUE1GAME-26APR19PSGOL-PSG | PSG | 75c | 2.0c | 5000 | 5325 | 223596 | 61687 | 223596 | 62049 | 10076 | $7397 | 7-30d |
| KXLIGUE1GAME-26APR19ASMAUX-AUX | Auxerre | 16c | 2.0c | 28473 | 6300 | 236292 | 80599 | 246949 | 81541 | 7770 | $8024 | 7-30d |
| KXLIGUE1RELEGATION-26-AUX | Auxerre | 43c | 74.0c | 100 | 100 | 703 | 100 | 703 | 100 | 6752 | $0 | 30d+ |
| KXLIGUE1GAME-26APR19PSGOL-OL | Lyon | 10c | 1.0c | 250 | 5512 | 248644 | 124040 | 306302 | 165720 | 6366 | $5148 | 7-30d |
| KXLIGUE1TOP4-26-OM | Marseille | 63c | 60.0c | 5 | 79 | 5 | 179 | 5 | 1077 | 5512 | $31 | 7-30d |
| KXLIGUE1GAME-26APR19ASMAUX-ASM | Monaco | 64c | 1.0c | 40 | 41017 | 110710 | 186718 | 111710 | 187539 | 5121 | $4155 | 7-30d |
| KXLIGUE1GAME-26APR19RCSREN-REN | Stade Rennais | 40c | 1.0c | 25042 | 3500 | 104213 | 193144 | 104613 | 193364 | 3298 | $3458 | 7-30d |
| KXLIGUE1GAME-26APR19FCMPAR-PAR | Paris | 45c | 2.0c | 4650 | 10361 | 117298 | 93757 | 117458 | 95057 | 2723 | $1232 | 7-30d |
| KXLIGUE1GAME-26APR22PSGFCN-FCN | Nantes | 7c | 2.0c | 250 | 3949 | 58929 | 23615 | 58929 | 24177 | 2007 | $1992 | 7-30d |
| KXLIGUE1GAME-26APR19RCSREN-RCS | Strasbourg Alsace | 34c | 1.0c | 3793 | 23298 | 151072 | 169358 | 151592 | 169419 | 1988 | $1038 | 7-30d |
| KXLIGUE1SPREAD-26APR19PSGOL-PSG1 | PSG wins by over 1.5 goals | 54c | 1.0c | 400 | 6925 | 9179 | 19193 | 9479 | 59539 | 1950 | $1834 | 7-30d |
| KXLIGUE1GAME-26APR19FCNSTB-STB | Stade Brest | 30c | 2.0c | 10680 | 17436 | 140734 | 215863 | 140974 | 216364 | 1634 | $1037 | 7-30d |
| KXLIGUE1GAME-26APR19FCNSTB-FCN | Nantes | 40c | 1.0c | 3526 | 3950 | 161831 | 211751 | 162831 | 211931 | 1076 | $805 | 7-30d |
| KXLIGUE1GAME-26APR19FCMPAR-TIE | Tie | 27c | 2.0c | 13273 | 3928 | 140638 | 140176 | 142930 | 140576 | 969 | $952 | 7-30d |
| KXLIGUE1GAME-26APR19PSGOL-TIE | Tie | 15c | 1.0c | 5158 | 3500 | 391609 | 216575 | 394006 | 216975 | 642 | $627 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLIGUE1 | LIGUE 1 | annual | 18 | 0 | $1,343 | 181,534 | nanc |
| KXLIGUE1GAME | Ligue 1 Game | custom | 45 | 42 | $36,649 | 44,379 | 1.3c |
| KXLIGUE1TOP4 | Ligue 1 Top 4 Finishers | annual | 18 | 6 | $39 | 12,079 | 45.7c |
| KXLIGUE1RELEGATION | Ligue 1 Relegation | annual | 18 | 2 | $0 | 11,283 | 73.5c |
| KXLIGUE1SPREAD | Ligue 1 Spread | custom | 20 | 10 | $2,149 | 3,186 | 1.0c |
| KXLIGUE1TOTAL | Ligue 1 Total | custom | 20 | 19 | $1,217 | 1,420 | 1.3c |
| KXLIGUE1BTTS | Ligue 1 BTTS | custom | 5 | 5 | $47 | 252 | 2.0c |
| KXLIGUE11H | Ligue 1 First Half Winner | custom | 15 | 15 | $0 | 3 | 4.7c |

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
