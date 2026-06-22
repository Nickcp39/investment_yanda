# NBIS Research Run — Layer 3/4: Financials & Accounting + Claim Verification

- Run date: 2026-06-18
- Method: general-purpose research subagent; primary docs fetched from SEC EDGAR (FY2025 20-F filed Apr 30 2026; Q1 2026 6-K filed May 13 2026), cross-referenced with Nebius IR press releases/shareholder letters
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Claims here are NOT yet promoted to facts. Every figure must pass through `claim_ledger.csv` (with source ID + status + confidence) before use in `facts.md`, analysis, or memo.
- Subagent id (may expire across sessions): acc3acae3022bd3a6
- Subagent tokens: 84,888 | tool_uses: 18

---

# Nebius Group (NASDAQ: NBIS) — Audited Financial Base & Claim Verification

*As-of 2026-06-18. Latest reported period: Q1 2026 (reported May 13, 2026). Foreign private issuer, **U.S. GAAP** (not IFRS), files 20-F/6-K. SEC CIK 0001513845. All figures USD.*

> **Note on reporting basis:** In 2025 Nebius reclassified **Toloka** to discontinued operations (it had already spun out the Russian/Yandex assets). This created a **restatement** of FY2024: the originally reported FY2024 group revenue of **$117.5M** became **$91.5M on a continuing-operations basis**. Both numbers are "real" — they sit on different bases. The verification table flags this explicitly.

---

## 1. CLAIM VERIFICATION TABLE (vs the old YouTube-sourced brief)

| # | Claim (from YouTube commentator) | Verdict | Actual figure | Source |
|---|---|---|---|---|
| 1 | FY2024 rev ~$117M vs FY2023 ~$21M | **VERIFIED (original basis); restated lower** | FY2024 **$117.5M** as originally reported (+462%); **restated to $91.5M** continuing-ops in FY2025 20-F. FY2023 ~$21M original → **$9.8M** restated | [PRIMARY] FY2024 6-K (Feb 20 2025); [PRIMARY] FY2025 20-F income stmt "Total revenues 9.8 / 91.5 / 529.8" |
| 2 | Q4 2024 rev ~$38M | **VERIFIED** | **$37.9M** (+466% YoY) original; ~$35.2M on restated basis | [PRIMARY] FY2024 6-K, Feb 20 2025 |
| 3 | Q1 2025 ARR ~$200M | **REFUTED (too low)** | **$249M** end-Mar-2025 (+684% YoY); ~$310M by April | [PRIMARY] Q1 2025 shareholder letter (6-K), May 20 2025 |
| 4 | FY2025 revenue guidance ~$700M | **REFUTED / mislabeled** | No revenue guide given; company guides **year-end ARR**: original **$750M–$1.0B**, raised to **$900M–$1.1B** (Aug 2025). Actual FY2025 *revenue* = **$529.8M** | [PRIMARY] FY2024 6-K; Q2 2025 release |
| 5 | Cash ~$2B+ | **VERIFIED for YE2024; now far higher** | $2,434.7M (Dec-31-2024) → dipped to $1,447.0M (Q1'25) → **$9,298.2M (Mar-31-2026)** | [PRIMARY] FY2025 20-F; Q1 2026 6-K MD&A |
| 6 | FY2025 capex ~$1B+ | **VERIFIED but understated** | FY2025 actual capex **$4,066.0M** (~$4.07B). FY2024 was $807.5M | [PRIMARY] FY2025 20-F cash-flow stmt |
| 7 | Microsoft contract ~$17.4B multi-year | **VERIFIED (exact)** | **$17,392.9M** through Oct 2031 (5-yr); up to **$19.4B** with options; **$6,958.1M upfront**; take-or-pay | [PRIMARY] FY2025 20-F: "up to $17,392.9… irrespective of actual utilization… upfront payments of ~$6,958.1" |
| 8 | GPUs ~20k end-2024 → 35–60k in 2025 | **CAN'T VERIFY (not company-disclosed)** | Nebius reports **megawatts**, not fleet GPU counts. ~25MW end-2024 → ~1GW target end-2025; >3.5GW contracted by Q1'26. "60k/35k" are per-site ceilings (Finland/Kansas City), not fleet totals | [PRIMARY] shareholder letters (MW); GPU counts only in secondary/site press |
| 9 | EBITDA positive within 2025 | **VERIFIED** | **Core/Nebius AI segment** turned positive adj. EBITDA in **Q2 2025**; **group** adj. EBITDA positive **Q4 2025 (+$15.0M)**. Group FY2025 still −$64.9M | [PRIMARY] FY2025 20-F segment recon; Q2/Q4 2025 releases |
| 10 | NVIDIA owns ~1.2M NBIS shares | **VERIFIED (but understates exposure)** | ~1.2M common shares (~$134M) per NVIDIA 13F (6/30/25). Plus **$2.0B pre-funded warrant for 21,065,936 shares** (Mar 2026) — not in 13F until exercised | [SECONDARY] 13F coverage; [PRIMARY] Q1 2026 6-K (warrant) |

**Net read on the old commentator:** Directionally right on the hard, checkable numbers (FY2024 rev, Q4 rev, Microsoft deal exact, cash, EBITDA turn, NVIDIA stake). **Wrong/sloppy on three:** Q1'25 ARR was **$249M not ~$200M** (#3); the "~$700M FY2025 revenue guidance" conflates ARR with revenue and is below the real **$750M–$1.0B ARR** target (#4); and 2025 capex was **~$4B, not ~$1B** (#6 — understated by ~4x). GPU counts (#8) are not company-disclosed.

---

## 2. QUARTERLY FINANCIAL ACTUALS (2024 → Q1 2026)

**Revenue & ARR** (group revenue; ARR = core AI, "last month of quarter × 12" — *unaudited, not in 20-F*):

| Period | Group revenue | YoY | ARR (exit) | Group adj. EBITDA |
|---|---|---|---|---|
| Q4 2024 | $37.9M (orig) / $35.2M (restated) | +466% | $90M (Dec'24) | −$75.5M (orig) |
| **FY2024** | **$117.5M orig / $91.5M restated** | +462% | $90M | **−$226.3M** (restated) |
| Q1 2025 | $55.3M | +385% | **$249M** (Mar'25) | −$62.6M |
| Q2 2025 | $105.1M | +625% | $430M (Jun'25) | core positive; group neg. |
| Q3 2025 | $146.1M | +355% | (capacity sold out) | −$45.9M |
| Q4 2025 | $227.7M | +547% | **$1.25B** (Dec'25) | **+$15.0M** ← first group-positive |
| **FY2025** | **$529.8M** | +479% | $1.25B | **−$64.9M** |
| **Q1 2026** | **$399.0M** | **+684%** | **$1.9B** (Mar'26) | **+$129.5M** |

*Q1/Q2 2024 quarterly revenue were never broken out; only Q3 2024 ($43.3M) and Q4 2024 disclosed.*

**Margins (FY2025 / latest):** Gross margin **~69% FY2025, ~70% Q4'25**. Cost of revenue fell to **26% of revenue in Q1 2026** (from 49% in Q1 2025) — real operating leverage. **Core Nebius AI segment** adj. EBITDA margin: ~19% (Q3'25) → 24% (Q4'25) → ~45% (Q1'26). **Group operating margin remains deeply negative** — FY2025 operating loss; D&A jumped to **$417.9M** (FY2025) from $77.1M (FY2024).

**Is adjusted EBITDA positive?** Yes at group level since **Q4 2025**, and strongly positive in Q1 2026 (+$129.5M vs −$53.7M a year earlier). Caveat: FY2025 *pre-tax* net income of +$13.8M was driven entirely by a **+$598.9M non-cash ClickHouse revaluation gain** — strip that out and the group is still loss-making operationally.

**Capex & intensity** (computed; company doesn't state intensity):
- FY2024 $807.5M → FY2025 **$4,066.0M** → Q1 2026 **$2,472.9M** (≈$2.5B in one quarter)
- Intensity: FY2024 ~8.8× revenue · FY2025 ~7.7× · Q1'26 ~6.2× quarterly revenue. **Capex enormously exceeds revenue** — this is a capital-consumption story funded by external financing + customer prepayments.

**Cash, debt, net position:**

| Date | Cash & equiv | Convertible debt (carrying) | Net cash/(debt), carrying |
|---|---|---|---|
| Dec-31-2024 | $2,434.7M | ~$6.1M | ~net cash |
| Mar-31-2025 | $1,447.0M | — | — |
| Sep-30-2025 | $4,794.8M | — | — |
| **Dec-31-2025** | **$3,678.1M** | **$4,127.7M** ($4,836.8M principal) | **≈ −$450M net debt** (carrying) |
| **Mar-31-2026** | **$9,298.2M** | **$8,450.4M** ($10,041.8M principal) | **≈ +$848M net cash** (carrying) |

> All debt is **convertible notes** — no term loans or drawn credit facilities. On a **principal** basis the company is net-debt (~−$762M at Q1'26); on a carrying basis it's modest net cash. Aggregators calling it cleanly "net cash" overstate it — flag the convention.

**Free cash flow** (company reports no FCF line; OCF − capex):

| Period | OCF | Capex | Implied FCF |
|---|---|---|---|
| FY2024 | −$269.9M (cont. ops) | −$807.5M | **≈ −$1,077M** |
| FY2025 | +$401.9M* | −$4,066.0M | **≈ −$3,664M** |
| Q1 2026 | +$2,258.0M* | −$2,472.9M | **≈ −$215M** |

\* OCF is **heavily inflated by customer prepayments** (Microsoft/Meta take-or-pay upfronts): FY2025 OCF included ~$982.5M of advances; Q1 2026 deferred revenue rose ~$3.2B. **FCF is deeply negative and the gap is plugged by financing + customer cash, not organic generation.**

**FY2026 guidance (raised at Q1 2026 call, May 13 2026):**
- Revenue **$3.0B–$3.4B**
- **ARR exit-rate $7B–$9B by Dec 2026** (raised from an earlier $4.3B target; >half already contracted)
- Group adj. EBITDA margin ~**40%**
- **Capex $20B–$25B** (raised from $16–20B). ⚠️ *One open flag:* some June-2026 secondary snippets cite **$31–35B** capex paired with a "$6.8B Q1" figure that does **not** match audited Q1 capex of $2,472.9M — likely a later (Q2 2026?) revision or error. **Recommend confirming against the Q2 2026 6-K when it drops (~Aug 2026).**

---

## 3. FINANCING & DILUTION HISTORY (since Oct-21-2024 Nasdaq relisting)

| # | Date | Type | Amount | Key terms / participants |
|---|---|---|---|---|
| 1 | Dec 2 2024 | Equity private placement | **$700M** | 33,333,334 Class A @ **$21.00**; NVIDIA, Accel, Orbis |
| 2 | Jun 2025 | Convertible notes | **$1.0B** | $500M 2.00% due 2029 + $500M 3.00% due 2031; conv. ~$51.45 (+40%) |
| 3 | Sep 2025 | Public equity follow-on | **$1.0B** (+$150M greenshoe) | ~10.8M Class A @ **$92.50**; GS/MS/BofA/Citi |
| 4 | Sep 2025 | Convertible notes (upsized $2.0B→$2.75B) | **$2.75B** | $1.375B 1.00% due 2030 + $1.375B 2.75% due 2032; conv. ~$138.75 |
| 5 | Nov 2025 | ATM equity program | up to 25M Class A shares | filed w/ Q3 results; 1.25% commission |
| 6 | Mar 2026 | NVIDIA pre-funded warrant (equity) | **$2.0B** | 21,065,936 Class A @ $0.0001 exercise (~$94.97 eff.); NVIDIA to deploy >5GW NVIDIA systems by 2030 |
| 7 | Mar 2026 | Convertible notes | **~$4.34B** | $2.25B 1.25% due 2031 + $1.75B 2.625% due 2033 + over-allotment |

**Totals raised since relisting: ~$12.5B+** (~$3.7B equity/warrant + ~$8.1B converts + ATM capacity).

**Share count & dilution:**
- At relisting (Sep-30-2024): **~199.3M** total (163.6M Class A + 35.7M Class B)
- Mar-31-2026: **253,898,194** total (220.4M Class A + 33.5M Class B, ex-treasury)
- **Basic dilution ≈ +27%** over ~18 months. **Plus overhang not yet in basic count:** 21.07M NVIDIA warrant shares + convertible-note conversion shares (2029/2031/2030/2032/2031/2033 notes). Fully-diluted dilution is materially higher.

*Holder note (not a raise): Leopold Aschenbrenner's Situational Awareness LP disclosed a 13G — 12,410,060 Class A (5.6%, ~$2.6B) on May 27, 2026.*

---

## 4. ACCOUNTING-QUALITY FLAGS (all [PRIMARY] from FY2025 20-F, filed Apr 30 2026)

1. **🚩 GPU/server depreciation life extended 4→5 years**, effective Jan 1 2026, applied prospectively. Verbatim: *"the estimated useful lives of such assets should be extended from four to five years… we expect this change… will reduce the depreciation expenses for fiscal year 2026 by approximately $167.6 million."* Servers/GPUs were at **4 years** through FY2025 (more conservative than peers' 6 yrs, but the change happens in the same year as the controls weakness below). Method: straight-line.

2. **🚩 Adverse ICFR opinion — two consecutive years** (FY2024 & FY2025). **Two open material weaknesses** at Dec-31-2025: **(a) fixed assets/PP&E** — *"controls… over depreciation start dates, and timely reconciliation around the asset count process"* were not effective; **(b) TripleTen revenue recognition.** The fixed-asset MW sits directly on top of the depreciation accounting and the useful-life change. P&E and revenue-classification are both **Critical Audit Matters.**

3. **Microsoft (and Meta) revenue = take-or-pay, booked as service revenue under ASC 606 — not a lease.** *"irrespective of actual utilization."* The service-vs-lease judgment is the **#1 CAM.** Reserved-capacity revenue recognized **ratably over the service term**; ~$6.96B upfront sits in **deferred revenue** ($16.3M → $1,577.5M YoY) with a **significant financing component** generating interest expense. A **separate Meta take-or-pay agreement** exists on the same terms.

4. **ClickHouse +$598.9M non-cash revaluation gain (ASC 321)** flatters FY2025 pre-tax income to +$13.8M (a CAM). Net income is not a clean read on operations.

5. **ARR is unaudited** ("last month × 12") — not in the 20-F, and flattering during a steep ramp.

6. **🚩 Auditor instability:** former PwC-Russia ("Technologies of Trust") for legacy ops → small Dutch firm **Reanda** (2 yrs, both adverse ICFR) → **Deloitte** appointed for FY2026 pending AGM.

7. **Prior going-concern doubt** existed through FY2023; *removed* in 2025 post-recapitalization. No current doubt.

8. **FPI (20-F) disclosure gaps vs a US 10-K filer:** no 10-Q (annual 20-F only, 4-month deadline; interims are voluntary **unaudited** 6-Ks); exempt from SEC proxy rules and **Section 16** insider reporting; Dutch governance in lieu of some Nasdaq rules; **no segment-asset disclosure** (CODM doesn't review segment assets). *But:* reports **U.S. GAAP**, so the IFRS-vs-GAAP gap previously anticipated does **not** apply.

---

## 5. COULD NOT VERIFY / OPEN ITEMS

- **GPU fleet counts (~20k → 35–60k):** not company-disclosed; Nebius reports MW. The 60k/35k figures are per-site capacity ceilings, not deployed fleet totals.
- **NVIDIA exact current share count/%:** the 1.2M common-share figure is from secondary 13F coverage; the 21.07M warrant shares are pre-exercise. A primary 13F was not parsed.
- **FY2026 capex final number:** primary letters defer to the call; call says **$20–25B**, but **$31–35B** appears in some June-2026 secondary snippets with a non-matching "$6.8B Q1" — needs the **Q2 2026 6-K** to confirm whether guidance was raised again.
- **Exact relisting share count (199.3M):** sourced via EDGAR search of the financial-statement exhibits; cross-check against the Sep-30-2024 6-K ex99-2 if precision to the share matters.
- **Q2/Q3 2025 individual quarterly capex split** (only 9-month $2,010.0M and Q1 $543.9M confirmed individually).

---

**Bottom line for the memo:** NBIS is a hyper-growth AI neocloud — revenue +479% in FY2025, ARR $90M→$1.9B in five quarters, core-segment EBITDA economics turning genuinely positive (~45% segment margin Q1'26), anchored by **contractual take-or-pay backlog** (Microsoft ~$17.4B + Meta). The bear-case risks are equally concrete and well-documented: **capex running 6–8× revenue**, **deeply negative FCF (~−$3.7B FY2025)** funded by ~$12.5B of dilutive financing (+27% basic dilution plus convert/warrant overhang), and **two consecutive adverse ICFR opinions with an open fixed-asset material weakness landing in the same year as a $167.6M earnings-boosting depreciation-life extension** — under an auditor (Reanda) being replaced by Deloitte. Diligence the depreciation change and the financing-component accounting on customer prepayments closely.

*Primary documents fetched directly from SEC EDGAR: FY2025 20-F (filed Apr 30 2026) and Q1 2026 6-K MD&A/financials (filed May 13 2026). Quarterly press releases and shareholder letters from Nebius IR cross-referenced.*
