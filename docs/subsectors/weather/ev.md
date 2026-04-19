# climate_ev

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **4** (4 contested)
- Total 24h volume: **$3**
- Total open interest: **11,281**
- Top-OI mean spread (median across series): **4.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **4**
- Median spread: **4.0c**
- Median TOB bid / ask size: **134 / 68** contracts
- Median depth within 5c of best bid / ask — **647 / 568** contracts
- Median depth within 10c of best bid / ask — **734 / 848** contracts
- Median depth within 5c of midpoint — bid: **446** / ask: **510** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **125**
- Mean informed-signal proxy: **-1.423** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.40c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 499 | 2.44 | -1.444 | 7.00 | 23.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| EVSHARE-30JAN-50 | Above 50% | 23c | 4.0c | 169 | 500 | 245 | 1081 | 775 | 1081 | 4084 | $0 | 30d+ |
| EVSHARE-30JAN-20 | Above 20% | 60c | 5.0c | 11 | 20 | 1237 | 520 | 1237 | 614 | 3557 | $2 | 30d+ |
| EVSHARE-30JAN-30 | Above 30%:: Expectation | 39c | 4.0c | 194 | 2 | 694 | 510 | 694 | 510 | 3290 | $1 | 30d+ |
| EVSHARE-30JAN-10 | Above 10% | 86c | 3.0c | 100 | 115 | 600 | 615 | 600 | 3051 | 350 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXEVSHARE | Above 50% | nan | 4 | 4 | $3 | 11,281 | 4.3c |

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
