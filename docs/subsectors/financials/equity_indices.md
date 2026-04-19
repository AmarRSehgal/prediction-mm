# fin_equity_indices

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **199** (44 contested)
- Total 24h volume: **$68,344**
- Total open interest: **1,441,874**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **58**
- Median spread: **16.0c**
- Median TOB bid / ask size: **81 / 91** contracts
- Median depth within 5c of best bid / ask — **534 / 635** contracts
- Median depth within 10c of best bid / ask — **791 / 746** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **55**
- Mean informed-signal proxy: **-1.034** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.98c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 92 | 11.03 | -2.813 | 40.30 | 17.6 |
| 7-30d | 17 | 1.31 | 0.437 | 3.75 | 45.3 |
| 30d+ | 3066 | 1.86 | -0.731 | 7.00 | 195.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNASDAQ100Y-26DEC31H1600-T19000 | 18,999.99 or below | 12c | 1.0c | 1010 | 327 | 2045 | 1411 | 2074 | 3078 | 628956 | $295 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-T33000 | 33,000.01 or above | 10c | 4.0c | 1014 | 3000 | 1026 | 3000 | 2084 | 4785 | 36195 | $373 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B27750 | 27,500 to 27,999.99 | 5c | 2.0c | 1027 | 2484 | 2698 | 6632 | 2698 | 6632 | 32514 | $3 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B28750 | 28,500 to 28,999.99 | 6c | 1.0c | 90 | 2277 | 1852 | 7500 | 1852 | 7500 | 32370 | $0 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B26250 | 26,000 to 26,499.99 | 5c | 2.0c | 1539 | 3175 | 3690 | 5520 | 3690 | 5520 | 31848 | $0 | 30d+ |
| KXNASDAQ100POS-26DEC31H1600-T25249.85 | 25,249.86 or above | 60c | 1.0c | 117 | 139 | 2702 | 4688 | 2702 | 4688 | 27856 | $32 | 30d+ |
| KXSP500ADDQ-26JUL01-SOFI | SoFi | 26c | 12.0c | 9 | 1294 | 509 | 1334 | 1047 | 1334 | 4043 | $93 | 30d+ |
| KXSP500ADDQ-26JUL01-MSTR | Strategy (MicroStrategy) | 5c | 7.0c | 1757 | 300 | 2174 | 1688 | 2174 | 1688 | 3688 | $0 | 30d+ |
| KXSP500ADDQ-26JUL01-CRWV | CoreWeave | 8c | 8.0c | 1150 | 500 | 2227 | 642 | 2227 | 642 | 2424 | $245 | 30d+ |
| KXSP500ADDQ-26JUL01-PSTG | Pure Storage | 11c | 6.0c | 500 | 99 | 610 | 444 | 960 | 952 | 1965 | $250 | 30d+ |
| KXSP500ADDQ-26JUL01-ALNY | Alnylam Pharmaceuticals | 36c | 5.0c | 5 | 70 | 537 | 100 | 537 | 600 | 1421 | $631 | 30d+ |
| KXNASDAQ100MAXY-26DEC31H1600-T29499.99 | 29,500 or above | 56c | 86.8c | 492 | 200 | 492 | 1200 | 492 | 1200 | 1402 | $0 | 30d+ |
| KXNASDAQ100MAXY-26DEC31H1600-T29999.99 | 30,000 or above | 33c | 6.0c | 51 | 9 | 51 | 9 | 51 | 9 | 1173 | $13 | 30d+ |
| KXSP500ADDQ-26JUL01-AFRM | Affirm Holdings | 5c | 6.0c | 599 | 150 | 1249 | 654 | 1249 | 884 | 1143 | $0 | 30d+ |
| KXSP500REMOVEQ-26JUL01-TTD | The Trade Desk | 6c | 8.0c | 306 | 220 | 1006 | 720 | 1006 | 720 | 900 | $204 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNASDAQ100Y | Nasdaq yearly range | annual | 30 | 2 | $1,358 | 1,250,485 | 2.5c |
| KXTRUTHSOCIAL | Number of Trump Truth Social posts this  | weekly | 9 | 0 | $53,353 | 79,305 | nanc |
| KXNASDAQ100POS | NASDAQ100 Positive | annual | 1 | 1 | $32 | 27,856 | 0.9c |
| KXNASDAQ100MAXY | Nasdaq max yearly | annual | 17 | 14 | $13 | 26,274 | 48.9c |
| KXNASDAQ100MINY | NASDAQ100 Min | annual | 3 | 0 | $2,045 | 24,704 | nanc |
| KXSP500ADDQ | Companies added to SP500  | one_off | 9 | 4 | $1,219 | 18,596 | 6.7c |
| KXNASDAQ100 | Nasdaq range | daily | 60 | 0 | $6,712 | 5,147 | nanc |
| KXSP500REMOVEQ | Companies removed from SP500 | one_off | 9 | 3 | $217 | 4,782 | 7.3c |
| KXNASDAQ100U | Nasdaq above/below | hourly | 60 | 19 | $3,045 | 4,098 | 23.7c |
| KXTRUMPDELETE | How many Truth Social posts will Trump d | one_off | 1 | 1 | $350 | 627 | 7.0c |

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
