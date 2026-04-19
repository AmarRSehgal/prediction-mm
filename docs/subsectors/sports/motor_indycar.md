# sports_motor_indycar

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **9** (9 contested)
- Total 24h volume: **$37,210**
- Total open interest: **65,545**
- Top-OI mean spread (median across series): **2.7 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **9**
- Median spread: **3.0c**
- Median TOB bid / ask size: **83 / 649** contracts
- Median depth within 5c of best bid / ask — **1153 / 1128** contracts
- Median depth within 10c of best bid / ask — **2599 / 1328** contracts
- Median depth within 5c of midpoint — bid: **296** / ask: **1128** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **123**
- Mean informed-signal proxy: **-0.216** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **1.53c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 609 | 1.43 | -0.071 | 7.95 | 86.8 |
| 30d+ | 495 | 2.61 | -0.984 | 10.00 | 50.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXINDYCARSERIES-NTTICS26-APAL | Alex Palou | 64c | 3.0c | 46 | 878 | 296 | 1128 | 296 | 1128 | 12467 | $47 | 30d+ |
| KXINDYCARRACE-BEAC26-PAOW | Pato O’Ward | 7c | 3.0c | 83 | 83 | 4197 | 483 | 4197 | 983 | 8597 | $6418 | 7-30d |
| KXINDYCARRACE-BEAC26-KYKI | Kyle Kirkwood | 30c | 3.0c | 83 | 663 | 249 | 989 | 374 | 2156 | 7321 | $9812 | 7-30d |
| KXINDYCARRACE-BEAC26-SCMC | Scott McLaughlin | 6c | 1.0c | 25076 | 465 | 30660 | 1328 | 30660 | 1328 | 6974 | $3915 | 7-30d |
| KXINDYCARSERIES-NTTICS26-KKIR | Kyle Kirkwood | 15c | 3.0c | 19 | 906 | 269 | 1220 | 314 | 1220 | 6436 | $277 | 30d+ |
| KXINDYCARRACE-BEAC26-SCDI | Scott Dixon | 7c | 1.0c | 70 | 649 | 1153 | 1398 | 4532 | 1398 | 6097 | $4230 | 7-30d |
| KXINDYCARRACE-BEAC26-FERO | Felix Rosenqvist | 6c | 3.0c | 2 | 511 | 2599 | 3753 | 2599 | 3753 | 6046 | $4848 | 7-30d |
| KXINDYCARRACE-BEAC26-WIPO | Will Power | 7c | 2.0c | 490 | 83 | 4686 | 822 | 4686 | 1262 | 5843 | $2859 | 7-30d |
| KXINDYCARRACE-BEAC26-ALPA | Alex Palou | 26c | 3.0c | 83 | 659 | 766 | 825 | 766 | 2228 | 5766 | $4804 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXINDYCARRACE | Pato O’Ward | nan | 7 | 7 | $36,887 | 46,643 | 2.3c |
| KXINDYCARSERIES | Alex Palou | nan | 2 | 2 | $324 | 18,903 | 3.0c |

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
