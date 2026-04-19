# eco_realestate_retail

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **16** (5 contested)
- Total 24h volume: **$745**
- Total open interest: **52,476**
- Top-OI mean spread (median across series): **4.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **8**
- Median spread: **7.0c**
- Median TOB bid / ask size: **250 / 254** contracts
- Median depth within 5c of best bid / ask — **255 / 362** contracts
- Median depth within 10c of best bid / ask — **274 / 362** contracts
- Median depth within 5c of midpoint — bid: **251** / ask: **313** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **258**
- Mean informed-signal proxy: **-0.271** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.66c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 831 | 2.52 | -0.242 | 10.00 | 18.3 |
| 30d+ | 1233 | 1.82 | -0.174 | 7.00 | 84.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXHFHOUSING-27 | Before Jan 1, 2027 | 64c | 1.0c | 5976 | 388 | 5976 | 1138 | 7127 | 1148 | 29442 | $84 | 30d+ |
| KXHOUSINGSTART-26APR17-T1.325 | Above 1.325M | 70c | 9.0c | 259 | 272 | 259 | 272 | 259 | 272 | 10173 | $507 | 7-30d |
| KXBUILDPERMS-26APR17-T1.400 | Above 1.400M | 8c | 6.0c | 1 | 351 | 885 | 351 | 885 | 351 | 2924 | $38 | 7-30d |
| KXBUILDPERMS-26APR17-T1.350 | Above 1.350M | 37c | 4.0c | 1 | 24 | 251 | 274 | 251 | 274 | 2683 | $3 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.375 | Above 1.375M | 12c | 8.0c | 251 | 122 | 251 | 372 | 884 | 372 | 2606 | $0 | 7-30d |
| KXBUILDPERMS-26APR17-T1.300 | Above 1.300M | 94c | 3.0c | 1 | 250 | 1 | 878 | 251 | 878 | 1279 | $73 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.350 | Above 1.350M | 32c | 9.0c | 272 | 259 | 272 | 260 | 288 | 260 | 738 | $0 | 7-30d |
| KXHOUSINGSTART-26APR17-T1.400 | Above 1.400M | 6c | 8.0c | 250 | 142 | 250 | 392 | 250 | 392 | 618 | $40 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXHFHOUSING | Bill taxing/banning hedge funds owning s | custom | 1 | 1 | $84 | 29,442 | 1.0c |
| KXHOUSINGSTART | Monthly housing starts | custom | 8 | 3 | $547 | 15,328 | 8.7c |
| KXBUILDPERMS | Building permits for month | custom | 7 | 1 | $114 | 7,706 | 4.0c |

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
