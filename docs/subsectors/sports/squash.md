# sports_squash

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **126** (5 contested)
- Total 24h volume: **$1,424**
- Total open interest: **78,503**
- Top-OI mean spread (median across series): **1.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **6**
- Median spread: **1.5c**
- Median TOB bid / ask size: **2318 / 5011** contracts
- Median depth within 5c of best bid / ask — **3648 / 6766** contracts
- Median depth within 10c of best bid / ask — **4245 / 6766** contracts
- Median depth within 5c of midpoint — bid: **3638** / ask: **6766** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **72**
- Mean informed-signal proxy: **-0.487** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **3.79c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 433 | 3.43 | -0.506 | 21.70 | 218.9 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPSASQUASH-26M-MAELS | Marwan ElShorbagy | 7c | 1.0c | 15958 | 20035 | 23843 | 26136 | 30961 | 26136 | 31572 | $435 | 30d+ |
| KXPSASQUASH-26M-MASA | Mostafa Asal | 50c | 1.0c | 8388 | 9521 | 11988 | 12952 | 12038 | 12952 | 6126 | $972 | 30d+ |
| KXPSASQUASH-26M-DELI | Diego Elias | 36c | 1.0c | 4373 | 11529 | 6903 | 14767 | 6936 | 14807 | 4243 | $751 | 30d+ |
| KXPSASQUASH-26W-AORF | Amina Orfi | 10c | 2.0c | 12 | 180 | 394 | 518 | 1555 | 518 | 2077 | $0 | 30d+ |
| KXPSASQUASH-26W-HELH | Hania El Hammamy | 42c | 3.0c | 10 | 501 | 173 | 579 | 173 | 579 | 1684 | $16 | 30d+ |
| KXPSASQUASH-26W-NELS | Nour ElSherbini | 36c | 2.0c | 263 | 327 | 263 | 348 | 263 | 348 | 1645 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPSASQUASH | Professional Squash Association (PSA) Wo | annual | 126 | 5 | $1,424 | 78,503 | 1.3c |

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
