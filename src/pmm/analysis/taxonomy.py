"""Sub-sector taxonomy for Kalshi series.

Kalshi's 18 top-level categories are too coarse. For MM triage we need a
finer breakdown that separates HFT-saturated from truly illiquid subsectors.

Rules:
- Map each series (by ticker + title) to a sub-sector string.
- Return "unknown" if no rule matches; caller can refine.
"""
from __future__ import annotations

import re


# Ordered: first match wins. Patterns are matched case-insensitive against
# f"{ticker} {title}".
SUBSECTOR_RULES: list[tuple[str, str]] = [
    # ---- Sports: team sports by sub-league ----
    (r"\bMLB\b|PROBASEBALL", "sports_baseball_us"),
    (r"KBO", "sports_baseball_kbo"),
    (r"NPB", "sports_baseball_npb"),
    (r"\bNFL\b|PROFOOTBALL|SUPERBOWL|\bSB\b", "sports_nfl"),
    (r"\bNBA\b|PROBASKETBALL", "sports_nba"),
    (r"\bWNBA\b", "sports_wnba"),
    (r"\bNHL\b", "sports_nhl"),
    (r"MLS|MAJORLEAGUESOCCER", "sports_soccer_mls"),
    (r"LIGAMX", "sports_soccer_ligamx"),
    (r"PREMIERLEAGUE|\bEPL\b|ENGLISHPREMIER", "sports_soccer_epl"),
    (r"LALIGA|LIGAAGAME|SPANISHLEAGUE", "sports_soccer_laliga"),
    (r"SERIEA", "sports_soccer_seriea"),
    (r"BUNDESLIGA", "sports_soccer_bundesliga"),
    (r"LIGUE1", "sports_soccer_ligue1"),
    (r"EREDIVISIE", "sports_soccer_eredivisie"),
    (r"JLEAGUE", "sports_soccer_jleague"),
    (r"KLEAGUE", "sports_soccer_kleague"),
    (r"BELGIANPL", "sports_soccer_belgian"),
    (r"EKSTRAKLASA", "sports_soccer_polish"),
    (r"UCL|CHAMPIONSLEAGUE", "sports_soccer_ucl"),
    (r"DFBPOKAL", "sports_soccer_dfb"),
    (r"WORLDCUP|\bWC\b", "sports_soccer_worldcup"),
    (r"INTLFRIENDLY|NATIONALTEAM", "sports_soccer_intl"),
    # Cricket (split by tournament / format)
    (r"CRICKETWOMEN|WPLGAME", "sports_cricket_womens"),
    (r"IPLGAME|IPLFIRST|IPLTEAM|IPLFINAL|IPLTOTAL|IPLFOUR|IPLSIX|IPLWINNER|KXIPL$", "sports_cricket_ipl"),
    (r"PSLGAME|^KXPSL$", "sports_cricket_psl"),
    (r"CRICKETODI|ASIACUPCRICKET", "sports_cricket_odi"),
    (r"CRICKETT20|CRICKETTEST|T20MATCH|T20WORLDCUP|T20FIRST|T20FOUR|T20SIX|SAUDIPL", "sports_cricket_t20_misc"),
    # Rugby (split by league)
    (r"\bNRL\b|NRLCHAMP|NRLMATCH", "sports_rugby_nrl"),
    (r"SIXNATION", "sports_rugby_sixnations"),
    (r"GALLAGHER|RUGBYGPREM", "sports_rugby_gallagher"),
    (r"FRA14|RUGBYFRA", "sports_rugby_top14"),
    (r"ESLMATCH|SUPERLEAGUERUGBY|RUGBYESL", "sports_rugby_esl"),
    (r"RUGBYMLR|MLRMATCH", "sports_rugby_mlr"),
    (r"RUGBY", "sports_rugby_misc"),
    (r"ATPCHALLENGER|CHALLENGERMATCH|WTACHALLENGER", "sports_tennis_challenger"),
    (r"ITFMATCH|ITFWMATCH", "sports_tennis_itf"),
    (r"USOPEN|FRENCHOPEN|WIMBLEDON|AUSOPEN", "sports_tennis_grandslam"),
    (r"PGA|GOLF|MASTERS|HOLEINONE", "sports_golf"),
    (r"UFC|BOXING|MMA|FLOYDTYSON|WBC|WBA|BANTAMWEIGHT", "sports_combat"),
    (r"NASCAR", "sports_motor_nascar"),
    (r"INDYCAR", "sports_motor_indycar"),
    (r"F1RACE|FORMULA1|\bF1\b", "sports_motor_f1"),
    (r"MOTOGP", "sports_motor_motogp"),
    (r"OLYMPICS|\bWO\b|OLY", "sports_olympics"),
    (r"VALORANT", "sports_esports_valorant"),
    (r"CS2GAME|CS2QUALIF|CSGO|COUNTERSTRIKE|HLTV", "sports_esports_cs2"),
    (r"DOTA", "sports_esports_dota"),
    (r"RAINBOW|R6GAME", "sports_esports_r6"),
    (r"OVERWATCH|OWGAME", "sports_esports_overwatch"),
    (r"LOLTOTAL|LOL1STTIMEWIN|LOLWORLDS|CHARCOUNTLOL", "sports_esports_lol"),
    (r"WARZONE|CODWAR|CALLOFDUTY", "sports_esports_cod"),
    (r"CHESS.*ESPORT|EWCCHESS", "sports_esports_chess"),
    (r"MOBILELEGENDS|HONOROFKINGS", "sports_esports_mobile"),
    (r"TFT|TEAMFIGHTTACTICS|EASPORTS|ESPORTS|EWC|PGL", "sports_esports_misc"),
    (r"DARTS", "sports_darts"),
    (r"SQUASH", "sports_squash"),
    (r"ACBGAME|LIGAACB", "sports_basketball_acb"),
    (r"CBAGAME|CBASPREAD|CBATOTAL", "sports_basketball_cba"),
    (r"BBSERIEA", "sports_basketball_italy_lega"),
    (r"NCAAB|CBB|COLLEGEBASKETBALL|MARMAD", "sports_ncaabball"),
    (r"NCAAF|COLLEGEFOOTBALL|CFP|SEC|BIGTEN|BIGEAST", "sports_ncaafootball"),
    (r"\bTGL\b", "sports_golf_tgl"),
    (r"COACH|MANAGER", "sports_coachhire"),
    (r"DRAFT", "sports_draft"),

    # ---- Weather ----
    (r"HIGHT|HIGHNY|HIGHCHI|HIGHDAL|HIGHLAX|HIGHLAX|HIGHMIA|HIGHAUS|HIGHTDAL|HIGHTSATX|HIGHTSFO|HIGHTDEN|HIGHTAUS|HIGHTMIA|HIGHTBOS|HIGHTORD|HIGHTPDX|HIGHTNYC|PHILHIGH|TEMPNYCH|TEMPLAXH|TEMPMIAH|TEMPCHIH|TEMPDCH|TEMPATLH|TEMPLASH|TEMPDENH|TEMPBOSH|TEMPAUSH|TEMPSFOH|TEMPPDXH|TEMPJFKH|TEMPORDH|LOWLAX|LOWNY|LOWCHI", "weather_temp"),
    (r"SNOW", "weather_snow"),
    (r"RAIN", "weather_rain"),
    (r"HURRICAN|TORNADO|EMERGENCY|EARTHQUAKE|ERUPT|KILAUEA|KILUAEA|WILDFIRE|FIRE|DISASTER", "weather_disaster"),
    (r"AVGTEMP|MONTHRANGE|HMONTH|WARMING|CO2", "weather_climate"),
    (r"EVSHARE", "climate_ev"),

    # ---- Economics ----
    (r"\bCPI\b", "eco_cpi"),
    (r"\bPPI\b", "eco_ppi"),
    (r"\bNFP\b|JOBS|UNEMPLOYMENT|PAYROLL|U3|CHCUTS", "eco_jobs"),
    (r"\bGDP\b|NGDP", "eco_gdp"),
    (r"FEDDECISION|FEDHIKE|DOTPLOT|FOMC|\bFED\b", "eco_fed"),
    (r"RATECUT|RATEHIKE|RBADECISION|CBDECISION", "eco_ratedecisions"),
    (r"RETAILSALES|HOUSING|BUILDPERMS|HOMESALES|HOMEVAL", "eco_realestate_retail"),
    (r"REALWAGES|WEALTH|DEBT|INFLATION|ARINFLATION", "eco_macro_misc"),
    (r"JOBREVISION", "eco_jobs"),

    # ---- Financials / Rates ----
    (r"\bINX\b|SP500|SPX|NASDAQ100|NASDAQ|DJIA|RUT", "fin_equity_indices"),
    (r"TNOTE|TREASURY|YIELD|\bTENYR\b", "fin_rates"),
    (r"USDJPY|USDEUR|EURUSD|GBPUSD|USDBRL|USDMEX|USDCNY|USDCAD|USDCHF|USDAUD|FX\b", "fin_fx"),
    (r"^KXGBP$|^KXEURO$|\bKXCOFFEEM\b|TETHER|^KXPRICE", "fin_misc"),

    # ---- Commodities ----
    (r"\bWTI\b|\bBRENT\b|OIL\b|KXGAS|NATGAS|NGASW|GASMIN", "comm_energy"),
    (r"\bGOLD\b|KXGOLD", "comm_gold"),
    (r"SILVER|PLATINUM|PALLADIUM", "comm_precious_other"),
    (r"COPPER|NICKEL|COBALT|LITHIUM|STEEL|ALUMINUM|IRON", "comm_metals_industrial"),
    (r"CORN|WHEAT|SOYBEAN|COTTON|COCOA|COFFEE|SUGAR|LCATTLE|CATTLE|HOGS", "comm_agri"),

    # ---- Crypto ----
    (r"BTC|BITCOIN|KXBTC", "crypto_btc"),
    (r"\bETH\b|ETHER|KXETH", "crypto_eth"),
    (r"SOL\b|SOLANA", "crypto_sol"),
    (r"DOGE|MEME|SHIB|PEPE", "crypto_meme"),
    (r"CRYPTO|BLOCKCHAIN|DEFI|NFT|STABLECOIN", "crypto_misc"),

    # ---- Politics ----
    (r"HOUSERACE|SENATE|GOVPARTY|GOVRACE|GUBERNATORIAL", "pol_race"),
    (r"PRIMARY", "pol_primary"),
    (r"TRUMP|BIDEN|HARRIS|VANCE|DESANTIS|NEWSOM|KAMALA|OBAMA|CLINTON", "pol_figures"),
    (r"CONFIRM|SUPREMECOURT|\bSCOTUS\b|JUDGE|NOMINAT", "pol_confirmation"),
    (r"IMPEACH", "pol_events"),
    (r"GOVTCUT|SHUTDOWN|DEBTCEILING|BUDGET", "pol_fiscal"),
    (r"ELON|MARS", "pol_exotic"),
    (r"POPE", "pol_religion"),

    # ---- Companies / earnings ----
    (r"EARNINGS|EPS|BEAT", "companies_earnings"),
    (r"ACQUIRE|MERGER|BUYOUT", "companies_ma"),
    (r"IPO|SPINOFF", "companies_ipo"),
    (r"CEO|LAYOFF|FIRED|RESIGN", "companies_execs"),

    # ---- Entertainment ----
    (r"OSCAR|ACADEMY|ACTOR|ACTRESS|BESTPICT|BESTDIRECT|BESTACT|TONY|EMMY|GRAMMY|CRITICSCHOICE", "ent_awards"),
    (r"ROTTENTOMATO|\bRT\b[A-Z]", "ent_movie_ratings"),
    (r"BOX.*OFFICE|OPENINGWEEKEND", "ent_movie_box"),
    (r"BILLBOARD|ALBUM|SPOTIFY|TAYLORSWIFT|HARRYSTYLES|YTUBE|MUSIC|CHART|AMA|AMAS|ARTIST", "ent_music"),
    (r"DANCING|DWTS|REALITYSHOW", "ent_tv_reality"),
    (r"WRESTLEM|WWE|PAYPERVIEW", "ent_wrestling"),
    (r"MEDIAINTERVIEW", "ent_media"),

    # ---- Science / tech ----
    (r"GPT|OPENAI|ANTHROPIC|GROK|GEMINI|LLAMA|AGI|AICODE", "tech_ai"),
    (r"SPACEX|STARSHIP|LAUNCH|ROCKET|NASA|MARS|MOON|SATELLITE", "tech_space"),
    (r"TESLA|CYBERTRUCK|FSD", "tech_ev_tesla"),
    (r"NEWPOPE|POPE|ROYAL|KING|QUEEN|PRINCE|PRINCESS", "world_royalty"),
    (r"COVID|PANDEMIC|VIRUS|VACCINE|OZEMPIC|WEGOVY|DRUG", "health_misc"),

    # ---- World / geopolitics ----
    (r"ISRAEL|GAZA|PALESTINE|HAMAS|IRAN|HEZBOLLAH", "world_mideast"),
    (r"UKRAINE|RUSSIA|PUTIN|NATO", "world_russia_ukraine"),
    (r"CHINA|TAIWAN|XIJINPING", "world_china"),
    (r"NORTHKOREA|KIMJONG", "world_northkorea"),

    # ---- Rankings / misc ----
    (r"RANKLIST", "rankings_misc"),
    (r"REBOOT|REMAKE", "ent_reboots"),
    (r"STOCKXLABUBU", "collectibles"),
]


_COMPILED = [(re.compile(p, re.IGNORECASE), s) for p, s in SUBSECTOR_RULES]


def classify(ticker: str, title: str = "") -> str:
    text = f"{ticker} {title}"
    for pat, sub in _COMPILED:
        if pat.search(text):
            return sub
    return "unknown"
