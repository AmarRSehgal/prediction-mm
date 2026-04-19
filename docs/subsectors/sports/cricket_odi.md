# sports_cricket_odi

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **2** (2 contested)
- Total 24h volume: **$5,457**
- Total open interest: **7,638**
- Top-OI mean spread (median across series): **9.0 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **2**
- Median spread: **9.0c**
- Median TOB bid / ask size: **20 / 26** contracts
- Median depth within 5c of best bid / ask — **10569 / 13684** contracts
- Median depth within 10c of best bid / ask — **10639 / 28754** contracts
- Median depth within 5c of midpoint — bid: **20** / ask: **26** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **85**
- Mean informed-signal proxy: **-3.111** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **5.45c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 170 | 4.78 | -2.077 | 19.65 | 45.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCRICKETODIMATCH-26APR20NZBAN-NZ | New Zealand | 44c | 9.0c | 3 | 15 | 10101 | 20163 | 10241 | 30163 | 4926 | $3081 | 3-7d |
| KXCRICKETODIMATCH-26APR20NZBAN-BAN | Bangladesh | 56c | 9.0c | 36 | 36 | 11037 | 7206 | 11037 | 27346 | 2712 | $2375 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCRICKETODIMATCH | New Zealand | nan | 2 | 2 | $5,457 | 7,638 | 9.0c |

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
