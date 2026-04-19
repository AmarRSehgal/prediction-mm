# ent_music

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **84** (84 with open markets)
- Open markets: **1990** (663 contested)
- Total 24h volume: **$208,824**
- Total open interest: **1,801,675**
- Top-OI mean spread (median across series): **9.3 cents**
- **MM profile: Moderate (mixed)**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **41 / 78** contracts
- Median cumulative depth within 5c of mid — bid: **94** / ask: **121** contracts
- Median cumulative depth within 10c of mid — bid: **569** / ask: **612** contracts
- Mean trades per market (last 3000): **161**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 6-12h | 41 | 0.00 | 0.000 | 0.00 | 0.0 |
| 12-24h | 58 | 0.00 | 0.000 | 0.00 | 0.0 |
| 1-3d | 43 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 136 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 5899 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 26031 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCANAL-29 | During Trump's term | 33c | 2.0c | 525 | 517 | 20201 | 2364 | 91086 | $207 | 30d+ |
| KXSPOTIFYALBUMRELEASEDATEDRAKE-26-MAY01 | Before May | 24c | 1.0c | 221 | 43 | 1722 | 2709 | 68046 | $9375 | 7-30d |
| KXFEATUREDRAKE-27-FUT | Future | 52c | 5.0c | 3996 | 112 | 3996 | 154 | 45378 | $407 | 30d+ |
| KXTOPARTIST-26B-BAD | Bad Bunny | 74c | 2.0c | 1468 | 324 | 3595 | 350 | 39449 | $91 | 30d+ |
| KXWTAMATCH-26APR19KOSPOD-POD | Veronika Podrez | 16c | 1.0c | 79 | 6424 | 29547 | 40020 | 33780 | $34108 | 7-30d |
| KXTOPARTISTUSA-26-DRA | :: | 72c | 1.0c | 1273 | 9 | 3276 | 1518 | 33044 | $654 | 30d+ |
| KXWTAMATCH-26APR19RYBMUC-RYB | Elena Rybakina | 70c | 1.0c | 250 | 20992 | 38992 | 50263 | 30526 | $30356 | 7-30d |
| KXLLAMA5-27 | Before 2027 | 24c | 5.0c | 515 | 21 | 515 | 21 | 26277 | $201 | 30d+ |
| KXTOPARTISTUSA-26-BAD | :: | 21c | 2.0c | 1587 | 640 | 2761 | 2159 | 26168 | $277 | 30d+ |
| KXTOPARTIST-26B-DRA | Drake | 8c | 1.0c | 27 | 223 | 1071 | 1758 | 22873 | $350 | 30d+ |
| KXWTAMATCH-26APR19KOSPOD-KOS | Marta Kostyuk | 84c | 1.0c | 9874 | 307 | 24435 | 46413 | 21535 | $50244 | 7-30d |
| KXSPOTIFYMAU-26JUL-780 | above 780 Million | 8c | 1.0c | 16447 | 8838 | 30598 | 15440 | 19287 | $156 | 30d+ |
| KXRANKLISTSONGSPOTUSA-26MAY01-NOA | :: | 38c | 1.0c | 1 | 60 | 1 | 1635 | 18794 | $505 | 7-30d |
| KXTOPARTISTUSA-26-TAY | :: | 7c | 1.0c | 3816 | 1078 | 5642 | 2587 | 18669 | $23 | 30d+ |
| KXSPOTIFYALBUMRELEASEDATEDRAKE-26-JUN01-26 | Before June | 66c | 1.0c | 41 | 425 | 563 | 1223 | 17938 | $3622 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTOPARTISTUSA | TOP ARTIST USA | one_off | 16 | 2 | $1,362 | 175,093 | 1.5c |
| KXTOPARTIST | Top Artist on Spotify | annual | 10 | 1 | $781 | 144,803 | 2.0c |
| KX1ALBUM | WHO WILL HAVE A NUMBER 1 ALBUM ON THE BI | one_off | 107 | 55 | $5,274 | 120,828 | 7.7c |
| KXALBUMRELEASE | WHO WILL RELEASE A NEW ALBUM | one_off | 101 | 92 | $1,565 | 106,520 | 12.7c |
| KX1SONG | WILL ARTIST HAVE A NUMBER ONE SONG ON BI | annual | 115 | 37 | $4,211 | 97,709 | 4.3c |
| KXSPOTIFYALBUMRELEASEDATEDRAKE | Will drake release an album by date | one_off | 4 | 4 | $14,171 | 91,665 | 2.0c |
| KXCANAL | Panama Canal retaken | custom | 1 | 1 | $207 | 91,086 | 2.0c |
| KXRANKLISTSONGSPOTUSA | WHO WIL HAVE A #1 song on Spotify  | monthly | 36 | 4 | $4,052 | 90,804 | 3.0c |
| KXFEATUREDRAKE | Who will be featured on Drake album | one_off | 21 | 18 | $1,034 | 84,544 | 7.0c |
| KXWTAMATCH | WTA Tennis Match | custom | 4 | 4 | $114,130 | 76,800 | 1.7c |

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
