# Subsector analysis

Per-subsector research. Each file groups Kalshi markets with **similar structure**
(resolution mechanism, trading pattern, informed-flow profile) so we can form
consistent MM policies per group rather than per-contract.

## How subsectors are defined

Kalshi's 18 top-level categories are too coarse — "Sports" contains both
HFT-saturated MLS ($1M 24h vol, 4c spread) and niche KBO (30-60c spread,
$10K vol, zero HFT). The taxonomy in `src/pmm/analysis/taxonomy.py` splits
these based on league / asset class / release cadence.

Current classification rules: ~120 subsectors across 12 top-level folders.

## Folders

- `sports/` — by league / sport
- `weather/` — daily temp / hourly / snow / rain / disaster / climate
- `economics/` — CPI / PPI / jobs / GDP / Fed / rates / real estate
- `commodities/` — energy / gold / precious / industrial metals / agri
- `financials/` — equity indices / rates / FX / misc
- `crypto/` — BTC / ETH / SOL / memes / misc
- `politics/` — races / primaries / figures / confirmations / fiscal
- `entertainment/` — awards / movies / music / TV / wrestling
- `tech/` — AI / space / Tesla
- `world/` — Middle East / Russia-Ukraine / China / royalty
- `companies/` — earnings / M&A / IPO / execs
- `rankings/`, `health/`, `misc/` — smaller buckets

## Per-subsector doc structure

Each file follows a common template:

1. **Market structure** — ticker patterns, example tickers, resolution
   mechanism, frequency.
2. **Live stats** — as of sweep date: n open / contested markets, spreads,
   volume, OI.
3. **MM profile** — HFT-saturated / Niche / Dead; informed-flow risk;
   counterparty composition.
4. **Time windows (UTC)** — safe / quiet / dangerous windows specific to
   the subsector.
5. **Verdict** — v0 target? yes / no / secondary, with reasons.

## Generation

Most docs are auto-generated from live data by
`scripts/generate_subsector_docs.py`, which pulls the latest sector-scan
output and fills the template. Curated notes (informed-flow analysis, time
windows) are preserved across regenerations via a `<!-- KEEP -->` marker.

Regenerate after a fresh sector scan:

```bash
.venv/bin/python scripts/sector_scan.py            # refresh data
.venv/bin/python scripts/generate_subsector_docs.py # rebuild docs
```
