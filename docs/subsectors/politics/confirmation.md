# pol_confirmation

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **22** (22 with open markets)
- Open markets: **182** (117 contested)
- Total 24h volume: **$11,880**
- Total open interest: **641,728**
- Top-OI mean spread (median across series): **6.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **127**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median depth within 5c of best bid / ask — **332 / 350** contracts
- Median depth within 10c of best bid / ask — **350 / 375** contracts
- Median depth within 5c of midpoint — bid: **225** / ask: **300** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **44**
- Mean informed-signal proxy: **-0.776** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.79c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 5527 | 2.10 | -0.602 | 7.00 | 51.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXOSCARNOMPIC-27-PRO | Project Hail Mary:: | 68c | 6.0c | 64 | 9 | 4608 | 2599 | 6683 | 3521 | 37635 | $88 | 30d+ |
| KXSCOTUSMARIJUANAGUN | Before 2026 | 16c | 3.0c | 17 | 50 | 611 | 550 | 611 | 550 | 18272 | $130 | 30d+ |
| KXSCOURT-29-JH | James Ho | 10c | 0.1c | 699 | 1599 | 1774 | 2107 | 12567 | 2152 | 12914 | $67 | 30d+ |
| KXSCOURT-29-AC | Aileen Cannon | 10c | 2.0c | 2904 | 1608 | 9458 | 2367 | 25131 | 2406 | 12675 | $136 | 30d+ |
| KXSCOTUSRESIGN-29-CT | Clarence Thomas | 48c | 5.0c | 13 | 79 | 650 | 579 | 713 | 931 | 11136 | $796 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-0 | 0 | 20c | 5.0c | 1003 | 1151 | 1023 | 2152 | 1078 | 2157 | 11097 | $0 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-1 | 1 | 30c | 5.0c | 1015 | 222 | 1015 | 1238 | 1040 | 1238 | 10249 | $84 | 30d+ |
| KXSCOURT-29-TED | Ted Cruz | 6c | 2.9c | 3 | 500 | 20209 | 1951 | 20209 | 1951 | 10181 | $209 | 30d+ |
| KXSCOURT-29-AO | Andrew Oldham | 14c | 2.0c | 500 | 1353 | 500 | 1855 | 1487 | 1855 | 9945 | $0 | 30d+ |
| KXSCOTUSRESIGN-29-SA | Samuel Alito | 58c | 3.0c | 25 | 134 | 580 | 634 | 972 | 634 | 9377 | $131 | 30d+ |
| KXSCOURT-29-AT | Amul Thapar | 8c | 3.9c | 833 | 647 | 1333 | 1313 | 5389 | 1320 | 8796 | $0 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-2 | 2 | 34c | 5.0c | 20 | 2018 | 1243 | 2018 | 1243 | 2034 | 8398 | $106 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-3 | 3 | 11c | 2.0c | 10 | 2880 | 1010 | 3955 | 26510 | 4290 | 8374 | $0 | 30d+ |
| KXSCOURT-29-KL | Kenneth Lee | 8c | 0.9c | 500 | 20 | 527 | 525 | 10069 | 525 | 7738 | $2834 | 30d+ |
| KXSCOURT-29-NR | Neomi Rao | 6c | 2.3c | 668 | 1822 | 13366 | 1877 | 13366 | 1927 | 7416 | $20 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMOVWISUPREMECOURT | Wisconsin Supreme Court election margin  | one_off | 9 | 0 | $3,647 | 204,063 | nanc |
| KXSCOURT | Next SCOTUS justice | custom | 34 | 2 | $3,878 | 194,373 | 2.0c |
| KXOSCARNOMPIC | Oscar nominations for Best Picture | annual | 29 | 26 | $1,026 | 81,063 | 6.7c |
| KXNEWSCOTUSCONF | SCOTUS confirmations | custom | 10 | 4 | $262 | 57,746 | 5.0c |
| KXSCOTUSRESIGN | SCOTUS members resigning | custom | 4 | 4 | $927 | 26,674 | 4.3c |
| KXOSCARNOMACTO | Oscar nominations for Best Actor | annual | 16 | 16 | $1,440 | 20,511 | 7.0c |
| KXSCOTUSMARIJUANAGUN | SCOTUS Marijuana gun ban | one_off | 1 | 1 | $130 | 18,272 | 3.0c |
| KXGOVWINOMR | Wisconsin Republican Governor Nomination | custom | 7 | 0 | $0 | 7,410 | nanc |
| KXOSCARNOMACTR | Oscar nominations for Best ActRESS | annual | 13 | 13 | $3 | 5,651 | 7.3c |
| KXOSCARNOMDIR | Oscar nominations for Best Director | annual | 11 | 11 | $374 | 5,384 | 7.7c |

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
