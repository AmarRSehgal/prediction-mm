# comm_agri

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **352** (308 contested)
- Total 24h volume: **$35,669**
- Total open interest: **109,585**
- Top-OI mean spread (median across series): **33.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **37.0c**
- Median TOB bid / ask size: **71 / 76** contracts
- Median depth within 5c of best bid / ask — **91 / 100** contracts
- Median depth within 10c of best bid / ask — **96 / 251** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **22**
- Mean informed-signal proxy: **-1.069** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **6.41c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 903 | 5.38 | -1.224 | 29.00 | 37.4 |
| 7-30d | 3590 | 5.74 | -0.449 | 27.00 | 35.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCOCOAMON-26APR3017-T3367.99 | above $3367.99 | 7c | 6.0c | 5 | 5 | 2162 | 47 | 2162 | 47 | 3724 | $2459 | 7-30d |
| KXSOYBEANMON-26APR3017-T1156.99 | above 1156.99¢ | 74c | 11.0c | 5 | 120 | 5 | 281 | 5 | 325 | 2956 | $16 | 7-30d |
| KXCOCOAMON-26APR3017-T3267.99 | above $3267.99 | 49c | 6.0c | 5 | 5 | 44 | 5 | 54 | 116 | 2935 | $2825 | 7-30d |
| KXSUGARMON-26APR3017-T13.89 | above 13.89¢ | 34c | 29.0c | 5 | 10 | 95 | 363 | 715 | 660 | 2492 | $22 | 7-30d |
| KXCOFFEEMON-26APR3017-T279.99 | above 279.99¢ | 76c | 8.0c | 9 | 254 | 9 | 254 | 9 | 414 | 2404 | $402 | 7-30d |
| KXSOYBEANMON-26APR3017-T1166.99 | above 1166.99¢ | 55c | 42.0c | 81 | 96 | 81 | 96 | 472 | 96 | 2369 | $2 | 7-30d |
| KXSOYBEANW-26APR2417-T1175.99 | above 1175.99¢ | 41c | 50.0c | 96 | 2 | 417 | 3 | 1778 | 89 | 2206 | $2175 | 3-7d |
| KXWHEATMON-26APR3017-T634.99 | above 634.99¢ | 20c | 35.0c | 350 | 191 | 1152 | 794 | 1152 | 794 | 2021 | $3 | 7-30d |
| KXCORNMON-26APR3017-T455.99 | above 455.99¢ | 45c | 21.0c | 2 | 199 | 2 | 351 | 229 | 351 | 1915 | $1505 | 7-30d |
| KXSUGARW-26APR2417-T13.49 | above 13.49¢ | 36c | 21.0c | 4 | 44 | 105 | 565 | 321 | 666 | 1832 | $1746 | 3-7d |
| KXSOYBEANW-26APR2417-T1180.99 | above 1180.99¢ | 36c | 36.0c | 8 | 77 | 89 | 744 | 1487 | 744 | 1803 | $1770 | 3-7d |
| KXSUGARMON-26APR3017-T13.99 | above 13.99¢ | 35c | 42.0c | 1 | 101 | 1 | 277 | 1012 | 277 | 1780 | $15 | 7-30d |
| KXCOFFEEMON-26APR3017-T289.99 | above 289.99¢ | 25c | 18.0c | 2 | 129 | 98 | 354 | 793 | 354 | 1780 | $1 | 7-30d |
| KXLCATTLEMON-26APR3017-T253.99 | above 253.99¢ | 22c | 27.0c | 5 | 5 | 1137 | 203 | 1137 | 304 | 1768 | $1 | 7-30d |
| KXCOFFEEMON-26APR3017-T299.99 | above 299.99¢ | 16c | 15.0c | 30 | 12 | 30 | 28 | 1187 | 28 | 1734 | $11 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCOCOAMON | Cocoa Monthly | monthly | 24 | 13 | $5,953 | 14,345 | 16.7c |
| KXLCATTLEMON | Live Cattle Monthly | monthly | 24 | 19 | $795 | 12,811 | 28.0c |
| KXCOFFEEMON | Coffee Monthly | monthly | 20 | 8 | $447 | 12,484 | 13.7c |
| KXSUGARMON | Sugar Monthly | monthly | 24 | 24 | $164 | 12,017 | 40.7c |
| KXCORNMON | Corn Monthly | monthly | 24 | 24 | $4,417 | 11,916 | 17.0c |
| KXWHEATMON | Wheat Monthly | monthly | 24 | 23 | $581 | 9,812 | 36.3c |
| KXSOYBEANMON | Soybean monthly | monthly | 20 | 17 | $54 | 9,016 | 31.3c |
| KXCORNW | Corn Weekly | weekly | 40 | 33 | $6,141 | 6,980 | 45.7c |
| KXSOYBEANW | Soybean Weekly | weekly | 30 | 26 | $5,363 | 6,369 | 40.3c |
| KXCOFFEEW | Weekly Coffee Price | weekly | 24 | 24 | $1,629 | 3,919 | 36.3c |

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
