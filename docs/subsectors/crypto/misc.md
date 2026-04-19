# crypto_misc

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **5** (5 with open markets)
- Open markets: **39** (23 contested)
- Total 24h volume: **$7,014**
- Total open interest: **594,792**
- Top-OI mean spread (median across series): **4.7 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **24**
- Median spread: **5.0c**
- Median TOB bid / ask size: **47 / 144** contracts
- Median cumulative depth within 5c of mid — bid: **681** / ask: **1260** contracts
- Median cumulative depth within 10c of mid — bid: **1317** / ask: **1266** contracts
- Mean trades per market (last 3000): **360**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 1002 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 7643 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCRYPTOSTRUCTURE-26JAN-JUN | Before June | 7c | 4.9c | 92 | 102 | 7715 | 3684 | 90520 | $2226 | 30d+ |
| KXCRYPTOSTRUCTURE-26JAN-27 | Before 2027 | 58c | 3.0c | 12 | 265 | 184 | 1765 | 34971 | $63 | 30d+ |
| KXCRYPTORETURNY-26-XRP | Ripple (XRP) | 27c | 4.0c | 46 | 42 | 1321 | 1298 | 25991 | $265 | 30d+ |
| KXCRYPTORETURNY-26-BTC | Bitcoin (BTC) | 41c | 2.0c | 20 | 1259 | 74 | 1259 | 20379 | $223 | 30d+ |
| KXCRYPTOSTRUCTURE-26JAN-JUL | Before July | 26c | 4.0c | 11 | 634 | 551 | 2584 | 18589 | $585 | 30d+ |
| KXCRYPTORETURNY-26-SOL | Solana (SOL) | 27c | 6.0c | 29 | 1250 | 1279 | 1270 | 14746 | $110 | 30d+ |
| KXCRYPTORETURNY-26-LINK | Chainlink (LINK) | 34c | 5.0c | 1250 | 14 | 1272 | 1296 | 13792 | $76 | 30d+ |
| KXCRYPTORETURNY-26-ETH | Ethereum (ETH) | 34c | 5.0c | 59 | 1259 | 1309 | 1260 | 13698 | $112 | 30d+ |
| KXTRUMPCRYPTOCONF-26-DJT | Donald Trump | 86c | 5.0c | 12 | 113 | 524 | 213 | 13201 | $0 | 7-30d |
| KXCRYPTOSTRUCTURE-26JAN-AUG | Before August | 46c | 8.0c | 500 | 983 | 1500 | 983 | 12672 | $312 | 30d+ |
| KXCRYPTORETURNY-26-DOT | Polkadot (DOT) | 10c | 6.0c | 48 | 1270 | 1598 | 1390 | 9030 | $282 | 30d+ |
| KXCRYPTOPAY-27 | In 2026 | 36c | 3.0c | 24 | 25 | 812 | 777 | 8932 | $234 | 30d+ |
| KXCRYPTORETURNY-26-SHIBA | Shiba Inu (SHIB) | 21c | 4.0c | 18 | 119 | 1268 | 1371 | 5369 | $182 | 30d+ |
| KXTRUMPCRYPTOCONF-26-NPIN | Nick Pinto | 54c | 5.0c | 32 | 233 | 139 | 383 | 4041 | $415 | 7-30d |
| KXTRUMPCRYPTOCONF-26-ETRU | Eric Trump | 71c | 6.0c | 9 | 105 | 138 | 255 | 3897 | $785 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCRYPTOSTRUCTURE | Crypto market structure | custom | 5 | 3 | $4,424 | 435,160 | 4.7c |
| KXCRYPTORETURNY | Crypto being positive | annual | 10 | 10 | $1,227 | 110,730 | 4.7c |
| KXTRUMPCRYPTOCONF | Who will attend Trump's crypto & busines | one_off | 11 | 9 | $1,129 | 33,288 | 5.0c |
| KXCRYPTOPAY | Crypto payments from tech firms | custom | 1 | 1 | $234 | 8,930 | 3.0c |
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
