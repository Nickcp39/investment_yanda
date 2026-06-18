# 00 Freeze Case - PFE 2022-02-08

## 1. Case Identity

- Ticker: PFE
- Company: Pfizer Inc.
- Exchange / share class: NYSE common stock
- Pipeline version: lean_six_module_v0
- Case type: P1 Lean Case (MATERIAL PACK ONLY — no decision in this round)
- Collector scope: as-of 2022-02-08 only
- Scorer scope: outcome evidence after a future locked decision only (NOT in this pack)

## 2. Time Boundary

- As-of date: 2022-02-08
- Price date: 2022-02-08 close
- As-of price: $51.70 (NYSE close; Yahoo chart API daily close)
- Shares outstanding used for market cap: ~5.613 billion (5,612,866,598 common shares outstanding as of 2021-10-03, from Q3 2021 10-Q, the latest share count public before the as-of date)
- Approximate as-of equity value: ~$290 billion ($51.70 x ~5.613B)
- Currency: USD

## 3. Anchor Event

- 2022-02-08 (before market open): Pfizer reported Q4/FY2021 results and issued first 2022 full-year guidance.
- Record full-year 2021 revenue ($81.3B) and record-high 2022 guidance ($98-102B), driven by the COVID-19 franchise (Comirnaty vaccine + Paxlovid oral antiviral).
- Stock screens optically cheap (~8x forward 2022 adjusted-EPS guidance midpoint).

## 4. Decision Question (deferred to a FUTURE blind test — NOT answered here)

Cheap cash machine, or false-cheap peak-earnings trap? At ~8x guided 2022 earnings, is Pfizer a mispriced cash compounder with a re-armed pipeline, or is the market correctly discounting a temporary COVID earnings spike sitting in front of a mid-decade patent cliff?

This material pack collects evidence only. It contains NO buy/sell verdict, NO context label, NO valuation conclusion. The decision_card / thesis / financial_reality / inversion_trap files are the future test and are deliberately absent.

## 5. Allowed Evidence

| Evidence type | Cutoff rule | Notes |
|---|---|---|
| Company releases | Public on or before 2022-02-08 | Pfizer Q4/FY2021 earnings release (8-K ex-99, 2022-02-08), Paxlovid EUA release (2021-12-22), dividend release (2021-12-10), EPIC-HR data releases (Nov 2021) are allowed. |
| SEC filings | Filed on or before 2022-02-08 | Pfizer Q3 2021 10-Q (filed Nov 2021) allowed for share count. NOTE: the FY2021 10-K was filed 2022-02-24 and is therefore OUT — not used. |
| Earnings call | Held 2022-02-08 | Q4 2021 earnings call transcript (2022-02-08) allowed. |
| Trading / market data | Dated on or before 2022-02-08 | 2022-02-08 close and surrounding trading days allowed. |
| Industry / regulatory context | Published on or before 2022-02-08 | FDA Paxlovid authorization (Dec 2021), dated analyst forecasts (e.g., SVB Leerink Nov 2021) allowed as narrative context. |
| News / commentary | Public on or before 2022-02-08 | Dated earnings-reaction coverage (2022-02-08) allowed as narrative context, not core proof. |

## 6. Forbidden Evidence (per LOOKAHEAD_CHECKER registry, pfe_2022-02-08 row)

- Any 2022-2024 COVID-revenue decline / collapse relative to these guidance figures.
- The Seagen acquisition (announced 2023) and any later M&A.
- Any later guidance cuts or revisions after 2022-02-08.
- The later fall in the stock toward ~$25.
- Any post-2022-02-08 realization or confirmation of the patent-cliff outcome.
- The FY2021 10-K (filed 2022-02-24) and all later filings, results, prices, and analyst actions.
- Any wording implying the collector already knows how the COVID franchise or the stock turned out ("later", "subsequently", "went on to", "collapsed to", etc.).

## 7. Freeze Checklist

- [x] As-of date fixed (2022-02-08).
- [x] Price input fixed ($51.70 close; ~$290B equity value).
- [x] Allowed evidence listed; 10-K (2022-02-24) explicitly excluded as post-as-of.
- [x] Forbidden evidence listed (per registry).
- [x] Material-only: no decision, no context label, no valuation verdict in this pack.
- [x] As-of price history saved to backtests/data/asof_2022-02-08_pfe_quotes.csv.
