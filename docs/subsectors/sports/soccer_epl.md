# sports_soccer_epl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **55** (20 contested)
- Total 24h volume: **$86,946**
- Total open interest: **8,227,316**
- Top-OI mean spread (median across series): **2.0 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **20**
- Median spread: **2.0c**
- Median TOB bid / ask size: **178 / 130** contracts
- Median cumulative depth within 5c of mid — bid: **3494** / ask: **3874** contracts
- Median cumulative depth within 10c of mid — bid: **4655** / ask: **4426** contracts
- Mean trades per market (last 3000): **513**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 136 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 10116 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPREMIERLEAGUE-26-MCI | Man City | 40c | 1.0c | 42299 | 12 | 102623 | 125539 | 1464752 | $62217 | 30d+ |
| KXPREMIERLEAGUE-26-ARS | Arsenal | 60c | 1.0c | 6000 | 66777 | 113472 | 295536 | 1068685 | $19212 | 30d+ |
| KXEPLTOP4-26-CHE | Chelsea | 8c | 1.0c | 16 | 48 | 16 | 336 | 152968 | $1034 | 30d+ |
| KXEPLTOP4-26-MUN | Man Utd | 88c | 2.0c | 44 | 44 | 1239 | 6407 | 95630 | $2680 | 30d+ |
| KXEPLTOP4-26-LFC | Liverpool | 45c | 2.0c | 9 | 201 | 157 | 254 | 85626 | $158 | 30d+ |
| KXEPLTOP4-26-AVL | Aston Villa | 66c | 3.0c | 24 | 24 | 43 | 307 | 36368 | $987 | 30d+ |
| KXEPLBTTS-26APR19MCIARS | Both Teams To Score | 52c | 2.0c | 275 | 420 | 9950 | 14856 | 1920 | $1191 | 7-30d |
| KXEPLBTTS-26APR19EVELFC | Both Teams To Score | 57c | 1.0c | 415 | 310 | 13447 | 15077 | 654 | $654 | 7-30d |
| KXEPLBTTS-26APR22BOULEE | Both Teams To Score | 58c | 3.0c | 10 | 111 | 4152 | 3288 | 109 | $90 | 7-30d |
| KXEPLBTTS-26APR19AVLSUN | Both Teams To Score | 50c | 1.0c | 2027 | 182 | 13844 | 14461 | 34 | $34 | 7-30d |
| KXEPLBTTS-26APR19NFOBUR | Both Teams To Score | 51c | 2.0c | 1164 | 158 | 14141 | 15382 | 6 | $6 | 7-30d |
| KXEPLBTTS-26APR22BURMCI | Both Teams To Score | 52c | 4.0c | 10 | 10 | 4018 | 3796 | 1 | $1 | 7-30d |
| KXEPLBTTS-26APR20CRYWHU | Both Teams To Score | 57c | 2.0c | 632 | 1226 | 3806 | 4055 | 1 | $0 | 7-30d |
| KXEPLBTTS-26APR25FULAVL | Both Teams To Score | 58c | 7.0c | 110 | 134 | 220 | 544 | 0 | $0 | 7-30d |
| KXEPLBTTS-26APR25LFCCRY | Both Teams To Score | 56c | 6.0c | 110 | 111 | 420 | 521 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPREMIERLEAGUE | PREMIER LEAGUE | annual | 20 | 2 | $81,034 | 7,497,928 | 1.0c |
| KXEPLTOP4 | EPL top 4 teams | annual | 20 | 3 | $4,967 | 727,497 | 2.3c |
| KXEPLBTTS | EPL Both Teams to Score | custom | 15 | 15 | $945 | 1,890 | 2.0c |

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
