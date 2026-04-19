# sports_darts

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **8** (4 contested)
- Total 24h volume: **$915**
- Total open interest: **10,282**
- Top-OI mean spread (median across series): **43.3 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **20.0c**
- Median TOB bid / ask size: **169 / 79** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **24** / ask: **258** contracts
- Mean trades per market (last 3000): **82**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 494 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPREMDARTS-26-LLIT | Luke Littler | 51c | 6.0c | 44 | 4 | 49 | 227 | 1900 | $199 | 30d+ |
| KXPREMDARTS-26-LHUM | Luke Humphries | 8c | 8.0c | 943 | 168 | 1183 | 468 | 1891 | $57 | 30d+ |
| KXPREMDARTS-26-JCLA | Jonny Clayton | 37c | 45.0c | 10 | 319 | 0 | 0 | 1446 | $62 | 30d+ |
| KXPREMDARTS-26-MVAN | Michael van Gerwen | 8c | 11.0c | 293 | 146 | 0 | 0 | 1172 | $57 | 30d+ |
| KXPREMDARTS-26-GVAN | Gian van Veen | 16c | 30.0c | 1283 | 12 | 0 | 0 | 1009 | $57 | 30d+ |
| KXPREMDARTS-26-GPRI | Gerwyn Price | 24c | 29.0c | 10 | 12 | 0 | 0 | 552 | $57 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPREMDARTS | Premier League Darts Champion | annual | 8 | 4 | $915 | 10,282 | 43.3c |

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
