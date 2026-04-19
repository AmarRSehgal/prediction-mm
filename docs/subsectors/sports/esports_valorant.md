# sports_esports_valorant

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **140** (140 contested)
- Total 24h volume: **$71,656**
- Total open interest: **83,082**
- Top-OI mean spread (median across series): **12.0 cents**
- **MM profile: Niche opportunity**

## Book depth (from comprehensive scan)

- Markets sampled: **140**
- Median spread: **8.5c**
- Median TOB bid / ask size: **502 / 497** contracts
- Median depth within 5c of best bid / ask — **2149 / 2150** contracts
- Median depth within 10c of best bid / ask — **2202 / 2183** contracts
- Median depth within 5c of midpoint — bid: **636** / ask: **497** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **14**
- Mean informed-signal proxy: **1.203** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **11.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 7-30d | 2022 | 4.52 | -0.021 | 25.05 | 46.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXVALORANTGAME-26APR190400T1RRQ-T1 | T1 | 69c | 4.0c | 15 | 155 | 264 | 1576 | 587 | 2221 | 17746 | $17600 | 7-30d |
| KXVALORANTGAME-26APR190400T1RRQ-RRQ | Rex Regum Qeon | 31c | 3.0c | 3 | 67 | 201 | 708 | 354 | 717 | 12103 | $12260 | 7-30d |
| KXVALORANTGAME-26APR190600GENGNS-GENG | Gen.G Esports | 34c | 1.0c | 400 | 7010 | 1191 | 20567 | 5462 | 21846 | 10368 | $8544 | 7-30d |
| KXVALORANTGAME-26APR190500TETEC-TE | Trace Esports | 57c | 1.0c | 522 | 386 | 822 | 16731 | 1886 | 16731 | 7670 | $7672 | 7-30d |
| KXVALORANTGAME-26APR190600GENGNS-NS | Nongshim RedForce | 66c | 2.0c | 340 | 275 | 9443 | 5154 | 10781 | 5154 | 5783 | $6456 | 7-30d |
| KXVALORANTGAME-26APR190500TETEC-TEC | TEC Esports | 45c | 1.0c | 675 | 325 | 7182 | 1106 | 7413 | 1526 | 3317 | $4436 | 7-30d |
| KXVALORANTMAP-26APR190700XLGAG-2-XLG | XLG Gaming | 60c | 7.0c | 250 | 1130 | 2750 | 2620 | 2750 | 3120 | 2780 | $77 | 7-30d |
| KXVALORANTGAME-26APR192000SEN100T-100T | 100 Thieves | 67c | 2.0c | 295 | 1765 | 2417 | 3853 | 3829 | 3853 | 2513 | $2652 | 7-30d |
| KXVALORANTMAP-26APR201030DPETE-1-DP | Dark Passage | 26c | 11.0c | 1000 | 1000 | 2000 | 2128 | 2002 | 2128 | 2173 | $86 | 7-30d |
| KXVALORANTMAP-26APR191130TLABONK-1-TLA | Team Liquid Academy | 28c | 46.0c | 1 | 124 | 343 | 335 | 343 | 335 | 1838 | $143 | 7-30d |
| KXVALORANTMAP-26APR190400T1RRQ-1-T1 | T1 | 67c | 36.0c | 47 | 39 | 47 | 165 | 107 | 456 | 1418 | $1586 | 7-30d |
| KXVALORANTGAME-26APR191130TLABONK-TLA | Team Liquid Academy | 48c | 71.0c | 303 | 20 | 421 | 21 | 532 | 24 | 1281 | $133 | 7-30d |
| KXVALORANTGAME-26APR190700XLGAG-XLG | XLG Gaming | 65c | 6.0c | 600 | 600 | 4594 | 4784 | 4594 | 4784 | 1264 | $1234 | 7-30d |
| KXVALORANTGAME-26APR191330NVUBJK-NVU | Misa Esports | 78c | 5.0c | 500 | 500 | 1321 | 500 | 1321 | 503 | 1253 | $1252 | 7-30d |
| KXVALORANTMAP-26APR201030DPETE-1-ETE | Eternal Fire Passion | 64c | 1.0c | 2000 | 1 | 2000 | 1 | 2000 | 1 | 1133 | $203 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXVALORANTGAME | T1 | nan | 46 | 46 | $67,428 | 70,348 | 2.7c |
| KXVALORANTMAP | XLG Gaming | nan | 94 | 94 | $4,229 | 12,734 | 21.3c |

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
