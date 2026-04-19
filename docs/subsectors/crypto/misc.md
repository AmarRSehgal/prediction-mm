# crypto_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **5** (5 with open markets)
- Open markets: **39** (23 contested)
- Total 24h volume: **$6,310**
- Total open interest: **595,094**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **5.0c**
- Median TOB bid / ask size: **49 / 116** contracts
- Median depth within 5c of best bid / ask — **1270 / 1260** contracts
- Median depth within 10c of best bid / ask — **1506 / 1268** contracts
- Median depth within 5c of midpoint — bid: **681** / ask: **1256** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **303**
- Mean informed-signal proxy: **-0.517** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.23c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1003 | 2.01 | -0.118 | 8.00 | 35.2 |
| 30d+ | 6272 | 1.72 | -0.573 | 6.00 | 62.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCRYPTOSTRUCTURE-26JAN-JUN | Before June | 7c | 4.9c | 92 | 102 | 22177 | 12289 | 22177 | 18489 | 90520 | $2158 | 30d+ |
| KXCRYPTOSTRUCTURE-26JAN-27 | Before 2027 | 58c | 3.0c | 12 | 265 | 684 | 1765 | 1684 | 2235 | 34971 | $63 | 30d+ |
| KXCRYPTORETURNY-26-XRP | Ripple (XRP) | 27c | 4.0c | 46 | 10 | 1519 | 1298 | 4572 | 1298 | 25991 | $265 | 30d+ |
| KXCRYPTORETURNY-26-BTC | Bitcoin (BTC) | 40c | 5.0c | 21 | 1251 | 1303 | 1251 | 1517 | 1251 | 20379 | $234 | 30d+ |
| KXCRYPTOSTRUCTURE-26JAN-JUL | Before July | 26c | 5.0c | 42 | 634 | 1550 | 3934 | 1650 | 4934 | 18589 | $575 | 30d+ |
| KXCRYPTORETURNY-26-SOL | Solana (SOL) | 27c | 6.0c | 1279 | 9 | 1479 | 1260 | 1495 | 1265 | 14746 | $110 | 30d+ |
| KXCRYPTORETURNY-26-LINK | Chainlink (LINK) | 34c | 5.0c | 1272 | 14 | 1272 | 1296 | 1672 | 1296 | 13792 | $76 | 30d+ |
| KXCRYPTORETURNY-26-ETH | Ethereum (ETH) | 34c | 6.0c | 1287 | 9 | 1309 | 1260 | 1309 | 1260 | 13705 | $112 | 30d+ |
| KXTRUMPCRYPTOCONF-26-DJT | Donald Trump | 86c | 5.0c | 12 | 113 | 774 | 213 | 1274 | 1578 | 13201 | $0 | 7-30d |
| KXCRYPTOSTRUCTURE-26JAN-AUG | Before August | 46c | 7.0c | 50 | 983 | 1550 | 2283 | 1550 | 2383 | 12672 | $175 | 30d+ |
| KXCRYPTORETURNY-26-DOT | Polkadot (DOT) | 10c | 6.0c | 48 | 1270 | 2398 | 1390 | 5421 | 1390 | 9030 | $282 | 30d+ |
| KXCRYPTOPAY-27 | In 2026 | 36c | 3.0c | 24 | 25 | 963 | 1033 | 1294 | 3028 | 8932 | $234 | 30d+ |
| KXCRYPTORETURNY-26-SHIBA | Shiba Inu (SHIB) | 21c | 4.0c | 18 | 1369 | 1268 | 1370 | 1268 | 1370 | 5369 | $182 | 30d+ |
| KXTRUMPCRYPTOCONF-26-NPIN | Nick Pinto | 54c | 5.0c | 10 | 233 | 267 | 383 | 302 | 383 | 4041 | $159 | 7-30d |
| KXTRUMPCRYPTOCONF-26-ETRU | Eric Trump | 71c | 6.0c | 8 | 104 | 287 | 254 | 287 | 254 | 3896 | $786 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCRYPTOSTRUCTURE | Crypto market structure | custom | 5 | 3 | $3,660 | 435,167 | 5.0c |
| KXCRYPTORETURNY | Crypto being positive | annual | 10 | 10 | $1,260 | 110,742 | 4.3c |
| KXTRUMPCRYPTOCONF | Who will attend Trump's crypto & busines | one_off | 11 | 9 | $1,156 | 33,568 | 5.3c |
| KXCRYPTOPAY | Crypto payments from tech firms | custom | 1 | 1 | $234 | 8,932 | 3.0c |
| KXTRADEDEFICIT | Trade Deficit by Date | custom | 12 | 0 | $0 | 6,685 | nanc |

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
