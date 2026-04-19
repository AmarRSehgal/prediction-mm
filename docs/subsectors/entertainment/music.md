# ent_music

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **84** (84 with open markets)
- Open markets: **1942** (662 contested)
- Total 24h volume: **$238,437**
- Total open interest: **1,838,718**
- Top-OI mean spread (median across series): **9.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **7.0c**
- Median TOB bid / ask size: **46 / 74** contracts
- Median depth within 5c of best bid / ask — **536 / 586** contracts
- Median depth within 10c of best bid / ask — **904 / 835** contracts
- Median depth within 5c of midpoint — bid: **100** / ask: **124** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **138**
- Mean informed-signal proxy: **-1.256** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.80c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 37 | 5.47 | -0.344 | 18.70 | 127.4 |
| 3-7d | 82 | 5.73 | 1.234 | 30.00 | 116.4 |
| 7-30d | 3833 | 1.59 | -0.551 | 6.10 | 73.4 |
| 30d+ | 23592 | 2.73 | -0.903 | 11.00 | 36.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXCANAL-29 | During Trump's term | 33c | 2.0c | 525 | 514 | 21226 | 2365 | 23934 | 4018 | 91086 | $279 | 30d+ |
| KXSPOTIFYALBUMRELEASEDATEDRAKE-26-MAY01 | Before May | 24c | 1.0c | 254 | 33 | 1837 | 1889 | 2870 | 1889 | 68054 | $8752 | 7-30d |
| KXWTAMATCH-26APR19RYBMUC-RYB | Elena Rybakina | 70c | 1.0c | 261 | 4014 | 43825 | 43220 | 44901 | 54723 | 56438 | $56781 | 7-30d |
| KXFEATUREDRAKE-27-FUT | Future | 53c | 6.0c | 3996 | 112 | 4301 | 134 | 14690 | 506 | 45378 | $403 | 30d+ |
| KXTOPARTIST-26B-BAD | Bad Bunny | 74c | 2.0c | 1468 | 324 | 3610 | 325 | 5632 | 567 | 39449 | $86 | 30d+ |
| KXWTAMATCH-26APR19KOSPOD-POD | Veronika Podrez | 15c | 1.0c | 12921 | 86 | 34916 | 56840 | 37248 | 56851 | 39402 | $39878 | 7-30d |
| KXTOPARTISTUSA-26-DRA | :: | 72c | 1.0c | 1270 | 9 | 3273 | 1511 | 4273 | 1570 | 33043 | $655 | 30d+ |
| KXWTAMATCH-26APR19KOSPOD-KOS | Marta Kostyuk | 86c | 1.0c | 617 | 10367 | 36304 | 51155 | 37324 | 53543 | 27830 | $63867 | 7-30d |
| KXLLAMA5-27 | Before 2027 | 24c | 5.0c | 515 | 41 | 515 | 600 | 726 | 2656 | 26277 | $201 | 30d+ |
| KXTOPARTISTUSA-26-BAD | :: | 21c | 2.0c | 1587 | 628 | 2761 | 2139 | 2798 | 2139 | 26168 | $258 | 30d+ |
| KXTOPARTIST-26B-DRA | Drake | 7c | 1.0c | 1005 | 4 | 2050 | 1764 | 3458 | 3047 | 22873 | $350 | 30d+ |
| KXSPOTIFYMAU-26JUL-780 | above 780 Million | 8c | 1.0c | 14572 | 8674 | 33365 | 15442 | 34801 | 15442 | 19287 | $156 | 30d+ |
| KXRANKLISTSONGSPOTUSA-26MAY01-NOA | :: | 38c | 2.0c | 15 | 14 | 36 | 1509 | 506 | 1509 | 18820 | $434 | 7-30d |
| KXTOPARTISTUSA-26-TAY | :: | 7c | 1.0c | 3816 | 1048 | 5642 | 2557 | 9669 | 2899 | 18699 | $53 | 30d+ |
| KXSPOTIFYALBUMRELEASEDATEDRAKE-26-JUN01-26 | Before June | 66c | 1.0c | 58 | 438 | 599 | 1232 | 684 | 1232 | 17932 | $3260 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXTOPARTISTUSA | TOP ARTIST USA | one_off | 16 | 2 | $1,884 | 175,141 | 1.5c |
| KXTOPARTIST | Top Artist on Spotify | annual | 10 | 1 | $626 | 144,803 | 2.0c |
| KXWTAMATCH | WTA Tennis Match | custom | 4 | 4 | $163,885 | 126,658 | 1.0c |
| KX1ALBUM | WHO WILL HAVE A NUMBER 1 ALBUM ON THE BI | one_off | 107 | 55 | $5,760 | 121,209 | 7.0c |
| KXALBUMRELEASE | WHO WILL RELEASE A NEW ALBUM | one_off | 101 | 92 | $1,763 | 106,715 | 12.7c |
| KX1SONG | WILL ARTIST HAVE A NUMBER ONE SONG ON BI | annual | 115 | 37 | $3,210 | 97,709 | 4.3c |
| KXSPOTIFYALBUMRELEASEDATEDRAKE | Will drake release an album by date | one_off | 4 | 4 | $12,624 | 91,405 | 1.3c |
| KXRANKLISTSONGSPOTUSA | WHO WIL HAVE A #1 song on Spotify  | monthly | 36 | 4 | $4,140 | 91,258 | 2.7c |
| KXCANAL | Panama Canal retaken | custom | 1 | 1 | $279 | 91,086 | 2.0c |
| KXFEATUREDRAKE | Who will be featured on Drake album | one_off | 21 | 18 | $974 | 84,544 | 6.7c |

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
