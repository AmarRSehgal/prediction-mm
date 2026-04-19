# comm_metals_industrial

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **11** (11 with open markets)
- Open markets: **286** (268 contested)
- Total 24h volume: **$691**
- Total open interest: **20,010**
- Top-OI mean spread (median across series): **24.8 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **200**
- Median spread: **39.0c**
- Median TOB bid / ask size: **60 / 60** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **7**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 97 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 52 | 0.00 | 0.000 | 0.00 | 0.0 |
| 7-30d | 382 | 0.00 | 0.000 | 0.00 | 0.0 |
| 30d+ | 866 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXBEZELP-NAUT-27 | a steel Nautilus reference | 14c | 5.0c | 211 | 5 | 211 | 12 | 3597 | $114 | 30d+ |
| KXIRONMAN-27JAN01 | By Jan 1, 2027 | 32c | 7.0c | 203 | 10 | 203 | 21 | 3158 | $61 | 30d+ |
| KXCOPPERMON-26APR3017-T6.17 | above $6.17 | 53c | 31.0c | 96 | 177 | 0 | 0 | 1477 | $6 | 7-30d |
| KXCOPPERMON-26APR3017-T5.99 | above $5.99 | 81c | 22.0c | 1 | 81 | 0 | 0 | 1173 | $1 | 7-30d |
| KXCOPPERMON-26APR3017-T5.93 | above $5.93 | 66c | 33.0c | 2 | 4 | 0 | 0 | 1171 | $12 | 7-30d |
| KXWCMESSIRONALDO-26LMESCRON-LMES | Lionel Messi | 52c | 11.0c | 500 | 500 | 0 | 0 | 1145 | $0 | 30d+ |
| KXCOPPERMON-26APR3017-T6.05 | above $6.05 | 53c | 22.0c | 71 | 177 | 0 | 0 | 708 | $8 | 7-30d |
| KXCOPPERMON-26APR3017-T5.87 | above $5.87 | 78c | 34.0c | 96 | 27 | 0 | 0 | 550 | $0 | 7-30d |
| KXCOPPERMON-26APR3017-T5.57 | above $5.57 | 82c | 34.0c | 96 | 200 | 0 | 0 | 534 | $0 | 7-30d |
| KXCOPPERMON-26APR3017-T6.41 | above $6.41 | 30c | 45.0c | 647 | 182 | 0 | 0 | 505 | $1 | 7-30d |
| KXLITHIUMMON-26APR3017-T166499.99 | 
    above ¥166499.99
 | 57c | 33.0c | 71 | 60 | 0 | 0 | 479 | $0 | 7-30d |
| KXCOPPERMON-26APR3017-T5.69 | above $5.69 | 92c | 1.0c | 6 | 4 | 6 | 4 | 466 | $1 | 7-30d |
| KXCOPPERMON-26APR3017-T5.63 | above $5.63 | 82c | 33.0c | 76 | 249 | 0 | 0 | 315 | $1 | 7-30d |
| KXCOPPERD-26APR2017-T5.98 | above $5.98 | 86c | 17.0c | 60 | 60 | 0 | 0 | 298 | $1 | 1-3d |
| KXCOPPERMON-26APR3017-T5.45 | above $5.45 | 85c | 28.0c | 81 | 200 | 0 | 0 | 252 | $0 | 7-30d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXCOPPERMON | Copper Monthly Price | monthly | 40 | 25 | $74 | 9,681 | 24.7c |
| KXBEZELP | Will Patek release a steel Nautilus refe | one_off | 1 | 1 | $113 | 3,595 | 7.0c |
| KXIRONMAN | RDJ returns as Iron Man | custom | 1 | 1 | $47 | 3,150 | 8.0c |
| KXWCMESSIRONALDO | Goal Contributions Messi and Ronaldo | custom | 3 | 3 | $0 | 1,378 | 11.0c |
| KXCOPPERD | Daily Copper | daily | 40 | 39 | $409 | 989 | 25.0c |
| KXLITHIUMMON | Lithium Monthly | monthly | 40 | 40 | $0 | 751 | 21.3c |
| KXNICKELSTOP | Will the nickel be discontinued? | one_off | 1 | 0 | $0 | 286 | nanc |
| KXLITHIUMW | Lithium Weekly | weekly | 40 | 40 | $23 | 104 | 33.3c |
| KXNICKELMON | Nickel Monthly | monthly | 40 | 40 | $18 | 58 | 30.0c |
| KXCOPPERW | Copper Weekly Price | weekly | 40 | 39 | $5 | 15 | 98.0c |

## Curated notes

<!-- KEEP-START -->
### Market structure
- Series: KXCOPPERD (daily), KXCOPPERW (weekly), KXNICKELW, KXCOBALTW, KXLITHIUMMON, KXSTEELMON, KXALUMINUM.
- Resolution: LME/COMEX/SHFE settlement (varies by metal).
- Structure: strike ladder.
- Close time: 21:00 UTC daily (where applicable).

### Informed flow profile
- **Dominantly retail with a tail of industrial commentators.**
- **HFT presence: near zero.** Copper median spread ~33c; steel / nickel / lithium
  near-dead (limited listings).
- Industrial-supply-chain traders: China PMI, Chile mining strikes, EV battery demand.
  These inform the macro narrative but rarely trade Kalshi directly.

### Time windows (UTC)
- **SAFE**: 00:00 - 01:00 UTC (between US close and Asian metals open).
- **QUIET/DANGEROUS**: 01:00 - 09:00 UTC (Asian / Chinese metals session is live; important
  for copper especially — China PMI releases, SHFE volume).
- **SAFE**: 09:00 - 11:00 UTC (between Asian close and EU open).
- **QUIET**: 11:00 - 13:30 UTC (LME open; moderate flow).
- **DANGEROUS**: 13:30 - 16:00 UTC (US open + macro releases).

### Correlation / basket structure
- Copper - very sensitive to China growth indicators.
- Strike ladder monotone, same arb/CDF as other commodities.
- Copper / silver / gold sometimes co-move on commodity-cycle narratives.

### Verdict
- **v0 target: secondary.**
- Why: widest spreads in the commodity complex; lowest competition.
- Caveats:
  - **Low volume** — 24h vol per market is small; fill rate may not support
    meaningful PnL.
  - **China session risk** — quiet by US standards but informed-flow from Asian time zones.
- Path: passively quote with wide spreads; acceptable if fills are rare.
<!-- KEEP-END -->
