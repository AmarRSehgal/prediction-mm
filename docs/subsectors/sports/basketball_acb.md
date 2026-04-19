# sports_basketball_acb

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **10** (10 contested)
- Total 24h volume: **$228**
- Total open interest: **207**
- Top-OI mean spread (median across series): **10.0 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **10**
- Median spread: **15.0c**
- Median TOB bid / ask size: **500 / 676** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **500** / ask: **3177** contracts
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 17 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXACBGAME-26APR190630MALGRA-MAL | CB Malaga | 73c | 6.0c | 272 | 178 | 272 | 178 | 168 | $181 | 7-30d |
| KXACBGAME-26APR190600FCBLLE-LLE | Caprabo Lleida | 24c | 6.0c | 500 | 626 | 500 | 1182 | 33 | $41 | 7-30d |
| KXACBGAME-26APR190600FCBLLE-FCB | FC Barcelona | 74c | 9.0c | 540 | 1335 | 540 | 1335 | 4 | $4 | 7-30d |
| KXACBGAME-26APR190630MALGRA-GRA | CB Granada | 23c | 6.0c | 398 | 439 | 398 | 1543 | 2 | $2 | 7-30d |
| KXACBGAME-26APR191300CANRMA-RMA | Real Madrid | 80c | 18.0c | 500 | 3636 | 0 | 0 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191300CANRMA-CAN | CB 1939 Canarias | 26c | 15.0c | 500 | 606 | 0 | 0 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191200VALBAS-VAL | Valencia Basket | 77c | 18.0c | 500 | 2857 | 0 | 0 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191200VALBAS-BAS | Basquet Girona | 30c | 15.0c | 500 | 635 | 0 | 0 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191100BRESPB-SPB | CB San Pablo Burgos | 73c | 18.0c | 540 | 2262 | 0 | 0 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191100BRESPB-BRE | CB Breogan | 34c | 15.0c | 500 | 718 | 0 | 0 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXACBGAME | Liga ACB Basketball Game | custom | 10 | 10 | $228 | 207 | 10.0c |

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
