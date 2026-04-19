# pol_fiscal

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **6** (6 with open markets)
- Open markets: **50** (26 contested)
- Total 24h volume: **$100,928**
- Total open interest: **1,447,829**
- Top-OI mean spread (median across series): **7.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **33**
- Median spread: **4.0c**
- Median TOB bid / ask size: **100 / 83** contracts
- Median cumulative depth within 5c of mid — bid: **527** / ask: **1351** contracts
- Median cumulative depth within 10c of mid — bid: **1184** / ask: **1510** contracts
- Mean trades per market (last 3000): **477**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 39 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 15705 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXGOVTSHUTLENGTH-26FEB07-G90 | :: Past 10AM 5/15 | 64c | 2.0c | 1029 | 33 | 7428 | 3522 | 320500 | $3765 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G100 | :: Past 10AM 5/25 | 55c | 1.0c | 494 | 55 | 2752 | 2180 | 216039 | $6634 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G80 | :: Past 10AM 5/5 | 80c | 3.0c | 794 | 27 | 4476 | 1185 | 117516 | $3847 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G75 | :: Past 10AM 4/30 | 90c | 1.0c | 492 | 2049 | 4453 | 19524 | 82093 | $8348 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-A110 | :: Past 10AM 6/4 | 36c | 2.0c | 10 | 421 | 434 | 1726 | 37857 | $1446 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G200 | :: Past 10AM 9/2 | 7c | 3.0c | 32 | 2 | 1223 | 16258 | 36968 | $489 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G300 | :: Past 10AM 12/11 | 6c | 4.0c | 70 | 2 | 3126 | 31610 | 33267 | $166 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G85 | :: Past 10AM 5/10 | 74c | 2.0c | 318 | 416 | 4152 | 6682 | 29913 | $1353 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G130 | :: Past 10AM 6/24 | 17c | 2.0c | 20 | 475 | 449 | 1600 | 28109 | $6008 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G95 | :: Past 10AM 5/20 | 63c | 2.0c | 5 | 83 | 1799 | 3264 | 25717 | $3129 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G150 | :: Past 10AM 7/14 | 10c | 1.0c | 400 | 5021 | 2245 | 16396 | 21705 | $1061 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G120 | :: Past 10AM 6/14 | 22c | 3.0c | 61 | 6 | 1686 | 12559 | 21622 | $1017 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G140 | :: Past 10AM 7/4 | 13c | 2.0c | 20 | 1 | 1266 | 8648 | 19587 | $2758 | 30d+ |
| KXNUMSHUTDOWNS-27JAN01-T2 | 2 | 55c | 3.0c | 505 | 500 | 1505 | 1500 | 2205 | $0 | 30d+ |
| KXNUMSHUTDOWNS-27JAN01-T3 | 3 | 22c | 3.0c | 504 | 500 | 1607 | 1510 | 1875 | $105 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGOVTSHUTLENGTH | How long will the next government shutdo | one_off | 15 | 10 | $100,348 | 1,349,074 | 1.3c |
| KXGOVTCUTS | Government budget cuts | custom | 11 | 0 | $160 | 84,398 | nanc |
| KXNUMSHUTDOWNS | Number of government shutdowns? | one_off | 4 | 3 | $105 | 5,407 | 3.3c |
| KXGOVTSPEND | Government budget increases | custom | 9 | 5 | $0 | 3,114 | 9.2c |
| KXHBUDGETRES | House budget resolution | custom | 5 | 4 | $301 | 3,067 | 7.3c |
| KXSBUDGETRES | Seante budget resolution | custom | 6 | 4 | $15 | 2,769 | 16.0c |

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
