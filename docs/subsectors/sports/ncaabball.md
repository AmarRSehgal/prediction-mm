# sports_ncaabball

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **5** (5 with open markets)
- Open markets: **205** (52 contested)
- Total 24h volume: **$122,200**
- Total open interest: **2,389,412**
- Top-OI mean spread (median across series): **33.0 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **58**
- Median spread: **89.5c**
- Median TOB bid / ask size: **300 / 5** contracts
- Median depth within 5c of best bid / ask — **1300 / 605** contracts
- Median depth within 10c of best bid / ask — **1578 / 605** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **118**
- Mean informed-signal proxy: **-4.638** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **8.05c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 142 | 11.46 | -1.659 | 72.00 | 42.6 |
| 3-7d | 23 | 0.88 | -0.294 | 2.20 | 56.5 |
| 30d+ | 6768 | 0.66 | -0.365 | 2.30 | 115.8 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXMARMAD-27-MICH | Michigan | 15c | 1.0c | 4891 | 906 | 43360 | 49022 | 46890 | 52373 | 115894 | $7669 | 30d+ |
| KXNCAABASEBALL-26-TEX | Texas | 10c | 2.0c | 882 | 4769 | 11603 | 12126 | 17152 | 12126 | 110937 | $575 | 30d+ |
| KXNCAABASEBALL-26-UCLA | UCLA | 15c | 1.0c | 1045 | 169 | 1946 | 8761 | 2449 | 8885 | 108377 | $1673 | 30d+ |
| KXNCAABASEBALL-26-GT | Georgia Tech | 12c | 1.0c | 19 | 88 | 4405 | 9693 | 9018 | 10193 | 78333 | $4058 | 30d+ |
| KXMARMAD-27-DUKE | Duke | 11c | 2.0c | 9361 | 770 | 16004 | 26905 | 7837177 | 51587 | 58223 | $4222 | 30d+ |
| KXNCAABASEBALL-26-TXAM | Texas A&M | 6c | 1.0c | 219 | 788 | 9880 | 7412 | 9880 | 7412 | 56852 | $1898 | 30d+ |
| KXNCAABASEBALL-26-UGA | Georgia | 6c | 1.0c | 22 | 1953 | 4381 | 5983 | 4381 | 5983 | 52986 | $561 | 30d+ |
| KXNCAABASEBALL-26-UNC | North Carolina | 6c | 1.0c | 16148 | 3157 | 24285 | 3211 | 24285 | 3711 | 47619 | $2292 | 30d+ |
| KXMARMAD-27-ILL | Illinois | 8c | 2.6c | 268 | 1000 | 21250 | 16735 | 10053437 | 21094 | 40657 | $4263 | 30d+ |
| KXMARMAD-27-CONN | UConn | 9c | 2.9c | 98 | 500 | 10858 | 31800 | 10415825 | 56045 | 36611 | $16463 | 30d+ |
| KXMARMAD-27-FLA | Florida | 8c | 3.3c | 200 | 1000 | 12302 | 23304 | 10129685 | 49032 | 30673 | $1440 | 30d+ |
| KXMARMAD-27-ARIZ | Arizona | 5c | 0.1c | 387 | 2202 | 10120826 | 9798 | 10120826 | 20261 | 11234 | $676 | 30d+ |
| KXNCAABBGS-26-RCHO | :: UCLA | 72c | 47.0c | 500 | 80 | 500 | 457 | 500 | 457 | 2130 | $52 | 30d+ |
| KXNCAABBGAME-26APR182200MICWAH-MIC | Michigan State | nanc | nanc | nan | nan | nan | nan | nan | nan | 1739 | $1739 | 1-3d |
| KXNCAABBGAME-26APR181300NORTHO-NOR | Northern Colorado | 30c | 58.0c | 692 | 77 | 692 | 176 | 692 | 176 | 949 | $1647 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXNCAABASEBALL | College Baseball Champion | custom | 42 | 3 | $67,250 | 1,808,399 | 1.3c |
| KXMARMAD | College Basketball Champion | custom | 71 | 2 | $40,986 | 563,129 | 2.0c |
| KXNCAABBGAME | College Baseball Game | custom | 18 | 11 | $13,912 | 12,357 | 63.0c |
| KXNCAABBGS | College Baseball Golden Spikes Award | custom | 32 | 2 | $52 | 5,528 | 33.0c |
| KXNCAABBPLAYOFFS | College Baseball Playoff Qualifiers | custom | 42 | 34 | $0 | 0 | 93.0c |

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
