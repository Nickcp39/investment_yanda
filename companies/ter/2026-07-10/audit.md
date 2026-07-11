# TER Audit — as_of 2026-07-10

## Completeness scoring
| Block | Weight | Done | Score |
|---|---:|---|---:|
| Evidence spine (M1): anchor Q + FY, price 2-source | 20 | ✅ strong primary | 18 |
| Theme/mechanism (M2) | 10 | ✅ | 10 |
| Profit pool / durability (M3): moat + segment | 15 | 🟡 segment op-income OPEN | 9 |
| Financial reality (M4): multi-year + owner earnings | 20 | 🟡 10-K/10-Q line items OPEN | 12 |
| Inversion / trap (M5) | 10 | ✅ | 9 |
| Price / position / monitor (M6) | 15 | ✅ scenarios + bands | 13 |
| Operator (proxy) | 10 | 🔴 proxy OPEN | 3 |
| **Total** | 100 | | **~58** |

**Completeness ≈ 58% → band 40–60 → verdict ceiling = WATCH.** (Consistent with price + capital-cycle also pointing to WATCH; the ceiling is not the sole binding factor but it confirms it.)

## Verdict-ceiling rule check
- `<40 INFO-GAP / 40–60 WATCH / 60–80 STARTER / >80 CORE`. At ~58%, **max verdict = WATCH.** Even if price were attractive, we could not stamp STARTER without closing 10-K/proxy gaps. Here price/cycle independently agree → WATCH is robust, not a completeness artifact.

## Internal consistency
- **as_of_price $359.60** identical across decision_card.json/.md, facts.md, valuation.md, model/scenario_model.csv → **T5 PASS** (freshness gate).
- Market cap $56.29B = 156.54M × $359.60 → T3 PASS.
- 52wk band containment + low/high hug + distance-from-high → T1/T2/T4 PASS.
- Freshness gate **STATUS: PASS (exit 0)**; T6 WARNs (guidance/litigation 72–73d old) expected — Q1'26 is the latest disclosure (Q2 prints post-as_of). Documented, non-blocking.

## Stale-claim check
- No stale files; all as_of 2026-07-10. Robotics FY2025 (~$308M) explicitly marked **derived (O4)**, not primary. Multi-year revenue tagged to SEC history (S009). Q1'25 robotics loss / breakeven from B1 (S005), flagged tier.

## Language check
- "DECISION_DRAFT", "WATCH", "draft", "one-pass" used throughout. **No "complete / 完整完成" claim.** Compliant with `research_completion_checker.md`.

## Residual risks to the audit
- Segment op-income (O2) is the biggest open item — it would sharpen the robotics-drag and ATE-profitability picture but is very unlikely to flip WATCH.
- Advantest share trend (O5) is the only item that could, over time, change the *structural* thesis (veto path).
