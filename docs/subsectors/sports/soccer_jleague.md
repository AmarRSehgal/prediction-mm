# sports_soccer_jleague

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **12** (12 contested)
- Total 24h volume: **$1,958**
- Total open interest: **1,671**
- Top-OI mean spread (median across series): **1.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **12**
- Median spread: **2.0c**
- Median TOB bid / ask size: **1065 / 1594** contracts
- Median cumulative depth within 5c of mid — bid: **4799** / ask: **4668** contracts
- Median cumulative depth within 10c of mid — bid: **5239** / ask: **5023** contracts
- Mean trades per market (last 3000): **13**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 153 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXJLEAGUEGAME-26APR19GAMFAG-GAM | Gamba | 49c | 2.0c | 1807 | 1759 | 4944 | 5040 | 809 | $803 | 7-30d |
| KXJLEAGUEGAME-26APR19MITREY-MIT | Mito H | 21c | 1.0c | 1 | 10371 | 12255 | 18048 | 601 | $494 | 7-30d |
| KXJLEAGUEGAME-26APR19MITREY-REY | Kashiwa | 51c | 2.0c | 3304 | 2760 | 12419 | 11460 | 378 | $714 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-NGE | Nagoya | 50c | 2.0c | 1657 | 1687 | 4535 | 4993 | 144 | $144 | 7-30d |
| KXJLEAGUEGAME-26APR19GAMFAG-FAG | Fagiano O | 24c | 1.0c | 1618 | 309 | 4655 | 4526 | 135 | $136 | 7-30d |
| KXJLEAGUEGAME-26APR19MITREY-TIE | Tie | 28c | 2.0c | 4867 | 3596 | 8651 | 9167 | 33 | $33 | 7-30d |
| KXJLEAGUEGAME-26APR19GAMFAG-TIE | Tie | 28c | 1.0c | 159 | 1500 | 6352 | 4099 | 33 | $33 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-AVI | Avispa | 24c | 1.0c | 1653 | 336 | 6784 | 3712 | 22 | $38 | 7-30d |
| KXJLEAGUEGAME-26APR19NGEAVI-TIE | Tie | 28c | 1.0c | 1 | 1786 | 3954 | 4810 | 4 | $4 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-TIE | Tie | 42c | 76.0c | 512 | 10 | 0 | 0 | 0 | $0 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-GAM | Gamba | 42c | 76.0c | 512 | 10 | 0 | 0 | 0 | $0 | 7-30d |
| KXJLEAGUEGAME-26APR22GAMAVI-AVI | Avispa | 42c | 76.0c | 512 | 10 | 0 | 0 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXJLEAGUEGAME | Japan J League Game | custom | 12 | 12 | $1,958 | 1,671 | 1.3c |

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
