# Research brief for era agents · 美股风气40年 (1986–2026)

Study folder: `studies/美股风气40年_兴衰统计_2026-10-06/`. Cut-off date: **2026-10-06**.

## What the study answers

For every US-equity investment "fashion" (风气/主题) in the last ~40 years:
1. When did the hype start, when did it peak, when did it bottom? (dated marker events with sources)
2. Was the underlying theme **real**? Did the technology/demand actually materialise, and how many years did that take?
3. What happened to **the stocks that were the stars at the time** (not today's survivors picked in hindsight):
   died (bankrupt / liquidated / delisted), acquired (at what price vs peak), survived but never regained peak,
   survived and made new highs, still in progress.
4. How long each stage took (rise, crash, death, recovery).

## Rules (the user wants verifiable, no hype)

- Every factual claim needs a source URL. Prefer primary/near-primary: SEC EDGAR filings (8-K, S-1, 10-K),
  company press releases, court/bankruptcy records, exchange notices, Fed/Census/BLS/EIA, contemporaneous
  reporting (NYT, WSJ, Reuters, AP, CNBC, Bloomberg, FT, Fortune, Barron's). Wikipedia is acceptable as a
  secondary source but flag `"confidence": "medium"` unless confirmed elsewhere.
- **Never invent a number.** If you cannot find it, write `null` and say so in `notes`. A gap is fine; a
  fabricated peak price is not.
- Choose baskets **as of the time** ("当年口径"): the names media, IPO calendars, theme-ETF top holdings,
  period lists (e.g. "Four Horsemen of the Nasdaq", Cramer's FANG 2013, ARKK top-10 Feb 2021) put forward.
  Deliberately include the losers. State how the basket was chosen in `basket_method` with a source.
- 5–10 companies per theme; 3–6 themes per era. Mix of eventual winners, survivors-that-never-recovered,
  acquired, and dead.
- Prices: say whether a price is nominal-as-traded or split-adjusted. For companies still trading (or with
  history on Yahoo Finance under a current ticker), give `yahoo_ticker` — the lead analyst will pull the
  full price history from Yahoo and compute peaks/drawdowns/recovery itself, so for those you mainly need
  the ticker and the qualitative story. For dead/acquired/delisted names, Yahoo usually has no data, so
  give peak price/market cap, the fate date and the final value per share (0 for wiped-out equity, deal
  price for acquisitions) with sources.
- Write in Chinese for `*_cn` / narrative fields, English OK for names and quotes. Keep quotes < 15 words.

## Output

1. `data/research/<era_id>.json` — exactly this shape:

```json
{
  "era_id": "e2_1995_2002",
  "era_range": "1995-2002",
  "macro_context_cn": "利率/流动性/监管背景，一段话，带来源",
  "macro_sources": ["url"],
  "themes": [
    {
      "id": "dotcom",
      "name_cn": "互联网 .com",
      "name_en": "Dot-com",
      "one_line_cn": "一句话：这个风气在赌什么",
      "hype_start": {"date": "1995-08", "event_cn": "Netscape IPO 首日大涨", "source": "url"},
      "peak": {"date": "2000-03", "event_cn": "纳指 2000-03-10 收盘 5048.62", "source": "url"},
      "trough": {"date": "2002-10", "event_cn": "...", "source": "url"},
      "proxy_tickers": ["^IXIC"],
      "proxy_note_cn": "可用于主题层面回撤计算的指数/ETF（如有）；ETF 需晚于主题时才存在要说明",
      "what_killed_it_cn": "加息/盈利证伪/欺诈/供给泛滥(IPO/SPAC)/技术不成熟…一段话",
      "reality_verdict": "真实且巨大 | 真实但比股价预期慢得多 | 真实但利润没留给当年的股东 | 基本是炒作 | 进行中",
      "reality_evidence": [
        {"claim_cn": "美国电商占零售比 2019 年约 11%", "date": "2019", "source": "url"}
      ],
      "time_to_reality": {"years": 15, "from": "1995", "to": "2010", "marker_cn": "什么事件/数据算‘兑现’", "source": "url"},
      "basket_method": "如何选出当年明星 + source",
      "companies": [
        {
          "name": "Pets.com",
          "ticker_then": "IPET",
          "yahoo_ticker": null,
          "role_cn": "龙头 | 明星 | 沾边蹭概念 | 卖铲子",
          "hype_date": "2000-02",
          "peak_date": "2000-02",
          "peak_price": 14.0,
          "price_basis": "nominal",
          "peak_mcap_usd_bn": null,
          "fate": "dead | acquired | survived_new_high | survived_below_peak | in_progress",
          "fate_date": "2000-11",
          "final_value_per_share": 0.0,
          "fate_detail_cn": "一两句",
          "sources": ["url1", "url2"],
          "confidence": "high | medium | low",
          "notes": ""
        }
      ]
    }
  ]
}
```

`fate` definitions (as of 2026-10-06): `dead` = bankrupt/liquidated/delisted with equity ~wiped out;
`acquired` = taken over (give price and compare with peak); `survived_new_high` = still listed and has
exceeded the hype-era peak (split-adjusted); `survived_below_peak` = still listed, never regained it;
`in_progress` = the theme is still live (2023–2026 names). If you are unsure between the two survived
states, give `yahoo_ticker` and put your best guess — the lead analyst will recompute from prices.

2. `data/research/<era_id>_notes.md` — 1–2 pages of Chinese narrative per era: what drove each fashion,
   the liquidity/rate backdrop, the "tell-tale signs" at the peak (renamings, IPO/SPAC floods, magazine
   covers, retail frenzy), what killed it, and anything surprising. Cite inline with URLs.

Return a short summary (≤ 200 words) when done: themes covered, counts per fate, biggest gaps/uncertainties.
