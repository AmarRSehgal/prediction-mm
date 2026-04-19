# fin_equity_indices

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **199** (47 contested)
- Total 24h volume: **$44,378**
- Total open interest: **1,426,299**
- Top-OI mean spread (median across series): **7.5 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **59**
- Median spread: **17.0c**
- Median TOB bid / ask size: **32 / 99** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **4** / ask: **1** contracts
- Mean trades per market (last 3000): **71**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 6-12h | 302 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 232 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 224 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 138 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 17 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 3296 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNASDAQ100Y-26DEC31H1600-T19000 | 18,999.99 or below | 12c | 2.0c | 1011 | 327 | 1043 | 1398 | 628956 | $295 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-T33000 | 33,000.01 or above | 10c | 4.0c | 1014 | 3000 | 1026 | 3000 | 36195 | $373 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B27750 | 27,500 to 27,999.99 | 5c | 2.0c | 1027 | 2484 | 2698 | 6632 | 32514 | $3 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B28750 | 28,500 to 28,999.99 | 6c | 1.0c | 90 | 2277 | 1852 | 7500 | 32370 | $0 | 30d+ |
| KXNASDAQ100Y-26DEC31H1600-B26250 | 26,000 to 26,499.99 | 5c | 2.0c | 1539 | 3175 | 3690 | 5520 | 31848 | $0 | 30d+ |
| KXNASDAQ100POS-26DEC31H1600-T25249.85 | 25,249.86 or above | 60c | 1.0c | 117 | 139 | 2702 | 4688 | 27856 | $33 | 30d+ |
| KXTRUTHSOCIAL-26APR18-B210 | 200-220 | 31c | 1.0c | 27 | 32 | 62 | 52 | 5816 | $3650 | 6-12h |
| KXTRUTHSOCIAL-26APR18-B189 | 180-199 | 66c | 21.0c | 69 | 4 | 0 | 0 | 4575 | $6236 | 6-12h |
| KXSP500ADDQ-26JUL01-SOFI | SoFi | 27c | 9.0c | 9 | 1294 | 9 | 1294 | 4043 | $93 | 30d+ |
| KXSP500ADDQ-26JUL01-MSTR | Strategy (MicroStrategy) | 5c | 7.0c | 1757 | 300 | 2174 | 800 | 3688 | $0 | 30d+ |
| KXSP500ADDQ-26JUL01-CRWV | CoreWeave | 8c | 8.0c | 1150 | 500 | 1670 | 627 | 2424 | $245 | 30d+ |
| KXSP500ADDQ-26JUL01-PSTG | Pure Storage | 11c | 6.0c | 500 | 99 | 500 | 344 | 1965 | $250 | 30d+ |
| KXSP500ADDQ-26JUL01-ALNY | Alnylam Pharmaceuticals | 36c | 5.0c | 5 | 70 | 537 | 100 | 1421 | $631 | 30d+ |
| KXNASDAQ100MAXY-26DEC31H1600-T29499.99 | 29,500 or above | 56c | 86.8c | 492 | 200 | 0 | 0 | 1402 | $0 | 30d+ |
| KXNASDAQ100MAXY-26DEC31H1600-T29999.99 | 30,000 or above | 33c | 6.0c | 51 | 9 | 51 | 9 | 1173 | $13 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNASDAQ100Y | Nasdaq yearly range | annual | 30 | 2 | $1,424 | 1,250,485 | 3.0c |
| KXTRUTHSOCIAL | Number of Trump Truth Social posts this  | weekly | 9 | 3 | $31,146 | 65,370 | 24.3c |
| KXNASDAQ100POS | NASDAQ100 Positive | annual | 1 | 1 | $33 | 27,856 | 1.0c |
| KXNASDAQ100MAXY | Nasdaq max yearly | annual | 17 | 14 | $13 | 26,274 | 48.9c |
| KXNASDAQ100MINY | NASDAQ100 Min | annual | 3 | 0 | $2,045 | 24,704 | nanc |
| KXSP500ADDQ | Companies added to SP500  | one_off | 9 | 4 | $1,215 | 18,594 | 6.7c |
| KXSP500REMOVEQ | Companies removed from SP500 | one_off | 9 | 3 | $6 | 4,808 | 7.0c |
| KXNASDAQ100U | Nasdaq above/below | hourly | 60 | 19 | $2,940 | 3,972 | 29.0c |
| KXNASDAQ100 | Nasdaq range | daily | 60 | 0 | $5,206 | 3,608 | nanc |
| KXTRUMPDELETE | How many Truth Social posts will Trump d | one_off | 1 | 1 | $350 | 627 | 8.0c |

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
