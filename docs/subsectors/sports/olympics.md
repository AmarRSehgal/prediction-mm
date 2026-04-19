# sports_olympics

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **2** (2 contested)
- Total 24h volume: **$439**
- Total open interest: **6,728**
- Top-OI mean spread (median across series): **7.5 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **2**
- Median spread: **7.5c**
- Median TOB bid / ask size: **257 / 264** contracts
- Median depth within 5c of best bid / ask — **842 / 780** contracts
- Median depth within 10c of best bid / ask — **2007 / 780** contracts
- Median depth within 5c of midpoint — bid: **764** / ask: **280** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **190**
- Mean informed-signal proxy: **-1.721** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.38c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 381 | 1.91 | -1.074 | 7.00 | 20.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AMAZONFTC-29DEC31 | Government wins | 58c | 6.0c | 14 | 29 | 1183 | 1061 | 1183 | 1061 | 5882 | $64 | 30d+ |
| KXSORONDO-28 | Yes | 14c | 9.0c | 500 | 500 | 500 | 500 | 2831 | 500 | 846 | $375 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXAMAZONFTC | Courts consider Amazon a monopoly | custom | 1 | 1 | $64 | 5,882 | 6.0c |
| KXSORONDO | Rajon Rando Summer Olympics Flag Footbal | one_off | 1 | 1 | $375 | 846 | 9.0c |

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
