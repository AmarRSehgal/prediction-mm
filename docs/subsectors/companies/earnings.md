# companies_earnings

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **29** (29 with open markets)
- Open markets: **366** (344 contested)
- Total 24h volume: **$21,883**
- Total open interest: **69,714**
- Top-OI mean spread (median across series): **9.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **5 / 30** contracts
- Median cumulative depth within 5c of mid — bid: **15** / ask: **50** contracts
- Median cumulative depth within 10c of mid — bid: **171** / ask: **350** contracts
- Mean trades per market (last 3000): **15**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 2910 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXDATASET13-26SEP01 | Before September | 20c | 6.0c | 5 | 5 | 105 | 305 | 5870 | $6 | 30d+ |
| KXDATASET13-27JAN01 | Before 2027 | 21c | 1.0c | 38 | 109 | 38 | 309 | 4701 | $4 | 30d+ |
| KXEARNINGSMENTIONPG-26APR24-REVE | Revenue | 40c | 7.0c | 5 | 28 | 5 | 93 | 4602 | $1978 | 30d+ |
| KXEARNINGSMENTIONRDDT-26APR30-EMPL | Emplifi | 35c | 14.0c | 16 | 24 | 0 | 0 | 1793 | $1793 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-BUYB | Buyback | 56c | 3.0c | 3 | 21 | 172 | 157 | 1484 | $348 | 30d+ |
| KXEARNINGSMENTIONUAL-26APR22-AMER | American Airlines | 40c | 1.0c | 30 | 269 | 51 | 755 | 1408 | $586 | 30d+ |
| KXEARNINGSMENTIONINTC-26APR23-DIVI | Dividend | 30c | 4.0c | 5 | 31 | 195 | 231 | 1402 | $213 | 30d+ |
| KXEARNINGSMENTIONTSLA-26APR22-SCHG | Supercharger / Super Charger | 38c | 7.0c | 5 | 31 | 5 | 81 | 1400 | $556 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-HIPP | Hippo | 29c | 1.0c | 20 | 3 | 170 | 3 | 1231 | $10 | 30d+ |
| KXEARNINGSMENTIONTSLA-26APR22-CYBR | Cybertruck | 68c | 4.0c | 4 | 16 | 69 | 866 | 1225 | $4 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-MA | M&A / Acquisition | 92c | 1.0c | 14 | 10 | 614 | 296 | 1159 | $0 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-CATA | Catastrophe | 70c | 1.0c | 15 | 64 | 15 | 93 | 1138 | $13 | 30d+ |
| KXEPSTEINLIST-27JAN-DJT | Donald Trump | 72c | 1.0c | 1439 | 409 | 1941 | 3088 | 1105 | $0 | 30d+ |
| KXEARNINGSMENTIONUAL-26APR22-NONS | Nonstop / Non-Stop | 22c | 2.0c | 16 | 5 | 509 | 585 | 1073 | $152 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-PET | Pet Insurance | 56c | 6.0c | 5 | 25 | 155 | 264 | 1068 | $45 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXDATASET13 | Will the DOJ release Data Set 13 (Epstei | one_off | 2 | 2 | $10 | 10,571 | 3.0c |
| KXEARNINGSMENTIONUAL | United Airlines Earnings Mention | one_off | 17 | 17 | $2,146 | 7,654 | 4.0c |
| KXEARNINGSMENTIONPGR | Progressive Earnings Call | one_off | 10 | 9 | $439 | 7,609 | 1.7c |
| KXEARNINGSMENTIONPG | Proctor & Gamble Earnings | one_off | 13 | 12 | $2,699 | 6,315 | 9.0c |
| KXEARNINGSMENTIONTSLA | Tesla earnings mention | one_off | 17 | 12 | $2,930 | 5,995 | 5.7c |
| KXEARNINGSMENTIONINTC | Intel Earnings Call | one_off | 15 | 14 | $1,072 | 4,554 | 13.3c |
| KXEARNINGSMENTIONBA | Boeing Earnings Call | one_off | 11 | 11 | $1,988 | 3,707 | 9.3c |
| KXEARNINGSMENTIONALK | Alaska Airlines Earnings | one_off | 13 | 12 | $543 | 3,110 | 6.3c |
| KXEARNINGSMENTIONRDDT | Reddit Earnings | one_off | 13 | 13 | $2,389 | 2,884 | 15.0c |
| KXEPSTEINLIST | Epstein list | custom | 18 | 18 | $7 | 2,355 | 1.3c |

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
