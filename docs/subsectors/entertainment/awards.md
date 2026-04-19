# ent_awards

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **36** (36 with open markets)
- Open markets: **420** (134 contested)
- Total 24h volume: **$28,640**
- Total open interest: **720,257**
- Top-OI mean spread (median across series): **6.2 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median cumulative depth within 5c of mid — bid: **248** / ask: **300** contracts
- Median cumulative depth within 10c of mid — bid: **334** / ask: **490** contracts
- Mean trades per market (last 3000): **51**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 10183 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBOND-30-CAL | Callum Turner | 45c | 3.0c | 79 | 3105 | 729 | 4853 | 112133 | $416 | 30d+ |
| KXBOND-30-ATJ | Aaron Taylor-Johnson | 18c | 2.0c | 238 | 4576 | 738 | 6332 | 67721 | $222 | 30d+ |
| KXBOND-30-JACO | Jacob Elordi | 22c | 3.0c | 465 | 3668 | 1065 | 5739 | 49624 | $240 | 30d+ |
| KXOSCARPIC-27-ODY | The Odyssey:: | 29c | 2.0c | 75 | 1 | 3798 | 3226 | 38164 | $890 | 30d+ |
| KXOSCARPIC-27-PRO | Project Hail Mary:: | 8c | 3.0c | 143 | 474 | 10868 | 6026 | 36406 | $4437 | 30d+ |
| KXOSCARPIC-27-DUN | Dune: Part Three:: | 8c | 2.0c | 57 | 970 | 2577 | 3551 | 31272 | $3693 | 30d+ |
| KXBOND-30-JOS | Josh O'Connor | 9c | 2.0c | 480 | 4979 | 1040 | 7650 | 25318 | $80 | 30d+ |
| KXOSCARPIC-27-SOC | The Social Reckoning:: | 8c | 2.0c | 345 | 995 | 3440 | 4856 | 21863 | $701 | 30d+ |
| KXOSCARPIC-27-DIG | Digger:: | 7c | 2.0c | 720 | 3929 | 2805 | 7638 | 15608 | $25 | 30d+ |
| KXBOND-30-TOMH | Tom Holland | 5c | 4.0c | 250 | 5 | 1149 | 743 | 14337 | $1708 | 30d+ |
| KXACTORWHITELOTUS-27-DEE | Deepika Padukone | 18c | 7.0c | 22 | 110 | 22 | 110 | 4942 | $0 | 30d+ |
| KXOSCARPIC-27-WIL | Wild Horse Nine:: | 8c | 4.0c | 875 | 4440 | 2200 | 9898 | 4879 | $0 | 30d+ |
| KXOSCARACTO-27-JOH | John Malkovich:: Wild Horse Nine | 28c | 8.0c | 122 | 409 | 322 | 462 | 4358 | $0 | 30d+ |
| KXACTORWHITELOTUS-27-JOD | Jodie Comer | 7c | 2.0c | 45 | 100 | 245 | 300 | 4308 | $0 | 30d+ |
| KXEMMYTVMOVIE-26SEP14-PEAK | Peaky Blinders: The Immortal Man::   | 19c | 1.0c | 15 | 28 | 143 | 324 | 3580 | $3157 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBOND | Next Bond actor | custom | 20 | 3 | $5,008 | 407,517 | 2.0c |
| KXOSCARPIC | Oscar for Best Picture | annual | 26 | 1 | $12,186 | 207,909 | 3.0c |
| KXACTORWHITELOTUS | WHO WILL BE THE ACTOR IN WHITELOTUS | one_off | 23 | 7 | $9 | 14,397 | 6.3c |
| KXGRAMMYNOMNAOTY | Grammy nominees for New Artist of the Ye | annual | 64 | 10 | $309 | 10,667 | 6.0c |
| KXOSCARACTO | Oscar for Best Actor | annual | 11 | 2 | $24 | 8,628 | 7.5c |
| KXOSCARDIR | Oscar for Best Director | annual | 10 | 2 | $489 | 7,644 | 5.5c |
| KXOSCARNOMASPLAY | Best Adapted Screenplay | one_off | 8 | 7 | $45 | 4,803 | 7.3c |
| KXEMMYLIMITEDACTR | Emmy for Movie/Limited Actress | annual | 11 | 3 | $360 | 4,685 | 5.3c |
| KXACTORSONNYCROCKETT | Who will play Sonny Crocket in Miami Vic | one_off | 10 | 3 | $1 | 4,021 | 11.0c |
| KXOSCARNOMSBANIMATEDF | OSCAR NOM FOR BEST ANIMATED FEATURE | one_off | 6 | 6 | $0 | 3,921 | 5.7c |

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
