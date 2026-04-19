# world_russia_ukraine

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **49** (18 contested)
- Total 24h volume: **$6,216**
- Total open interest: **171,589**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **32**
- Median spread: **5.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median cumulative depth within 5c of mid — bid: **500** / ask: **440** contracts
- Median cumulative depth within 10c of mid — bid: **2214** / ask: **548** contracts
- Mean trades per market (last 3000): **74**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 553 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 1823 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSAVEAMERICACLOTURE-MAY26-SCOL | Susan Collins | 15c | 1.0c | 975 | 1328 | 2775 | 7131 | 9521 | $2321 | 7-30d |
| KXLOSEREELECTIONDSEN-2026-1 | Exactly 1 | 21c | 2.0c | 481 | 2617 | 2552 | 8179 | 8302 | $0 | 30d+ |
| KXSAVEAMERICACLOTURE-MAY26-MMCC | Mitch McConnell | 10c | 0.1c | 200 | 998 | 2400 | 998 | 8255 | $19 | 7-30d |
| KXLOSEREELECTIONDSEN-2026-0 | Exactly 0 | 72c | 1.0c | 2948 | 707 | 2949 | 3131 | 7647 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-5 | 5 or more | 24c | 4.0c | 5 | 360 | 497 | 1360 | 6590 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-4 | Exactly 4 | 30c | 1.0c | 170 | 28 | 1170 | 350 | 5769 | $0 | 30d+ |
| KXPUTINZELENSKYYLOCATION-28-HUNG | Hungary | 14c | 1.0c | 31 | 16 | 531 | 36 | 5090 | $0 | 30d+ |
| KXSAVEAMERICACLOTURE-MAY26-BCAS | Bill Cassidy | 6c | 0.9c | 1955 | 100 | 3858 | 479 | 4242 | $98 | 7-30d |
| KXSAVEAMERICACLOTURE-MAY26-RPAU | Rand Paul | 20c | 3.0c | 5 | 20 | 22 | 570 | 3922 | $309 | 7-30d |
| KXLOSEREELECTIONRSEN-2026-3 | Exactly 3 | 17c | 1.0c | 250 | 206 | 3301 | 276 | 3438 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-1 | Exactly 1 | 9c | 2.0c | 277 | 201 | 1277 | 1639 | 2937 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-2 | Exactly 2 | 10c | 7.0c | 67 | 236 | 67 | 236 | 2675 | $0 | 30d+ |
| KXPUTINDJTLOCATION-29-HUN | Hungary | 14c | 5.0c | 15 | 1 | 115 | 401 | 2586 | $0 | 30d+ |
| KXFLIGHTSRUSSIA-25-27 | Before 2027 | 16c | 5.0c | 7 | 500 | 289 | 654 | 2405 | $278 | 30d+ |
| KXPUTINDJTLOCATION-29-RUS | Russia | 10c | 7.0c | 32 | 100 | 132 | 300 | 2195 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSAVEAMERICACLOTURE | Which Senators will vote to invoke clotu | one_off | 13 | 2 | $4,846 | 88,863 | 3.0c |
| KXLOSEREELECTIONDSEN | Democratic senators losing re-election | one_off | 6 | 2 | $0 | 28,919 | 1.5c |
| KXLOSEREELECTIONRSEN | Republican senators losing re-election | one_off | 6 | 3 | $0 | 23,115 | 2.0c |
| KXPUTINDJTLOCATION | Putin DJT meeting location | custom | 10 | 3 | $24 | 13,142 | 6.0c |
| KXPUTINZELENSKYYLOCATION | Where will Zelenskyy and Putin meet next | one_off | 8 | 3 | $6 | 9,694 | 4.7c |
| KXGALLEGOOUT | Ruben Gallego out as Senator? | one_off | 3 | 2 | $1,341 | 2,138 | 7.5c |
| KXFLIGHTSRUSSIA | Flights Russia | custom | 1 | 1 | $0 | 2,127 | 5.0c |
| KXRUCRUDEX | Russia crude exports in [month] below x. | one_off | 1 | 1 | $0 | 1,996 | 7.0c |
| KXSANCTIONRUSSIA | Will a bill sanctioning Russia become la | one_off | 1 | 1 | $0 | 1,594 | 6.0c |

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
