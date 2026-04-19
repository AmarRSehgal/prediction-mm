# comm_agri

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **352** (304 contested)
- Total 24h volume: **$41,669**
- Total open interest: **109,444**
- Top-OI mean spread (median across series): **34.2 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **38.0c**
- Median TOB bid / ask size: **20 / 73** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **22**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 881 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 3512 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCOCOAMON-26APR3017-T3367.99 | above $3367.99 | 7c | 6.0c | 5 | 5 | 1365 | 47 | 3724 | $2759 | 7-30d |
| KXSOYBEANMON-26APR3017-T1156.99 | above 1156.99¢ | 76c | 13.0c | 5 | 197 | 0 | 0 | 2956 | $16 | 7-30d |
| KXCOCOAMON-26APR3017-T3267.99 | above $3267.99 | 49c | 6.0c | 5 | 5 | 5 | 5 | 2935 | $3031 | 7-30d |
| KXSUGARMON-26APR3017-T13.89 | above 13.89¢ | 36c | 37.0c | 10 | 10 | 0 | 0 | 2492 | $22 | 7-30d |
| KXCOFFEEMON-26APR3017-T279.99 | above 279.99¢ | 76c | 8.0c | 9 | 254 | 9 | 254 | 2404 | $644 | 7-30d |
| KXSOYBEANMON-26APR3017-T1166.99 | above 1166.99¢ | 55c | 43.0c | 81 | 117 | 0 | 0 | 2369 | $2 | 7-30d |
| KXSOYBEANW-26APR2417-T1175.99 | above 1175.99¢ | 34c | 31.0c | 75 | 2 | 0 | 0 | 2206 | $2317 | 3-7d |
| KXWHEATMON-26APR3017-T634.99 | above 634.99¢ | 20c | 35.0c | 350 | 181 | 0 | 0 | 2020 | $1 | 7-30d |
| KXCORNMON-26APR3017-T455.99 | above 455.99¢ | 40c | 12.0c | 2 | 272 | 0 | 0 | 1915 | $1505 | 7-30d |
| KXSUGARW-26APR2417-T13.49 | above 13.49¢ | 37c | 22.0c | 10 | 10 | 0 | 0 | 1832 | $1852 | 3-7d |
| KXSOYBEANW-26APR2417-T1180.99 | above 1180.99¢ | 38c | 30.0c | 20 | 20 | 0 | 0 | 1799 | $1848 | 3-7d |
| KXSUGARMON-26APR3017-T13.99 | above 13.99¢ | 36c | 43.0c | 1 | 176 | 0 | 0 | 1780 | $15 | 7-30d |
| KXCOFFEEMON-26APR3017-T289.99 | above 289.99¢ | 25c | 18.0c | 2 | 129 | 0 | 0 | 1780 | $1 | 7-30d |
| KXLCATTLEMON-26APR3017-T253.99 | above 253.99¢ | 25c | 33.0c | 5 | 5 | 0 | 0 | 1768 | $1 | 7-30d |
| KXCOFFEEMON-26APR3017-T299.99 | above 299.99¢ | 10c | 3.0c | 10 | 12 | 10 | 12 | 1734 | $31 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCOCOAMON | Cocoa Monthly | monthly | 24 | 13 | $6,448 | 14,345 | 17.7c |
| KXLCATTLEMON | Live Cattle Monthly | monthly | 24 | 19 | $1,325 | 12,811 | 28.3c |
| KXCOFFEEMON | Coffee Monthly | monthly | 20 | 5 | $947 | 12,482 | 9.3c |
| KXSUGARMON | Sugar Monthly | monthly | 24 | 24 | $144 | 12,018 | 43.7c |
| KXCORNMON | Corn Monthly | monthly | 24 | 24 | $4,419 | 11,916 | 13.3c |
| KXWHEATMON | Wheat Monthly | monthly | 24 | 23 | $570 | 9,791 | 35.3c |
| KXSOYBEANMON | Soybean monthly | monthly | 20 | 17 | $65 | 9,016 | 32.0c |
| KXCORNW | Corn Weekly | weekly | 40 | 33 | $7,195 | 6,903 | 47.7c |
| KXSOYBEANW | Soybean Weekly | weekly | 30 | 25 | $5,808 | 6,325 | 33.0c |
| KXCOFFEEW | Weekly Coffee Price | weekly | 24 | 24 | $4,056 | 3,919 | 38.0c |

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
