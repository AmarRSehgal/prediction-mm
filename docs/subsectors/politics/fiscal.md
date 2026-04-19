# pol_fiscal

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **6** (6 with open markets)
- Open markets: **50** (26 contested)
- Total 24h volume: **$92,925**
- Total open interest: **1,447,777**
- Top-OI mean spread (median across series): **7.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **33**
- Median spread: **4.0c**
- Median TOB bid / ask size: **108 / 118** contracts
- Median depth within 5c of best bid / ask — **1184 / 1510** contracts
- Median depth within 10c of best bid / ask — **1354 / 1599** contracts
- Median depth within 5c of midpoint — bid: **527** / ask: **1351** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **268**
- Mean informed-signal proxy: **-0.466** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.11c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 39 | 2.45 | 1.161 | 7.00 | 112.9 |
| 30d+ | 8784 | 0.90 | -0.257 | 3.00 | 93.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXGOVTSHUTLENGTH-26FEB07-G90 | :: Past 10AM 5/15 | 65c | 2.0c | 12 | 22 | 7433 | 4321 | 16202 | 4321 | 320400 | $3750 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G100 | :: Past 10AM 5/25 | 55c | 1.0c | 494 | 2 | 2752 | 2137 | 8347 | 2137 | 216085 | $6678 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G80 | :: Past 10AM 5/5 | 80c | 3.0c | 693 | 26 | 5447 | 1708 | 8065 | 12311 | 117516 | $4222 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G75 | :: Past 10AM 4/30 | 90c | 2.0c | 636 | 2090 | 5131 | 19539 | 5246 | 30725 | 82093 | $8089 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-A110 | :: Past 10AM 6/4 | 36c | 2.0c | 10 | 380 | 1184 | 1685 | 1184 | 2520 | 37857 | $1392 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G200 | :: Past 10AM 9/2 | 8c | 4.0c | 32 | 2 | 2432 | 16135 | 256380 | 16214 | 36970 | $491 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G300 | :: Past 10AM 12/11 | 6c | 4.0c | 60 | 2 | 5067 | 31614 | 5067 | 31624 | 33277 | $136 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G85 | :: Past 10AM 5/10 | 74c | 2.0c | 108 | 456 | 8564 | 12692 | 8564 | 12692 | 29897 | $1550 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G130 | :: Past 10AM 6/24 | 17c | 2.0c | 20 | 464 | 1199 | 2089 | 1354 | 2089 | 28145 | $6043 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G95 | :: Past 10AM 5/20 | 62c | 3.0c | 523 | 205 | 2786 | 3386 | 2786 | 3389 | 25768 | $3185 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G150 | :: Past 10AM 7/14 | 10c | 1.0c | 400 | 5021 | 2245 | 16396 | 6137 | 17146 | 21705 | $658 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G120 | :: Past 10AM 6/14 | 22c | 3.0c | 61 | 14 | 1686 | 12567 | 2861 | 12567 | 21622 | $1083 | 30d+ |
| KXGOVTSHUTLENGTH-26FEB07-G140 | :: Past 10AM 7/4 | 14c | 3.0c | 395 | 250 | 1266 | 9375 | 1924 | 9375 | 19605 | $181 | 30d+ |
| KXNUMSHUTDOWNS-27JAN01-T2 | 2 | 55c | 3.0c | 505 | 500 | 1505 | 1500 | 1505 | 3524 | 2205 | $0 | 30d+ |
| KXNUMSHUTDOWNS-27JAN01-T3 | 3 | 22c | 3.0c | 504 | 500 | 1615 | 1510 | 1615 | 1510 | 1875 | $105 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGOVTSHUTLENGTH | How long will the next government shutdo | one_off | 15 | 10 | $92,362 | 1,349,022 | 2.7c |
| KXGOVTCUTS | Government budget cuts | custom | 11 | 0 | $142 | 84,398 | nanc |
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
