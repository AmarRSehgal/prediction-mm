# eco_fed

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **19** (19 with open markets)
- Open markets: **352** (166 contested)
- Total 24h volume: **$537,405**
- Total open interest: **19,308,531**
- Top-OI mean spread (median across series): **3.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median cumulative depth within 5c of mid — bid: **500** / ask: **500** contracts
- Median cumulative depth within 10c of mid — bid: **662** / ask: **622** contracts
- Mean trades per market (last 3000): **254**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 9463 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 41323 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXFEDDECISION-26JUN-C25 | Cut 25bps | 9c | 1.0c | 3103 | 1344 | 4374 | 17343 | 274367 | $10330 | 30d+ |
| KXFEDDECISION-26JUN-H0 | Hike 0bps | 90c | 1.0c | 1506 | 5845 | 5852 | 186023 | 247515 | $5591 | 30d+ |
| FEDHIKE-26DEC31 | By Dec 31, 2026 | 17c | 1.0c | 510 | 12 | 31024 | 1868 | 109816 | $152 | 30d+ |
| KXLEAVEPOWELLGOV-26AUG01 | Before August | 56c | 1.0c | 5 | 527 | 5791 | 1527 | 82775 | $103 | 30d+ |
| KXFEDCHAIRCONFIRMED-26JUL01 | Before Jul 1, 2026 | 84c | 3.0c | 36 | 297 | 1786 | 1477 | 68341 | $26 | 30d+ |
| KXFEDCHAIRCONFIRMED-26JUN01 | Before Jun 1, 2026 | 67c | 4.0c | 461 | 641 | 4963 | 4480 | 59666 | $704 | 30d+ |
| KXFEDCHAIRCONFIRMED-26AUG01 | Before Aug 1, 2026 | 88c | 1.0c | 537 | 68 | 6648 | 1399 | 55343 | $11 | 30d+ |
| KXRATECUT-26DEC31 | Cuts | 64c | 2.8c | 32 | 1000 | 4122 | 1019 | 49289 | $3309 | 30d+ |
| KXFEDGOVNOM-27-SMIR | Stephen Miran | 67c | 8.0c | 24 | 782 | 424 | 782 | 44344 | $1 | 30d+ |
| KXLEAVEPOWELLGOV-26AUG01-JUN | Before June | 30c | 1.0c | 801 | 1478 | 2901 | 2478 | 39539 | $153 | 30d+ |
| KXFEDGOVNOM-27-JSHE | Judy Shelton | 5c | 4.0c | 274 | 2 | 3866 | 2478 | 38514 | $0 | 30d+ |
| KXFEDCHAIRCONFIRMED-26MAY15 | Before May 15, 2026 | 36c | 1.0c | 210 | 102 | 1530 | 1254 | 36228 | $877 | 7-30d |
| KXFED-26JUN-T3.50 | 3.50% | 87c | 2.0c | 210 | 200 | 1247 | 6251 | 28200 | $758 | 30d+ |
| KXFEDMENTION-26APR-TRUM | Trump | 6c | 1.0c | 567 | 5222 | 30671 | 14231 | 25218 | $6241 | 7-30d |
| KXLEAVEPOWELLGOV-26AUG01-27 | Before 2027 | 70c | 1.0c | 11 | 17 | 3319 | 1525 | 24517 | $21 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXFEDDECISION | Fed meeting | custom | 75 | 28 | $411,771 | 12,443,652 | 1.0c |
| KXFED | Fed funds rate | custom | 120 | 64 | $79,308 | 3,040,600 | 2.3c |
| KXFEDCHAIRCONFIRM | Who will be confirmed as fed chair? | one_off | 4 | 0 | $8,443 | 2,462,137 | nanc |
| KXFEDCHAIRCONFIRMED | Will Trump's Fed Chair pick be confirmed | one_off | 5 | 4 | $1,821 | 329,294 | 2.7c |
| KXFEDMENTION | Fed mention | custom | 48 | 34 | $27,151 | 308,994 | 1.0c |
| KXFEDHIKE | Next Fed rate hike | custom | 4 | 3 | $1,223 | 200,683 | 5.0c |
| KXLEAVEPOWELLGOV | jerome powell leave as Fed governor | one_off | 3 | 3 | $308 | 146,829 | 1.0c |
| KXFEDGOVNOM | Fed governor nominee | one_off | 12 | 2 | $1 | 106,263 | 7.0c |
| KXFEDLEADJUNE | Who will chair the June FOMC meeting? | one_off | 8 | 2 | $432 | 71,364 | 4.0c |
| KXRATECUT | Fed rate cut | annual | 1 | 1 | $3,267 | 49,280 | 1.8c |

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
