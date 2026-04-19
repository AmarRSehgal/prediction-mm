# sports_baseball_kbo

_Auto-generated. Curated notes (KEEP block) preserved across runs._

## Summary

- Series: **2** (2 with open markets)
- Open markets: **46** (36 contested)
- Total 24h volume: **$19,943**
- Total open interest: **35,543**
- Top-OI mean spread (median across series): **52.3 cents**
- **MM profile: Toxic flow**

## Book depth (from comprehensive scan)

- Markets sampled: **36**
- Median spread: **85.0c**
- Median TOB bid / ask size: **555 / 10** contracts
- Median depth within 5c of best bid / ask — **1568 / 2151** contracts
- Median depth within 10c of best bid / ask — **1622 / 2182** contracts
- Median depth within 5c of midpoint — bid: **0** / ask: **0** (useful for tight-spread markets only)
- Mean trades per market (last 3000): **40**
- Mean informed-signal proxy: **-6.092** (sign(trade) * forward cent-move; >0 = toxic)
- Mean abs consecutive-trade move: **8.59c**

## Informed flow by time-to-expiry

Trades grouped by how close they occurred to the market's resolution.
Larger `informed_signal_c` (cents) = takers predict direction of next trade.
Larger `mean_abs_move` = more price movement between consecutive trades.

| TTE bucket | n_trades | mean_abs_move_c | informed_signal_c | p95_abs_move_c | mean_size |
|---|---:|---:|---:|---:|---:|
| 1-3d | 558 | 5.20 | -1.156 | 27.00 | 35.0 |
| 3-7d | 892 | 2.28 | -0.848 | 9.35 | 63.4 |

## Top markets (by OI)

| ticker | subtitle | mid | spread_c | tob_bid | tob_ask | d5c_bid | d5c_ask | d10c_bid | d10c_ask | oi | vol_24h | tte_now |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| KXKBOGAME-26APR170530LGSAM-LG | LG Twins | 31c | 44.0c | 21 | 1 | 2559 | 1 | 3005 | 1 | 7272 | $3126 | 1-3d |
| KXKBOGAME-26APR170530LGSAM-SAM | Samsung Lions | 51c | 58.0c | 222 | 45 | 1481 | 121 | 2037 | 1380 | 5277 | $709 | 1-3d |
| KXKBOGAME-26APR190100LGSAM-LG | LG Twins | 60c | 8.0c | 26 | 18 | 146 | 19 | 211 | 20 | 4512 | $3376 | 1-3d |
| KXKBOGAME-26APR190100KIADOO-KIA | Kia Tigers | 43c | 2.0c | 3 | 45 | 76 | 2031 | 282 | 2971 | 3613 | $3332 | 1-3d |
| KXKBOGAME-26APR190400KIWKTW-KTW | KT Wiz | 68c | 3.0c | 91 | 125 | 2760 | 2198 | 2983 | 2198 | 3472 | $3152 | 3-7d |
| KXKBOGAME-26APR170530SSGNCD-SSG | SSG Landers | 68c | 36.0c | 71 | 2 | 71 | 1402 | 71 | 1501 | 3238 | $1714 | 1-3d |
| KXKBOGAME-26APR170530SSGNCD-NCD | NC Dinos | 18c | 9.0c | 483 | 1 | 1041 | 1 | 1431 | 1 | 2960 | $1435 | 1-3d |
| KXKBOGAME-26APR190100LGSAM-SAM | Samsung Lions | 42c | 14.0c | 10 | 304 | 45 | 304 | 46 | 304 | 2578 | $4011 | 1-3d |
| KXKBOGAME-26APR190100SSGNCD-SSG | SSG Landers | 40c | 15.0c | 164 | 35 | 201 | 99 | 355 | 101 | 2406 | $2606 | 1-3d |
| KXKBOGAME-26APR190400KIWKTW-KIW | Kiwoom Heroes | 32c | 6.0c | 1040 | 8 | 2663 | 2238 | 2663 | 3522 | 2214 | $2177 | 3-7d |
| KXKBOGAME-26APR170530HANLOT-LOT | Lotte Giants | 30c | 47.0c | 996 | 5 | 1735 | 6 | 1735 | 6 | 1714 | $116 | 1-3d |
| KXKBOGAME-26APR190100SSGNCD-NCD | NC Dinos | 56c | 10.0c | 96 | 5 | 157 | 91 | 157 | 91 | 1299 | $1253 | 1-3d |
| KXKBOGAME-26APR190100HANLOT-HAN | Hanwha Eagles | 53c | 10.0c | 72 | 39 | 294 | 658 | 294 | 710 | 1141 | $1351 | 1-3d |
| KXKBOGAME-26APR190100KIADOO-DOO | Doosan Bears | 57c | 7.0c | 47 | 6 | 1047 | 2243 | 1071 | 2243 | 948 | $965 | 1-3d |
| KXKBOGAME-26APR190100HANLOT-LOT | Lotte Giants | 44c | 9.0c | 11 | 5 | 46 | 77 | 46 | 168 | 909 | $909 | 1-3d |

## Top series by OI

| series | title | freq | n_mkts | n_con | 24h_vol | total_oi | top_oi_spread |
|---|---|---|---:|---:|---:|---:|---:|
| KXKBOGAME | KBO Game | custom | 36 | 36 | $19,943 | 35,543 | 52.3c |
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
