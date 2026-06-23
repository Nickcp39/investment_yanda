# Audit — CEG (completeness + verdict-ceiling)

Last updated: **2026-06-22** · Price **$277.64** · Status **DECISION_DRAFT**

Mirrors `companies/googl/audit.md` (verdict-ceiling rule) + the mega7 CHECKER A–F gate. This is the Runner's self-audit; the independent Checker re-runs it separately.

## 1. Completeness score: ~76/100 → ceiling = STARTER

| completeness | verdict ceiling |
|---|---|
| < 40% | INFO-GAP |
| 40–60% | WATCH |
| **60–80%** | **STARTER** ← CEG sits here (~76) |
| > 80% | CORE discussable |

**Why ~76 and not higher:** this is one live refresh pass on a seed (DECISION_DRAFT). The evidence base is strong and now partly primary-upgraded (10-Q leverage/shares), but four gaps cap it below CORE (§4).

**Why not lower (not WATCH):** the thesis gate PASSES on primary evidence (FERC defused, PTC survived, leverage de-risked, positive structural ROIC), and there is a real margin of safety (Street targets all above price; bear floored ~−20%). So the *price* does not force WATCH (unlike GOOGL, where no margin → WATCH).

## 2. A–F Gate

### A. Scope & Definition
- [x] ticker / share class / **as_of=2026-06-22** / decision purpose / horizon frozen (`step0_plan.md`).
- [x] Completion criteria written before the verdict (thesis gate, stop conditions).
- [x] Status label not stale (DECISION_DRAFT, dated 2026-06-22).

### B. Evidence (M1)
- [x] `source_register.md` covers every source used (name + date + link/path + tier).
- [x] `raw/` excerpts for the headline primary claims (10-Q, Q1 release, FERC, §45U).
- [x] `claim_ledger.csv` (30 rows) carries source tier + status + source_id + value/unit.
- [x] `facts.md` holds only verified or explicitly-flagged derived claims. **Secondary $100–115/MWh PPA estimates explicitly EXCLUDED as unconfirmed.**
- [x] No bare claims in the memo (each ties to a C-id or explicit OPEN).
- [x] Source tiering: primary > secondary; KOL/social never a fact, never supports BUY.

### C. 11-stage coverage
- [x] Stages 0–10 each ≥ P0 (Business / Financial Quality / Value Chain / Moat / Bottleneck / Operator / Inversion / Valuation all have artifacts).
- [x] Stage 8 IC Panel exists (`ic_panel.md`): 5 souls; quotes sourced or labeled as lens — **no fabricated quotes**.

### D. Model & Math (M4/M6)
- [x] Revenue/EPS driver model tied to evidence (FY26 guide midpoint $11.50; ~24x).
- [x] Owner-earnings read separated (positive/growing vs NBIS negative).
- [x] Implied expectations reverse-engineered from the **current price** ($277.64 = $11.50 × ~24.1x).
- [x] Three scenarios reconciled to sources/assumptions; arithmetic auditable (`model/scenario_model.csv`: 12.0×18=216, 13.0×25=325, 13.8×30=414).

### E. Open Questions
- [x] Each open question classified blocking / monitoring / non-blocking (§4).
- [x] Blocking items explicitly cap the verdict; non-blocking given a reason.

### F. Audit & Consistency
- [x] Internal audit for stale self-description; README/research_status reflect current state.
- [x] Number reconciliation: `as_of_price` ($277.64), market cap (~$100.3B), P/E (~24x), FCF yield (~1.2%) consistent across files (T5 single-value-of-truth PASS).
- [x] `decision_card.json` schema complete with version stamps (`lean-6module-v1` / `none` / `2026-06-22`).
- [x] Final answer reports the true status (DECISION_DRAFT), not a prettier one.

## 3. Freshness gate (MECHANICAL, hard门)
- [x] `python scripts/verify_freshness.py --dossier companies/ceg/2026-06-22` → **exit 0, status PASS**.
- [x] `freshness.json` manifest present; every LIVE field ≥2 independent sources.
- [x] Price via Yahoo chart API, cross-checked ≥2 sources (3 within 0.21%).
- [x] T1 band ✓ / T2 no-hug ✓ / T3 mcap-identity ✓ / T5 single-value ✓ / T6 guidance-fresh ✓ (T4 SKIP — no distance-claim regex match; not a failure).

## 4. The four gaps that cap below CORE (verdict-ceiling drivers)

| # | Gap | Class | Caps? |
|---|---|---|---|
| G1 | SEC 10-K (FY2025) headline + **combined-entity FCF** not second-confirmed (FY25 release IR links rotted; FCF still standalone) | blocking-for-CORE | Yes — needs a clean primary FCF before CORE |
| G2 | **No NEW premium-nuclear hyperscaler PPA** (CyrusOne is gas); Crane upside locked to MSFT at undisclosed price | blocking-for-CORE (the equity catalyst) | Yes — the binding economic constraint |
| G3 | Calpine deleverage to ~2.0x by 2027 is still partly a **forecast** (though ~2.25x + LS Power done is part-proven) | monitoring | Partial — de-risked vs seed; verify each 10-Q |
| G4 | Year-by-year **hedge ratios** undisclosed → near-term power-price sensitivity not precisely modelable | monitoring | No (haircut, not a cap) |

## 5. Verdict-ceiling verification

- Completeness ~76 → **ceiling STARTER**. Card verdict = STARTER. **Not exceeded.** ✓
- **Size vs durability:** merchant-power cyclicality + Calpine gas dilution → durability ceiling caps **below CORE** independent of completeness (METHODOLOGY: cyclicals capped below Core). Suggested size 2% initial / 5% max is consistent with STARTER on a quality-but-cyclical name. ✓
- **M6 price-cap test:** there IS a margin of safety (bear floored ~−20%; Street low $296 > price), so M6 does **not** cap below completeness. The ceiling is completeness (STARTER), not price. ✓

## 6. One-line audit read

A strong, partly-primary-upgraded DECISION_DRAFT: the thesis gate passes on primary evidence, the freshness gate passes mechanically, leverage is de-risked vs the seed, and the verdict (STARTER) is correctly capped by completeness — not inflated by the headline beats. CORE needs a clean combined FCF + a NEW premium PPA.
