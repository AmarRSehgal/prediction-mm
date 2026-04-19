# sports_motor

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **17** (17 with open markets)
- Open markets: **489** (52 contested)
- Total 24h volume: **$660,266**
- Total open interest: **5,915,052**
- Top-OI mean spread (median across series): **6.2 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **156**
- Median spread: **37.0c**
- Median TOB bid / ask size: **993 / 1990** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **221**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2484 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 31975 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXF1-26-CL | :: Ferrari | 6c | 1.0c | 4222 | 75 | 194462 | 6907 | 291186 | $834 | 30d+ |
| KXF1-26-GR | :: Mercedes AMG Motorsport | 44c | 1.0c | 1464 | 4692 | 35997 | 12934 | 273084 | $406 | 30d+ |
| KXF1-26-OP | :: McLaren | 6c | 1.0c | 506 | 2375 | 207786 | 5117 | 270271 | $0 | 30d+ |
| KXF1-26-KA | :: Mercedes AMG Motorsport | 32c | 1.0c | 15038 | 6 | 68480 | 4337 | 269069 | $11372 | 30d+ |
| KXF1CONSTRUCTORS-26-FER | Ferrari | 12c | 1.0c | 2950 | 742 | 20599 | 12134 | 174712 | $798 | 30d+ |
| KXNASCARCUPSERIES-NCS26-TRED | Tyler Reddick | 19c | 3.0c | 4 | 1140 | 3857 | 3863 | 148545 | $889 | 30d+ |
| KXF1CONSTRUCTORS-26-MER | Mercedes AMG Motorsport | 76c | 2.0c | 374 | 326 | 3075 | 4238 | 131310 | $464 | 30d+ |
| KXF1CONSTRUCTORS-26-MCL | McLaren | 7c | 2.0c | 1923 | 2925 | 8721 | 41925 | 130483 | $80 | 30d+ |
| KXNASCARCUPSERIES-NCS26-KLAR | Kyle Larson | 10c | 2.0c | 7785 | 1503 | 30001 | 3812 | 90100 | $1381 | 30d+ |
| KXNASCARCUPSERIES-NCS26-DHAM | Denny Hamlin | 14c | 3.0c | 431 | 724 | 5117 | 4574 | 89716 | $1132 | 30d+ |
| KXNASCARRACE-ADV26-CHBE | Christopher Bell | 14c | 1.0c | 300 | 33016 | 6348 | 37935 | 86503 | $22664 | 7-30d |
| KXNASCARCUPSERIES-NCS26-CBEL | Christopher Bell | 8c | 2.0c | 11 | 542 | 9848 | 3839 | 84322 | $41 | 30d+ |
| KXNASCARCUPSERIES-NCS26-WBYR | William Byron | 7c | 2.0c | 4992 | 1470 | 8448 | 9474 | 82027 | $128 | 30d+ |
| KXNASCARCUPSERIES-NCS26-RBLA | Ryan Blaney | 10c | 2.0c | 23 | 505 | 6512 | 5606 | 80821 | $570 | 30d+ |
| KXNASCARCUPSERIES-NCS26-CELL | Chase Elliott | 7c | 2.0c | 2651 | 352 | 20616 | 2352 | 73076 | $20 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXF1 | Formula 1 | annual | 22 | 2 | $13,021 | 2,459,731 | 1.0c |
| KXNASCARCUPSERIES | NASCAR Cup Series Champion | annual | 30 | 4 | $11,831 | 1,345,377 | 2.7c |
| KXF1CONSTRUCTORS | Formula 1 Constructors | annual | 11 | 2 | $5,152 | 885,627 | 1.5c |
| KXNASCARRACE | NASCAR Race | custom | 74 | 6 | $544,429 | 838,525 | 8.7c |
| KXF1RACE | F1 Race | custom | 22 | 2 | $5,837 | 95,347 | 2.0c |
| KXINDYCARSERIES | IndyCar Series Champion | annual | 25 | 2 | $802 | 65,254 | 3.0c |
| KXINDYCARRACE | IndyCar Race | custom | 25 | 4 | $41,855 | 53,923 | 16.7c |
| KXNASCARTRUCKSERIES | NASCAR Truck Series Champion | annual | 36 | 3 | $186 | 41,342 | 3.7c |
| KXNASCARTOP10 | NASCAR Top 10 Finishers | custom | 37 | 7 | $24,960 | 39,441 | 72.3c |
| KXNASCARAUTOPARTSSERIES | NASCAR Auto Parts Series Champion | annual | 40 | 3 | $707 | 32,631 | 5.0c |

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
