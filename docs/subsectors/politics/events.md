# pol_events

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **8** (6 contested)
- Total 24h volume: **$14,832**
- Total open interest: **1,143,712**
- Top-OI mean spread (median across series): **2.2 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **1.5c**
- Median TOB bid / ask size: **2058 / 1485** contracts
- Median cumulative depth within 5c of mid — bid: **11243** / ask: **5720** contracts
- Median cumulative depth within 10c of mid — bid: **12845** / ask: **5720** contracts
- Mean trades per market (last 3000): **1313**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 7876 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIMPEACH-27-JAN01 | Before Jan 1, 2027 | 12c | 2.0c | 1143 | 1100 | 11861 | 7430 | 397888 | $5848 | 30d+ |
| KXIMPEACH-28-JAN01 | Before Jan 1, 2028 | 66c | 1.0c | 2972 | 1870 | 13377 | 8744 | 168525 | $2092 | 30d+ |
| KXIMPEACH-29-JAN20 | Before Jan 20, 2029 | 70c | 3.0c | 42 | 47 | 3914 | 2513 | 68435 | $1021 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-27 | Before 2027 | 34c | 5.0c | 9 | 524 | 944 | 1754 | 27265 | $302 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-28 | Before 2028 | 40c | 1.0c | 10124 | 4176 | 10624 | 5676 | 242 | $2 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-29JAN20 | Before Jan 20, 2029 | 50c | 1.0c | 13049 | 4263 | 13549 | 5763 | 98 | $6 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIMPEACH | President impeached | custom | 4 | 3 | $14,523 | 1,115,593 | 2.0c |
| KXCALLIMPEACHRCONGRESS | Republican Congressman impeachment | custom | 3 | 3 | $310 | 27,606 | 2.3c |
| KXPERUIMPEACH | Will José María Balcázar be impeached? | one_off | 1 | 0 | $0 | 513 | nanc |

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
