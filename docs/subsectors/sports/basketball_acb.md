# sports_basketball_acb

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **10** (10 contested)
- Total 24h volume: **$421**
- Total open interest: **332**
- Top-OI mean spread (median across series): **6.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **10**
- Median spread: **9.0c**
- Median TOB bid / ask size: **500 / 115** contracts
- Median depth within 5c of best bid / ask — **606 / 1558** contracts
- Median depth within 10c of best bid / ask — **614 / 2930** contracts
- Median depth within 5c of midpoint — bid: **366** / ask: **109** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **-6.186** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **10.47c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 19 | 9.64 | -3.214 | 38.15 | 22.3 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXACBGAME-26APR190630MALGRA-MAL | CB Malaga | 73c | 6.0c | 232 | 106 | 338 | 4038 | 338 | 6031 | 168 | $249 | 7-30d |
| KXACBGAME-26APR190600FCBLLE-FCB | FC Barcelona | 73c | 8.0c | 500 | 22 | 606 | 4743 | 606 | 4743 | 129 | $129 | 7-30d |
| KXACBGAME-26APR190600FCBLLE-LLE | Caprabo Lleida | 24c | 5.0c | 2 | 617 | 608 | 1736 | 608 | 1842 | 33 | $41 | 7-30d |
| KXACBGAME-26APR191300CANRMA-RMA | Real Madrid | 78c | 9.0c | 3 | 104 | 503 | 104 | 607 | 8554 | 3 | $3 | 7-30d |
| KXACBGAME-26APR190630MALGRA-GRA | CB Granada | 22c | 6.0c | 500 | 433 | 606 | 1522 | 616 | 1628 | 2 | $2 | 7-30d |
| KXACBGAME-26APR191300CANRMA-CAN | CB 1939 Canarias | 25c | 13.0c | 604 | 72 | 604 | 1364 | 619 | 1364 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191200VALBAS-VAL | Valencia Basket | 74c | 9.0c | 500 | 111 | 500 | 111 | 611 | 7406 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191200VALBAS-BAS | Basquet Girona | 28c | 14.0c | 111 | 615 | 611 | 1444 | 621 | 1444 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191100BRESPB-SPB | CB San Pablo Burgos | 69c | 10.0c | 500 | 119 | 619 | 4017 | 619 | 4017 | 0 | $0 | 7-30d |
| KXACBGAME-26APR191100BRESPB-BRE | CB Breogan | 33c | 14.0c | 619 | 798 | 619 | 1595 | 619 | 1595 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXACBGAME | Liga ACB Basketball Game | custom | 10 | 10 | $421 | 332 | 6.7c |

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
