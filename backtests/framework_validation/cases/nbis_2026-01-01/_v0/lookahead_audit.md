# QA Lookahead Audit - NBIS 2026-01-01

## 0. Audit Verdict

- Verdict: **CLEAN** for runner files.
- As-of date: 2026-01-01. Price date: 2025-12-31 close ($83.71).
- No post-cutoff fact is used as a load-bearing claim. Every source resolves to a publication date on or before 2026-01-01, and the load-bearing figures trace to allowed primary sources. The one item flagged for special scrutiny (the $7-9B exit-2026 ARR target) was **independently verified to have been public on 2025-11-11** in the Q3 2025 shareholder letter; it is NOT a look-ahead leak (detail in Sections 4-5).
- Auditor note: `outcome_score.md` does not yet exist and is scorer-only; it is exempt from this audit.
- Files audited:
  - `case_control.md`
  - `sources_used.csv`
  - `raw_extracts.md`
  - `evidence_spine.md`
  - `thesis_mechanism.md`
  - `profit_pool_durability.md`
  - `financial_reality.md`
  - `inversion_trap_test.md`
  - `decision_card.md`
  - `decision_card.json`

## 1. Source Date Check

Independently web-verified rows are marked "yes (web)". Rows verified by internal consistency / EDGAR accession against an already-verified filing cluster are marked "yes (filing)".

| source_id | claimed public_date | verified? | allowed (<= 2026-01-01)? | issue |
|---|---|---|---|---|
| S001 | 2025-02-20 | yes (web) | yes | none. Confirmed FY2024 release 2025-02-20; rev $117.5M, Q4 $37.9M, cash $2,449.6M all match |
| S002 | 2025-04-30 | yes (filing) | yes | none. FY2024 20-F; standard ~April 20-F filing date, EDGAR accession 000155837025005991 |
| S003 | 2025-05-20 | yes (filing) | yes | none. Q1'25 release; same EDGAR cluster as S004 |
| S004 | 2025-05-20 | yes (filing) | yes | none. Q1'25 shareholder letter, Ex-99.2 of same 6-K |
| S005 | 2025-08-07 | yes (filing) | yes | none. Q2'25 release; EDGAR accession 000110465925075028 |
| S006 | 2025-08-07 | yes (filing) | yes | none. Q2'25 shareholder letter, Ex-99.2 of same 6-K |
| S007 | 2025-09-08 | yes (filing) | yes | none. Microsoft announcement 6-K Ex-99.1 |
| S008 | 2025-09-08 | yes (filing) | yes | none. Microsoft terms 6-K, accession 000110465925088312 |
| S009 | 2025-09-10 | yes (web) | yes | none. Confirmed $2.75B converts priced 2025-09-10 (1.00%/2030 + 2.75%/2032) |
| S010 | 2025-09-10 | yes (web) | yes | none. Confirmed $1.0B equity at $92.50 priced 2025-09-10 |
| S011 | 2025-09-15 | yes (web) | yes | none. Confirmed closings ~$4.2B announced 2025-09-15 |
| S012 | 2025-11-11 | yes (web) | yes | none. Q3'25 results released 2025-11-11 (6-K furnished; EDGAR stamp 11/12) |
| S013 | 2025-11-11 | yes (web) | yes | none. Q3'25 shareholder letter PDF; cover reads "November 11, 2025" (verified from the document itself) |
| S014 | 2025-12-31 | yes (web) | yes | none. 2025-12-31 close $83.71 consistent with late-Dec tape |
| S015 | 2024-12-02 | yes (web) | yes | none. $700M raise at $21.00 (NVIDIA/Accel/Orbis) corroborated in the FY2024 release |
| S016 | 2024-10-17 | yes (filing) | yes | none. Relisting announcement; NBIS trading resumed 2024-10-21 |
| S017 | 2024-02-05 | yes (filing) | yes | none. Yandex divestiture 6-K Ex-99.1 |
| S018 | 2025-03-27 | yes (web) | yes | none. CoreWeave IPO priced $40 on 2025-03-27 |
| S019 | 2025-11-10 | yes (filing) | yes | none. CoreWeave Q3'25 release, one day before NBIS Q3 |
| S020 | 2025-04-10 | yes (filing) | yes | none. IEA "Energy and AI" report (April 2025) |
| S021 | 2025-12-13 | yes (web) | yes | none. Nasdaq-100 annual changes announced 2025-12-12/13, effective 2025-12-22; NBIS NOT added (adds were ALNY/FER/INSM/MPWR/STX/WDC). Confirms NO index-inclusion tailwind at as-of |
| S022 | 2025-12-30 | yes (web) | yes | none. Benzinga short-interest article; 33.07M sh = 15.47% of float, 2.76 days to cover - exact match |
| S023 | 2025-10-01 | yes (filing) | yes | none. Avride/Uber up to $375M disclosed in the Q3 2025 letter (S013); dated Oct 2025 |

**Result: 0 source-date problems. All 23 sources are dated on or before 2026-01-01.**

## 2. Claim Traceability (spot-check)

| claim | module(s) | source_id | traceable? |
|---|---|---|---|
| As-of price $83.71 (2025-12-31 close); ~$21.1B mkt cap on 251.8M sh | M1 / M6 / json | S014 (+ S012 share count) | yes |
| Q3'25 revenue $146.1M (+355% YoY, +39% QoQ); core ~90% of rev | M1 / M4 | S012, S013 | yes |
| Core ARR ramp ~$220M -> $249M -> $430M -> $551M | M1 / M2 / M3 / M4 | S001, S004, S006, S013 | yes |
| Core adj-EBITDA positive ~19% margin; group adj EBITDA -$5.2M | M3 / M4 | S005, S013 | yes |
| Q2'25 GAAP +$502.5M was a Toloka revaluation, not operations; adj net loss -$91.5M | M4 | S005 | yes |
| Balance sheet 9/30/25: cash $4,794.8M, debt ~$4,106.8M (net-cash) | M4 | S012 | yes |
| Microsoft deal ~$17.4B (to ~$19.4B) through 2031, 5-yr, Vineland NJ | M2 / M3 | S007, S008 | yes |
| Meta deal ~$3B / 5-yr, announced 2025-11-11, capacity-limited | M2 / M3 | S012, S013 | yes (verified verbatim) |
| Contracted power raised to >2.5GW by CYE2026 (from 1GW); 800MW-1GW connected | M2 / M3 / M5 | S013 | yes (verified verbatim) |
| $7-9B exit-2026 ARR target (stated twice in CEO letter) | M1 / M2 / M4 / M6 | S013 | yes (verified verbatim - see S4/S5) |
| Sept 2025 raise ~$4.2-4.3B: $2.75B converts + $1.0B equity at $92.50; conv ~$138.75 | M4 / M6 | S009, S010, S011 | yes |
| 4-year hardware depreciation schedule | M2 / M4 | S013 | yes (and correctly NOT the later 5-yr change) |
| NBIS NOT in Nasdaq-100; short interest ~15.5% of float | M1 / M5 | S021, S022 | yes |
| CoreWeave comp: ~$23B IPO EV, MSFT 62% of 2024 rev; Q3'25 rev $1.36B | M3 / M4 | S018, S019 | yes |

All load-bearing claims trace to an allowed source_id. No orphan claims found.

## 3. Outcome-Aware Language Check

- No hindsight phrasing found. Scanned all module files for "later", "as we now know", "went on to", "subsequently", "turned out", "rallied", "in hindsight", "we now know", and any 2026 price. None present as outcome statements.
- The only forward-looking language is management's own as-of guidance (quoted as guidance, e.g. the $7-9B ARR target and the 2.5GW power plan), and the Runner's own scenario hypotheticals (base/upside/downside), which are framed as prospective judgments, not knowledge of the result.
- The decision is consistently framed as a 2026-01-01 starter judgment under uncertainty (e.g. M6 "Runner Dissent" explicitly reasons about not knowing the outcome). No reference to any post-as-of price, result, or event as fact.

## 4. Post-Cutoff Fact Intrusion (item-by-item)

Each later event/figure from the brief was checked against all runner files. "Not used" = does not appear as a used fact anywhere in the package.

| # | Later event / figure | Real public date | Used in runner files? | Verdict |
|---|---|---|---|---|
| 1 | Q4 2025 / FY2025 results | ~2026-02-12 | No. Trajectory stops at Q3'25 (9/30/25). FY2025 ARR (~$1.25B) does NOT appear. | CLEAN |
| 2 | FY2025 20-F | ~2026-04-30 | No. Only the FY2024 20-F (S002) is used. | CLEAN |
| 3 | Q1 2026 results / shareholder letter | 2026-05-13 | No. Q1'26 ARR (~$1.9B) and FY2026 revenue guide ($3.0-3.4B) do NOT appear. | CLEAN |
| 4 | Second Meta agreement (~$27B) | 2026-03-16 | No. Only the ~$3B Meta deal (announced 2025-11-11, verified verbatim in S013) is used. The $27B / $12B+$15B / Vera Rubin / "starting early 2027" details are absent. | CLEAN |
| 5 | NVIDIA $2B pre-funded warrant | 2026-03-11 | No. Only the Dec 2024 $700M strategic raise (S015) and NVIDIA's supplier/investor status are used. The 21,065,936-share warrant is absent. | CLEAN |
| 6 | Bloom Energy ~$2.6B / 328 MW deal | 2026-05-14 (announced ~05-20/21) | No. Power discussion is limited to the 2.5GW contracted plan from S013. Bloom Energy / 328 MW / fuel cells are absent. | CLEAN |
| 7 | Server depreciation life change 4->5 years | Q1 2026 (announced 2026) | No. The package consistently uses the **4-year** schedule (S013) and even cites it as a conservatism flag. The 5-year change is absent. | CLEAN |
| 8 | Nasdaq-100 inclusion | ~2026-06 | No. The package correctly states NBIS was **NOT** added in the Dec 2025 reconstitution (S021) and lists "no index tailwind yet" as an as-of negative. | CLEAN |
| 9 | 2026 convertible/equity financings (e.g. March 2026 $4.0B converts) | 2026 | No. Only the September 2025 raise (S009-S011) and the Nov-2025-announced ATM (up to 25M Class A sh) are used. The 2026 $4.0B convert is absent. | CLEAN |
| 10 | Any stock price after 2025-12-31 close (~$83.71) | post-2025-12-31 | No. The as-of price is the 2025-12-31 close $83.71; no later price is referenced. | CLEAN |

**No post-cutoff fact intrusion.** Notably, several of the most tempting leaks (FY2025 ARR beat, the $27B Meta deal, the depreciation change, Nasdaq-100 inclusion) are exactly the facts a hindsight-contaminated case would have used to inflate the bull thesis - and none appear. The package is disciplined precisely where it would matter most.

## 5. ARR Target Special Scrutiny (the $7-9B vs $4.3B question)

This was the highest-risk item. Finding: **the $7-9B exit-2026 ARR target was genuinely public on 2025-11-11; using it is NOT a leak.** Verified directly against the primary source (the Q3 2025 shareholder letter PDF, extracted verbatim):

- **Letter body (verbatim):** *"...the extensive work that we have undertaken to build out our capacity, we believe that we can achieve annualized run-rate revenue (ARR) of $7 billion to $9 billion by the end of 2026."* This appears in the body and is consistent with the brief's "stated twice."
- **Cover infographic (verbatim, "momentum into 2026" panel):** lists *"$7-9 billion"* alongside the power-ramp graphic (Connected power CYE2026 "800 MW - 1 GW", Contracted power CYE2026 ">2.5 GW"). So the cover ALSO carries the $7-9B figure.
- **The conflicting "$4.3 billion" on the cover is a typo/design artifact in the ORIGINAL document, and it is the September capital raised - not an ARR target.** The same letter states verbatim: *"On the financing front, we raised a total of $4.3 billion in convertible notes and a follow-on equity offering in September..."* The cover's stray line *"$4.3 billion expected annualized run-rate revenue at year-end 2026"* mislabels the financing figure; the document's own body and its own cover ARR-panel both say $7-9B.

Conclusion: The Runner's handling (treat the stated ARR target as $7-9B; flag the $4.3B cover line as a likely design artifact = the Sept raise) is **correct and matches the primary source.** The $7-9B figure was NOT first stated in any 2026 disclosure - it originates in the 2025-11-11 letter that is squarely within the allowed evidence window. There is no inflation-via-look-ahead here. (For reference, the post-cutoff record confirms management *reiterated* the same $7-9B ARR target in the Q1 2026 call, consistent with it being a standing 2025-vintage target rather than a later raise.)

The correct as-of figure is therefore **$7-9B exit-2026 ARR (as-of 2025-11-11)** - exactly what the Runner used. No correction required.

## 6. Evidence Misuse

- **No KOL / social / video used as proof.** M1 explicitly states no KOL/social/video material was load-bearing and that the post-cutoff `companies/nbis/` folder was NOT read (per case control). Confirmed: no such citations appear.
- **Two secondary items, both correctly down-weighted:**
  - S022 (Benzinga short interest) - used only for positioning/sentiment ("contested tape"), not as a cash-flow fact. Independently verified accurate. Acceptable.
  - The Goldman Sachs "$68 -> $155" target headline (appears in `raw_extracts.md` section L only) - labeled "secondary, dated headline" and NOT carried into the decision logic or the JSON drivers. The Nov-2025 raise to $155 is pre-cutoff and verified. Used as narrative anchor only. Acceptable; not load-bearing.
- **Management optimism is treated as framing, not proof.** M2/M4 repeatedly haircut management language: the $7-9B ARR is explicitly called a run-rate that "can flatter lumpiness," deal economics are flagged as undisclosed (M1 open questions Q1-Q5), and the financing path is called "unproven." The optimistic framing is verified-or-hedged, not taken at face value.
- **One internal inconsistency, immaterial:** S013's `used_for` text says "core grew 400% YoY" while the cover panel growth figure differs in places; this is a paraphrase of management's own wording and does not affect any decision input. Non-load-bearing.

## 7. Decision

- **Final verdict: CLEAN.** The runner package uses no information dated after 2026-01-01 as a load-bearing claim, contains no outcome-aware language, and survives item-by-item post-cutoff intrusion testing. All 23 sources are date-valid.
- **The special-scrutiny ARR target is legitimate.** The $7-9B exit-2026 ARR figure was public on 2025-11-11 (verified verbatim from the primary source). It is the correct as-of figure; the $4.3B is a cover typo equal to the September raise, and the Runner correctly identified it as such. No claim must be removed or corrected.
- **Materiality:** N/A - there is no leak. Had the $7-9B figure been a 2026-only number, it would have been a material leak (it is the central bull metric underpinning M2 +2, M4 +1, and the M6 STARTER). Because it is verified as a 2025-vintage, as-of-available target, the locked STARTER (2.0% initial, 4.0% max) verdict stands on legitimately point-in-time evidence. The case may be scored.
