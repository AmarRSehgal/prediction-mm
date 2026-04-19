# sports_esports_lol

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **1** (1 with open markets)
- Open markets: **36** (36 contested)
- Total 24h volume: **$1,573**
- Total open interest: **1,619**
- Top-OI mean spread (median across series): **22.7 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **36**
- Median spread: **11.0c**
- Median TOB bid / ask size: **500 / 500** contracts
- Median depth within 5c of best bid / ask — **1495 / 1107** contracts
- Median depth within 10c of best bid / ask — **1519 / 1146** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **2**
- Mean informed-signal proxy: **3.412** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **4.56c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 67 | 3.05 | 0.250 | 13.10 | 28.6 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXLOLTOTALMAPS-26APR190400NSBRO-3 | Over 2.5 maps | 44c | 59.0c | 1 | 1 | 1 | 2 | 2 | 3 | 858 | $766 | 7-30d |
| KXLOLTOTALMAPS-26APR190600T1DRX-3 | Over 2.5 maps | 36c | 2.0c | 216 | 197 | 5704 | 4821 | 5704 | 10148 | 446 | $661 | 7-30d |
| KXLOLTOTALMAPS-26APR191100GXVIT-3 | Over 2.5 maps | 48c | 7.0c | 1528 | 119 | 2028 | 1646 | 2028 | 1646 | 93 | $43 | 7-30d |
| KXLOLTOTALMAPS-26APR200500OMGWB-3 | Over 2.5 maps | 38c | 13.0c | 500 | 500 | 1000 | 1000 | 1000 | 1000 | 86 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR190500IGTES-3 | Over 2.5 maps | 50c | 5.0c | 49 | 1199 | 549 | 1199 | 1541 | 1199 | 66 | $66 | 7-30d |
| KXLOLTOTALMAPS-26APR190700ALBLG-3 | Over 2.5 maps | 44c | 5.0c | 996 | 112 | 2246 | 1910 | 2246 | 1910 | 45 | $31 | 7-30d |
| KXLOLTOTALMAPS-26APR190730GZGAM-3 | Over 2.5 maps | 49c | 4.0c | 500 | 644 | 2493 | 2642 | 2493 | 2642 | 25 | $6 | 7-30d |
| KXLOLTOTALMAPS-26APR201100G2SHFT-3 | Over 2.5 maps | 50c | 69.0c | 1 | 1 | 1 | 25 | 2 | 25 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR211100SLYGAL-5 | Over 4.5 maps | 40c | 7.0c | 500 | 128 | 1994 | 2124 | 1994 | 2124 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR211100SLYGAL-4 | Over 3.5 maps | 76c | 13.0c | 500 | 500 | 1000 | 1000 | 1000 | 1024 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR201315KCSK-3 | Over 2.5 maps | 35c | 10.0c | 500 | 138 | 1994 | 2128 | 1994 | 2128 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR200400NSEAGENGA-3 | Over 2.5 maps | 36c | 11.0c | 992 | 500 | 1992 | 1179 | 1992 | 1179 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR200700IGBLG-3 | Over 2.5 maps | 38c | 13.0c | 500 | 500 | 1000 | 1000 | 1000 | 1000 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR191200LEVLLL-3 | Over 2.5 maps | 40c | 6.0c | 500 | 500 | 2497 | 2496 | 2497 | 2496 | 0 | $0 | 7-30d |
| KXLOLTOTALMAPS-26APR200600KTCFOXY-3 | Over 2.5 maps | 43c | 12.0c | 991 | 671 | 1991 | 2162 | 1991 | 2162 | 0 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXLOLTOTALMAPS | Over 2.5 maps | nan | 36 | 36 | $1,573 | 1,619 | 22.7c |

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
