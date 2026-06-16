# GOOGL Monitor v2

Last updated: 2026-06-16

Status: `P0_PASS_1 monitoring draft, not final research completion`

Decision state: `WATCH / 0% position`

Purpose: Layer 10 monitoring for the Google v2 rerun. This file turns the
inversion paths in `inversion_risk_v2.md` into observable quarterly metrics,
event triggers, and action rules.

Core monitor question:

> Is Alphabet still converting commercial intent and AI infrastructure into
> owner earnings per share, or are Search economics, capex, Cloud margins,
> regulation, dilution, and valuation moving against us?

---

## 1. Update Rules

Cadence:

- Quarterly: update after each earnings release, 10-Q/10-K, and earnings call.
- Event-driven: update immediately after DOJ, court, EC, DMA, or material
  financing/capex filings.
- Before any investment action: refresh price, market cap, share count, net
  cash/debt, financing dilution, and the implied-expectations model.

Data discipline:

- Use filed numbers first: 10-Q, 10-K, 8-K, Exhibit 99.1, prospectus, and court
  or regulator documents.
- Treat management call commentary as useful but not sufficient for closing a
  risk path unless paired with numeric evidence.
- Do not treat non-operating equity gains as owner earnings.
- Do not upgrade from `WATCH` only because revenue grows. The required proof is
  FCF/share and owner-earnings conversion after AI capex, SBC, and dilution.

Status labels:

- Green: risk is not currently damaging the thesis.
- Yellow: risk is live or evidence is incomplete; stay `WATCH`.
- Red: kill criterion triggered; rerun thesis and valuation before any buy
  discussion.

---

## 2. Quarterly Metrics Dashboard

Fill the future quarter columns after each filing. Q1'26 is the current baseline
from the P0 pass.

| Metric | Formula / unit | Q1'26 baseline | Q2'26 | Q3'26 | Q4'26 | Green | Yellow | Red / kill | Primary source |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Search & other growth | YoY revenue growth | +19.1% | TBD | TBD | TBD | >=10% | 8% to 10%, or one quarter below 8% with macro explanation | <=8% for 2 quarters without macro-only explanation | 10-Q / Exhibit 99.1 |
| Paid clicks | YoY growth | +13% | TBD | TBD | TBD | >5% | 0% to 5%, or sharp deceleration | Negative for 2 quarters, especially if AI usage is rising | 10-Q MD&A |
| CPC | YoY growth | +5% | TBD | TBD | TBD | Positive and broadly consistent with advertiser ROI | Flat to slightly negative | Negative for 2 quarters while paid clicks stay positive | 10-Q MD&A |
| TAC rate | TAC / Google advertising revenue | 19.7% | TBD | TBD | TBD | <=21% and stable/down | >21% or +100 bps YoY | +300 bps YoY, or remedy/default changes clearly lift TAC | 10-Q / derived |
| Google Network growth | YoY revenue growth | -3.9% | TBD | TBD | TBD | Weakness isolated to Network | Network decline worsens but Search/YouTube hold | Network weakness spreads to Search/YouTube owned surfaces | 10-Q / Exhibit 99.1 |
| Cloud revenue growth | YoY revenue growth | +63.4% | TBD | TBD | TBD | >30% with margin discipline | 20% to 30%, or high growth with falling margin | <20%, or growth bought with margin collapse | 10-Q / Exhibit 99.1 |
| Cloud operating margin | Cloud OI / Cloud revenue | 32.9% | TBD | TBD | TBD | >=30% | 25% to 30%, or -500 bps QoQ/YoY | <20% for 2 quarters, or Cloud OI flat/down YoY | 10-Q / derived |
| Cloud backlog / RPO conversion | Backlog and expected conversion timing | $462B backlog; just over 50% expected within 24 months | TBD | TBD | TBD | Conversion tracking to >=50% within 24 months with stable margin | Backlog grows but conversion/margin unclear | Materially below 50% 24-month conversion, or low-margin TPU hardware dominates | 10-Q / call |
| Capex / OCF | Purchases of PPE / OCF | 77.9% | TBD | TBD | TBD | <60% | 60% to 70%, or single-quarter >70% with clear ROI evidence | >70% for full year without ROI evidence, or >90% quarter with no explanation | Cash flow statement / derived |
| FCF/share | (OCF - capex) / diluted or average shares | Q1 $0.83; TTM about $5.32 | TBD | TBD | TBD | TTM FCF/share grows YoY | Flat/down for 1 year | Down for 2 years while capex remains elevated | Exhibit 99.1 / derived |
| Share count | Class A/B/C outstanding and diluted shares | Outstanding 12.116B; diluted 12.238B | TBD | TBD | TBD | Stable/down after SBC | Up <1% annualized | Up >1% in a year or >2% over 2 years while FCF/share flat/down | Balance sheet / EPS table |
| SBC | SBC expense and SBC/revenue | Cash-flow SBC $6.751B; 10-Q total SBC $7.2B | TBD | TBD | TBD | SBC/revenue stable/down and buybacks offset dilution | SBC grows near revenue or buybacks only offset SBC | SBC grows faster than revenue and share count rises | Cash flow statement / SBC note |
| Buyback / debt / equity issuance | Repurchases, debt proceeds, equity/preferred/ATM | Buybacks $0; debt proceeds $31.379B; $80B equity plan announced | TBD | TBD | TBD | Buybacks resume and offset SBC; no recurring equity issuance | Buybacks paused or debt rises while capex rises | Recurring equity/preferred/debt funding for AI capex without ROI proof | 10-Q / 424B5 / FWP |
| DOJ / EU events | Remedy status and economic effect | Search remedies ordered; DOJ adtech remedy risk live; EC DMA/fines live | TBD | TBD | TBD | Fines or narrow behavioral remedies only | Data sharing, default limits, remedy uncertainty | Structural divestiture, default distribution impairment, or TAC/share damage | DOJ / court / EC |

Current dashboard read:

- Green: Search & other growth, paid clicks, CPC, Cloud revenue, Cloud margin.
- Yellow: TAC/regulatory interface, Network weakness, Cloud backlog quality,
  capex/OCF, FCF/share, SBC, share count, buyback/debt/equity issuance, DOJ/EU.
- Red: valuation remains red under current-like price and draft owner-earnings
  branches. This monitor does not open a position while valuation is red.

---

## 3. Risk Path To Metric Map

| Inversion path | Primary metrics | Secondary checks | Current status |
|---|---|---|---|
| AI answer / agent disintermediation | Search & other growth, paid clicks, CPC | Search share proxies, merchant attribution, Gemini/AI Mode usage, UCP adoption | Green/yellow: revenue strong, but AI interface risk unresolved |
| Search RPM risk | CPC, paid clicks, Services margin, AI RPM proxy | Ad load, advertiser ROAS, other cost of revenues | Yellow: AI RPM not disclosed |
| Capex black hole | Capex/OCF, FCF/share, assets not yet in service, purchase commitments | D&A, energy cost, debt/equity issuance, buybacks | Yellow/red watch: Q1 capex/OCF 77.9% |
| Cloud margin deterioration | Cloud revenue, Cloud OI margin, backlog conversion | TPU hardware timing, Wiz margin headwind, utilization | Green/yellow: Q1 margin strong, durability unproven |
| Regulatory structural remedy | DOJ/EU event log, TAC rate, Search share proxies | Contract changes, data sharing, adtech remedies | Yellow: search remedies ordered; adtech structural risk live |
| Ad budget migration | Search CPC by vertical if available, Google advertising growth, Network growth | YouTube DR, retail/finance commentary, merchant platform adoption | Yellow: Network down, Search still strong |
| Talent / product execution | Gemini/AI Mode usage if disclosed, Cloud AI growth, product adoption | SBC/revenue, key departures, model quality, incidents | Yellow: strong claims, limited public metrics |
| Governance / control risk | Share count, buybacks, debt/equity issuance, ROI disclosure | compensation metrics, capex escalation, acquisition/backstop commitments | Yellow: control structure plus financing/capex opacity |
| Valuation risk | Price/OE, OE yield, required OE CAGR, FCF/share | dilution, buyback pause, terminal multiple | Red: current-like price requires successful capex conversion |

---

## 4. Kill Criteria Rollup

| Kill ID | Trigger | Why it matters | Action |
|---|---|---|---|
| K1 Search crack | Search & other <=8% YoY for 2 quarters without macro-only explanation | Core commercial-intent moat is weakening | Move to `REJECT / AVOID` unless AI RPM and FCF/share evidence offsets |
| K2 AI RPM crack | AI Search RPM 20%+ below traditional Search RPM for 4 quarters, or CPC negative for 2 quarters while paid clicks positive | Query growth is not translating into economics | Rebuild Search unit model with lower RPM and lower terminal multiple |
| K3 Capex black hole | Full-year capex/OCF >70% for 2 years without ROI evidence, or FCF/share down for 2 years | Owner earnings are being consumed by infrastructure | Use defensive owner-earnings branch; no buy until FCF/share turns |
| K4 Cloud margin crack | Cloud OI margin <20% for 2 quarters, or OI flat/down despite revenue growth | Cloud is not a high-return second engine | Lower Cloud multiple and capex return assumptions |
| K5 Structural remedy | Divestiture, forced adtech separation, default distribution impairment, or mandated data access with measurable share/TAC damage | Moat mechanics are legally impaired | Rerun moat, value chain, and valuation before any action |
| K6 Ad budget migration | Google advertising growth <5% for 4 quarters while digital ad market is positive | Advertiser ROI is migrating away | Rebuild ad growth and terminal margin assumptions |
| K7 Product/talent miss | Two major AI product cycles behind peers, or Gemini/AI Mode usage declines for 2 quarters after launch | Distribution alone is not enough | Downgrade operator/product execution score |
| K8 Governance dilution | Net share count up >2% over 2 years while FCF/share flat/down | Capital allocation harms minority owners | Apply governance discount and dilution branch |
| K9 Valuation no MOS | Price implies <8% 10-year IRR under conservative owner-earnings branches | Good company can still be bad investment | Maintain `WATCH / 0%`; update buy-below only after model rebuild |

---

## 5. Event Dashboard

| Event | Latest status as of 2026-06-16 | Green | Yellow | Red / kill | Source |
|---|---|---|---|---|---|
| DOJ Search case | Remedies ordered in Sep 2025: limits on exclusive contracts, certain data access, and syndication obligations | Remedies absorbed with stable share/TAC | Data sharing/default limits create uncertainty | Remedies cause Search share loss, TAC +300 bps, or forced asset separation | DOJ search remedies release |
| DOJ adtech case | DOJ prevailed in 2025; Alphabet 10-K says DOJ proposal includes structural remedies that could harm business | Fines or narrow conduct remedy | Remedy pending or behavioral separation | Ad Manager / AdX / publisher ad server divestiture or structural separation | DOJ adtech release; FY2025 10-K |
| EU DMA Search / Play | EC preliminary findings say Google Search may favor own services and Play may restrict steering | No breach or narrow compliance change | Binding compliance changes under review | Changes materially reduce Search traffic, Play economics, or data advantage | EC DMA preliminary findings |
| EU adtech fine/remedy | EC press release reports EUR 2.95B fine over adtech practices; Alphabet has accrued EC-related fines | Fine only, no structural impact | Conduct remedies and appeals ongoing | EU requires structural adtech separation or conflicts cannot be cured behaviorally | EC press release; SEC filings |
| Financing / equity issuance | June 2026 filings describe $80B equity plan, $40B ATM, $10B Berkshire private placement, preferred/common offerings | One-off financing, no net dilution after buybacks resume | ATM/preferred/common issuance proceeds but ROI still unclear | Recurring equity/preferred issuance for capex while share count and FCF/share deteriorate | FWP / 424B5 |
| Capex guide | 2026 capex guide $180B to $190B; 2027 significantly higher | Guide peaks and normalizes | Guide rises but ROI evidence improves | Guide rises again with no utilization/payback disclosure | 424B5 / earnings calls |

---

## 6. Upgrade Conditions

Move from `WATCH` to `STARTER` only if multiple conditions are true at the same
time:

- Search & other remains double-digit growth while AI answer/agent penetration
  rises.
- Paid clicks and CPC remain positive, or AI Search RPM is disclosed as
  comparable to traditional Search.
- Cloud operating margin stays near or above 30% across several quarters after
  higher depreciation begins.
- Backlog conversion tracks management's 24-month expectation without margin
  deterioration.
- Capex/OCF peaks and begins moving below 60% to 70%.
- TTM FCF/share turns up.
- Share count is stable or declining after SBC and financing.
- Management provides a credible capex ROI framework: utilization, payback,
  incremental ROIC, depreciation life, and capacity allocation.
- Price offers margin of safety under defensive or mixed owner-earnings branches.

---

## 7. Downgrade Conditions

Move from `WATCH` to `REJECT / AVOID` if:

- Any red kill criterion in Section 4 triggers and is not quickly disproven.
- Search growth cracks while capex remains elevated.
- Cloud margin proves temporary and backlog conversion is low quality.
- AI capex is repeatedly raised without return evidence.
- Buybacks stay paused, share count rises, and SBC remains large.
- Regulatory remedies become structural or cause measurable Search/adtech
  economics damage.
- The stock price still requires the growth branch after the defensive and mixed
  branches deteriorate.

---

## 8. Quarterly Update Template

Use this template after each quarterly filing:

| Date | Filing / event | Metrics updated | Status changes | View change | Required follow-up |
|---|---|---|---|---|---|
| 2026-06-16 | Q1'26 P0 pass | Baseline dashboard created | WATCH maintained | Search and Cloud strong; capex/FCF/share and valuation remain blockers | Close AI RPM, capex split, Cloud backlog margin, ROI framework |
| TBD | Q2'26 earnings | TBD | TBD | TBD | TBD |
| TBD | Q3'26 earnings | TBD | TBD | TBD | TBD |
| TBD | Q4'26 / FY2026 | TBD | TBD | TBD | TBD |

---

## 9. Still-Unresolved Blockers

- AI Overviews / AI Mode RPM versus traditional Search RPM.
- Maintenance capex versus growth capex.
- Cloud backlog margin, cancellation terms, customer mix, and realized
  conversion economics.
- Numeric AI capex hurdle rate, utilization target, payback period, and
  incremental ROIC.
- Financing dilution from preferred/common/ATM/private placement after final
  issuance terms and share count.
- Refreshed buy-below table after owner-earnings model rebuild.

---

## 10. Source Anchors

- Alphabet Q1 2026 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000048/goog-20260331.htm
- Alphabet Q1 2026 earnings release, Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000043/googexhibit991q12026.htm
- Alphabet FY2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Alphabet Q1 2026 official earnings call transcript: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
- Alphabet June 2026 FWP: https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/d160205dfwp.htm
- Alphabet June 2026 424B5 supplement: https://www.sec.gov/Archives/edgar/data/1652044/000119312526257690/d159942d424b5.htm
- DOJ search remedies press release: https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google
- DOJ adtech monopolization press release: https://www.justice.gov/opa/pr/department-justice-prevails-landmark-antitrust-case-against-google
- European Commission DMA preliminary findings on Alphabet: https://digital-markets-act.ec.europa.eu/commission-sends-preliminary-findings-alphabet-under-digital-markets-act-2025-03-19_en
- European Commission adtech fine press release: https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1992
- Local models: `companies/googl/model/search_unit_economics_v2.csv`, `companies/googl/model/capex_bridge_v2.csv`, `companies/googl/model/cloud_quality_v2.csv`, `companies/googl/model/owner_earnings_v2.csv`, `companies/googl/model/implied_expectations_v2.csv`
