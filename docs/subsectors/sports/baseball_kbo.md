# sports_baseball_kbo

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **36** (26 contested)
- Total 24h volume: **$10,131**
- Total open interest: **22,717**
- Top-OI mean spread (median across series): **44.0 cents**
- **MM profile: Mixed / thin**

## Book depth (from comprehensive scan)

- Markets sampled: **26**
- Median spread: **62.0c**
- Median TOB bid / ask size: **1031 / 1030** contracts
- Median cumulative depth within 5c of mid — bid: **0** / ask: **0** contracts
- Median cumulative depth within 10c of mid — bid: **0** / ask: **0** contracts
- Mean trades per market (last 3000): **27**
- Mean informed-signal proxy: **0.000** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **0.00c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 212 | 0.00 | 0.000 | 0.00 | 0.0 |
| 3-7d | 500 | 0.00 | 0.000 | 0.00 | 0.0 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | depth_5c_bid | depth_5c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXKBOGAME-26APR170530LGSAM-LG | LG Twins | 42c | 67.0c | 499 | 47 | 0 | 0 | 7267 | $3126 | 1-3d |
| KXKBOGAME-26APR170530LGSAM-SAM | Samsung Lions | 52c | 57.0c | 3 | 53 | 0 | 0 | 5277 | $719 | 1-3d |
| KXKBOGAME-26APR170530SSGNCD-SSG | SSG Landers | 48c | 71.0c | 10 | 10 | 0 | 0 | 3198 | $1612 | 1-3d |
| KXKBOGAME-26APR170530SSGNCD-NCD | NC Dinos | 18c | 9.0c | 483 | 1 | 483 | 1 | 2960 | $1435 | 1-3d |
| KXKBOGAME-26APR170530HANLOT-LOT | Lotte Giants | 30c | 47.0c | 996 | 5 | 0 | 0 | 1714 | $116 | 1-3d |
| KXKBOGAME-26APR170530HANLOT-HAN | Hanwha Eagles | 50c | 88.0c | 1112 | 3 | 0 | 0 | 807 | $148 | 1-3d |
| KXKBOGAME-26APR190100SSGNCD-SSG | SSG Landers | 43c | 3.0c | 80 | 1030 | 2015 | 2173 | 511 | $811 | 3-7d |
| KXKBOGAME-26APR190400KIWKTW-KTW | KT Wiz | 65c | 6.0c | 1031 | 1048 | 2531 | 2048 | 357 | $243 | 3-7d |
| KXKBOGAME-26APR190400KIWKTW-KIW | Kiwoom Heroes | 34c | 9.0c | 1031 | 1030 | 1031 | 1030 | 250 | $143 | 3-7d |
| KXKBOGAME-26APR190100LGSAM-SAM | Samsung Lions | 48c | 3.0c | 1258 | 788 | 2758 | 5599 | 162 | $1473 | 3-7d |
| KXKBOGAME-26APR190100KIADOO-KIA | Kia Tigers | 58c | 4.0c | 2000 | 287 | 3997 | 2287 | 130 | $126 | 3-7d |
| KXKBOGAME-26APR190100SSGNCD-NCD | NC Dinos | 56c | 4.0c | 1035 | 1823 | 2535 | 6053 | 102 | $41 | 3-7d |
| KXKBOGAME-26APR210530KIAKTW-KIA | Kia Tigers | 41c | 78.0c | 25 | 3 | 0 | 0 | 87 | $87 | 3-7d |
| KXKBOGAME-26APR190100LGSAM-LG | LG Twins | 52c | 3.0c | 1000 | 1030 | 2926 | 2397 | 61 | $61 | 3-7d |
| KXKBOGAME-26APR190100HANLOT-HAN | Hanwha Eagles | 56c | 1.0c | 11 | 1795 | 2125 | 5022 | 58 | $96 | 3-7d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXKBOGAME | KBO Game | custom | 26 | 26 | $10,131 | 22,717 | 44.0c |
| KXKBO | KBO Champion | custom | 10 | 0 | $0 | 0 | nanc |

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
