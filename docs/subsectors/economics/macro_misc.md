# eco_macro_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **27** (27 with open markets)
- Open markets: **723** (285 contested)
- Total 24h volume: **$27,850**
- Total open interest: **1,169,880**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **364 / 346** contracts
- Median depth within 10c of best bid / ask — **772 / 370** contracts
- Median depth within 5c of midpoint — bid: **260** / ask: **260** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **95**
- Mean informed-signal proxy: **-1.166** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.69c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 28 | 6.18 | -3.182 | 29.05 | 91.8 |
| 3-7d | 155 | 2.68 | -1.176 | 11.95 | 39.1 |
| 7-30d | 4035 | 1.22 | -0.383 | 5.00 | 46.0 |
| 30d+ | 14770 | 3.10 | -0.772 | 12.30 | 166.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCAWEALTHTAX-26 | In 2026 | 36c | 5.0c | 12 | 26 | 1523 | 1317 | 1640 | 1428 | 122855 | $501 | 30d+ |
| KXLCPIMAXYOY-27-P4.5 | At least 4.5% | 32c | 10.0c | 10 | 9 | 365 | 1332 | 365 | 2490 | 40760 | $560 | 30d+ |
| KXLCPIMAXYOY-27-P4 | At least 4% | 50c | 6.0c | 33 | 34 | 636 | 1367 | 712 | 1367 | 39019 | $1172 | 30d+ |
| KXLCPIMAXYOY-27-P3.5 | At least 3.5% | 95c | 2.4c | 333 | 333 | 4985 | 2478 | 6600 | 2478 | 34760 | $0 | 30d+ |
| KXECONSTATCPICORE-26MAY-T-0.2 | Exactly -0.2% | 11c | 5.0c | 20 | 14 | 1525 | 308 | 9174 | 328 | 30368 | $0 | 30d+ |
| KXCPIYOY-26APR-T3.7 | 3.7 | 24c | 1.0c | 107 | 1000 | 212 | 1000 | 7412 | 1119 | 26575 | $195 | 7-30d |
| KXECONSTATCPIYOY-26MAY-T3.3 | Exactly 3.3% | 15c | 3.0c | 222 | 200 | 5222 | 339 | 5675 | 339 | 24425 | $149 | 30d+ |
| KXMUSKWEALTH-27-900 | More than $900 Billion | 84c | 2.0c | 522 | 509 | 641 | 559 | 960 | 760 | 23759 | $619 | 30d+ |
| KXLCPIMAXYOY-27-P5 | At least 5% | 21c | 2.8c | 17 | 13 | 350 | 1684 | 914 | 1684 | 23576 | $1600 | 30d+ |
| KXCPIYOY-26APR-T3.6 | 3.6 | 37c | 2.0c | 1000 | 5 | 2000 | 4632 | 2000 | 4632 | 20931 | $442 | 7-30d |
| KXMUSKWEALTH-27-1000 | More than $1 trillion | 80c | 2.0c | 526 | 511 | 526 | 511 | 526 | 511 | 15687 | $47 | 30d+ |
| KXCPIYOY-26APR-T3.5 | 3.5 | 70c | 2.0c | 1335 | 4479 | 2602 | 4479 | 2702 | 4479 | 10974 | $156 | 7-30d |
| KXUSFUND-27 | Before 2027 | 24c | 3.0c | 295 | 1185 | 1296 | 1409 | 2394 | 1559 | 10783 | $0 | 30d+ |
| KXCPIYOY-26APR-T3.8 | 3.8 | 11c | 5.0c | 47 | 17 | 2397 | 1017 | 2551 | 1047 | 10560 | $191 | 7-30d |
| KXMUSKWEALTH-27-1200 | More than  $1.2 trillion | 49c | 2.0c | 509 | 522 | 509 | 1034 | 509 | 1034 | 9156 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXECONSTATCPIYOY | year over year inflation | custom | 134 | 29 | $3,853 | 410,276 | 2.3c |
| KXLCPIMAXYOY | Inflation surge this year | one_off | 7 | 3 | $3,432 | 150,920 | 6.9c |
| KXCPIYOY | Inflation | monthly | 56 | 24 | $2,320 | 142,024 | 1.7c |
| KXCAWEALTHTAX | Will the California billionaire wealth t | one_off | 1 | 1 | $501 | 122,855 | 5.0c |
| KXMUSKWEALTH | Musk wealth | custom | 6 | 6 | $684 | 67,605 | 2.0c |
| KXECONSTATCPICORE | month over month core inflation | custom | 69 | 27 | $0 | 51,352 | 4.3c |
| KXJPMOMINF | Japan inflation MoM in [month] | monthly | 9 | 5 | $25 | 35,397 | 46.0c |
| KXECONSTATCPI | month over month inflation | custom | 76 | 35 | $2,581 | 32,083 | 4.3c |
| KXCPICOREYOY | Core inflation | monthly | 30 | 9 | $864 | 24,581 | 5.0c |
| KXPCECORE | US Core PCE inflation | monthly | 45 | 25 | $2,945 | 22,115 | 8.3c |

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
