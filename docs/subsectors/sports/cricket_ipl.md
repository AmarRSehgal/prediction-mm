# sports_cricket_ipl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **22** (22 contested)
- Total 24h volume: **$1,412,802**
- Total open interest: **1,463,750**
- Top-OI mean spread (median across series): **1.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **22**
- Median spread: **4.5c**
- Median TOB bid / ask size: **50 / 532** contracts
- Median depth within 5c of best bid / ask — **204 / 2668** contracts
- Median depth within 10c of best bid / ask — **304 / 3788** contracts
- Median depth within 5c of midpoint — bid: **66** / ask: **569** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **212**
- Mean informed-signal proxy: **-1.128** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.86c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 3-7d | 3973 | 0.25 | -0.126 | 1.00 | 278.3 |
| 7-30d | 702 | 2.54 | -1.343 | 11.00 | 25.2 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIPLGAME-26APR19RRKKR-RR | Rajasthan Royals | 62c | 1.0c | 10201 | 6624 | 18362 | 176071 | 20562 | 176951 | 712015 | $705368 | 3-7d |
| KXIPLGAME-26APR19RRKKR-KKR | Kolkata Knight Riders | 40c | 1.0c | 4281 | 57131 | 97866 | 74936 | 98011 | 75976 | 399053 | $403323 | 3-7d |
| KXIPLGAME-26APR19LSGPBKS-PBKS | Punjab Kings | 64c | 1.0c | 1214 | 135767 | 109574 | 286107 | 109894 | 286907 | 210195 | $178798 | 3-7d |
| KXIPLGAME-26APR19LSGPBKS-LSG | Lucknow Super Giants | 38c | 1.0c | 99812 | 133033 | 99907 | 233680 | 100042 | 234070 | 103275 | $101515 | 3-7d |
| KXIPLGAME-26APR20MIGT-MI | Mumbai Indians | 53c | 2.0c | 142 | 757 | 1776 | 7970 | 11786 | 28170 | 12236 | $7587 | 3-7d |
| KXIPLGAME-26APR20MIGT-GT | Gujarat Titans | 48c | 1.0c | 166 | 507 | 7045 | 3149 | 12045 | 23649 | 9824 | $6618 | 3-7d |
| KXIPLGAME-26APR21DCSRH-SRH | Sunrisers Hyderabad | 55c | 3.0c | 43 | 2 | 79 | 2717 | 99 | 3817 | 3952 | $1765 | 3-7d |
| KXIPLGAME-26APR21DCSRH-DC | Delhi Capitals | 48c | 3.0c | 23 | 48 | 67 | 247 | 67 | 1949 | 3322 | $1840 | 3-7d |
| KXIPLGAME-26APR22RRLSG-RR | Rajasthan Royals | 64c | 3.0c | 35 | 49959 | 228 | 52814 | 815 | 56814 | 2177 | $742 | 3-7d |
| KXIPLGAME-26APR23CSKMI-CSK | Chennai Super Kings | 42c | 5.0c | 50 | 17 | 165 | 151 | 165 | 1425 | 1809 | $592 | 7-30d |
| KXIPLGAME-26APR23CSKMI-MI | Mumbai Indians | 61c | 4.0c | 53 | 177 | 53 | 6035 | 53 | 6035 | 1156 | $701 | 7-30d |
| KXIPLGAME-26APR25PBKSDC-PBKS | Punjab Kings | 62c | 8.0c | 37 | 11 | 297 | 2553 | 397 | 2653 | 1136 | $1100 | 7-30d |
| KXIPLGAME-26APR22RRLSG-LSG | Lucknow Super Giants | 38c | 5.0c | 49 | 205 | 103 | 1751 | 103 | 4751 | 871 | $377 | 3-7d |
| KXIPLGAME-26APR24GTRCB-RCB | Royal Challengers Bengaluru | 63c | 2.0c | 53 | 12 | 70 | 2571 | 291 | 6266 | 828 | $795 | 7-30d |
| KXIPLGAME-26APR24GTRCB-GT | Gujarat Titans | 39c | 6.0c | 50 | 35 | 67 | 1412 | 67 | 3150 | 693 | $428 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIPLGAME | Rajasthan Royals | nan | 22 | 22 | $1,412,802 | 1,463,750 | 1.0c |

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
