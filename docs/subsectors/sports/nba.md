# sports_nba

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **38** (38 with open markets)
- Open markets: **1528** (710 contested)
- Total 24h volume: **$7,499,094**
- Total open interest: **66,234,935**
- Top-OI mean spread (median across series): **8.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **193**
- Median spread: **7.0c**
- Median TOB bid / ask size: **47 / 108** contracts
- Median cumulative depth within 5c of mid — bid: **79** / ask: **252** contracts
- Median cumulative depth within 10c of mid — bid: **600** / ask: **1110** contracts
- Mean trades per market (last 3000): **268**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 6162 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 46650 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNBA-26-SAS | San Antonio | 16c | 1.0c | 9512 | 1342 | 59861 | 236103 | 7075318 | $605244 | 30d+ |
| KXNBA-26-OKC | Oklahoma City | 48c | 1.0c | 133946 | 17141 | 298259 | 98695 | 5165205 | $621915 | 30d+ |
| KXNBA-26-DEN | Denver | 7c | 1.0c | 131572 | 179109 | 162090 | 706266 | 4293659 | $449796 | 30d+ |
| KXNBA-26-BOS | Boston | 14c | 1.0c | 3196 | 193577 | 164110 | 412315 | 4033450 | $263530 | 30d+ |
| KXNBAWEST-26-SAS | San Antonio | 21c | 2.0c | 2870 | 10 | 15026 | 9065 | 1466455 | $66873 | 30d+ |
| KXNBAEAST-26-BOS | Boston | 40c | 3.0c | 14493 | 320 | 34254 | 110634 | 1295034 | $140934 | 30d+ |
| KXNBAEAST-26-DET | Detroit | 19c | 1.0c | 25492 | 28317 | 70398 | 58372 | 959907 | $47282 | 30d+ |
| KXNBAEAST-26-NYK | New York | 15c | 1.0c | 15408 | 4354 | 20708 | 11079 | 957204 | $66353 | 30d+ |
| KXNBAEAST-26-CLE | Cleveland | 22c | 3.0c | 3258 | 26151 | 11844 | 37403 | 861323 | $70046 | 30d+ |
| KXNBAWEST-26-OKC | Oklahoma City | 64c | 2.0c | 697 | 112942 | 5633 | 125986 | 753349 | $92142 | 30d+ |
| KXNBAWEST-26-DEN | Denver | 13c | 2.0c | 5116 | 2794 | 14162 | 10994 | 588639 | $77971 | 30d+ |
| KXNBADRAFT1-26-ADYB | AJ Dybantsa | 67c | 2.0c | 224 | 388 | 349 | 1773 | 127397 | $55 | 30d+ |
| KXTEAMSINNBAF-26-OKCBOS | Oklahoma City vs Boston | 31c | 0.1c | 7653 | 1228 | 8560 | 15230 | 120156 | $23070 | 30d+ |
| KXNBADRAFT1-26-DPET | Darryn Peterson | 24c | 2.0c | 125 | 176 | 1186 | 1552 | 108493 | $152 | 30d+ |
| KXNBADRAFT1-26-CBOO | Cameron Boozer | 9c | 1.0c | 147 | 250 | 2489 | 2408 | 90511 | $224 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNBA | NBA Championship | annual | 16 | 3 | $5,737,668 | 51,693,747 | 1.0c |
| KXNBAEAST | NBA Eastern Conference Championship | annual | 8 | 4 | $612,656 | 6,720,663 | 1.7c |
| KXNBAWEST | NBA Western Conference Championship | annual | 8 | 3 | $463,650 | 5,617,626 | 1.3c |
| KXTEAMSINNBAF | Teams in NBA Finals | custom | 64 | 5 | $107,882 | 567,293 | 2.2c |
| KXNBADRAFT1 | NBA Draft First Pick | annual | 8 | 2 | $856 | 406,955 | 2.0c |
| KXNBASERIESSCORE | NBA Series Exact Score | custom | 61 | 34 | $198,310 | 364,220 | 7.7c |
| KXNBA1STTEAM | All-NBA 1st Team | annual | 17 | 2 | $10,264 | 246,056 | 2.5c |
| KXNBA1HTOTAL | NBA 1st Half Total Points | custom | 44 | 36 | $190,136 | 109,358 | 21.0c |
| KXNBA2NDTEAM | All-NBA 2nd Team | annual | 22 | 7 | $747 | 95,957 | 20.3c |
| KXNBASERIESSPREAD | NBA Series Game Spread | custom | 45 | 28 | $52,270 | 94,922 | 25.7c |

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
