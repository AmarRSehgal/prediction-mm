# pol_events

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **8** (6 contested)
- Total 24h volume: **$14,003**
- Total open interest: **1,144,442**
- Top-OI mean spread (median across series): **2.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **2.0c**
- Median TOB bid / ask size: **884 / 1351** contracts
- Median depth within 5c of best bid / ask — **10871 / 5720** contracts
- Median depth within 10c of best bid / ask — **11383 / 5720** contracts
- Median depth within 5c of midpoint — bid: **10529** / ask: **5720** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **637**
- Mean informed-signal proxy: **-0.645** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 3822 | 0.96 | -0.442 | 4.00 | 57.5 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIMPEACH-27-JAN01 | Before Jan 1, 2027 | 12c | 2.0c | 1143 | 832 | 12686 | 10159 | 99984 | 15647 | 398033 | $5530 | 30d+ |
| KXIMPEACH-28-JAN01 | Before Jan 1, 2028 | 66c | 2.0c | 590 | 1870 | 11117 | 8938 | 11141 | 10330 | 168574 | $2031 | 30d+ |
| KXIMPEACH-29-JAN20 | Before Jan 20, 2029 | 70c | 3.0c | 42 | 47 | 6417 | 4930 | 6417 | 5473 | 68435 | $360 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-27 | Before 2027 | 32c | 5.0c | 625 | 9 | 2106 | 1764 | 2136 | 1828 | 27265 | $201 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-28 | Before 2028 | 40c | 1.0c | 10124 | 4176 | 10624 | 5676 | 11624 | 5676 | 242 | $2 | 30d+ |
| KXCALLIMPEACHRCONGRESS-26-29JAN20 | Before Jan 20, 2029 | 50c | 1.0c | 13049 | 4263 | 14549 | 5763 | 14549 | 5763 | 98 | $6 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIMPEACH | President impeached | custom | 4 | 3 | $13,794 | 1,116,323 | 2.3c |
| KXCALLIMPEACHRCONGRESS | Republican Congressman impeachment | custom | 3 | 3 | $209 | 27,606 | 2.3c |
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
