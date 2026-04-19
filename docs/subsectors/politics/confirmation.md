# pol_confirmation

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **22** (22 with open markets)
- Open markets: **182** (117 contested)
- Total 24h volume: **$11,868**
- Total open interest: **642,389**
- Top-OI mean spread (median across series): **6.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **127**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median cumulative depth within 5c of mid — bid: **225** / ask: **300** contracts
- Median cumulative depth within 10c of mid — bid: **332** / ask: **350** contracts
- Mean trades per market (last 3000): **43**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 5521 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXOSCARNOMPIC-27-PRO | Project Hail Mary:: | 68c | 6.0c | 64 | 9 | 3012 | 2599 | 37635 | $115 | 30d+ |
| KXSCOTUSMARIJUANAGUN | Before 2026 | 16c | 3.0c | 17 | 61 | 581 | 561 | 18272 | $130 | 30d+ |
| KXSCOURT-29-JH | James Ho | 10c | 0.1c | 699 | 1646 | 1774 | 2154 | 12867 | $20 | 30d+ |
| KXSCOURT-29-AC | Aileen Cannon | 10c | 2.0c | 2904 | 1328 | 8458 | 1922 | 12675 | $136 | 30d+ |
| KXSCOTUSRESIGN-29-CT | Clarence Thomas | 48c | 5.0c | 18 | 15 | 555 | 584 | 11136 | $798 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-0 | 0 | 20c | 5.0c | 1003 | 1151 | 1023 | 2152 | 11097 | $60 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-1 | 1 | 30c | 5.0c | 1015 | 222 | 1015 | 1271 | 10249 | $84 | 30d+ |
| KXSCOURT-29-TED | Ted Cruz | 6c | 2.9c | 3 | 500 | 860 | 1951 | 10181 | $209 | 30d+ |
| KXSCOURT-29-AO | Andrew Oldham | 14c | 2.0c | 500 | 1353 | 500 | 1855 | 9945 | $0 | 30d+ |
| KXSCOTUSRESIGN-29-SA | Samuel Alito | 58c | 3.0c | 29 | 130 | 584 | 630 | 9377 | $658 | 30d+ |
| KXSCOURT-29-AT | Amul Thapar | 8c | 3.9c | 833 | 647 | 1333 | 1313 | 8796 | $0 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-2 | 2 | 34c | 5.0c | 20 | 2018 | 1118 | 2018 | 8398 | $106 | 30d+ |
| KXNEWSCOTUSCONF-29JAN20-3 | 3 | 11c | 2.0c | 10 | 2880 | 1010 | 2930 | 8374 | $662 | 30d+ |
| KXSCOURT-29-KL | Kenneth Lee | 8c | 0.9c | 500 | 9 | 527 | 525 | 7738 | $2834 | 30d+ |
| KXSCOURT-29-NR | Neomi Rao | 6c | 1.8c | 600 | 1822 | 2308 | 1877 | 7416 | $20 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMOVWISUPREMECOURT | Wisconsin Supreme Court election margin  | one_off | 9 | 0 | $1,625 | 204,141 | nanc |
| KXSCOURT | Next SCOTUS justice | custom | 34 | 2 | $4,872 | 194,326 | 1.5c |
| KXOSCARNOMPIC | Oscar nominations for Best Picture | annual | 29 | 26 | $602 | 81,454 | 6.7c |
| KXNEWSCOTUSCONF | SCOTUS confirmations | custom | 10 | 4 | $924 | 57,746 | 5.0c |
| KXSCOTUSRESIGN | SCOTUS members resigning | custom | 4 | 4 | $1,856 | 26,674 | 4.3c |
| KXOSCARNOMACTO | Oscar nominations for Best Actor | annual | 16 | 16 | $1,527 | 20,610 | 6.3c |
| KXSCOTUSMARIJUANAGUN | SCOTUS Marijuana gun ban | one_off | 1 | 1 | $141 | 18,272 | 3.0c |
| KXGOVWINOMR | Wisconsin Republican Governor Nomination | custom | 7 | 0 | $0 | 7,410 | nanc |
| KXOSCARNOMACTR | Oscar nominations for Best ActRESS | annual | 13 | 13 | $0 | 5,651 | 7.0c |
| KXOSCARNOMDIR | Oscar nominations for Best Director | annual | 11 | 11 | $277 | 5,459 | 7.3c |

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
