# sports_basketball_cba

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **20** (18 contested)
- Total 24h volume: **$7,900**
- Total open interest: **8,307**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **20**
- Median spread: **4.0c**
- Median TOB bid / ask size: **50 / 116** contracts
- Median cumulative depth within 5c of mid — bid: **75** / ask: **242** contracts
- Median cumulative depth within 10c of mid — bid: **938** / ask: **532** contracts
- Mean trades per market (last 3000): **14**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 289 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCBAGAME-26APR190735BRFZHE-ZHE | Zhejiang Lions | 78c | 3.0c | 1361 | 2411 | 3832 | 5589 | 4199 | $4161 | 7-30d |
| KXCBAGAME-26APR200735SBWJIA-SBW | Sichuan Blue Whales | 7c | 3.0c | 77 | 104 | 1747 | 267 | 1528 | $1066 | 7-30d |
| KXCBAGAME-26APR190735SHALEO-LEO | Shenzhen Leopards | 72c | 2.0c | 594 | 2494 | 4349 | 5720 | 664 | $664 | 7-30d |
| KXCBAGAME-26APR200735SBWJIA-JIA | Jiangsu Dragons | 94c | 2.0c | 15 | 127 | 15 | 10976 | 619 | $13 | 7-30d |
| KXCBAGAME-26APR190735BEDQIN-QIN | Qingdao Eagles | 38c | 1.0c | 50 | 1055 | 1250 | 4892 | 513 | $1018 | 7-30d |
| KXCBAGAME-26APR190735BRFZHE-BRF | Beijing Royal Fighters | 24c | 1.0c | 421 | 1794 | 2296 | 4696 | 438 | $279 | 7-30d |
| KXCBAGAME-26APR190735BEDQIN-BED | Beijing Ducks | 62c | 1.0c | 30 | 161 | 3668 | 2082 | 219 | $411 | 7-30d |
| KXCBAGAME-26APR190800NANXIN-XIN | Xinjiang Flying Tigers | 60c | 1.0c | 50 | 1040 | 50 | 5563 | 109 | $106 | 7-30d |
| KXCBAGAME-26APR190735SHALEO-SHA | Shandong Kirin | 28c | 2.0c | 1400 | 525 | 3828 | 3204 | 98 | $108 | 7-30d |
| KXCBAGAME-26APR200735JILNIN-NIN | Ningbo Rockets | 82c | 11.0c | 50 | 201 | 0 | 0 | 90 | $170 | 7-30d |
| KXCBAGAME-26APR200735LIASHAD-LIA | Liaoning Flying Leopards | 16c | 5.0c | 100 | 50 | 200 | 50 | 89 | $23 | 7-30d |
| KXCBAGAME-26APR200735JILNIN-JIL | Jilin Northeast Tigers | 18c | 8.0c | 100 | 149 | 100 | 199 | 80 | $80 | 7-30d |
| KXCBAGAME-26APR200735LIASHAD-SHAD | Shanghai Sharks | 84c | 5.0c | 50 | 8 | 50 | 217 | 34 | $18 | 7-30d |
| KXCBAGAME-26APR190800NANXIN-NAN | Nanjing Monkey Kings | 40c | 1.0c | 1000 | 50 | 3808 | 889 | 18 | $18 | 7-30d |
| KXCBAGAME-26APR200735TIAZGB-ZGB | Zhejiang Golden Bulls | 78c | 5.0c | 50 | 5 | 50 | 11 | 16 | $16 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCBAGAME | Chinese Basketball Association Game  | one_off | 20 | 18 | $7,900 | 8,307 | 3.0c |

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
