# Lookahead Audit (independent) — HWM 2024-05-15

Spec: [backtests/framework_validation/LOOKAHEAD_CHECKER.md](../../LOOKAHEAD_CHECKER.md) + [PROTOCOL.md](../../PROTOCOL.md) §3.

> **Role.** This is the binding audit by the **independent Lookahead Auditor** (a different agent than the
> Runner/collector). It verifies the case used NO information dated after **as_of = 2024-05-15** and no
> outcome-aware reasoning. Verdict scale: **CLEAN / CLEAN-WITH-NOTES / LEAK**.

## 0. Audit verdict

- **VERDICT: CLEAN.**
- 0 source-date problems. 0 load-bearing facts dated after 2024-05-15. 0 outcome-aware leakage. No post-as-of
  price anywhere (the only price-of-record is the **2024-05-15 close $82.75** plus trailing 52-week OHLC stats).
- The live `companies/hwm/` 2026 dossier was **NOT read** (verified: every `companies/hwm` reference in the case
  is an explicit "NOT read / forbidden" statement, never a sourced fact).
- Mechanical gate concurs: `verify_freshness` **PASS** (T7 — all **18** source dates ≤ 2024-05-15; price re-fetch
  $82.75 = card).

## 1. Source-date check (every `sources_used.csv` row: public_date ≤ 2024-05-15?)

| source_id | public_date | ≤ as_of? | web-verified? | note |
|---|---|---|---|---|
| S001 FY2023 10-K | 2024-02-13 | yes | — | primary (SEC EDGAR) |
| S002 Q4/FY2023 release | 2024-02-13 | yes | — | primary |
| S003 Q1'24 release | 2024-05-02 | yes | **YES** | **highest-risk row**; web-confirmed BusinessWire 20240502 + howmet.com/press-release/2024-05-02; rev $1.82B / EPS $0.59 match |
| S004 Q1'24 10-Q | 2024-05-02 | yes | — | primary; 13d before as_of |
| S005 Q1'24 call transcript | 2024-05-02 | yes | (S003 anchors the event) | management quotes; corroborated mirror |
| S006 as-of price CSV (Yahoo v8) | 2024-05-15 | yes (= last trade ≤ as_of) | re-fetched | $82.75 close; no split since 2016 (verified) → nominal = raw |
| S007 Plant officer bio | 2024-05-15 | yes | — | structural background |
| S008 RTX GTF charge (CNBC) | 2023-09-11 | yes | — | GTF crisis context |
| S009 GE Aerospace Q1'24 | 2024-04-23 | yes | **YES** | web-confirmed 2024-04-23; spare-parts volume strength matches |
| S010 Safran FY2023 | 2024-02-15 | yes | — | aftermarket corroboration |
| S011 RTX Q1'24 | 2024-04-23 | yes | — | P&W +23% |
| S012 IATA FY2023 RPK | 2024-01-31 | yes | — | traffic recovery |
| S013 Airbus Q1'24 | 2024-04-25 | yes | — | ramp toward 75/mo |
| S014 Boeing Q1'24 | 2024-04-24 | yes | — | near-term MAX headwind |
| S015 Airbus+Boeing YE2023 backlog | 2024-01-15 | yes | — | record backlog |
| S016 Lockheed F-35 2024 plan | 2024-01-26 | yes | — | defense steady |
| S017 Class 8 truck outlook (FTR Mar-2024) | 2024-03-15 | yes | — | Forged Wheels headwind |
| S018 Russian titanium / VSMPO | 2024-03-01 | yes | — | input constraint |

All **18** rows `public_date ≤ 2024-05-15`. **0 source-date problems.** The two most-recent / highest-risk rows
(S003 Q1'24 release, S009 GE Q1'24) were independently web-verified to their claimed dates and content. No source
dated after as_of; nothing one-day-after the boundary (cf. the AAPL/NVDA registry traps).

## 2. Claim traceability (load-bearing claims → allowed source)

| key claim | source_id(s) | traceable? |
|---|---|---|
| As-of price $82.75 (5/15/24); mkt cap ~$33.8B (408.17M sh) | S006, S004 | yes |
| FY2023 rev $6,640M (+17%); Engine Products $3,266M largest; op margin ~18.1% | S001, S002 | yes |
| FY2023 net income $765M; GAAP $1.83 ≈ adj $1.84; FCF $682M | S002 | yes |
| End-market mix 49/15/21/15 (~64% aero); GE ~12% / RTX ~9% | S001 | yes |
| Q1'24 rev $1.82B (+14% record); comm aero +23%; adj EBITDA $437M (24.0%); adj EPS $0.57 (+36%); 1st +ve Q1 FCF | S003 | yes |
| FY24 guide RAISED: rev $7.225–7.375B, adj EPS $2.31–2.39, adj EBITDA $1.72–1.78B, FCF $750–850M | S003 | yes |
| 737 MAX assumed ~20/mo; net replan +$200M FY rev; 35% incremental EBITDA margin | S005 | yes |
| Moody's Baa3 (2024-02-29) → IG at all 3 agencies; +40% dividend; $150M Q1 buyback @ $66.87 | S003, S005 | yes |
| GTF ~350 A320neo grounded/yr through 2026 (peak Q1'24); GE spares +25%; Safran aftermarket +33% | S008, S009, S010 | yes |
| Record ~11–12yr Airbus+Boeing backlog; Airbus toward 75/mo; IATA ~100% of 2019 | S015, S013, S012 | yes |
| Boeing Q1'24 below FAA 38/mo cap; FTR Class 8 −26% for 2024 | S014, S017 | yes |

No orphan / un-sourced load-bearing claim. Every load-bearing claim traces to a source dated ≤ as_of.

## 3. Outcome-aware language check

Scanned all case files (md + json) for hindsight tokens ("later", "subsequently", "as we now know", "went on to",
"rallied/surged to", "in hindsight", "turned out", "the run played out") and for any post-2024-05-15 price.
- **0 load-bearing matches.** The only "later" hits are (a) `case_control.md` defining the forbidden list
  (e.g. "it later rallied" as a *banned* example) and (b) the phrase "mid-to-later in a recovery" in
  `financial_reality.md` — a **cycle-position description**, not a hindsight claim about a realized outcome.
- **No post-as-of price.** HWM's run toward ~$280 (mid-2026) is **ABSENT**; the "278" grep hit is FY2023 Fastening
  Systems segment EBITDA **$278M** (a legitimate as-of figure), not a price. No +238% / +74% move appears.
- Forward content (the raised FY24 guide, GTF "through 2026" forecast, build-rate ramp) is correctly framed as
  **as-of management guidance / dated industry projection** (S003/S005/S008), not as a realized result.

## 4. Post-cutoff fact intrusion check (HWM-specific forbidden registry — each ABSENT)

| forbidden item (post-2024-05-15) | status | note |
|---|---|---|
| Any HWM quarterly result after Q1 2024 (Q2'24+) and the FY2024 10-K (filed 2025) | **ABSENT** | the case stops at the Q1'24 print (2024-05-02) |
| Any 2024-H2 / 2025 / 2026 result, guidance, financing, buyback, dividend, or contract event | **ABSENT** | only the dated H1'24 events (incl. the *planned* H2'24 dividend hike, announced 2024-05-02) appear |
| Any HWM price/market-cap after 2024-05-15 (the run to ~$280) | **ABSENT** | price-of-record is the 2024-05-15 close $82.75 + trailing 52wk OHLC only |
| Post-date GTF / Boeing-rate / Airbus-rate / Class-8 revisions | **ABSENT** | only the dated ≤ 2024-05-15 build-rate set is used |
| Later analyst / guru / institutional / index action | **ABSENT** | none cited; the price view rests on math + filings, not a post-date sell-side note |
| The live `companies/hwm/` 2026 dossier | **ABSENT (not read)** | explicit "NOT read" in case_control, evidence_spine, decision_card |

All registry items **ABSENT**.

## 5. Evidence-misuse check

- **KOL / social / video:** none load-bearing (evidence_spine §3 states none used as proof; verified — no
  Twitter/YouTube/Reddit/local-note source appears). The one transcript (S005, Insider Monkey mirror) is a
  management-call record, cross-checked against the primary release (S003), not a social lead.
- **Company optimism not stated as verified fact:** the record quarter / raised guide are quoted as *management
  guidance*; the demand upturn is corroborated **externally** (GE/Safran/RTX/Airbus/Boeing/IATA), not on HWM's word;
  the record 24% margin is explicitly flagged as **partly cyclical** (M4 §2, M5 §2), not extrapolated as permanent.

## 6. Decision-isolation check (full backtest case — decision present is OK)

- A full `decision_card` (.md + .json: STARTER / HOLD, ~3% initial / ~10% max, buy-below ~$72, kill criteria,
  runner_dissent) **is present** — correct for a P1 backtest case (not a materials-only pack).
- **The decision is justified with as-of reasoning only:** the STARTER-not-CORE call rests on the as-of 52-week-high
  entry and ~45×/~35× multiple vs the as-of raised guide — **not** on any post-as-of knowledge of where the stock
  went. No `outcome_score.md` is present in the folder (correct — the Scorer writes that post-lock).

## 7. Auditor conclusion

**CLEAN.** No post-2024-05-15 load-bearing fact, no outcome-aware language, no post-as-of price, no `companies/hwm/`
intrusion; the decision is reasoned entirely from in-window evidence. The two highest-risk source dates were
independently web-confirmed. The mechanical T7 gate concurs (PASS, 18/18). **Integrity-clean enough to score.**
