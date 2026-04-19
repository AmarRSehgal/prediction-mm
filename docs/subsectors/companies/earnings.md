# companies_earnings

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **29** (29 with open markets)
- Open markets: **366** (343 contested)
- Total 24h volume: **$21,592**
- Total open interest: **71,508**
- Top-OI mean spread (median across series): **8.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **6.0c**
- Median TOB bid / ask size: **5 / 30** contracts
- Median depth within 5c of best bid / ask — **196 / 280** contracts
- Median depth within 10c of best bid / ask — **294 / 662** contracts
- Median depth within 5c of midpoint — bid: **17** / ask: **50** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **15**
- Mean informed-signal proxy: **-1.226** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.80c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 2957 | 4.76 | -0.263 | 18.00 | 39.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXDATASET13-26SEP01 | Before September | 19c | 4.0c | 5 | 5 | 305 | 357 | 420 | 357 | 5805 | $103 | 30d+ |
| KXDATASET13-27JAN01 | Before 2027 | 21c | 1.0c | 38 | 109 | 38 | 309 | 370 | 1171 | 4701 | $4 | 30d+ |
| KXEARNINGSMENTIONPG-26APR24-REVE | Revenue | 32c | 10.0c | 5 | 45 | 752 | 195 | 1397 | 586 | 4645 | $2438 | 30d+ |
| KXEARNINGSMENTIONRDDT-26APR30-EMPL | Emplifi | 36c | 15.0c | 5 | 5 | 171 | 346 | 171 | 346 | 1793 | $1793 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-BUYB | Buyback | 56c | 3.0c | 3 | 21 | 172 | 157 | 172 | 307 | 1484 | $348 | 30d+ |
| KXEARNINGSMENTIONINTC-26APR23-DIVI | Dividend | 30c | 4.0c | 5 | 81 | 195 | 281 | 200 | 810 | 1411 | $208 | 30d+ |
| KXEARNINGSMENTIONUAL-26APR22-AMER | American Airlines | 40c | 1.0c | 30 | 269 | 330 | 758 | 330 | 1240 | 1408 | $173 | 30d+ |
| KXEARNINGSMENTIONTSLA-26APR22-SCHG | Supercharger / Super Charger | 38c | 7.0c | 5 | 29 | 5 | 473 | 687 | 692 | 1402 | $547 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-HIPP | Hippo | 29c | 1.0c | 20 | 3 | 170 | 3 | 831 | 82 | 1231 | $10 | 30d+ |
| KXEARNINGSMENTIONTSLA-26APR22-CYBR | Cybertruck | 68c | 4.0c | 4 | 16 | 204 | 1166 | 204 | 1166 | 1225 | $4 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-MA | M&A / Acquisition | 92c | 1.0c | 14 | 10 | 614 | 346 | 614 | 2598 | 1159 | $0 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-CATA | Catastrophe | 70c | 1.0c | 15 | 64 | 28 | 143 | 178 | 243 | 1138 | $13 | 30d+ |
| KXEPSTEINLIST-27JAN-DJT | Donald Trump | 72c | 1.0c | 1438 | 409 | 4740 | 3088 | 7740 | 3088 | 1105 | $0 | 30d+ |
| KXEARNINGSMENTIONUAL-26APR22-NONS | Nonstop / Non-Stop | 22c | 2.0c | 16 | 5 | 509 | 585 | 509 | 661 | 1073 | $152 | 30d+ |
| KXEARNINGSMENTIONPGR-26APR15-PET | Pet Insurance | 56c | 6.0c | 5 | 16 | 155 | 304 | 155 | 404 | 1068 | $54 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXDATASET13 | Will the DOJ release Data Set 13 (Epstei | one_off | 2 | 2 | $107 | 10,506 | 2.5c |
| KXEARNINGSMENTIONUAL | United Airlines Earnings Mention | one_off | 17 | 17 | $1,368 | 7,677 | 3.3c |
| KXEARNINGSMENTIONPGR | Progressive Earnings Call | one_off | 10 | 9 | $439 | 7,609 | 1.7c |
| KXEARNINGSMENTIONPG | Proctor & Gamble Earnings | one_off | 13 | 11 | $3,047 | 6,416 | 8.0c |
| KXEARNINGSMENTIONTSLA | Tesla earnings mention | one_off | 17 | 12 | $2,908 | 6,120 | 5.7c |
| KXEARNINGSMENTIONINTC | Intel Earnings Call | one_off | 15 | 14 | $1,722 | 4,563 | 10.3c |
| KXEARNINGSMENTIONALK | Alaska Airlines Earnings | one_off | 13 | 12 | $1,540 | 4,175 | 6.7c |
| KXEARNINGSMENTIONBA | Boeing Earnings Call | one_off | 11 | 11 | $1,627 | 3,750 | 7.0c |
| KXEARNINGSMENTIONRDDT | Reddit Earnings | one_off | 13 | 13 | $2,396 | 2,891 | 14.0c |
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
