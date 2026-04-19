# comm_metals_industrial

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration._

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
