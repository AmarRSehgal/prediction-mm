# ent_tv_reality

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **2** (2 contested)
- Total 24h volume: **$0**
- Total open interest: **833**
- Top-OI mean spread (median across series): **6.5 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **2**
- Median spread: **6.5c**
- Median TOB bid / ask size: **40 / 650** contracts
- Median depth within 5c of best bid / ask — **690 / 650** contracts
- Median depth within 10c of best bid / ask — **1884 / 1050** contracts
- Median depth within 5c of midpoint — bid: **690** / ask: **650** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **15**
- Mean informed-signal proxy: **-2.083** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.29c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 30 | 2.32 | -2.179 | 7.00 | 32.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMEDIAGUESTJAKESHANE-27-JAK | Jake Shane | 20c | 6.0c | 32 | 500 | 532 | 500 | 532 | 500 | 432 | $0 | 30d+ |
| KXMEDIAGUESTERICADAMS-27-ERI | Eric Adams | 12c | 7.0c | 49 | 800 | 849 | 800 | 3235 | 1600 | 401 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMEDIAGUESTJAKESHANE | WILL JAKE SHANE  BE ON DANCING WITH THE  | one_off | 1 | 1 | $0 | 432 | 6.0c |
| KXMEDIAGUESTERICADAMS | WILL ERIC ADAMS BE ON DANCING WITH THE S | one_off | 1 | 1 | $0 | 401 | 7.0c |

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
