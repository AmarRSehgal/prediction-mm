# tech_ev_tesla

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **7** (7 with open markets)
- Open markets: **43** (26 contested)
- Total 24h volume: **$11,204**
- Total open interest: **272,826**
- Top-OI mean spread (median across series): **3.2 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **37**
- Median spread: **7.0c**
- Median TOB bid / ask size: **250 / 186** contracts
- Median cumulative depth within 5c of mid — bid: **250** / ask: **500** contracts
- Median cumulative depth within 10c of mid — bid: **350** / ask: **595** contracts
- Mean trades per market (last 3000): **132**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 4880 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TESLAOPTIMUS-26DEC31 | Before 2027 | 19c | 1.0c | 26 | 84 | 5226 | 1751 | 108207 | $286 | 30d+ |
| KXTESLADELIVERYBY-27-500000 | Above 500000 in a single quarter | 19c | 3.0c | 107 | 1383 | 623 | 1883 | 29547 | $23 | 30d+ |
| KXTESLASEMI-27JAN-1000 | above 1000 | 57c | 5.0c | 12 | 500 | 12 | 500 | 20000 | $154 | 30d+ |
| KXTESLAROADSTER-27 | Before Jan 1, 2027 | 12c | 1.0c | 27 | 1313 | 38 | 1313 | 16289 | $0 | 30d+ |
| KXTESLASEMI-27JAN-5000 | above 5000 | 15c | 9.0c | 500 | 186 | 500 | 186 | 14234 | $0 | 30d+ |
| KXTSLA-26JULPROD-440000.0 | above 440000 | 48c | 3.0c | 24 | 48 | 119 | 574 | 11462 | $3320 | 30d+ |
| KXTSLA-26JULPROD-420000.0 | above 420000 | 62c | 3.0c | 33 | 17 | 33 | 83 | 10769 | $1399 | 30d+ |
| KXTESLAENERGYBY-27-15 | Above 15 GWh of energy deployed in a sin | 64c | 6.0c | 17 | 500 | 299 | 500 | 7168 | $0 | 30d+ |
| KXTSLA-26JULPROD-400000.0 | above 400000 | 61c | 2.0c | 71 | 5 | 92 | 25 | 6381 | $661 | 30d+ |
| KXTESLAENERGYBY-27-20 | Above 20 GWh of energy deployed in a sin | 34c | 3.0c | 3 | 500 | 28 | 500 | 6118 | $0 | 30d+ |
| KXTESLASEMI-27JAN-0 | above 0 | 94c | 4.0c | 5 | 500 | 87 | 1950 | 4356 | $0 | 30d+ |
| KXTSLA-26JULDELIV-420000.0 | above 420000 | 52c | 9.0c | 250 | 250 | 250 | 250 | 3896 | $22 | 30d+ |
| KXTSLA-26JULDELIV-410000.0 | above 410000 | 45c | 7.0c | 250 | 23 | 250 | 113 | 3454 | $1830 | 30d+ |
| KXTESLAENERGYBY-27-30 | Above 30 GWh of energy deployed in a sin | 15c | 7.0c | 36 | 6 | 536 | 506 | 3217 | $0 | 30d+ |
| KXTSLA-26JULPROD-380000.0 | above 380000 | 82c | 6.0c | 66 | 31 | 66 | 1057 | 2427 | $2189 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTESLAOPTIMUS | Tesla Optimus sale | custom | 1 | 1 | $278 | 108,205 | 1.0c |
| KXTSLA | Tesla KPI | one_off | 24 | 18 | $10,749 | 48,879 | 3.3c |
| KXTESLASEMI | How many Tesla semi trucks produced | one_off | 7 | 2 | $154 | 41,855 | 7.0c |
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
