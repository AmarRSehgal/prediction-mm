# sports_olympics

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **2** (2 contested)
- Total 24h volume: **$278**
- Total open interest: **6,589**
- Top-OI mean spread (median across series): **7.0 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **2**
- Median spread: **7.0c**
- Median TOB bid / ask size: **260 / 266** contracts
- Median cumulative depth within 5c of mid — bid: **766** / ask: **282** contracts
- Median cumulative depth within 10c of mid — bid: **844** / ask: **782** contracts
- Mean trades per market (last 3000): **190**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 380 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AMAZONFTC-29DEC31 | Government wins | 58c | 6.0c | 19 | 31 | 1033 | 63 | 5882 | $64 | 30d+ |
| KXSORONDO-28 | Yes | 14c | 8.0c | 500 | 500 | 500 | 500 | 846 | $353 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXAMAZONFTC | Courts consider Amazon a monopoly | custom | 1 | 1 | $64 | 5,882 | 6.0c |
| KXSORONDO | Rajon Rando Summer Olympics Flag Footbal | one_off | 1 | 1 | $214 | 707 | 8.0c |

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
