# sports_cricket_t20_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **7** (7 contested)
- Total 24h volume: **$1,860**
- Total open interest: **1,726**
- Top-OI mean spread (median across series): **47.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **7**
- Median spread: **66.0c**
- Median TOB bid / ask size: **10 / 19** contracts
- Median depth within 5c of best bid / ask — **886 / 113** contracts
- Median depth within 10c of best bid / ask — **886 / 239** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **11**
- Mean informed-signal proxy: **0.446** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.38c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 63 | 4.08 | 1.242 | 9.00 | 27.7 |
| 3-7d | 16 | 1.00 | 0.818 | 5.50 | 7.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXT20MATCH-26APR18SCOJER-SCO | Scotland A | 74c | 49.0c | 0 | 5 | 1000 | 5 | 1000 | 5 | 1650 | $1784 | 1-3d |
| KXT20MATCH-26APR19SCOJER-SCO | Scotland A | 49c | 66.0c | 113 | 515 | 132 | 515 | 132 | 642 | 59 | $59 | 3-7d |
| KXT20MATCH-26APR20UAENEP-UAE | United Arab Emirates | 35c | 28.0c | 10 | 2 | 3010 | 502 | 3011 | 902 | 8 | $8 | 3-7d |
| KXT20MATCH-26APR19SCOJER-JER | Jersey | 45c | 74.0c | 300 | 113 | 1077 | 113 | 4670 | 239 | 6 | $6 | 3-7d |
| KXT20MATCH-26APR20UAENEP-NEP | Nepal | 63c | 18.0c | 9 | 500 | 9 | 3000 | 9 | 4596 | 4 | $4 | 3-7d |
| KXT20MATCH-26APR21UAENEP-UAE | United Arab Emirates | 43c | 79.0c | 10 | 19 | 886 | 19 | 886 | 145 | 0 | $0 | 3-7d |
| KXT20MATCH-26APR21UAENEP-NEP | Nepal | 43c | 79.0c | 10 | 19 | 886 | 19 | 886 | 145 | 0 | $0 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXT20MATCH | Scotland A | nan | 7 | 7 | $1,860 | 1,726 | 47.7c |

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
