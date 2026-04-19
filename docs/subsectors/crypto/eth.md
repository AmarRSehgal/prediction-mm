# crypto_eth

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **14** (14 with open markets)
- Open markets: **387** (45 contested)
- Total 24h volume: **$39,723**
- Total open interest: **1,540,886**
- Top-OI mean spread (median across series): **3.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **63**
- Median spread: **3.0c**
- Median TOB bid / ask size: **214 / 500** contracts
- Median depth within 5c of best bid / ask — **5009 / 5168** contracts
- Median depth within 10c of best bid / ask — **5211 / 5184** contracts
- Median depth within 5c of midpoint — bid: **5000** / ask: **5076** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **203**
- Mean informed-signal proxy: **-0.912** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.76c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 27 | 7.23 | -0.308 | 20.75 | 41.8 |
| 15m-1h | 24 | 6.61 | -4.957 | 28.50 | 6.2 |
| 12-24h | 341 | 1.58 | -0.220 | 6.00 | 10.4 |
| 1-3d | 68 | 2.98 | -2.262 | 10.00 | 6.5 |
| 3-7d | 1096 | 0.77 | -0.254 | 4.00 | 10.7 |
| 7-30d | 2487 | 0.93 | 0.017 | 4.00 | 91.2 |
| 30d+ | 8767 | 0.89 | -0.233 | 3.00 | 93.1 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXETHMAXY-27JAN01-6000.00 | Above $6,000.00 | 12c | 1.0c | 50 | 4513 | 11035 | 19017 | 19254 | 24016 | 158741 | $392 | 30d+ |
| KXETHMINY-27JAN01-1250 | Below $1,250.00 | 38c | 1.0c | 99 | 2700 | 3479 | 5782 | 6479 | 5782 | 91716 | $2109 | 30d+ |
| KXETHMAXY-27JAN01-5000.00 | Above $5,000.00 | 15c | 2.0c | 18 | 2500 | 5458 | 8388 | 8458 | 10626 | 91159 | $8 | 30d+ |
| KXETHMAXY-27JAN01-3500.00 | Above $3,500.00 | 40c | 1.0c | 11 | 35 | 5924 | 3561 | 6788 | 6888 | 64860 | $1062 | 30d+ |
| KXETHMAXY-27JAN01-4000.00 | Above $4,000.00 | 28c | 4.0c | 2700 | 2500 | 6041 | 6776 | 6141 | 6876 | 63953 | $3 | 30d+ |
| KXETHMAXY-27JAN01-4500.00 | Above $4,500.00 | 21c | 1.0c | 19 | 3339 | 2613 | 8315 | 6182 | 8415 | 53232 | $40 | 30d+ |
| KXETHMINY-27JAN01-1000 | Below $1,000.00 | 26c | 3.0c | 2746 | 3300 | 5360 | 4140 | 8360 | 4150 | 51273 | $101 | 30d+ |
| KXETHMAXY-27JAN01-4750.00 | Above $4,750.00 | 18c | 3.0c | 0 | 2500 | 3326 | 6142 | 6401 | 6142 | 46459 | $0 | 30d+ |
| KXETHMINY-27JAN01-1500 | Below $1,500.00 | 48c | 5.0c | 14 | 2 | 4324 | 5502 | 4324 | 12527 | 42919 | $193 | 30d+ |
| KXETHMAXMON-ETH-26APR30-250000 | Above $2,500.00 | 50c | 4.0c | 1299 | 500 | 1299 | 3860 | 1299 | 3860 | 40020 | $4294 | 7-30d |
| KXETHMAXY-27JAN01-4250.00 | Above $4,250.00 | 24c | 3.0c | 2721 | 2707 | 5921 | 5907 | 6122 | 5917 | 36948 | $14 | 30d+ |
| KXETHMAXY-27JAN01-3750.00 | Above $3,750.00 | 34c | 7.0c | 2800 | 2500 | 6125 | 5724 | 9501 | 5932 | 36057 | $0 | 30d+ |
| KXETHMINY-27JAN01-1750 | Below $1,750.00 | 63c | 4.0c | 2700 | 2500 | 5725 | 5500 | 5755 | 8602 | 26330 | $519 | 30d+ |
| KXETHMAXMON-ETH-26APR30-300000 | Above $3,000.00 | 5c | 1.0c | 898 | 500 | 6235 | 4000 | 6235 | 4000 | 26081 | $3920 | 7-30d |
| KXETHMAXMON-ETH-26APR30-275000 | Above $2,750.00 | 16c | 2.0c | 513 | 1101 | 3563 | 4201 | 3672 | 4201 | 25686 | $3295 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXETHY | ETH price EOY  | annual | 18 | 0 | $4,438 | 566,360 | nanc |
| KXETHMAXY | How high will Ethereum get this year? | annual | 8 | 8 | $1,519 | 551,409 | 1.7c |
| KXETHMINY | How low will Ethereum fall this year? | one_off | 5 | 5 | $2,922 | 227,354 | 3.0c |
| KXETHMAXMON | ETH Monthly One touch | monthly | 8 | 2 | $12,313 | 126,169 | 3.0c |
| KXETHMINMON | ETH min one touch monthly | monthly | 8 | 1 | $3,055 | 29,904 | 3.0c |
| KXETHD | Ethereum price Above/below | hourly | 165 | 16 | $12,218 | 16,910 | 2.3c |
| KXETH15M | ETH 15M price up down | fifteen_min | 1 | 0 | $31 | 9,391 | nanc |
| KXALBUMRELEASETRAVYE | WILL KANYE WEST AND TRAVIS SCOTT RELEASE | one_off | 1 | 1 | $0 | 7,805 | 5.0c |
| KXETH | Ethereum range | hourly | 165 | 4 | $3,126 | 3,115 | 4.3c |
| KXPUBLICSWIFTLIVELY | Taylor Swift and Blake Lively seen toget | one_off | 1 | 1 | $0 | 1,303 | 1.0c |

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
