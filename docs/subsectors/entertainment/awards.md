# ent_awards

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **36** (36 with open markets)
- Open markets: **420** (128 contested)
- Total 24h volume: **$29,444**
- Total open interest: **721,362**
- Top-OI mean spread (median across series): **6.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **100 / 100** contracts
- Median depth within 5c of best bid / ask — **329 / 454** contracts
- Median depth within 10c of best bid / ask — **348 / 500** contracts
- Median depth within 5c of midpoint — bid: **275** / ask: **300** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **42**
- Mean informed-signal proxy: **-1.053** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.85c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 8474 | 2.22 | -0.556 | 8.00 | 57.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBOND-30-CAL | Callum Turner | 45c | 2.0c | 101 | 9 | 751 | 4845 | 751 | 4845 | 112154 | $815 | 30d+ |
| KXBOND-30-ATJ | Aaron Taylor-Johnson | 18c | 2.0c | 238 | 4576 | 738 | 6332 | 888 | 6883 | 67721 | $577 | 30d+ |
| KXBOND-30-JACO | Jacob Elordi | 22c | 3.0c | 465 | 3686 | 1065 | 5858 | 1065 | 5858 | 49524 | $460 | 30d+ |
| KXOSCARPIC-27-ODY | The Odyssey:: | 29c | 3.0c | 424 | 56 | 6247 | 5217 | 6248 | 5232 | 38122 | $944 | 30d+ |
| KXOSCARPIC-27-PRO | Project Hail Mary:: | 8c | 3.0c | 186 | 352 | 11066 | 8158 | 30643 | 11828 | 36528 | $4270 | 30d+ |
| KXOSCARPIC-27-DUN | Dune: Part Three:: | 8c | 2.0c | 57 | 865 | 2577 | 3447 | 6476 | 3448 | 31397 | $3795 | 30d+ |
| KXBOND-30-JOS | Josh O'Connor | 9c | 2.0c | 480 | 4979 | 1437 | 7650 | 4265 | 7650 | 25318 | $80 | 30d+ |
| KXOSCARPIC-27-SOC | The Social Reckoning:: | 8c | 2.0c | 345 | 995 | 3440 | 4856 | 21445 | 6846 | 21863 | $595 | 30d+ |
| KXOSCARPIC-27-DIG | Digger:: | 7c | 2.0c | 720 | 3929 | 7863 | 7838 | 7863 | 8026 | 15608 | $25 | 30d+ |
| KXBOND-30-TOMH | Tom Holland | 5c | 4.0c | 250 | 5 | 1149 | 743 | 1149 | 743 | 14337 | $1708 | 30d+ |
| KXACTORWHITELOTUS-27-DEE | Deepika Padukone | 18c | 7.0c | 22 | 110 | 234 | 310 | 234 | 310 | 4942 | $0 | 30d+ |
| KXOSCARPIC-27-WIL | Wild Horse Nine:: | 8c | 4.0c | 875 | 4440 | 8672 | 11543 | 8672 | 12145 | 4879 | $0 | 30d+ |
| KXACTORWHITELOTUS-27-JOD | Jodie Comer | 7c | 2.0c | 62 | 109 | 1020 | 309 | 1020 | 309 | 4308 | $0 | 30d+ |
| KXOSCARACTO-27-JOH | John Malkovich:: Wild Horse Nine | 26c | 8.0c | 122 | 409 | 322 | 662 | 322 | 662 | 4225 | $133 | 30d+ |
| KXEMMYTVMOVIE-26SEP14-PEAK | Peaky Blinders: The Immortal Man::   | 18c | 3.0c | 15 | 144 | 315 | 244 | 315 | 444 | 3631 | $3209 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXBOND | Next Bond actor | custom | 20 | 3 | $4,050 | 407,437 | 2.3c |
| KXOSCARPIC | Oscar for Best Picture | annual | 26 | 1 | $12,671 | 208,546 | 3.0c |
| KXACTORWHITELOTUS | WHO WILL BE THE ACTOR IN WHITELOTUS | one_off | 23 | 7 | $9 | 14,397 | 6.3c |
| KXGRAMMYNOMNAOTY | Grammy nominees for New Artist of the Ye | annual | 64 | 10 | $309 | 10,667 | 6.3c |
| KXOSCARACTO | Oscar for Best Actor | annual | 11 | 2 | $160 | 8,485 | 7.5c |
| KXOSCARDIR | Oscar for Best Director | annual | 10 | 2 | $492 | 7,644 | 4.5c |
| KXOSCARNOMASPLAY | Best Adapted Screenplay | one_off | 8 | 7 | $45 | 4,803 | 7.3c |
| KXEMMYLIMITEDACTR | Emmy for Movie/Limited Actress | annual | 11 | 3 | $371 | 4,685 | 4.7c |
| KXEMMYTVMOVIE | Emmy Award for TV Movie  | annual | 11 | 2 | $3,561 | 4,031 | 3.5c |
| KXACTORSONNYCROCKETT | Who will play Sonny Crocket in Miami Vic | one_off | 10 | 3 | $1 | 4,021 | 11.0c |

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
