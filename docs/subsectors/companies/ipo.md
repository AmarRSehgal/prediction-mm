# companies_ipo

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **24** (24 with open markets)
- Open markets: **300** (137 contested)
- Total 24h volume: **$27,583**
- Total open interest: **2,588,069**
- Top-OI mean spread (median across series): **8.3 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **185**
- Median spread: **8.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median depth within 5c of best bid / ask — **527 / 500** contracts
- Median depth within 10c of best bid / ask — **1119 / 501** contracts
- Median depth within 5c of midpoint — bid: **500** / ask: **500** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **111**
- Mean informed-signal proxy: **-1.693** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.73c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 20578 | 1.85 | -0.423 | 7.00 | 56.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXIPOSPACEX-26JUN01 | Before Jun 1, 2026 | 17c | 1.0c | 3249 | 4716 | 6309 | 21562 | 8570 | 27620 | 464735 | $7333 | 30d+ |
| KXIPOSPACEX-26JUL01 | Before Jul 1, 2026 | 76c | 2.0c | 51 | 3749 | 2097 | 7859 | 10122 | 15318 | 182526 | $886 | 30d+ |
| KXIPO-26-SPACEX | SpaceX | 95c | 2.0c | 15 | 82 | 1271 | 12567 | 6504 | 12567 | 100597 | $1587 | 30d+ |
| KXIPOSPACEX-26AUG01 | Before Aug 1, 2026 | 83c | 2.0c | 115 | 72 | 1272 | 35999 | 1272 | 35999 | 82667 | $109 | 30d+ |
| KXIPO-26-DATABRICKS | Databricks | 18c | 1.0c | 28 | 531 | 1248 | 1728 | 2549 | 2976 | 64443 | $155 | 30d+ |
| KXIPO-26-ANDURIL | Anduril | 9c | 1.0c | 27 | 34 | 1184 | 332 | 5131 | 1490 | 59148 | $13 | 30d+ |
| KXIPOSPACEX-26SEP01 | Before Sep 1, 2026 | 90c | 2.0c | 23 | 1022 | 4228 | 21358 | 4836 | 26064 | 50193 | $307 | 30d+ |
| KXIPO-26-OPENAI | OpenAI | 54c | 2.0c | 27 | 36 | 1152 | 5352 | 2243 | 5352 | 46334 | $827 | 30d+ |
| KXIPO-26-ANTHROPIC | Anthropic | 60c | 3.0c | 182 | 2500 | 1182 | 4168 | 5154 | 6188 | 44186 | $1444 | 30d+ |
| KXIPO-26-KRAKEN | Kraken | 67c | 6.0c | 25 | 18 | 554 | 1996 | 669 | 4296 | 35147 | $59 | 30d+ |
| KXIPO-26-CEREBRAS | Cerebras | 95c | 2.0c | 33 | 8 | 4069 | 3167 | 4573 | 3167 | 27727 | $50 | 30d+ |
| KXIPOSPACEX-26OCT01 | Before Oct 1, 2026 | 90c | 5.0c | 19 | 1026 | 1081 | 4429 | 1119 | 7591 | 26631 | $100 | 30d+ |
| KXIPOSPACEX-26NOV01 | Before Nov 1, 2026 | 90c | 3.0c | 66 | 187 | 1220 | 13650 | 8730 | 18310 | 21975 | $0 | 30d+ |
| KXIPO-26-DISCORD | Discord | 58c | 3.0c | 27 | 15 | 1252 | 1115 | 1252 | 1115 | 21519 | $117 | 30d+ |
| KXIPOSTARLINK-27JUN30 | Before Jun 30, 2027 | 12c | 2.0c | 513 | 63 | 514 | 666 | 4314 | 1300 | 21276 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXIPOSPACEX | When will spacex IPO | one_off | 14 | 5 | $11,182 | 1,745,834 | 1.3c |
| KXIPO | IPOs | custom | 27 | 18 | $5,214 | 522,661 | 1.7c |
| KXIPOSTARLINK | When will starlink IPO | one_off | 14 | 3 | $115 | 93,271 | 3.7c |
| KXIPOOPENAI | When will OPENAI Announce IPO? | one_off | 14 | 9 | $106 | 62,411 | 3.7c |
| KXIPOANDURIL | When will anduril IPO | one_off | 14 | 5 | $10,534 | 42,655 | 9.0c |
| KXKRAKENBANKPUBLIC | Kraken IPO | custom | 5 | 5 | $0 | 32,412 | 5.3c |
| KXIPOFANNIE | When will Fannie Mae IPO? | one_off | 14 | 2 | $0 | 20,801 | 6.5c |
| KXIPODISCORD | When will Discord IPO | one_off | 14 | 11 | $12 | 18,446 | 8.7c |
| KXSTRIPEIPO | When will Stripe Announce IPO? | one_off | 14 | 6 | $34 | 9,007 | 6.0c |
| KXFREDDIE | When will Freddie Mac IPO? | one_off | 14 | 0 | $1 | 8,262 | nanc |

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
