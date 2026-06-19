# M1 Evidence Spine - INTC 2021-04-23

Material-collection round only. This file audits the evidence and lists open questions. It contains
NO buy/sell verdict, NO thesis, NO valuation conclusion, NO position size. The decision question is
recorded in `case_control.md` and is deliberately left unanswered.

## 0. Collection Status

- Evidence mix collected: 3 filings/releases (S001/S002/S003 release+8-K, S004 10-Q) + 1 transcript (S005)
  + 1 price (S013) + dated news (S006-S009, S012) + peer/industry (S010-S011). Meets the P1 minimum mix.
- Confidence in the as-of factual base: high for reported financials and strategy; medium for
  competitive-share magnitude (constrained to pre-as-of data only).
- Strict-blind status: this case is the deliberate contrast to a later Intel case; no post-2021-04-23
  knowledge is used.

## 1. Load-Bearing Facts

| claim_id | fact | source_id | confidence |
|---|---|---|---|
| C001 | Q1 2021 GAAP revenue was $19.673B, down 1% YoY; non-GAAP revenue $18.6B, flat. | S003, S004 | high |
| C002 | GAAP gross margin was 55.2% (vs 60.6% PY); non-GAAP 58.4% (vs 64.5% PY) — off prior-year highs. | S003, S004 | high |
| C003 | DCG revenue was $5.6B, down 20% YoY. | S003 | high |
| C004 | DCG operating income fell to $1,273M from $3,492M YoY (~23% op margin on ~$5.6B revenue). | S004 | high |
| C005 | DCG decline driven by cloud-service-provider digestion, enterprise/government weakness, and lower ASPs (higher SoC volume, weaker core mix). | S004, S005 | high |
| C006 | CCG revenue was $10.6B, up 8%; notebook volumes set a record (+54% YoY) but notebook ASP fell 23% YoY on consumer/education mix. | S003, S004 | high |
| C007 | FY2021 guidance: revenue $77.0B GAAP / $72.5B non-GAAP; non-GAAP EPS $4.60; gross margin 54.5% GAAP / 56.5% non-GAAP. | S003 | high |
| C008 | FY2021 capital-spending guidance was $19.0-20.0B; Q1 2021 capex was $3,972M. | S003, S004 | high |
| C009 | Intel paid $1.4B in dividends and repurchased $2.3B of stock in Q1 2021; management said it remained committed to growing the dividend with lower buybacks during an investment phase. | S003, S004, S005 | high |
| C010 | Balance sheet (Mar 27, 2021): total assets $150,622M; stockholders' equity $79,807M; total debt $35,884M; cash + ST investments $7,609M; 4,038M shares outstanding. | S004 | high |
| C011 | On 2021-03-23, CEO Gelsinger announced "IDM 2.0": internal fabs + expanded third-party foundry use (modular tiles from 2023) + new Intel Foundry Services. | S001, S002, S005, S006 | high |
| C012 | IDM 2.0 included a ~$20B investment for two new fabs at the Ocotillo (Arizona) campus. | S001, S002, S006 | high |
| C013 | Intel Foundry Services is a standalone unit led by Dr. Randhir Thakur, offering U.S./Europe capacity and x86, Arm, and RISC-V IP. | S001, S005 | high |
| C014 | Intel expected to tape in the 7nm "Meteor Lake" compute tile in Q2 2021 and described 7nm as "progressing well." | S001, S005 | high (as management statement) |
| C015 | In July 2020, Intel disclosed a ~6-month 7nm product slip (yield ~12 months behind target); 7nm CPUs then expected late 2022 / early 2023; outsourcing flagged as a contingency. | S007, S008, S009 | high |
| C016 | AMD launched 3rd Gen EPYC "Milan" (7003) server CPUs on 2021-03-15; AMD held ~7.1% server-CPU share vs Intel ~92.9% as of ~Q4 2020 (up from ~4.5% in Q4 2019). | S010, S011 | medium |
| C017 | INTC closed at $59.24 on 2021-04-23 (adj $53.88); prior close $62.57; volume 77.5M; ~$239B equity value. | S013, S004 | high |
| C018 | INTC's April 2021 price area was around its highest in roughly two decades (since the dot-com era). | S013 | medium |

## 2. Evidence vs Interpretation

### Evidence (what the sources state)

- Headline Q1 2021 revenue was roughly flat-to-down YoY; reported EPS beat the company's own January guide.
- Gross margin and DCG operating margin were materially below prior-year levels, with company-cited
  causes being 10nm ramp unit costs, 7nm start-up costs, factory start-up costs, and mix.
- The client/PC business was strong on volume but with falling notebook ASPs (consumer/education mix).
- The company announced a capital-intensive strategy (IDM 2.0 + foundry + ~$20B Arizona) with FY2021
  capex guided to $19-20B, and explicitly framed 2021 as an "investment phase."
- A process-node delay (7nm) was a documented pre-existing condition; the strategy positions 7nm/IDM 2.0
  as the remedy. These are management statements, recorded as such.
- Competitive pressure in servers from AMD EPYC was a documented pre-as-of trend (Milan launch 2021-03-15;
  AMD share rising through 2020).

### Interpretation guardrails (collector does NOT resolve these)

- Whether the low headline multiple reflects durable cash generation or peak/decaying earnings is the
  decision question and is NOT answered here.
- Whether IDM 2.0 capex is value-accretive investment or margin-destructive over-build is NOT answered here.
- Whether DCG margin compression is cyclical/transition-driven or structural-share-loss-driven is NOT
  answered here.

### Sentiment / Narrative only

- Management's "progressing well" / "restore process leadership" / ">50 foundry customers" statements are
  recorded as management framing (S005), not verified outcomes.
- Trade-press framing (S012) is context only.

## 3. Contradictions / Tensions (recorded, not resolved)

| issue | one side | other side | status |
|---|---|---|---|
| Headline vs profitability | Revenue beat company guide; PC volumes at records. | GAAP & non-GAAP gross margin down 5-6 points YoY; DCG op income roughly halved. | Both documented (S003/S004); not resolved. |
| Strategy vs near-term economics | IDM 2.0 / foundry positioned as leadership restoration. | $19-20B capex + "investment phase" + lower buybacks signal elevated near-term spending. | Both documented (S001/S005); not resolved. |
| Data-center demand | Company cited cloud-digestion as a timing effect and enterprise/government as macro-driven. | AMD EPYC share gains through 2020 + Milan launch are a documented competitive factor. | Both documented (S004/S005 vs S010/S011); not resolved. |
| Valuation optics | Optically low headline multiple near a ~20-year-high price. | Margin and DCG trends are deteriorating YoY. | Both documented; the trap/quality question is deferred. |

## 4. Open Questions (for the future blind Runner, not answered here)

- Is the depressed DCG operating margin primarily 10nm-transition unit cost (transient) or share/pricing erosion (structural)?
- Does the $19-20B 2021 capex (and IDM 2.0 trajectory) represent accretive reinvestment or value destruction?
- Is FY2021 EPS near a peak (rich PC cycle) or a trough (margin pressure), and what is normalized owner earnings?
- How much of the low multiple is durable free-cash-flow strength vs a market discount for execution/process risk?
- What single metric (DCG margin, server share, 7nm milestone, capex-to-FCF) would most force a market update?

## 5. Source-Quality Notes

- Primary (highest): S004 (10-Q), S003 (earnings release / 8-K), S001/S002 (IDM 2.0 release + 8-K), S013 (price series).
- Management commentary: S005 (transcript) — reliable for what management said; framing not treated as fact.
- Secondary/dated news: S006-S009, S012 — used for dated context and corroboration.
- Peer/industry: S010-S011 — competition context, constrained to pre-as-of data.
- Deliberately excluded as post-as-of: Mercury Research Q1 2021 CPU-share report (published ~2021-05-09).

## 6. Handoff Note

This pack provides the as-of factual base and the open questions. No module verdict, context label, or
position size is assigned in this round. The blind Runner will produce those later from these materials.
