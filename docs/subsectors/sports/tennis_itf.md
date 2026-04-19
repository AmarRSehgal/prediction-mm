# sports_tennis_itf

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **346** (346 contested)
- Total 24h volume: **$84,185**
- Total open interest: **100,260**
- Top-OI mean spread (median across series): **14.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **198**
- Median spread: **88.0c**
- Median TOB bid / ask size: **116 / 15** contracts
- Median depth within 5c of best bid / ask — **7675 / 5516** contracts
- Median depth within 10c of best bid / ask — **7675 / 5520** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **7**
- Mean informed-signal proxy: **-4.242** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **7.18c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 3382 | 2.35 | -0.631 | 8.00 | 80.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXITFWMATCH-26APR18KINCHA-CHA | Hanna Chang | nanc | nanc | nan | nan | nan | nan | nan | nan | 43625 | $61334 | 7-30d |
| KXITFWMATCH-26APR18KINCHA-KIN | Hayu Kinoshita | nanc | nanc | nan | nan | nan | nan | nan | nan | 37889 | $42725 | 7-30d |
| KXITFWMATCH-26APR18LIUGAO-GAO | Duanrui Gao | 94c | 4.0c | 1 | 29 | 53 | 4080 | 503 | 4080 | 3352 | $2602 | 7-30d |
| KXITFWMATCH-26APR18LIUGAO-LIU | Le Yi Liu | 4c | 5.0c | 35 | 18 | 7493 | 293 | 7493 | 305 | 1480 | $1192 | 7-30d |
| KXITFMATCH-26APR18TREKAM-TRE | Julien Tremolieres | 24c | 11.0c | 17 | 11 | 54 | 146 | 130 | 149 | 986 | $1745 | 7-30d |
| KXITFWMATCH-26APR18YOSHAS-HAS | Mia Hasegawa | 44c | 79.0c | 500 | 5 | 6000 | 17 | 6000 | 17 | 174 | $106 | 7-30d |
| KXITFWMATCH-26APR18YOSHAS-YOS | Sara Yoshida | 60c | 70.0c | 2 | 20 | 7 | 7981 | 22 | 7981 | 163 | $164 | 7-30d |
| KXITFMATCH-26APR18TREKAM-KAM | Udit Kamboj | 80c | 11.0c | 50 | 13 | 50 | 50 | 134 | 75 | 161 | $421 | 7-30d |
| KXITFWMATCH-26APR18CARROO-ROO | Andrea Roots | 60c | 70.0c | 8 | 25 | 18 | 3013 | 50 | 3013 | 84 | $205 | 7-30d |
| KXITFWMATCH-26APR18SINSIN2-SIN2 | Swasti Singh | 50c | 91.0c | 500 | 8 | 1000 | 2669 | 1000 | 2669 | 81 | $81 | 7-30d |
| KXITFWMATCH-26APR18RATNAY-NAY | Rituparna Nayak | 50c | 91.0c | 500 | 31 | 1000 | 2716 | 1000 | 2716 | 58 | $58 | 7-30d |
| KXITFWMATCH-26APR18RAHGOW-GOW | Lakshmi Gowda | 50c | 91.0c | 500 | 31 | 1000 | 2673 | 1000 | 2673 | 58 | $0 | 7-30d |
| KXITFWMATCH-26APR18IMXLOI-LOI | Liron Loiter | 50c | 91.0c | 500 | 31 | 1000 | 2939 | 1000 | 2939 | 58 | $58 | 7-30d |
| KXITFMATCH-26APR18TOMKUA-KUA | Joshua Yirui KUAN | 46c | 42.0c | 5 | 5 | 11 | 58 | 31 | 58 | 56 | $162 | 7-30d |
| KXITFMATCH-26APR18TOMRIC-TOM | Patrick Toman | 60c | 69.0c | 4 | 5 | 9 | 2593 | 24 | 2593 | 20 | $20 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXITFWMATCH | ITF Women's Match | custom | 160 | 160 | $78,619 | 97,915 | 10.7c |
| KXITFMATCH | ITF Men's Match | custom | 186 | 186 | $5,565 | 2,345 | 18.7c |

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
