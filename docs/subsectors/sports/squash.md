# sports_squash

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **126** (5 contested)
- Total 24h volume: **$3,879**
- Total open interest: **78,465**
- Top-OI mean spread (median across series): **1.3 cents**
- **MM profile: HFT-saturated**

## Book depth (from comprehensive scan)

- Markets sampled: **7**
- Median spread: **2.0c**
- Median TOB bid / ask size: **263 / 501** contracts
- Median cumulative depth within 5c of mid — bid: **3044** / ask: **1100** contracts
- Median cumulative depth within 10c of mid — bid: **3044** / ask: **1100** contracts
- Mean trades per market (last 3000): **65**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 30d+ | 457 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXPSASQUASH-26M-MAELS | Marwan ElShorbagy | 7c | 1.0c | 15858 | 19534 | 23743 | 25635 | 31572 | $435 | 30d+ |
| KXPSASQUASH-26M-MZAK | Mohamad Zakaria | 5c | 3.0c | 44 | 100 | 3044 | 1100 | 8286 | $0 | 30d+ |
| KXPSASQUASH-26M-MASA | Mostafa Asal | 50c | 1.0c | 8096 | 9410 | 12002 | 12841 | 6088 | $935 | 30d+ |
| KXPSASQUASH-26M-DELI | Diego Elias | 36c | 1.0c | 6598 | 12329 | 9108 | 15329 | 3492 | $0 | 30d+ |
| KXPSASQUASH-26W-AORF | Amina Orfi | 10c | 2.0c | 12 | 85 | 394 | 423 | 2077 | $0 | 30d+ |
| KXPSASQUASH-26W-HELH | Hania El Hammamy | 42c | 3.0c | 10 | 501 | 32 | 579 | 1684 | $16 | 30d+ |
| KXPSASQUASH-26W-NELS | Nour ElSherbini | 36c | 2.0c | 263 | 327 | 263 | 348 | 1645 | $0 | 30d+ |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXPSASQUASH | Professional Squash Association (PSA) Wo | annual | 126 | 5 | $3,879 | 78,465 | 1.3c |

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
