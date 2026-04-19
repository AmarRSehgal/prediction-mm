# sports_baseball_kbo

_Auto-generated from sector scan. Curated notes in the KEEP block below are preserved across regenerations._

## Live stats

_Will be populated on next regeneration. See `INDEX.md` for latest snapshot._

## Curated notes

<!-- KEEP-START -->

### Market structure
- Resolution mechanism: official KBO game outcome (MLB Korea feed / official KBO records).
- Frequency: daily during season (roughly late March - mid October). 5-10 games per day.
- Typical close time: ~14:00 UTC (= 23:00 KST, after game end).
- Structure: two-sided per-team win/loss markets (home-team-wins, away-team-wins).
  Each game spawns 2 markets that trade [0, 1] on one team, approximately complementary.

### Informed flow profile
- **Retail vs pro: almost entirely retail** (US-based diaspora + curious bettors).
- **HFT presence: zero observed.** Spreads stay 30-60c even at OI 3000-7000 — unheard-of
  for a series with real volume on a HFT-active venue. This is the tell.
- Known asymmetries:
  - Lineup releases pre-game (pitcher changes, star-player DNPs): moderate info edge.
  - Weather / delays in Korea: low-info from US side.
  - In-play (once game starts): significant info edge for someone streaming the game.

### Time windows (UTC)
- Game time: ~09:30 UTC start, ~12:30-13:00 UTC end (18:30 KST start).
  Some games at 05:00 UTC (weekends, doubleheaders).
- **SAFE**: 14:00 UTC - next-day 08:00 UTC (post-game to pre-lineup-release). 18+ hours daily.
- **QUIET**: 08:00 - 09:30 UTC (lineup releases; some positioning but game hasn't started).
- **DANGEROUS**: 09:30 - 13:00 UTC (live play; any score change moves markets).
- **VERY DANGEROUS**: rain-delay announcements, injury news mid-game.
- Key events: playoff seeding decisions in September; KBO postseason (Oct-Nov) increases scrutiny.

### Correlation / basket structure
- Per-game: home-win + away-win ~ 1.00 (minus venue fee). Natural complementary hedge.
- Per-day: league-wide scoring environment correlates; 6 concurrent games all respond
  to weather / umpire-zone days. Useful for *risk* concentration limits, not arbitrage.
- No strike ladder (games are binary win/loss), unlike commodity daily ladders.

### Verdict
- **v0 target: YES — primary sports target.**
- Why:
  - 30-60c spreads persist at OI 3000-7000 (no HFT undercut).
  - $10K/day volume across series = enough flow to get fills.
  - Game schedule is perfectly predictable; dangerous window is a narrow 3-4h/day.
  - 18+ hours of "safe" quote time per day.
  - Correlation structure (home+away ~ 1) gives natural hedge.
- Caveats:
  - Per-market volume is small ($800-3000 per game). Initial size must be small (~$10-50).
  - Lineup-release windows (08:00-09:30 UTC) need a scheduled quote-widen.
  - In-play MM is not v0 — pull quotes at game start until we have in-play logic.
- Path: paper trade for 2 weeks to validate fill behavior and toxicity. Then live at $10 size.

<!-- KEEP-END -->
