# crypto_eth

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **387** (47 contested)
- Total 24h volume: **$44,286**
- Total open interest: **1,534,866**
- Top-OI mean spread (median across series): **2.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **44**
- Median spread: **3.5c**
- Median TOB bid / ask size: **218 / 548** contracts
- Median cumulative depth within 5c of mid — bid: **4580** / ask: **5000** contracts
- Median cumulative depth within 10c of mid — bid: **5282** / ask: **5104** contracts
- Mean trades per market (last 3000): **291**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 1242 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 342 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 68 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 17 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 2474 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 9919 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXETHMAXY-27JAN01-6000.00 | Above $6,000.00 | 12c | 1.0c | 50 | 4513 | 10785 | 19017 | 158741 | $392 | 30d+ |
| KXETHMINY-27JAN01-1250 | Below $1,250.00 | 38c | 2.0c | 558 | 2765 | 3366 | 5779 | 91716 | $2109 | 30d+ |
| KXETHMAXY-27JAN01-5000.00 | Above $5,000.00 | 15c | 3.0c | 2708 | 2500 | 5475 | 6988 | 91159 | $8 | 30d+ |
| KXETHMAXY-27JAN01-3500.00 | Above $3,500.00 | 40c | 1.0c | 15 | 2700 | 5961 | 3630 | 64860 | $1057 | 30d+ |
| KXETHMAXY-27JAN01-4000.00 | Above $4,000.00 | 28c | 4.0c | 2700 | 2500 | 2700 | 6597 | 63953 | $3 | 30d+ |
| KXETHMAXY-27JAN01-4500.00 | Above $4,500.00 | 21c | 1.0c | 19 | 3339 | 2546 | 8415 | 53232 | $40 | 30d+ |
| KXETHMINY-27JAN01-1000 | Below $1,000.00 | 26c | 3.0c | 2746 | 3300 | 3060 | 3300 | 51273 | $101 | 30d+ |
| KXETHMAXY-27JAN01-4750.00 | Above $4,750.00 | 18c | 3.0c | 0 | 2500 | 3086 | 6142 | 46459 | $0 | 30d+ |
| KXETHMINY-27JAN01-1500 | Below $1,500.00 | 48c | 5.0c | 14 | 2 | 1224 | 5502 | 42919 | $193 | 30d+ |
| KXETHMAXMON-ETH-26APR30-250000 | Above $2,500.00 | 52c | 5.0c | 500 | 500 | 3500 | 3860 | 40020 | $4621 | 7-30d |
| KXETHMAXY-27JAN01-4250.00 | Above $4,250.00 | 24c | 3.0c | 2721 | 2707 | 5921 | 2707 | 36948 | $14 | 30d+ |
| KXETHMAXY-27JAN01-3750.00 | Above $3,750.00 | 34c | 7.0c | 2800 | 2500 | 6000 | 2500 | 36057 | $0 | 30d+ |
| KXETHMINY-27JAN01-1750 | Below $1,750.00 | 62c | 5.0c | 2700 | 2500 | 2700 | 5500 | 26330 | $519 | 30d+ |
| KXETHMAXMON-ETH-26APR30-300000 | Above $3,000.00 | 6c | 2.0c | 820 | 3970 | 5424 | 3970 | 26081 | $3970 | 7-30d |
| KXETHMAXMON-ETH-26APR30-275000 | Above $2,750.00 | 17c | 1.0c | 10 | 459 | 3530 | 4331 | 25686 | $3039 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXETHY | ETH price EOY  | annual | 18 | 0 | $4,802 | 566,422 | nanc |
| KXETHMAXY | How high will Ethereum get this year? | annual | 8 | 8 | $1,918 | 551,407 | 1.3c |
| KXETHMINY | How low will Ethereum fall this year? | one_off | 5 | 5 | $2,895 | 227,381 | 2.7c |
| KXETHMAXMON | ETH Monthly One touch | monthly | 8 | 2 | $12,105 | 126,169 | 2.0c |
| KXETHMINMON | ETH min one touch monthly | monthly | 8 | 1 | $1,467 | 28,491 | 3.0c |
| KXETHD | Ethereum price Above/below | hourly | 165 | 15 | $17,917 | 20,733 | 1.3c |
| KXALBUMRELEASETRAVYE | WILL KANYE WEST AND TRAVIS SCOTT RELEASE | one_off | 1 | 1 | $3 | 7,805 | 5.0c |
| KXETH | Ethereum range | hourly | 165 | 6 | $3,024 | 3,111 | 1.7c |
| KXPUBLICSWIFTLIVELY | Taylor Swift and Blake Lively seen toget | one_off | 1 | 1 | $0 | 1,303 | 1.0c |
| KXETH15M | ETH 15M price up down | fifteen_min | 1 | 1 | $54 | 878 | 1.0c |

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
