# world_russia_ukraine

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **9** (9 with open markets)
- Open markets: **49** (18 contested)
- Total 24h volume: **$6,770**
- Total open interest: **172,634**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **32**
- Median spread: **5.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median depth within 5c of best bid / ask — **1604 / 533** contracts
- Median depth within 10c of best bid / ask — **2504 / 563** contracts
- Median depth within 5c of midpoint — bid: **502** / ask: **430** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **74**
- Mean informed-signal proxy: **-0.403** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.41c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 560 | 1.75 | -0.192 | 7.00 | 73.9 |
| 30d+ | 1823 | 2.87 | -0.574 | 9.00 | 37.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXSAVEAMERICACLOTURE-MAY26-SCOL | Susan Collins | 15c | 1.0c | 1838 | 2102 | 2138 | 8403 | 2552 | 10315 | 9521 | $2321 | 7-30d |
| KXLOSEREELECTIONDSEN-2026-1 | Exactly 1 | 21c | 2.0c | 481 | 2617 | 2552 | 8179 | 3802 | 9622 | 8302 | $0 | 30d+ |
| KXSAVEAMERICACLOTURE-MAY26-MMCC | Mitch McConnell | 9c | 0.8c | 745 | 548 | 2045 | 801 | 22978 | 7486 | 8255 | $19 | 7-30d |
| KXLOSEREELECTIONDSEN-2026-0 | Exactly 0 | 72c | 1.0c | 2948 | 707 | 2949 | 4131 | 3199 | 4331 | 7647 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-5 | 5 or more | 24c | 4.0c | 5 | 360 | 1931 | 1360 | 2829 | 1469 | 6590 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-4 | Exactly 4 | 30c | 1.0c | 170 | 28 | 1170 | 350 | 1270 | 350 | 5769 | $0 | 30d+ |
| KXPUTINZELENSKYYLOCATION-28-HUNG | Hungary | 14c | 1.0c | 31 | 16 | 537 | 16 | 936 | 516 | 5090 | $0 | 30d+ |
| KXSAVEAMERICACLOTURE-MAY26-BCAS | Bill Cassidy | 6c | 0.2c | 2049 | 100 | 6906 | 460 | 6967 | 460 | 4242 | $98 | 7-30d |
| KXSAVEAMERICACLOTURE-MAY26-RPAU | Rand Paul | 19c | 6.0c | 5 | 265 | 59 | 715 | 359 | 715 | 3922 | $309 | 7-30d |
| KXLOSEREELECTIONRSEN-2026-3 | Exactly 3 | 17c | 1.0c | 250 | 206 | 3301 | 1276 | 7482 | 1531 | 3438 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-1 | Exactly 1 | 9c | 2.0c | 277 | 201 | 1277 | 1639 | 6306 | 4567 | 2937 | $0 | 30d+ |
| KXLOSEREELECTIONRSEN-2026-2 | Exactly 2 | 10c | 7.0c | 67 | 236 | 11298 | 1236 | 22325 | 1246 | 2675 | $0 | 30d+ |
| KXPUTINDJTLOCATION-29-HUN | Hungary | 14c | 5.0c | 15 | 1 | 315 | 601 | 3875 | 601 | 2586 | $0 | 30d+ |
| KXFLIGHTSRUSSIA-25-27 | Before 2027 | 16c | 5.0c | 4 | 500 | 1216 | 654 | 4267 | 654 | 2405 | $278 | 30d+ |
| KXPUTINDJTLOCATION-29-RUS | Russia | 10c | 7.0c | 32 | 100 | 2456 | 300 | 2456 | 300 | 2195 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXSAVEAMERICACLOTURE | Which Senators will vote to invoke clotu | one_off | 13 | 2 | $5,122 | 89,631 | 2.0c |
| KXLOSEREELECTIONDSEN | Democratic senators losing re-election | one_off | 6 | 2 | $0 | 28,919 | 1.5c |
| KXLOSEREELECTIONRSEN | Republican senators losing re-election | one_off | 6 | 3 | $0 | 23,115 | 2.0c |
| KXPUTINDJTLOCATION | Putin DJT meeting location | custom | 10 | 3 | $24 | 13,142 | 6.0c |
| KXPUTINZELENSKYYLOCATION | Where will Zelenskyy and Putin meet next | one_off | 8 | 3 | $6 | 9,694 | 4.7c |
| KXFLIGHTSRUSSIA | Flights Russia | custom | 1 | 1 | $278 | 2,405 | 5.0c |
| KXGALLEGOOUT | Ruben Gallego out as Senator? | one_off | 3 | 2 | $1,341 | 2,138 | 6.5c |
| KXRUCRUDEX | Russia crude exports in [month] below x. | one_off | 1 | 1 | $0 | 1,996 | 9.0c |
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
