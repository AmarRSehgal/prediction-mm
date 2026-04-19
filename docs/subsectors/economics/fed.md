# eco_fed

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **19** (19 with open markets)
- Open markets: **352** (166 contested)
- Total 24h volume: **$541,184**
- Total open interest: **19,355,953**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **5.0c**
- Median TOB bid / ask size: **200 / 200** contracts
- Median depth within 5c of best bid / ask — **579 / 639** contracts
- Median depth within 10c of best bid / ask — **737 / 861** contracts
- Median depth within 5c of midpoint — bid: **500** / ask: **500** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **227**
- Mean informed-signal proxy: **-1.218** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.11c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 9516 | 0.87 | -0.260 | 3.00 | 31.9 |
| 30d+ | 35929 | 3.21 | -1.085 | 16.00 | 44.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXFEDDECISION-26JUN-C25 | Cut 25bps | 9c | 1.0c | 1436 | 3344 | 4013 | 23343 | 158773 | 30164 | 274367 | $10320 | 30d+ |
| KXFEDDECISION-26JUN-H0 | Hike 0bps | 90c | 1.0c | 1504 | 5841 | 11850 | 336117 | 16850 | 4161002 | 247518 | $596 | 30d+ |
| FEDHIKE-26DEC31 | By Dec 31, 2026 | 17c | 1.0c | 510 | 12 | 31024 | 2888 | 37859 | 4085 | 109816 | $152 | 30d+ |
| KXLEAVEPOWELLGOV-26AUG01 | Before August | 56c | 1.0c | 5 | 527 | 5791 | 1527 | 6791 | 1527 | 82775 | $103 | 30d+ |
| KXFEDCHAIRCONFIRMED-26JUL01 | Before Jul 1, 2026 | 84c | 3.0c | 37 | 297 | 4462 | 2111 | 5386 | 2611 | 68341 | $26 | 30d+ |
| KXFEDCHAIRCONFIRMED-26JUN01 | Before Jun 1, 2026 | 67c | 4.0c | 461 | 641 | 4962 | 5472 | 5162 | 8230 | 59666 | $709 | 30d+ |
| KXFEDCHAIRCONFIRMED-26AUG01 | Before Aug 1, 2026 | 88c | 1.0c | 537 | 68 | 6839 | 1474 | 7405 | 20123 | 55343 | $11 | 30d+ |
| KXRATECUT-26DEC31 | Cuts | 64c | 2.8c | 32 | 1000 | 4122 | 1019 | 4147 | 5716 | 49289 | $3310 | 30d+ |
| KXFEDGOVNOM-27-SMIR | Stephen Miran | 67c | 8.0c | 29 | 782 | 429 | 782 | 429 | 782 | 44344 | $1 | 30d+ |
| KXLEAVEPOWELLGOV-26AUG01-JUN | Before June | 30c | 1.0c | 801 | 1478 | 3901 | 2478 | 4973 | 2478 | 39539 | $153 | 30d+ |
| KXFEDGOVNOM-27-JSHE | Judy Shelton | 5c | 4.0c | 274 | 2 | 3866 | 3709 | 3866 | 3909 | 38514 | $0 | 30d+ |
| KXFEDCHAIRCONFIRMED-26MAY15 | Before May 15, 2026 | 36c | 2.0c | 817 | 500 | 1767 | 1652 | 2878 | 2252 | 36391 | $1440 | 7-30d |
| KXFED-26JUN-T3.50 | 3.50% | 87c | 2.0c | 210 | 218 | 1252 | 6251 | 1252 | 11715 | 28200 | $558 | 30d+ |
| KXFEDMENTION-26APR-TRUM | Trump | 6c | 1.0c | 510 | 5040 | 30728 | 15740 | 30728 | 20340 | 25267 | $6329 | 7-30d |
| KXLEAVEPOWELLGOV-26AUG01-27 | Before 2027 | 72c | 1.0c | 4 | 525 | 3319 | 1601 | 5881 | 1601 | 24517 | $21 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXFEDDECISION | Fed meeting | custom | 75 | 28 | $423,436 | 12,481,761 | 1.3c |
| KXFED | Fed funds rate | custom | 120 | 64 | $73,646 | 3,049,049 | 2.3c |
| KXFEDCHAIRCONFIRM | Who will be confirmed as fed chair? | one_off | 4 | 0 | $7,549 | 2,461,956 | nanc |
| KXFEDCHAIRCONFIRMED | Will Trump's Fed Chair pick be confirmed | one_off | 5 | 4 | $2,294 | 329,457 | 2.7c |
| KXFEDMENTION | Fed mention | custom | 48 | 34 | $26,844 | 309,806 | 1.0c |
| KXFEDHIKE | Next Fed rate hike | custom | 4 | 3 | $272 | 200,683 | 5.0c |
| KXLEAVEPOWELLGOV | jerome powell leave as Fed governor | one_off | 3 | 3 | $277 | 146,830 | 1.0c |
| KXFEDGOVNOM | Fed governor nominee | one_off | 12 | 2 | $1 | 106,263 | 7.0c |
| KXFEDLEADJUNE | Who will chair the June FOMC meeting? | one_off | 8 | 2 | $432 | 71,364 | 4.0c |
| KXRATECUT | Fed rate cut | annual | 1 | 1 | $3,310 | 49,289 | 2.8c |

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
