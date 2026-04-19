# sports_darts

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **8** (4 contested)
- Total 24h volume: **$888**
- Total open interest: **10,282**
- Top-OI mean spread (median across series): **34.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **25.5c**
- Median TOB bid / ask size: **557 / 200** contracts
- Median depth within 5c of best bid / ask — **957 / 392** contracts
- Median depth within 10c of best bid / ask — **1070 / 420** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **82**
- Mean informed-signal proxy: **-1.640** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.04c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 494 | 4.55 | -2.336 | 17.00 | 22.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPREMDARTS-26-LLIT | Luke Littler | 48c | 13.0c | 5 | 8 | 484 | 384 | 484 | 784 | 1900 | $199 | 30d+ |
| KXPREMDARTS-26-LHUM | Luke Humphries | 8c | 8.0c | 943 | 94 | 1183 | 441 | 1183 | 441 | 1891 | $57 | 30d+ |
| KXPREMDARTS-26-JCLA | Jonny Clayton | 32c | 39.0c | 5 | 254 | 957 | 254 | 1182 | 254 | 1446 | $62 | 30d+ |
| KXPREMDARTS-26-MVAN | Michael van Gerwen | 8c | 11.0c | 293 | 146 | 293 | 659 | 293 | 659 | 1172 | $57 | 30d+ |
| KXPREMDARTS-26-GVAN | Gian van Veen | 26c | 50.0c | 1283 | 400 | 1283 | 400 | 1283 | 400 | 1009 | $57 | 30d+ |
| KXPREMDARTS-26-GPRI | Gerwyn Price | 28c | 38.0c | 820 | 274 | 957 | 275 | 957 | 276 | 552 | $57 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPREMDARTS | Premier League Darts Champion | annual | 8 | 4 | $888 | 10,282 | 34.3c |

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
