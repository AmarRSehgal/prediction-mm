# tech_ai

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **10** (10 with open markets)
- Open markets: **53** (28 contested)
- Total 24h volume: **$2,186**
- Total open interest: **400,702**
- Top-OI mean spread (median across series): **5.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **35**
- Median spread: **5.0c**
- Median TOB bid / ask size: **41 / 111** contracts
- Median depth within 5c of best bid / ask — **541 / 519** contracts
- Median depth within 10c of best bid / ask — **620 / 561** contracts
- Median depth within 5c of midpoint — bid: **510** / ask: **504** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **241**
- Mean informed-signal proxy: **-1.272** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.62c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 8424 | 1.72 | -0.667 | 6.00 | 40.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| OAIAGI-26 | Before Dec 31, 2026 | 15c | 3.6c | 16 | 166 | 3195 | 3013 | 8851 | 3252 | 90290 | $5 | 30d+ |
| OAIAGI-27 | Before Dec 31, 2027 | 40c | 2.7c | 25 | 111 | 4260 | 3343 | 4760 | 4385 | 88364 | $23 | 30d+ |
| OAIAGI-29 | Before 2030 | 61c | 3.8c | 127 | 29 | 1344 | 3569 | 2452 | 3624 | 63097 | $27 | 30d+ |
| KXOAIANTH-40-ANTH | Anthropic | 72c | 5.0c | 150 | 26 | 650 | 648 | 660 | 678 | 23206 | $6 | 30d+ |
| KXGPTCOST-27 | Before 2027 | 37c | 6.0c | 510 | 22 | 510 | 786 | 510 | 1472 | 19870 | $38 | 30d+ |
| KXOAIANTH-40-OAI | OpenAI | 34c | 5.0c | 25 | 22 | 591 | 522 | 591 | 522 | 15857 | $14 | 30d+ |
| NYTOAI-27DEC31 | New York Times wins | 63c | 1.0c | 500 | 1 | 500 | 21 | 501 | 521 | 13776 | $54 | 30d+ |
| KXGROK-GROK5-26JUL01 | Before July | 19c | 4.0c | 639 | 19 | 1306 | 198 | 1632 | 824 | 9109 | $106 | 30d+ |
| KXOAIHARDWARE-27-EARBUDS | Earbuds/Headphones | 51c | 8.0c | 504 | 4 | 504 | 504 | 504 | 504 | 7390 | $4 | 30d+ |
| KXOAIHARDWARE-27-CLIPON | Clip-on device for clothing | 29c | 8.0c | 74 | 500 | 574 | 500 | 574 | 500 | 6009 | $0 | 30d+ |
| KXOAISCREEN-27 | Before 2027 | 20c | 7.0c | 32 | 501 | 562 | 501 | 610 | 501 | 5157 | $6 | 30d+ |
| KXANTHROPICDOD-28 | Before 2028 | 66c | 1.0c | 13 | 29 | 523 | 61 | 523 | 1061 | 4455 | $84 | 30d+ |
| KXAGICO-COMP-26Q2 | Before Jul 1, 2026 | 9c | 1.0c | 49 | 149 | 49 | 649 | 4023 | 778 | 4093 | $11 | 30d+ |
| KXOAIHARDWARE-27-GLASSES | Glasses | 12c | 10.0c | 500 | 743 | 1134 | 743 | 3710 | 743 | 4067 | $0 | 30d+ |
| KXOAIHARDWARE-27-PHONE | Phone | 11c | 6.0c | 32 | 500 | 1150 | 500 | 3720 | 500 | 3865 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXOAIAGI | OpenAI achieves AGI | custom | 3 | 3 | $55 | 241,751 | 3.4c |
| KXOAIANTH | Open AI vs Anthropic | one_off | 2 | 2 | $20 | 39,063 | 5.0c |
| KXOAIHARDWARE | What hardware will openAI/Jony Ive launc | custom | 10 | 4 | $4 | 27,892 | 8.7c |
| KXAGICO | Will any company achieve AGI before [dat | custom | 13 | 12 | $38 | 25,197 | 3.3c |
| KXGPTCOST | GPT cost | custom | 1 | 1 | $38 | 19,870 | 6.0c |
| KXNYTOAI | New York Times wins OpenAI lawsuit | custom | 1 | 1 | $54 | 13,776 | 1.0c |
| KXTECHRANKLISTAICODE | AI Coding | one_off | 18 | 0 | $1,756 | 11,994 | nanc |
| KXGROK | Grok | one_off | 3 | 3 | $131 | 11,548 | 6.3c |
| KXOAISCREEN | OpenAI screen | custom | 1 | 1 | $6 | 5,157 | 7.0c |
| KXANTHROPICDOD | Will Anthropic win its lawsuit against t | one_off | 1 | 1 | $84 | 4,455 | 1.0c |

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
