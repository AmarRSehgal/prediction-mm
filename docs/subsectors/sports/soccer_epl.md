# sports_soccer_epl

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **3** (3 with open markets)
- Open markets: **55** (19 contested)
- Total 24h volume: **$94,253**
- Total open interest: **8,233,099**
- Top-OI mean spread (median across series): **2.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **20**
- Median spread: **2.0c**
- Median TOB bid / ask size: **178 / 164** contracts
- Median depth within 5c of best bid / ask — **3765 / 4090** contracts
- Median depth within 10c of best bid / ask — **4165 / 4433** contracts
- Median depth within 5c of midpoint — bid: **3052** / ask: **3907** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **302**
- Mean informed-signal proxy: **-2.014** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **2.38c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 172 | 1.19 | -1.006 | 11.00 | 53.0 |
| 30d+ | 5864 | 0.92 | -0.357 | 3.00 | 133.7 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPREMIERLEAGUE-26-MCI | Man City | 40c | 1.0c | 2198 | 3236 | 94387 | 199717 | 161053 | 199867 | 1464581 | $62323 | 30d+ |
| KXPREMIERLEAGUE-26-ARS | Arsenal | 60c | 1.0c | 6000 | 66024 | 166717 | 288571 | 166993 | 288571 | 1068814 | $19965 | 30d+ |
| KXEPLTOP4-26-CHE | Chelsea | 8c | 1.0c | 16 | 48 | 4958 | 136 | 7876 | 827 | 152968 | $855 | 30d+ |
| KXEPLTOP4-26-MUN | Man Utd | 88c | 3.0c | 5 | 88 | 1788 | 6351 | 2936 | 13693 | 95630 | $2680 | 30d+ |
| KXEPLTOP4-26-LFC | Liverpool | 45c | 2.0c | 9 | 22 | 54 | 75 | 1025 | 575 | 85626 | $158 | 30d+ |
| KXEPLTOP4-26-AVL | Aston Villa | 64c | 2.0c | 2 | 20 | 22 | 188 | 564 | 212 | 36373 | $977 | 30d+ |
| KXEPLBTTS-26APR19MCIARS | Both Teams To Score | 52c | 1.0c | 335 | 655 | 9137 | 15533 | 15337 | 15833 | 2700 | $1960 | 7-30d |
| KXEPLBTTS-26APR19EVELFC | Both Teams To Score | 58c | 2.0c | 275 | 5862 | 15681 | 15626 | 16281 | 15926 | 1771 | $1706 | 7-30d |
| KXEPLBTTS-26APR22BURMCI | Both Teams To Score | 52c | 4.0c | 10 | 24 | 4928 | 4010 | 5228 | 4310 | 898 | $898 | 7-30d |
| KXEPLBTTS-26APR19AVLSUN | Both Teams To Score | 52c | 1.0c | 275 | 155 | 15737 | 17071 | 16837 | 17371 | 241 | $241 | 7-30d |
| KXEPLBTTS-26APR22BOULEE | Both Teams To Score | 58c | 3.0c | 10 | 131 | 4952 | 3408 | 4952 | 4008 | 109 | $90 | 7-30d |
| KXEPLBTTS-26APR19NFOBUR | Both Teams To Score | 51c | 2.0c | 769 | 2425 | 15374 | 15714 | 15974 | 16014 | 30 | $30 | 7-30d |
| KXEPLBTTS-26APR20CRYWHU | Both Teams To Score | 57c | 2.0c | 632 | 1226 | 3906 | 4255 | 4406 | 4555 | 1 | $0 | 7-30d |
| KXEPLBTTS-26APR25FULAVL | Both Teams To Score | 58c | 7.0c | 110 | 86 | 1120 | 906 | 1150 | 1216 | 0 | $0 | 7-30d |
| KXEPLBTTS-26APR25LFCCRY | Both Teams To Score | 56c | 6.0c | 110 | 179 | 1120 | 989 | 1120 | 1309 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPREMIERLEAGUE | PREMIER LEAGUE | annual | 20 | 2 | $84,939 | 7,500,185 | 1.0c |
| KXEPLTOP4 | EPL top 4 teams | annual | 20 | 3 | $4,670 | 727,521 | 2.3c |
| KXEPLBTTS | EPL Both Teams to Score | custom | 15 | 14 | $4,644 | 5,393 | 2.3c |

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
