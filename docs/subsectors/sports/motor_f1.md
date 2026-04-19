# sports_motor_f1

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **52** (52 contested)
- Total 24h volume: **$5,792**
- Total open interest: **107,166**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **52**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 130** contracts
- Median depth within 5c of best bid / ask — **318 / 452** contracts
- Median depth within 10c of best bid / ask — **362 / 556** contracts
- Median depth within 5c of midpoint — bid: **300** / ask: **278** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **45**
- Mean informed-signal proxy: **-1.369** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.38c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 143 | 0.80 | -0.488 | 4.00 | 63.5 |
| 30d+ | 2203 | 1.59 | -0.793 | 7.00 | 51.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXF1RACE-MIAGP26-LEC | :: Ferrari | 6c | 1.0c | 1501 | 1393 | 65576 | 54272 | 65576 | 54272 | 20437 | $1458 | 7-30d |
| KXF1RACE-MIAGP26-NOR | :: McLaren | 5c | 4.0c | 8 | 11043 | 51508 | 35945 | 51508 | 43505 | 16224 | $68 | 7-30d |
| KXF1RACE-MIAGP26-PIA | :: McLaren | 8c | 1.0c | 3259 | 5869 | 32240 | 35427 | 41476 | 35427 | 15033 | $932 | 7-30d |
| KXF1RACE-MIAGP26-HAM | :: Ferrari | 6c | 1.0c | 14 | 8802 | 8829 | 48410 | 8829 | 48410 | 11254 | $127 | 7-30d |
| KXF1RACE-MIAGP26-ANT | :: Mercedes AMG Motorsport | 37c | 2.0c | 162 | 3652 | 1662 | 20499 | 1662 | 21499 | 8818 | $1362 | 7-30d |
| KXF1RACE-MIAGP26-RUS | :: Mercedes AMG Motorsport | 40c | 1.0c | 367 | 9371 | 8893 | 17517 | 8893 | 17567 | 6468 | $463 | 7-30d |
| KXF1CHINA-27 | Before 2027 | 9c | 4.0c | 5 | 156 | 1789 | 589 | 4512 | 1077 | 3056 | $5 | 30d+ |
| KXF1RACEPODIUM-MIAGP26-PIA | :: McLaren | 48c | 6.0c | 5 | 155 | 380 | 830 | 880 | 830 | 2593 | $26 | 7-30d |
| KXF1FASTLAP-MIAGP26-ANT | :: Mercedes AMG Motorsport | 30c | 9.0c | 56 | 195 | 68 | 945 | 368 | 945 | 2377 | $154 | 7-30d |
| KXF1RACEPODIUM-MIAGP26-LEC | :: Ferrari | 39c | 2.0c | 125 | 187 | 375 | 625 | 375 | 10954 | 1999 | $25 | 7-30d |
| KXF1RACEPODIUM-MIAGP26-VER | :: Red Bull Racing | 10c | 6.0c | 160 | 356 | 2410 | 731 | 4767 | 731 | 1871 | $262 | 7-30d |
| KXF1FASTLAP-MIAGP26-PIA | :: McLaren | 10c | 9.0c | 500 | 294 | 11002 | 1044 | 11002 | 1044 | 1810 | $0 | 7-30d |
| KXF1RACEPODIUM-MIAGP26-HAM | :: Ferrari | 25c | 6.0c | 284 | 196 | 709 | 571 | 709 | 571 | 1804 | $0 | 7-30d |
| KXF1FASTLAP-MIAGP26-NOR | :: McLaren | 8c | 7.0c | 500 | 409 | 12934 | 1159 | 12934 | 1159 | 1643 | $83 | 7-30d |
| KXF1RACEPODIUM-MIAGP26-NOR | :: McLaren | 32c | 4.0c | 70 | 291 | 445 | 541 | 445 | 541 | 1574 | $270 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXF1RACE | :: Ferrari | nan | 6 | 6 | $4,410 | 78,234 | 2.0c |
| KXF1RACEPODIUM | :: McLaren | nan | 7 | 7 | $857 | 11,748 | 4.7c |
| KXF1FASTLAP | :: Mercedes AMG Motorsport | nan | 5 | 5 | $237 | 7,964 | 8.3c |
| KXF1CHINA | Before 2027 | nan | 1 | 1 | $5 | 3,056 | 4.0c |
| KXF1TOP5 | :: Red Bull Racing | nan | 11 | 11 | $53 | 2,474 | 7.0c |
| KXF1TOP10 | :: Williams | nan | 18 | 18 | $13 | 2,365 | 7.0c |
| KXF1RETIRE | Before the 2027 season | nan | 4 | 4 | $218 | 1,324 | 4.7c |

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
