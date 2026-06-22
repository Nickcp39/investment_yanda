# Monitor — NBIS

Last updated: 2026-06-18

Derived from `inversion_map.md` kill criteria + `bottleneck_map.md`. This is the live dashboard for the existing position (hold/trim/add triggers).

## Thesis Variables

| Variable | Why it matters | Source | Freq | 🟢 Green | 🟡 Yellow | 🔴 Red |
|---|---|---|---|---|---|---|
| **Active / connected power (MW)** | THE conversion metric; revenue is gated by live MW (bottleneck) | 6-K letter | Q | on/ahead of 800MW–1GW YE26 connected | flat QoQ / vague disclosure | declines or keeps being withheld + ARR slows |
| **MSFT/Meta tranche delivery** | delivery slip → clawback/LDs (path A/B) | 6-K, PR | Q | "delivered all commitments" | one tranche renegotiated | missed tranche / anchor cuts capex |
| **Customer concentration / breadth** | demand breadth vs 2-whale risk | 6-K, press | Q | named 3rd large anchor / self-serve % rising | flat | concentration confirmed >60% + take-back |
| **Deferred revenue growth (prepayments)** | funding flips to dilution if it stalls (path D) | balance sheet | Q | grows w/ backlog | flattens | falls while ATM/equity activated |
| **Capex / revenue & FCF** | capital-treadmill risk | 6-K | Q | ratio falling toward 2–3× | flat ~7× | rises / capex confirmed $31–35B w/o conversion |
| **Realized price per GPU-hour / rev per MW** | commoditization (path C/E) | calls, peers | Q | stable/up through GB300/Rubin | mild decline | sequential declines like Hopper −28% |
| **Depreciation policy** | earnings flattery / impairment (path C) | 20-F | A | 5yr holds, clean | — | 2nd life extension or GPU impairment |
| **ICFR / auditor** | accounting quality | 20-F | A | clean opinion (Deloitte FY26) | one weakness remains | new material weakness |
| **Valuation (EV/fwd-sales vs growth)** | priced-for-perfection risk | market | ongoing | de-rate toward base | at perfection (~now) | parabolic / new raise at low price |
| **Dilution (share count)** | per-share erosion | 6-K | Q | minimal | ATM tapped modestly | large equity raise |

## Event Calendar

| Event | Expected date | What to check | Action rule |
|---|---|---|---|
| **Q2 2026 6-K** | ~Aug 2026 | active MW (finally?), capex actual ($20–25B vs $31–35B — resolve C033), deferred-rev trend, MSFT/Meta tranches | if 2+ reds → trim |
| Nasdaq-100 inclusion | 2026-06-22 | passive-flow squeeze (technical, not thesis) | don't chase; consider trimming into strength |
| Q3 2026 6-K | ~Nov 2026 | connected-power progress vs 800MW–1GW YE26 | gate the YE26 conversion thesis |
| FY2026 20-F | ~Apr 2027 | ICFR (Deloitte), depreciation, contingencies, concentration | clears or confirms accounting flags |

## Open items to resolve (from claim_ledger)

- [ ] **C014 vs C015** — MSFT take-or-pay vs terminable: read 6-K ex-99.1 + 20-F rev-rec note. Highest-priority unknown for churn risk.
- [ ] Russia-divestiture indemnities / contingencies (C037).
- [ ] FY2026 capex actual (C032/C033).

## Change-My-Mind Log

| Date | New evidence | Prior view | Updated view | Action |
|---|---|---|---|---|
| 2026-06-18 | New-pipeline rerun on primary data | old brief "Watch" (single video source) | Strong competitive position, but priced for perfection; power not the bottleneck (build-and-energize is) | Hold; see memo-v1 |
