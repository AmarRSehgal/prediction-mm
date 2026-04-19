# companies_ma

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **25** (10 contested)
- Total 24h volume: **$2,789**
- Total open interest: **757,031**
- Top-OI mean spread (median across series): **3.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **16**
- Median spread: **3.0c**
- Median TOB bid / ask size: **345 / 403** contracts
- Median depth within 5c of best bid / ask — **3999 / 1230** contracts
- Median depth within 10c of best bid / ask — **6976 / 1425** contracts
- Median depth within 5c of midpoint — bid: **1936** / ask: **653** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **248**
- Mean informed-signal proxy: **-0.266** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.29c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 3970 | 1.03 | -0.374 | 4.00 | 71.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXGREENLANDPRICE-29JAN21-NOACQ | $0 / No Acquisition | 80c | 1.0c | 5511 | 1544 | 15251 | 8170 | 17252 | 12333 | 156265 | $750 | 30d+ |
| KXGREENLANDPRICE-29JAN21-749B | $600 billion to $899 billion | 5c | 0.1c | 2030 | 1833 | 64260 | 9844 | 64260 | 13000 | 68409 | $31 | 30d+ |
| KXUSAEXPANDTERRITORY-27JAN01 | Before Jan 2027 | 15c | 5.0c | 799 | 18 | 4028 | 605 | 10222 | 905 | 37310 | $632 | 30d+ |
| KXUSAEXPANDTERRITORY-28JAN01 | Before Jan 2028 | 22c | 4.0c | 64 | 114 | 1620 | 628 | 1716 | 1322 | 30556 | $547 | 30d+ |
| KXUSAEXPANDTERRITORY-29JAN21 | Before Jan 21, 2029 | 38c | 5.0c | 43 | 1991 | 1147 | 2491 | 1147 | 2673 | 23811 | $525 | 30d+ |
| KXCOMPANYACTIONMERGER-27-27MAY01 | Before May 1, 2027 | 24c | 2.0c | 1022 | 587 | 2016 | 1087 | 2059 | 1087 | 7343 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-27MAR01 | Before Mar 1, 2027 | 17c | 6.0c | 1834 | 1914 | 7280 | 5404 | 7280 | 5904 | 6672 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-27JAN01 | Before Jan 1, 2027 | 14c | 3.0c | 27 | 64 | 5546 | 2126 | 10885 | 2126 | 5732 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-26AUG01 | Before Aug 1, 2026 | 5c | 2.0c | 486 | 219 | 2486 | 1329 | 2486 | 1529 | 5286 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-27FEB01 | Before Feb 1, 2027 | 15c | 7.0c | 204 | 2825 | 5255 | 2825 | 12320 | 2825 | 5050 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-27APR01 | Before Apr 1, 2027 | 24c | 3.0c | 944 | 5 | 1524 | 505 | 1674 | 939 | 5042 | $73 | 30d+ |
| KXCOMPANYACTIONMERGER-27-26SEP01 | Before Sep 1, 2026 | 6c | 3.0c | 2522 | 669 | 7843 | 679 | 7843 | 679 | 4944 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-26DEC01 | Before Dec 1, 2026 | 12c | 5.0c | 40 | 75 | 3971 | 3710 | 7169 | 3710 | 3922 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-26JUL01 | Before Jul 1, 2026 | 5c | 3.0c | 150 | 19 | 1353 | 570 | 1353 | 1320 | 3146 | $0 | 30d+ |
| KXCOMPANYACTIONMERGER-27-26NOV01 | Before Nov 1, 2026 | 10c | 3.0c | 127 | 631 | 3668 | 1131 | 6784 | 1131 | 3084 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXGREENLANDPRICE | How much will Greenland be acquired for? | one_off | 8 | 1 | $1,004 | 569,293 | 1.0c |
| KXUSAEXPANDTERRITORY | Will the US acquire new territory? | one_off | 4 | 3 | $1,713 | 132,376 | 4.7c |
| KXCOMPANYACTIONMERGER | Company Merger | one_off | 13 | 6 | $73 | 55,362 | 3.7c |

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
