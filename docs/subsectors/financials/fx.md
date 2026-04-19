# fin_fx

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **40** (5 contested)
- Total 24h volume: **$306**
- Total open interest: **15,895**
- Top-OI mean spread (median across series): **57.0 cents**
- **MM profile: Wide but dead**

## Book depth (from comprehensive scan)

- Markets sampled: **5**
- Median spread: **68.0c**
- Median TOB bid / ask size: **1000 / 11** contracts
- Median depth within 5c of best bid / ask — **1000 / 79** contracts
- Median depth within 10c of best bid / ask — **2078 / 79** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **67**
- Mean informed-signal proxy: **-10.945** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **16.35c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 333 | 12.86 | -6.851 | 60.00 | 681.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXUSDBRLMAX-26DEC31-T5.9999 | 6 or above | 39c | 63.0c | 86 | 1 | 167 | 1 | 2078 | 1 | 6754 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T5.4999 | 5.5 or above | 43c | 68.0c | 99 | 18 | 478 | 79 | 5210 | 79 | 1658 | $4 | 30d+ |
| KXUSDBRLMAX-26DEC31-T6.7499 | 6.75 or above | 21c | 40.0c | 1000 | 2 | 1000 | 3 | 1000 | 3 | 1205 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T5.7499 | 5.75 or above | 48c | 90.0c | 1500 | 11 | 4180 | 312 | 4180 | 3096 | 1192 | $0 | 30d+ |
| KXUSDBRLMAX-26DEC31-T6.4999 | 6.5 or above | 44c | 87.0c | 1000 | 50 | 1000 | 260 | 1000 | 2496 | 818 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXUSDBRLMAX | USD/BRL max | annual | 10 | 5 | $4 | 13,013 | 57.0c |
| KXUSDJPY | USD/JPY daily range | daily | 15 | 0 | $156 | 2,684 | nanc |
| KXEURUSD | EUR/USD daily range | daily | 15 | 0 | $147 | 199 | nanc |

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
