# tech_ev_tesla

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **43** (26 contested)
- Total 24h volume: **$14,522**
- Total open interest: **275,210**
- Top-OI mean spread (median across series): **3.8 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **37**
- Median spread: **6.0c**
- Median TOB bid / ask size: **107 / 186** contracts
- Median depth within 5c of best bid / ask — **250 / 578** contracts
- Median depth within 10c of best bid / ask — **528 / 686** contracts
- Median depth within 5c of midpoint — bid: **250** / ask: **500** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **107**
- Mean informed-signal proxy: **0.183** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.68c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 3974 | 2.11 | -0.302 | 8.00 | 45.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TESLAOPTIMUS-26DEC31 | Before 2027 | 19c | 1.0c | 26 | 84 | 5370 | 1751 | 6762 | 2410 | 108239 | $346 | 30d+ |
| KXTESLADELIVERYBY-27-500000 | Above 500000 in a single quarter | 19c | 3.0c | 107 | 1383 | 1184 | 1883 | 1527 | 1883 | 29547 | $23 | 30d+ |
| KXTESLASEMI-27JAN-1000 | above 1000 | 57c | 5.0c | 10 | 500 | 12 | 500 | 544 | 516 | 20001 | $156 | 30d+ |
| KXTESLAROADSTER-27 | Before Jan 1, 2027 | 12c | 1.0c | 27 | 1313 | 38 | 1313 | 3746 | 1324 | 16289 | $0 | 30d+ |
| KXTESLASEMI-27JAN-5000 | above 5000 | 15c | 9.0c | 500 | 186 | 500 | 686 | 6396 | 686 | 14234 | $0 | 30d+ |
| KXTSLA-26JULPROD-440000.0 | above 440000 | 47c | 2.0c | 28 | 12 | 887 | 824 | 1887 | 1293 | 11462 | $3320 | 30d+ |
| KXTSLA-26JULPROD-420000.0 | above 420000 | 59c | 4.0c | 32 | 1 | 148 | 105 | 1728 | 695 | 10789 | $1432 | 30d+ |
| KXTESLAENERGYBY-27-15 | Above 15 GWh of energy deployed in a sin | 64c | 5.0c | 19 | 500 | 880 | 850 | 5574 | 850 | 7168 | $0 | 30d+ |
| KXTSLA-26JULPROD-400000.0 | above 400000 | 64c | 5.0c | 5 | 17 | 92 | 545 | 938 | 1183 | 6786 | $1189 | 30d+ |
| KXTESLAENERGYBY-27-20 | Above 20 GWh of energy deployed in a sin | 34c | 3.0c | 3 | 500 | 28 | 500 | 528 | 500 | 6118 | $0 | 30d+ |
| KXTSLA-26JULDELIV-420000.0 | above 420000 | 52c | 6.0c | 32 | 58 | 420 | 725 | 420 | 725 | 4822 | $948 | 30d+ |
| KXTESLASEMI-27JAN-0 | above 0 | 94c | 4.0c | 5 | 500 | 587 | 1950 | 611 | 1950 | 4356 | $0 | 30d+ |
| KXTSLA-26JULDELIV-410000.0 | above 410000 | 45c | 7.0c | 250 | 23 | 250 | 363 | 250 | 613 | 3454 | $1830 | 30d+ |
| KXTESLAENERGYBY-27-30 | Above 30 GWh of energy deployed in a sin | 15c | 7.0c | 36 | 8 | 536 | 508 | 4296 | 508 | 3217 | $0 | 30d+ |
| KXTSLA-26JULPROD-380000.0 | above 380000 | 81c | 4.0c | 66 | 317 | 66 | 3339 | 66 | 5229 | 2977 | $3077 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTESLAOPTIMUS | Tesla Optimus sale | custom | 1 | 1 | $346 | 108,239 | 1.0c |
| KXTSLA | Tesla KPI | one_off | 24 | 18 | $13,998 | 51,227 | 4.7c |
| KXTESLASEMI | How many Tesla semi trucks produced | one_off | 7 | 2 | $156 | 41,857 | 7.0c |
| KXTESLADELIVERYBY | Tesla deliveries by | custom | 5 | 1 | $23 | 31,163 | 3.0c |
| KXTESLAENERGYBY | Tesla energy business | custom | 4 | 3 | $0 | 17,918 | 5.3c |
| KXTESLAROADSTER | Tesla Roadster delivered | one_off | 1 | 1 | $0 | 16,289 | 1.0c |
| KXTESLACAR | Will Tesla release a car that is 30 thou | one_off | 1 | 0 | $0 | 8,518 | nanc |

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
