# crypto_btc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **16** (16 with open markets)
- Open markets: **473** (29 contested)
- Total 24h volume: **$524,875**
- Total open interest: **12,185,988**
- Top-OI mean spread (median across series): **2.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **29**
- Median spread: **1.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median depth within 5c of best bid / ask — **5605 / 4819** contracts
- Median depth within 10c of best bid / ask — **7978 / 5743** contracts
- Median depth within 5c of midpoint — bid: **4172** / ask: **4389** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **812**
- Mean informed-signal proxy: **-0.625** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.24c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 0-15m | 3207 | 1.07 | -0.305 | 4.00 | 74.6 |
| 15m-1h | 1342 | 1.38 | -0.301 | 4.00 | 89.6 |
| 7-30d | 6428 | 0.91 | -0.202 | 3.00 | 98.3 |
| 30d+ | 17109 | 0.67 | -0.234 | 3.00 | 90.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBTCMAX100-26-JUNE | Before July 2026 | 16c | 3.0c | 362 | 648 | 10292 | 10444 | 35855 | 12397 | 379064 | $7594 | 30d+ |
| KXBTCMAX100-26-MAY | Before June 2026 | 9c | 2.0c | 120 | 933 | 12781 | 7433 | 15094 | 9438 | 308906 | $2868 | 30d+ |
| KXBTCMINY-27JAN01-60000.00 | Below $60,000.00 | 60c | 1.0c | 23 | 20 | 7983 | 5743 | 8390 | 5743 | 228842 | $6721 | 30d+ |
| KXBTCMAXY-26DEC31-199999.99 | Above $199,999.99 | 6c | 1.0c | 5060 | 6 | 144211 | 30391 | 144211 | 34374 | 191673 | $1001 | 30d+ |
| KXBTCMAXY-26DEC31-99999.99 | Above $99,999.99 | 42c | 1.0c | 2500 | 216 | 6228 | 14056 | 6907 | 20032 | 189279 | $4735 | 30d+ |
| KXBTCMAXMON-BTC-26APR30-8000000 | Above $80,000.00 | 32c | 1.0c | 3801 | 158 | 17216 | 173 | 17465 | 2235 | 180747 | $17993 | 7-30d |
| KXBTCMINY-27JAN01-40000.00 | Below $40,000.00 | 24c | 1.0c | 870 | 516 | 6784 | 1201 | 6805 | 4694 | 172721 | $2091 | 30d+ |
| KXBTCMINY-27JAN01-50000.00 | Below $50,000.00 | 42c | 1.0c | 30 | 50 | 7360 | 4607 | 7550 | 4607 | 158894 | $3276 | 30d+ |
| KXBTCMINY-27JAN01-45000.00 | Below $45,000.00 | 32c | 1.0c | 40 | 3823 | 4004 | 4389 | 7056 | 4480 | 148983 | $778 | 30d+ |
| KXBTCMINY-27JAN01-55000.00 | Below $55,000.00 | 52c | 1.0c | 32 | 14 | 1538 | 3217 | 7438 | 3291 | 146707 | $3395 | 30d+ |
| KXBTCMAXY-26DEC31-149999.99 | Above $149,999.99 | 12c | 1.0c | 40 | 7783 | 10828 | 10041 | 91384 | 16984 | 104979 | $1436 | 30d+ |
| KXBTCMAX100-26-SEP | Before October 2026 | 31c | 4.0c | 21 | 237 | 263 | 8923 | 978 | 9025 | 98733 | $2501 | 30d+ |
| KXBTCMAXY-26DEC31-119999.99 | Above $119,999.99 | 21c | 1.0c | 40 | 2725 | 4172 | 7366 | 9460 | 13487 | 97682 | $1912 | 30d+ |
| KXBTCMAXY-26DEC31-129999.99 | Above $129,999.99 | 18c | 1.0c | 1010 | 2806 | 3649 | 7234 | 12012 | 7339 | 84475 | $2658 | 30d+ |
| KXBTCMAXMON-BTC-26APR30-8250000 | Above $82,500.00 | 19c | 1.0c | 1149 | 164 | 5605 | 3409 | 6005 | 3409 | 82415 | $11244 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBTCMAX150 | When will bitcoin hit 150k? | custom | 6 | 1 | $65,043 | 3,474,536 | 3.0c |
| KXBTCY | BTC price range EOY | annual | 28 | 0 | $87,794 | 3,027,156 | nanc |
| KXBTCMAX100 | When will bitcoin hit 100k? | annual | 5 | 3 | $36,871 | 1,507,693 | 4.3c |
| KXBTC2026200 | Will Bitcoin hit 200k in 2026?  | one_off | 1 | 0 | $15,751 | 1,367,212 | nanc |
| KXBTCMINY | How low will Bitcoin fall this year? | one_off | 5 | 5 | $16,260 | 856,147 | 1.0c |
| KXBTCMAXY | How high will Bitcoin get this year? | annual | 7 | 6 | $18,559 | 808,124 | 1.0c |
| KXBTCMAXMON | Bitcoin monthly one touch | monthly | 4 | 2 | $35,015 | 368,858 | 1.0c |
| KXBTCMINMON | BTC one touch minimum | monthly | 8 | 1 | $13,480 | 280,055 | 1.0c |
| KXBTC2026250 | Will Bitcoin hit 250k in 2026?  | one_off | 1 | 0 | $332 | 194,751 | nanc |
| KXBTCD | Bitcoin price Above/below | hourly | 200 | 2 | $225,320 | 147,705 | 3.0c |

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
