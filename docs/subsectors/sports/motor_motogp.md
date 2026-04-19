# sports_motor_motogp

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **5** (5 contested)
- Total 24h volume: **$0**
- Total open interest: **4,062**
- Top-OI mean spread (median across series): **7.4 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **5**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 126** contracts
- Median depth within 5c of best bid / ask — **375 / 376** contracts
- Median depth within 10c of best bid / ask — **375 / 376** contracts
- Median depth within 5c of midpoint — bid: **125** / ask: **370** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **49**
- Mean informed-signal proxy: **-1.380** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.68c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 245 | 3.85 | -1.100 | 17.00 | 23.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMOTOGP-26-MAMA | Marc Marquez | 26c | 7.0c | 125 | 5 | 375 | 380 | 375 | 380 | 1674 | $0 | 30d+ |
| KXMOTOGPTEAMS-26-APRI | Aprilia Racing | 83c | 8.0c | 1 | 175 | 226 | 325 | 226 | 367 | 1168 | $0 | 30d+ |
| KXMOTOGP-26-JOMA | Jorge Martin | 14c | 7.0c | 100 | 126 | 475 | 376 | 1928 | 376 | 1000 | $0 | 30d+ |
| KXMOTOGP-26-MABE | Marco Bezzecchi | 55c | 8.0c | 125 | 126 | 375 | 376 | 375 | 376 | 165 | $0 | 30d+ |
| KXMOTOGPTEAMS-26-DUCA | Ducati Lenovo Team | 12c | 7.0c | 75 | 295 | 225 | 520 | 838 | 520 | 55 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXMOTOGP | Marc Marquez | nan | 3 | 3 | $0 | 2,839 | 7.3c |
| KXMOTOGPTEAMS | Aprilia Racing | nan | 2 | 2 | $0 | 1,223 | 7.5c |

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
