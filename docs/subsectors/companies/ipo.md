# companies_ipo

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **24** (24 with open markets)
- Open markets: **300** (137 contested)
- Total 24h volume: **$27,248**
- Total open interest: **2,588,250**
- Top-OI mean spread (median across series): **7.3 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **185**
- Median spread: **8.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median cumulative depth within 5c of mid — bid: **500** / ask: **500** contracts
- Median cumulative depth within 10c of mid — bid: **737** / ask: **501** contracts
- Mean trades per market (last 3000): **167**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 30925 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIPOSPACEX-26JUN01 | Before Jun 1, 2026 | 17c | 1.0c | 3301 | 4811 | 6361 | 21141 | 464640 | $7456 | 30d+ |
| KXIPOSPACEX-26JUL01 | Before Jul 1, 2026 | 74c | 3.0c | 101 | 14 | 1127 | 5944 | 182526 | $979 | 30d+ |
| KXIPO-26-SPACEX | SpaceX | 94c | 1.0c | 72 | 31 | 1354 | 7444 | 100619 | $1200 | 30d+ |
| KXIPOSPACEX-26AUG01 | Before Aug 1, 2026 | 83c | 2.0c | 115 | 72 | 1272 | 28554 | 82667 | $109 | 30d+ |
| KXIPO-26-DATABRICKS | Databricks | 18c | 1.0c | 28 | 533 | 1248 | 1638 | 64443 | $155 | 30d+ |
| KXIPO-26-ANDURIL | Anduril | 9c | 1.0c | 27 | 36 | 1180 | 342 | 59148 | $13 | 30d+ |
| KXIPOSPACEX-26SEP01 | Before Sep 1, 2026 | 90c | 2.0c | 25 | 1022 | 1238 | 21342 | 50193 | $9 | 30d+ |
| KXIPO-26-OPENAI | OpenAI | 54c | 2.0c | 27 | 62 | 1152 | 3482 | 46316 | $883 | 30d+ |
| KXIPO-26-ANTHROPIC | Anthropic | 60c | 2.0c | 182 | 9 | 1182 | 3479 | 44186 | $1444 | 30d+ |
| KXIPO-26-KRAKEN | Kraken | 67c | 6.0c | 25 | 18 | 545 | 1013 | 35147 | $59 | 30d+ |
| KXIPO-26-CEREBRAS | Cerebras | 95c | 2.0c | 35 | 8 | 503 | 3166 | 27727 | $73 | 30d+ |
| KXIPOSPACEX-26OCT01 | Before Oct 1, 2026 | 90c | 5.0c | 51 | 1026 | 1092 | 3026 | 26631 | $0 | 30d+ |
| KXIPOSPACEX-26NOV01 | Before Nov 1, 2026 | 90c | 3.0c | 66 | 187 | 1236 | 13229 | 21975 | $0 | 30d+ |
| KXIPO-26-DISCORD | Discord | 58c | 3.0c | 37 | 9 | 102 | 1016 | 21519 | $117 | 30d+ |
| KXIPOSTARLINK-27JUN30 | Before Jun 30, 2027 | 12c | 2.0c | 513 | 81 | 513 | 666 | 21276 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIPOSPACEX | When will spacex IPO | one_off | 14 | 5 | $10,744 | 1,745,986 | 2.0c |
| KXIPO | IPOs | custom | 27 | 18 | $5,381 | 522,642 | 1.7c |
| KXIPOSTARLINK | When will starlink IPO | one_off | 14 | 3 | $0 | 93,321 | 3.7c |
| KXIPOOPENAI | When will OPENAI Announce IPO? | one_off | 14 | 9 | $136 | 62,410 | 3.3c |
| KXIPOANDURIL | When will anduril IPO | one_off | 14 | 5 | $10,534 | 42,655 | 9.0c |
| KXKRAKENBANKPUBLIC | Kraken IPO | custom | 5 | 5 | $0 | 32,412 | 5.3c |
| KXIPOFANNIE | When will Fannie Mae IPO? | one_off | 14 | 2 | $0 | 20,801 | 6.5c |
| KXIPODISCORD | When will Discord IPO | one_off | 14 | 11 | $46 | 18,445 | 8.7c |
| KXSTRIPEIPO | When will Stripe Announce IPO? | one_off | 14 | 6 | $34 | 9,007 | 5.7c |
| KXFREDDIE | When will Freddie Mac IPO? | one_off | 14 | 0 | $0 | 8,262 | nanc |

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
