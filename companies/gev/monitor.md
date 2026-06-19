# Monitor — GEV

Last updated: 2026-06-19

Derived from `inversion_map.md` kill criteria + `bottleneck_map.md`. This is the live dashboard. **No position at $1,109.73** — the triggers below govern when to START / UPGRADE / stay-out.

## Thesis Variables

| Variable | Why it matters | Source | Freq | 🟢 Green | 🟡 Yellow | 🔴 Red |
|---|---|---|---|---|---|---|
| **Price vs ~$950** | STARTER entry (~25x normalized — pays for cyclical risk) | market | ongoing | <~$950 → **STARTER trigger** | $950–1,150 (no add) | parabolic / new high (overpay) |
| **Reservation→firm conversion (2029–30 slots)** | durability test — durable rent vs booking peak | call, 10-Q | Q | 2029–30 reservations convert to firm at premium → **UPGRADE** | flat / vague | reservations cancel / pricing softens (kill a) |
| **2026 equipment pricing** | the cyclical premium (+10–20%) | call | Q | holds / rises | guide trims | rolls over (kill a) |
| **Wind FY EBITDA loss** | kill (b) — mildly triggered | call, 10-Q | Q | narrows toward break-even | ~$400M (at guide) | **> ~$400M / widening** → escalate (kill b) |
| **Hyperscaler 2027 capex guidance** | SHARED SWITCH — primary thesis-killer for equipment premium | hyperscaler earnings | Q | flat-to-up | flattening | **2027 decel** (kill d) → DOWNGRADE |
| **Segment ROIC as 24 GW/yr lands** | kill (c) — capex sink | 10-K/10-Q | A | holds as capacity lands 2027–28 | dips | compresses (kill c) |
| **Services RPO / attach** | the durable annuity | 10-Q | Q | grows w/ installed base | flat | attach/margin erodes |
| **Clean fwd-EBITDA multiple vs Siemens** | priced-for-permanence risk | market | ongoing | de-rates toward base (~30x) | premium persists (~now) | re-rates higher on cyclical peak |

## Event Calendar

| Event | Expected date | What to check | Action rule |
|---|---|---|---|
| **Q2 2026 earnings/call** | ~Jul 2026 | end-of-Q2 GW under contract (target ≥110 by YE26), 2029–30 reservation→firm, Wind loss run-rate, 2026 pricing | 2029–30 firm conversion → consider STARTER even >$950; Wind > ~$400M run-rate → note kill (b) escalation |
| Hyperscaler Q2/Q3 capex prints | ~Jul–Oct 2026 | 2027 capex *slope* (AMZN/GOOGL/MSFT/META) | any clear 2027 decel → DOWNGRADE bias (kill d) |
| **YE2026 update** | ~Dec 2026 | sold-out-through-2030 status; ≥110 GW under contract; dividend/buyback | sold-out-through-2030 confirmed → durability UPGRADE |
| Q3/Q4 2026 + FY2026 10-K | ~Oct 2026 / Feb 2027 | segment ROIC as capacity adds begin; normalized FCF (advance-payment strip) | ROIC dip as 24 GW/yr lands → kill (c) watch |

## Decision rules (summary)

- **START (STARTER):** price <~$950 **OR** 2029–30 slots convert reservations → firm orders at premium (durability proven).
- **UPGRADE:** sold-out-through-2030 confirmed + reservations converting → durable rent established.
- **STAY OUT / DOWNGRADE bias:** at $1,109 (priced for permanence); escalate if hyperscaler 2027 capex decelerates (kill d) or Wind FY loss > ~$400M (kill b).

## Open items to resolve (from claim_ledger)

- [ ] **Reservation-fee / cancellation terms** (governs kill a / durability) — undisclosed; pull from 10-Q notes or future disclosure.
- [ ] **GEV-specific heavy-duty GT share** vs Siemens/Mitsubishi split (C013, MED) — pin from industry data.
- [ ] **Clean normalized-FCF bridge** stripping advance-payment timing (C007) — needed to tighten EV/FCF.

## Change-My-Mind Log

| Date | New evidence | Prior view | Updated view | Action |
|---|---|---|---|---|
| 2026-06-19 | Initiation on primary data (10-K/10-Q/call/investor update) | (none — fresh case) | Excellent business (oligopoly + services annuity), but ~46–51x clean fwd-EBITDA prices the cyclical equipment premium as permanent; Wind kill mildly triggered | **WATCH** — STARTER sub-$950; see `memo-v1.md` |
