# NBIS Refresh Note — as_of 2026-07-10

**Type**: LIGHT REFRESH of `../2026-06-18/` (re-price + fold-in; **not** a rebuild)
**pipeline_version**: lean-6module-v1.1 · **weights_version**: none · **run_date**: 2026-07-10 · **status**: DECISION_DRAFT

---

## Old → New (the verdict-flip check)

| | 2026-06-18 (prior) | **2026-07-10 (this refresh)** |
|---|---|---|
| Price (last close ≤ as_of) | $286.69 | **$219.65 (−23.4%)** |
| Market cap (basic) | ~$72.79B | ~$55.77B |
| EV (basic) | ~$71.9B | ~$54.92B |
| Off 52wk high | −4.0% (ATH region) | **−26.7% (mid-range)** |
| EV/RPO | 2.2× | **1.64×** |
| EV/ARR on YE26 exit $7–9B | 8–10× | **6.1–7.8×** |
| Base-case IRR to end-2028 | ~6–14%/yr | **+18 to +27%/yr (clears the ~12–15% hurdle)** |
| Bear / Bull IRR | ~−50%+ total / ~+95% total | **−17 to −22%/yr / +46 to +50%/yr** |
| Gap to buy-below $180 / $150 | −37% / −48% below | **−18% / −32% below** |
| M6 signal | −2 | **−1** |
| **new_money_verdict** | **WATCH (0%)** | **WATCH (0%) — "warming"** |
| **existing_position_verdict** | **HOLD** | **HOLD** (basis ~$190–195, +~50% → **+~13%**) |
| binding_constraint | PRICE (no MOS, priced for perfection) | PRICE (still above buy-below band; but "perfection" flag eased) |

**Does the ~23% drop flip the verdict toward STARTER? NO.** It moves the price **much closer** to the STARTER entry band and improves the skew, but does **not**: (a) reach the ~$150–180 buy-below band ($219.65 is still ~18–32% above it), nor (b) clear the ~70% completeness cap (active MW still withheld; Q2'26 6-K not out). New money = **WATCH, warming**; existing = **HOLD**.

## What moved

1. **Re-priced (freshness gate)**: $286.69 → **$219.65** (2026-07-10 close, last ≤ as_of).
   - Yahoo chart re-fetch **$219.65** + websearch historical **$219.65** (+1.60% on the day) → 2 independent sources, **0.0% delta**.
   - Path: peaked $276.17 (06-30) → dropped on 07-01 (Meta-cloud report) → $229.18 → troughed intraday ~$195.19 (07-07) → recovered to $219.65 (07-10). Net **−23.4%**.
   - 52wk band $49.00 / $299.86; price now **−26.7% off the high**, +348% off the low → `low_high_hug_justified=false`.
   - `verify_freshness.py` → **STATUS: PASS (exit 0)** (see `freshness_check.json`).

2. **M6 −2 → −1** (only leg that changed): multiples compressed, base IRR clears the hurdle, "priced for perfection" eased. Still negative because price is above the buy-below band and the buy-below is held (not loosened).

3. **Meta "sell excess compute" (~2026-07-01)** recorded as an **ELEVATED K-B SENTIMENT watch** (Bloomberg "people familiar"), **NOT a fundamental downgrade** — the $27B Meta contract is intact. It spotlights the pre-existing ~90% 2-customer concentration and a possible anchor-as-competitor dynamic.

4. **Capital-cycle lens (applied)**: neocloud rental = low-barrier, mid-late, **PEAK-lean** — Meta flooding surplus supply is a textbook top-signal. One-directional caution (compress, never lift). Micron Q3 FY2026 read-through (HBM sold out through 2026, HBM4 for NVIDIA Vera Rubin) confirms the durable bottleneck is **upstream (memory)**, not in NBIS's rental link.

## What did NOT change (carried forward)

- **All FILED financials** (FY2025 20-F / Q1'26 6-K): revenue, capex ~7.7×, FCF ≈ −$3.66B, RPO $33.585B, deferred rev, cash/debt, shares (253.9M basic / 308.97M diluted), contracts (MSFT $17.4→19.4B, Meta $2.88B + ~$27B), power (>3.5GW contracted, ~170MW active YE2025), accounting flags (4→5yr depreciation, adverse ICFR, ClickHouse mark), governance (Volozh super-voting control). **NBIS Q2 2026 6-K is not yet out → no new filed earnings.**
- **M1–M5 signals** (0 / +1 / 0 / −1 / −2), business_verdict **good**, existing **HOLD**, buy-below **~$150–180**, kill criteria (K-B elevated but not tripped).
- Business/moat/bottleneck/inversion maps and raw filings live in `../2026-06-18/`.

## Honesty label
**DECISION_DRAFT**, not COMPLETE. LIVE price passed the mechanical ≥2-source freshness gate (PASS). Blocking OPEN unchanged: **active MW withheld** (Q1'26 + Q2'26) — the conversion-proof metric; resolve at Q2'26 6-K (~late July/Aug). Also open: FY2026 capex actual, exact concentration %, Russia indemnities. The genuine two-sided tension (base IRR now clears the hurdle vs price still above buy-below) is documented in `runner_dissent` — the disciplined call holds WATCH.
