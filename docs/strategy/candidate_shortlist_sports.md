# Sports Candidate Deep-Dive (2026-04-18)

Follow-up to `candidate_shortlist.md`. Sweep of 35 niche-sports series on Kalshi
(1175 open markets, 1090 contested). Listed open markets, summary stats, plus
orderbook deep-dive for top-OI markets per series.

## Critical finding — series-median spreads are misleading

Most sports series show a bimodal spread distribution:

- **Top-OI matches in a series** (headline games, primetime):
  quoted to 1-2 cent spreads by HFT MMers.
- **Long tail of low-OI matches** (unpopular teams, off-peak games):
  30-95 cent spreads, often one-sided.

A "median spread of 23c" for IPL does NOT mean real MM opportunity — it means
the 10 headline IPL games are 1c spread (HFT) and the 14 obscure ones are 80c
(no one quotes). A naive "wide median" filter targets the dead tail, not a
real niche.

**Real niches are series where even the HIGH-OI markets stay wide.**

## Real niches (where top-OI markets have > 5c spread)

### 1. KBO — Korean baseball (PRIMARY SPORTS TARGET)

- **Series**: `KXKBOGAME`
- **26 open markets, 26 contested**, 47c median spread
- **High-OI markets remain wide**: LG Twins OI 7267 @ 44c spread; Samsung Lions
  OI 5277 @ 40c spread; SSG Landers OI 3213 @ 33c spread
- **Volume**: $800-$3100 per game, ~$10K total 24h
- **Why it survives as a niche**: US audience does not watch; Korean fans trade
  on Korean books; no established HFT MMers. Informed flow from US is ~zero.
- **Game schedule**: 18:30 KST = 09:30-13:00 UTC daily during season.
- **Safe windows (KBO-specific)**:
  - 14:00-08:00 UTC: post-game / pre-game, genuine quiet window
  - 08:00-09:00 UTC: lineup releases, slight info risk but small
- **Dangerous**:
  - 09:30-13:00 UTC: live play, in-play flow + leaked info
  - Injury / weather postponement announcements (ad hoc)

### 2. PSL — Pakistan Super League cricket (SECONDARY)

- **Series**: `KXPSLGAME`
- **22 markets, 22 contested**, 60c median spread
- **High-OI markets**: Multan Sultans OI 4420 @ 11c; Peshawar Zalmi OI 2444 @ 8c
  — spreads stay decent, not 1c-saturated
- **Volume**: $2-4K per active game, $8K total 24h
- **Schedule**: Pakistan evening = ~14:00-19:00 UTC
- **Risk**: Match-fixing history in Pakistan cricket; informed flow exists from
  subcontinent betting markets. Higher toxicity than KBO.

### 3. Cricket ODI International (PROMISING)

- **Series**: `KXCRICKETODIMATCH`
- Only 2 markets right now (NZ vs Bangladesh ODI), but **both contested at
  14-19c spreads with OI 4200 / 2400 and $4K+ vol**
- Series is event-driven (only active during ODI series tours); limited but
  clean MM window during a series.
- Similar informed-flow risk as PSL (subcontinent / UK bookmakers).

### 4. Liga ACB basketball (Spain) — marginal

- **Series**: `KXACBGAME`, 10 markets, 10 contested
- 15c median; best market CB Malaga OI 168 @ 6c spread — decent but small OI
- Volumes tiny ($180 per game, $228 total 24h). MM possible, PnL ceiling low.

### 5. Dota 2 map-level (marginal)

- **Series**: `KXDOTA2MAP`, 32 markets
- 5-8c spreads on active matches, but OI per market is ~100. Dead-low flow.
- Not a real opportunity until a major tournament is live.

## Series to AVOID for MM (despite appearances)

### HFT-saturated at the top

Top-OI matches in these series are 1-2c spread. Don't let the series median
fool you.

| Series | Top-OI example | Spread | OI |
|--------|---------------|--------|-----|
| KXIPLGAME | Rajasthan Royals | 1c | 252,156 |
| KXCS2GAME | Vitality | 1c | 4,282 |
| KXVALORANTGAME | Gen.G Esports | 2c | 2,700 |
| KXRUGBYNRLMATCH | Newcastle Knights | 2c | 357 |

You'd be quoting against HFT. Skip unless you find a specific off-peak match
that slipped through.

### All European top soccer (MLS, La Liga, Serie A, Bundesliga, Ligue 1)

Medians 2-4c. Major retail volume but competitively MM'd. Not v0 material.

### Tennis lower tours (ITF, Challenger)

Spreads ARE wide (80-88c median) but volume is tiny ($200 per series 24h).
You'd be only-MM with no trades.

## Top KBO markets added to collector watchlist

(see `research/data/watchlist.txt`; merged with commodity list)

- KXKBOGAME-26APR170530LGSAM-LG (LG Twins, spread 67c, OI 7267)
- KXKBOGAME-26APR170530LGSAM-SAM (Samsung Lions, spread 34c, OI 5277)
- KXKBOGAME-26APR170530SSGNCD-SSG (SSG, spread 26c, OI 3213)
- KXKBOGAME-26APR170530SSGNCD-NCD (NC Dinos, spread 60c, OI 2960)
- KXKBOGAME-26APR170530HANLOT-LOT (Lotte, spread 47c, OI 1714)
- KXKBOGAME-26APR170530HANLOT-HAN (Hanwha, spread 86c, OI 807)
- Plus 4 more KBO markets closing in the next 24h

## Revised v0 thesis

Three parallel tracks, different risk profiles:

1. **Commodity daily strike ladders** (Brent / Gold / Silver / Copper):
   steady, moderate size, underlying-arb risk. Target 20-35c spreads.
2. **KBO game-level markets**: true niche, very low toxicity, wider spreads
   (30-60c). Tiny size initially. Big spreads but smaller contracts.
3. **PSL / Cricket ODI Intl (when active)**: medium-width spreads (10-20c),
   moderate volume, higher toxicity than KBO — experiment cautiously.

Total markets on collector: **64 tickers** (39 commodity + weather/econ control,
25 niche sports — KBO is primary, PSL + Cricket ODI + Liga ACB + Dota 2 as
secondary).

Run time: 6 hours starting 2026-04-18 17:18 UTC. This will cover KBO post-game
period and overnight US hours, so we'll see how spreads behave without any
live-play information.

## Next steps after collection finishes

1. Verify KBO spreads persist overnight (they should — no one is awake to tighten).
2. Measure post-trade drift on KBO — is there directional flow between trades?
3. Check whether KBO and PSL markets have adjacent-strike correlation structure
   we can exploit (e.g., first-innings-lead markets? Run totals? Need to explore
   series hierarchy).
4. Build an event calendar: KBO schedule, PSL schedule, EIA inventory, FOMC.
5. Revisit `risk_parameters.md` with calibrated numbers per market.
