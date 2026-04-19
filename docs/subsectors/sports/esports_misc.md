# sports_esports_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **1** (1 contested)
- Total 24h volume: **$0**
- Total open interest: **2,291**
- Top-OI mean spread (median across series): **8.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **1**
- Median spread: **8.0c**
- Median TOB bid / ask size: **105 / 100** contracts
- Median depth within 5c of best bid / ask — **455 / 301** contracts
- Median depth within 10c of best bid / ask — **455 / 301** contracts
- Median depth within 5c of midpoint — bid: **105** / ask: **301** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **104**
- Mean informed-signal proxy: **-0.272** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.54c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 104 | 0.52 | -0.291 | 2.00 | 17.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXNEWCITY-29 | Before 2029 | 39c | 8.0c | 105 | 100 | 455 | 301 | 455 | 301 | 2291 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNEWCITY | Before 2029 | nan | 1 | 1 | $0 | 2,291 | 8.0c |

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
