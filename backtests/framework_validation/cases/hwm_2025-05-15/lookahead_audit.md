# Lookahead Audit (independent) — HWM 2025-05-15

Spec: [backtests/framework_validation/LOOKAHEAD_CHECKER.md](../../LOOKAHEAD_CHECKER.md) + [PROTOCOL.md](../../PROTOCOL.md) §3.

> **Role.** This is the binding audit by the **independent Lookahead Auditor** (a different agent than the
> Runner/collector). It supersedes the Runner's earlier pre-lock self-check. It verifies the case used NO
> information dated after **as_of = 2025-05-15** and no outcome-aware reasoning. Verdict: **CLEAN /
> CLEAN-WITH-NOTES / LEAK**.

## 0. Audit verdict

- **VERDICT: CLEAN-WITH-NOTES.** One trivial, non-load-bearing wording note (§3, Note A); no fix required to score.
- 0 source-date problems. 0 load-bearing facts dated after 2025-05-15. 0 outcome-aware leakage of any realized
  result. No post-as-of price anywhere (the only price-of-record is the **2025-05-15 close $161.29** plus trailing
  Apr–May 2025 daily OHLC and 52-week band stats).
- The live `companies/hwm/` 2026 dossier was **NOT read** (verified: every `companies/hwm` reference is an explicit
  "NOT read / forbidden" statement, never a sourced fact).
- Mechanical gate concurs: `verify_freshness` **PASS** (T7 — all **9** source dates ≤ 2025-05-15; price re-fetch
  $161.2899… = card $161.29).

## 1. Source-date check (every `sources_used.csv` row: public_date ≤ 2025-05-15?)

| source_id | public_date | ≤ as_of? | web-verified? | note |
|---|---|---|---|---|
| S001 FY2024 Q4 release | 2025-02-13 | yes | — | primary |
| S002 FY2024 10-K | 2025-02-13 | yes | — | primary (SEC EDGAR) |
| S003 Q1'25 release | 2025-05-01 | yes | **YES** | **highest-risk row**; web-confirmed BusinessWire 20250501 + howmet.com/press-release/2025-05-01; rev $1.94B / EPS $0.84 match |
| S004 Q1'25 call transcript | 2025-05-01 | yes | (S003 anchors the event) | primary commentary mirror |
| S005 Q1'25 10-Q | 2025-05-01 | yes | — | primary; 14d before as_of |
| S006 as-of price CSV (Yahoo v8) | 2025-05-15 | yes (= last trade ≤ as_of) | re-fetched | $161.29 close; no split since 2016 (verified) → nominal = raw |
| S007 Boeing/Airbus Mar-2025 deliveries | 2025-04-10 | yes | **YES** | web-confirmed pub date 2025-04-10; Boeing 130 / 737 MAX < 38/mo / backlogs 8,720 & 6,319 all match |
| S008 Arconic→Howmet spin-off | 2020-04-01 | yes | — | background |
| S009 Q1'25 webcast notice | 2025-04-10 | yes | — | event-date anchor |

All **9** rows `public_date ≤ 2025-05-15`. **0 source-date problems.** The two most-recent / highest-risk rows
(S003 Q1'25 release, S007 Mar-2025 delivery tracker) were independently web-verified to their claimed dates and
content. Note S007 is dated 2025-04-10 but reports **March-2025** data — correctly in-window (publication and
reference period both ≤ as_of); no later monthly tracker was pulled.

## 2. Claim traceability (load-bearing claims → allowed source)

| key claim | source_id(s) | traceable? |
|---|---|---|
| As-of price $161.29 (5/15/25); mkt cap ~$65.2B (~404M sh); EV ~$67.9B | S006, S005 | yes |
| Q1'25 rev $1.94B (+6%); comm aero +9%; op income $494M (+34%, 25.4%); adj EBITDA $560M (28.8%); adj EPS $0.86 (+51%) | S003 | yes |
| Engine Products $996M (+13%), Fastening +6%, Structures +8%, Wheels −13% | S003 | yes |
| Spares ~20% of rev (+33%); aero/defense spares +40%; defense aero +19%; LEAP destocking clears H2'25 | S004 | yes |
| FY25 guide RAISED: adj EBITDA $2.225–2.275B, adj EPS $3.36–3.44, FCF $1.10–1.20B (from Feb $2.13B/$3.17/$1.075B) | S003, S001 | yes |
| Net debt/EBITDA record-low ~1.4x → target ~1.1x; Fitch upgrade to BBB+; ~$2.0B buyback; dividend doubled to $0.10 | S004, S003 | yes |
| FY2024 rev $7.43B (+12%); op income $1.633B; adj EBITDA $1.914B (25.8%); FCF $977M; COGS 71.9%→68.9%; comm aero +20% | S001, S002 | yes |
| Boeing Q1'25 130 deliveries (737 MAX < FAA-cap 38/mo); Airbus 136; backlogs ~10–11 years | S007 | yes |
| Pure-play post-Arconic spin-off (Apr 1 2020); CEO John Plant (ex-TRW) | S008, S004 | yes |
| Tariff net <$15M 2025 after mitigation (gross ~$80M) | S004 | yes |

No orphan / un-sourced load-bearing claim. Every load-bearing claim traces to a source dated ≤ as_of.

## 3. Outcome-aware language check

Scanned all case files (md + json) for hindsight tokens ("later", "subsequently", "as we now know", "went on to",
"rallied/surged to", "in hindsight", "turned out", "the up-cycle played out") and for any post-2025-05-15 price.

- **0 load-bearing matches** that reference a realized post-as-of outcome.
- **Note A (trivial, non-load-bearing — basis for CLEAN-WITH-NOTES).** `raw_extracts.md` §C (line ~58) reads
  *"Initial FY2025 guide (Feb): … — **subsequently raised at Q1** (see A)."* The flagged token "subsequently" here
  refers to the **Q1'25 raise dated 2025-05-01 (in-window)** — i.e. it describes a Feb→May sequence that is entirely
  ≤ as_of, not a post-cutoff event. It is descriptive, not hindsight about the stock's outcome, and is not a
  load-bearing claim on its own (the raise itself is independently sourced to S003/S001). **No leak; no fix required.**
  Recommend (optional) rewording to "raised at the Q1 update (S003)" to avoid tripping future token scans.
- **No post-as-of price.** HWM's run to ~$278–280 (mid-2026), the ~$305 analyst target, the ~52.7x forward P/E, and
  the raised **2026** revenue outlook ($9.575–9.725B) are all **ABSENT from every module and the decision**. They
  appear in the case ONLY inside (a) `case_control.md`'s forbidden-evidence list and (b) the prior Runner self-check's
  "ABSENT/excluded" registry — i.e. named as things to exclude, never used as facts. (Independently grep-verified.)
- All forward content (the raised **FY25** guide ranges, the build-rate ramp, spares trajectory, LEAP destocking
  clearing by Q3/Q4) is correctly framed as **as-of management guidance / dated industry projection**, never as a
  realized result. Open questions (cycle position, spares durability, the appropriate multiple, Boeing dependence)
  are recorded as **unresolved**, never as a known outcome.

## 4. Post-cutoff fact intrusion check (HWM-specific forbidden registry — each ABSENT)

| forbidden item (post-2025-05-15) | status | note |
|---|---|---|
| Q2 2025 results / any 2025-H2 / FY2025 actuals | **ABSENT** | the case stops at the Q1'25 print (2025-05-01) |
| Any 2026 result, Q1'26 release, guidance update, or FY2026 outlook ($9.575–9.725B) | **ABSENT** | surfaced in web results but NOT opened/used in any module |
| Any HWM price after 2025-05-15 (the ~$278–280 mid-2026 level) | **ABSENT** | price-of-record is the 2025-05-15 close only; ~$280 / 52.7x excluded |
| Later analyst PT / rating (the ~$305 target, "Strong Buy" tallies) | **ABSENT** | excluded; only as-of forward-P/E arithmetic on the raised FY25 guide is used |
| Later buyback / dividend actions beyond Q1 + April 2025 | **ABSENT** | only the dated $125M Q1 + $100M April buyback and the $0.10 dividend appear |
| Post-as-of Boeing/Airbus delivery data (Oct/Dec 2025, 2026) | **ABSENT** | only the March-2025 (pub 2025-04-10) tracker is used |
| The live `companies/hwm/` 2026 dossier | **ABSENT (not read)** | explicit "NOT read" in case_control, evidence_spine, decision_card |

All registry items **ABSENT**.

## 5. Evidence-misuse check

- **KOL / social / video:** none load-bearing. No Twitter/YouTube/Reddit/local-note source is used as proof. The
  webcast notice (S009) is an event-date anchor only; the Forecast International tracker (S007) is cycle-position
  context, not proof HWM must win.
- **Company optimism not stated as verified fact:** management's "record" quarter and raised guide are quoted as
  *management guidance*; the **>100% incremental margins are explicitly flagged as NOT a sustainable run-rate**
  (financial_reality §1/§3, M4 finding), and the up-cycle earnings are treated as *up-cycle* (M4/M5), not
  extrapolated as permanent.

## 6. Decision-isolation check (full backtest case — decision present is OK)

- A full `decision_card` (.md + .json: STARTER / HOLD, ~3% initial / ~8–10% max, buy-below ~$145, kill criteria,
  runner_dissent) **is present** — correct for a P1 backtest case (not a materials-only pack).
- **The decision is justified with as-of reasoning only:** the STARTER-not-CORE / no-chase call rests on the as-of
  fresh 52-week-high entry (−0.27% off high) and ~47×/~30× multiple vs the as-of raised FY25 guide — **not** on any
  post-as-of knowledge that the stock subsequently ran to ~$280. (Had the decision used the outcome, a $161 entry
  that nearly doubled would have argued for CORE, not a cautious STARTER — the conservative call is itself evidence
  the outcome was not used.) No `outcome_score.md` is present in the folder (correct — the Scorer writes that
  post-lock).

## 7. Auditor conclusion

**CLEAN-WITH-NOTES.** No post-2025-05-15 load-bearing fact, no outcome-aware language about a realized result, no
post-as-of price, no `companies/hwm/` intrusion; the decision is reasoned entirely from in-window evidence. The two
highest-risk source dates were independently web-confirmed. The single note (the in-window "subsequently raised at
Q1" phrasing, §3 Note A) is trivial and non-load-bearing — an optional reword, not a leak. The mechanical T7 gate
concurs (PASS, 9/9). **Integrity-clean enough to score.**
