# crypto_btc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **473** (40 contested)
- Total 24h volume: **$825,258**
- Total open interest: **12,301,054**
- Top-OI mean spread (median across series): **2.5 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **55**
- Median spread: **2.0c**
- Median TOB bid / ask size: **501 / 207** contracts
- Median cumulative depth within 5c of mid — bid: **5367** / ask: **4399** contracts
- Median cumulative depth within 10c of mid — bid: **6627** / ask: **6712** contracts
- Mean trades per market (last 3000): **910**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 1443 | 0.00 | 0.000 | 0.00 | 0.0 |
| 15m-1h | 1752 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 2096 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 19 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 9221 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 38727 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBTCMAX100-26-JUNE | Before July 2026 | 16c | 3.0c | 63 | 700 | 9364 | 6865 | 379064 | $7910 | 30d+ |
| KXBTCMAX100-26-MAY | Before June 2026 | 8c | 3.0c | 1679 | 933 | 11613 | 7433 | 308906 | $2716 | 30d+ |
| KXBTCMINY-27JAN01-60000.00 | Below $60,000.00 | 60c | 1.0c | 32 | 20 | 7971 | 2743 | 228842 | $6721 | 30d+ |
| KXBTCMAXY-26DEC31-199999.99 | Above $199,999.99 | 6c | 1.0c | 5013 | 3210 | 88360 | 33391 | 191673 | $1001 | 30d+ |
| KXBTCMAXY-26DEC31-99999.99 | Above $99,999.99 | 43c | 1.0c | 2573 | 140 | 2796 | 12456 | 189279 | $4646 | 30d+ |
| KXBTCMAXMON-BTC-26APR30-8000000 | Above $80,000.00 | 34c | 4.0c | 3550 | 46 | 13550 | 4132 | 180706 | $16073 | 7-30d |
| KXBTCMINY-27JAN01-40000.00 | Below $40,000.00 | 24c | 1.0c | 948 | 607 | 6862 | 1293 | 172721 | $2294 | 30d+ |
| KXBTCMINY-27JAN01-50000.00 | Below $50,000.00 | 42c | 1.0c | 23 | 40 | 7174 | 1603 | 158894 | $3428 | 30d+ |
| KXBTCMINY-27JAN01-45000.00 | Below $45,000.00 | 32c | 1.0c | 15 | 723 | 4009 | 4399 | 148983 | $904 | 30d+ |
| KXBTCMINY-27JAN01-55000.00 | Below $55,000.00 | 55c | 1.0c | 49 | 12 | 102 | 3245 | 146728 | $3602 | 30d+ |
| KXBTCMAXY-26DEC31-149999.99 | Above $149,999.99 | 12c | 1.0c | 40 | 7783 | 9463 | 10041 | 104979 | $1436 | 30d+ |
| KXBTCMAX100-26-SEP | Before October 2026 | 31c | 4.0c | 21 | 237 | 84 | 1598 | 98733 | $2501 | 30d+ |
| KXBTCMAXY-26DEC31-119999.99 | Above $119,999.99 | 21c | 1.0c | 40 | 2725 | 4172 | 7355 | 97682 | $2121 | 30d+ |
| KXBTCMAXY-26DEC31-129999.99 | Above $129,999.99 | 18c | 1.0c | 1010 | 2806 | 3649 | 7229 | 84475 | $2658 | 30d+ |
| KXBTCMAXMON-BTC-26APR30-8250000 | Above $82,500.00 | 18c | 5.0c | 1571 | 347 | 4571 | 3576 | 82313 | $11331 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBTCMAX150 | When will bitcoin hit 150k? | custom | 6 | 1 | $17,985 | 3,438,768 | 3.0c |
| KXBTCY | BTC price range EOY | annual | 28 | 0 | $93,806 | 3,026,742 | nanc |
| KXBTCMAX100 | When will bitcoin hit 100k? | annual | 5 | 3 | $41,131 | 1,507,562 | 4.0c |
| KXBTC2026200 | Will Bitcoin hit 200k in 2026?  | one_off | 1 | 0 | $14,686 | 1,365,285 | nanc |
| KXBTCMINY | How low will Bitcoin fall this year? | one_off | 5 | 5 | $16,941 | 856,180 | 1.3c |
| KXBTCMAXY | How high will Bitcoin get this year? | annual | 7 | 6 | $16,094 | 805,597 | 1.0c |
| KXBTCMAXMON | Bitcoin monthly one touch | monthly | 4 | 2 | $35,226 | 368,708 | 3.0c |
| KXBTCMINMON | BTC one touch minimum | monthly | 8 | 1 | $9,847 | 277,032 | 1.0c |
| KXBTCD | Bitcoin price Above/below | hourly | 200 | 14 | $520,923 | 275,782 | 1.3c |
| KXBTC2026250 | Will Bitcoin hit 250k in 2026?  | one_off | 1 | 0 | $1,168 | 194,741 | nanc |

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
