# NBIS Research Run — Layer 9: Market Data & Valuation Inputs

- Run date: 2026-06-18
- Method: general-purpose research subagent; primary SEC filings (Q1'26 6-K, FY2025 20-F, NVIDIA 13F, Situational Awareness 13G) + secondary aggregators (stockanalysis.com, MarketBeat, Benzinga) cross-checked across 3+ sources. SEC.gov direct fetch 403'd; figures cross-confirmed via filing-text indexes + Business Wire/EQS mirrors.
- Status: ⚠️ **UNAUDITED RESEARCH DIGEST.** Prices are intraday/volatile — NBIS was at fresh all-time highs on the research date ahead of Nasdaq-100 inclusion (eff. 6/22/26). Every price/multiple is date-stamped but "current" is good to within hours, not days. Promote through `claim_ledger.csv` before use.
- Subagent id (may expire across sessions): a715b781342c0b802
- Subagent tokens: 62,847 | tool_uses: 8

---

# Nebius Group (NASDAQ: NBIS) — Market Data & Valuation Inputs
**As of 2026-06-18** · Buy-side data pack

> **Volatility warning:** NBIS was making fresh all-time highs *on the research date* (6/18/26) ahead of its Nasdaq-100 inclusion effective 6/22/26. Intraday swings are large (6/18 day range $290.34–$298.61). Source provenance flagged **[PRIMARY]** (SEC/IR) or **[SECONDARY]** (aggregator/news, cross-checked 3+ sources).

## SNAPSHOT TABLE — all as of 2026-06-18 (unless noted)

| Metric | Value | Basis / Note | Source |
|---|---|---|---|
| **Share price** | **~$287.73 intraday** (prev close $280.91, 6/17) | Day range $290–$299; all-time high $298.61 set 6/18 | [SEC] stockanalysis.com |
| **52-week range** | **$43.89 – $298.61** | Low = Apr 2025 tariff selloff; high = 6/18/26 | [SEC] stockanalysis/Yahoo |
| **Shares out (basic)** | **253,898,194** | 3/31/26 (220.4M Cl A + 33.5M Cl B); aggregators ~256M (ongoing ATM) | **[PRIMARY]** SEC 6-K |
| **Shares out (diluted, wtd-avg)** | **308,971,701** | Q1'26 EPS basis; ~22% above basic (converts/warrants/RSUs) | **[PRIMARY]** SEC 6-K |
| **Market cap** | **~$73B basic / ~$89B diluted** | At $287.73 | [SEC] / derived |
| **Cash & equivalents** | **$9,298.2M** | 3/31/26 (no separate ST-investments line) | **[PRIMARY]** SEC 6-K |
| **Total debt (carrying)** | **$8,450.4M** | All convertible notes; accretes to **$10,041.8M** at maturity | **[PRIMARY]** SEC 6-K |
| **Net cash** | **~+$0.85B (carrying)** / **~−$0.7B (at accreted maturity)** | $2B NVIDIA warrants are equity, NOT debt | **[PRIMARY]** SEC 6-K |
| **Enterprise value** | **~$72.5B (basic) / ~$88.5B (diluted)** | EV ≈ market cap since ~net-cash-neutral | derived |
| **EV/Rev FY25 (actual)** | **~136x** ($72.5B / $529.8M) | TTM-basis (~$0.88B) ≈ 82x | derived |
| **EV/Rev FY26E** | **~21x** ($72.5B / $3.44B consensus) | — | derived |
| **EV/ARR (current $1.92B)** | **~38x** | ARR as of 3/31/26 | derived |
| **EV/ARR (FY26 exit $7–9B)** | **~8–10x** | On management's year-end guide | derived |
| **EV/EBITDA** | **n/m** | FY25 adj. EBITDA −$65M (Q1'26 turned +$129.5M) | **[PRIMARY]** |
| **Short interest** | **~17.5% of float** (44.3M sh, 2.6 days) | Settlement 5/29/26, declining | [SEC] Nasdaq/MarketBeat |

---

## 1. PRICE HISTORY MILESTONES

Reconciled path (all **[SECONDARY]** aggregators except where noted):

| Date | Level | Note |
|---|---|---|
| Dec 2024 | ~$28 | Post-relisting baseline |
| **Apr 2025** | **~$43.89** (52-wk low) | Market/tariff selloff trough |
| Sep 2025 | ~$92.50 → ~$114 | Secondary offering priced $92.50; ~$114 area |
| **Oct 2025** | **~$141 (2025 peak)** | AI-contract momentum; 2025 ATH |
| Nov 2025 | ~$130 | Meta 5-yr / $3B deal announced |
| Dec 2025 | ~$93–98 | ~30% pullback off Oct peak; MSFT deal news |
| ~Jan 2026 | ~$86–87 | YTD-2026 start (implied from +236% YTD) |
| **Jun 17–18, 2026** | **~$281–299 (all-time high)** | Nasdaq-100 inclusion (eff. 6/22/26) catalyst |

**Net:** ~$28 → trough ~$44 → ~$92–114 → 2025 peak ~$141 → pullback ~$93 → ~$86 → **current ATH ~$288–299.** Performance: **YTD-2026 ~+236%**, 1-yr ~+333%, FY2025 ~+248%.
*Caveat:* one source (ts2.tech) cited an $18.31 low and a separate ~40% "DeepSeek" plunge — that was the **Jan 2025** event (Yandex/relisting era), not the relevant 52-wk trough. Treat **$43.89** as authoritative.

> NOTE FOR THE FILE: user bought "a few weeks ago" (≈ May 2026) and is +50% as of 2026-06-18. That implies an entry around ~$190–195. Confirm with user; relevant for the hold/trim cost-basis frame.

---

## 2. VALUATION MULTIPLES & PEER COMPARISON

**NBIS (EV ≈ $72.5B basic):**
| Multiple | Value |
|---|---|
| EV/Revenue, FY25 actual ($529.8M) | **~136x** |
| EV/Revenue, TTM (~$0.88B) | **~82x** |
| EV/Revenue, FY26E ($3.44B) | **~21x** |
| EV/Revenue, FY27E ($11.2B, high dispersion) | **~6.4x** |
| EV/ARR, current ($1.92B) | **~38x** |
| EV/ARR, FY26 exit ($7–9B) | **~8–10x** |
| P/S, trailing | **~140x** |
| EV/EBITDA | n/m (EBITDA only just positive in Q1'26) |

**Peer set (all 6/18/26, [SECONDARY] stockanalysis.com):**

| Company | Price | Mkt cap | EV | Net debt | EV/Sales TTM | EV/Sales FWD |
|---|---|---|---|---|---|---|
| **NBIS** | $289 | $74B | **$72B** | **−$0.2B (net cash)** | **~82x** | **~13–21x** |
| **CoreWeave (CRWV)** | $118 | $64B | **~$95.7B** (incl. leases) | **+$32.9B** | **15.4x** | **~7.7x** |
| IREN | $59.50 | $21B | $22.5B | +$1.8B | 29.7x | 10.1x |
| Applied Digital (APLD) | $46.71 | $13B | $14.1B | +$1.1B | 44.2x | 22.8x |
| Astera Labs (ALAB) | $390 | $67B | $63B | −$1.1B | 63.0x | 36.8x |
| Oracle (ORCL) | — | $652B | $652B | +$124B | 9.7x | 5.9x |
| Hyperscalers (MSFT/GOOGL) | — | — | — | — | ~9–10x | ~8x |

**Key takeaways:**
- **NBIS vs CRWV is a balance-sheet story.** Both ~$64–74B equity, but CRWV carries **~$33B net debt** (EV ~$96B incl. ~$10B finance leases) while NBIS is **net cash** (EV ≈ market cap). NBIS's trailing EV/Sales (82x) dwarfs CRWV's (15.4x) purely because CRWV is ~12 months ahead on the revenue curve (FY25: $5.13B vs $0.53B).
- **On a forward basis the gap compresses dramatically:** CRWV ~7.7x FY26 vs NBIS ~21x FY26 / ~6.4x FY27. Trailing multiples are noise at 200%+ growth — **forward EV/Sales is the only defensible anchor.**
- **CRWV EV is lease-sensitive:** ~$95.7B incl. finance leases vs ~$85.8B ex-leases (~$10B / ~2 turns of EV/Sales swing). NBIS being net-cash sidesteps this — ensure like-for-like EV construction when comping.
- **Sector context:** AI-infra stayed **rich** in mid-2026 (neocloud band 15x–82x trailing, ~4x–37x forward; medians ~25–30x) even as SaaS compressed hard. The market is now **rewarding net cash + contracted backlog and penalizing leverage** — CRWV de-rated post-Q1 (now $118 vs $187 high), while net-cash names (NBIS, ALAB) held premiums.

---

## 3. CONSENSUS ESTIMATES

| Metric | FY2025 (actual) | FY2026E | FY2027E | FY2028E |
|---|---|---|---|---|
| **Revenue** | **$529.8M** [PRIMARY] | **~$3.44B** (raised from $3.30B) | **~$11.2B** ⚠️ wide range | ~$21.3B |
| **Net income** | ~$10M (one-offs) | −$461M | −$780M (loss widens) | **+$108M (first profit)** |
| **EPS** | — | −$2.64 | (loss) | positive |
| **FCF** | −$3.7B | **−$19.0B** | **−$20.4B** | **−$17.1B** |

(Estimates [SECONDARY]: Simply Wall St / stockanalysis.com, ~6/11/26.)

- **ARR exit-rate:** Management guides **$7–9B ARR by year-end 2026** [PRIMARY, reaffirmed 5/13/26], from $1.25B (YE25) → $1.92B (Q1'26). >Half already contracted (Meta + Microsoft, ~$27B + $19.4B deals). Analysts generally model the **low-to-mid** end.
- **⚠️ FY2027 revenue is the single weakest consensus number** — estimates span **$4.3B / $7.8B / $11.2B**. Disagreement is on how fast contracted capacity converts to recognized revenue. Management's own $7–9B *exit-ARR* framework implies 2027 revenue ≥$7–9B, making the low estimates look conservative. **Treat FY2027 as unsettled.**
- **Positive FCF: NOT in the consensus window (through ≥FY2028).** Driven by capex guided to ~$20–25B in 2026 (call-only figure). Do **not** conflate with: (a) adj. EBITDA, already ~40% margin guided for 2026, or (b) non-GAAP net profit, expected ~2028. **Free cash flow stays deeply negative well past 2028.**

---

## 4. ANALYST COVERAGE

**Consensus = Buy / Moderate Buy, zero Sell ratings.** Aggregators disagree on the *average* PT (panel/staleness differences):

| Aggregator | Rating | # | Avg PT | High | Low |
|---|---|---|---|---|---|
| stockanalysis.com | Buy | 16 | **$244** | $380 | $120 |
| MarketBeat | Mod. Buy | 15 | **$203** | $287 | $120 |
| Benzinga | Buy | — | **$205** | $287 | $120 |
| Alpha Spread | — | — | $232 | $325.50 | $79.12 |

(stockanalysis **median = $257.50**.)

**Named bank targets (post-Q1'26 hike wave):**
| Firm | Rating | PT | Date |
|---|---|---|---|
| **Citigroup** | Buy | **$287** ← Street-high (major bank) | 5/15/26 |
| Bank of America | Buy | $280 (↑ from $240) | 6/8/26 |
| Citizens JMP | Mkt Outperform | $270 | 5/14/26 |
| BNP Paribas Exane | Neutral | $255 | 6/2/26 |
| D.A. Davidson | Neutral | $250 | 5/18/26 |
| Cantor Fitzgerald | Overweight | $129 | 4/9/26 |
| Morgan Stanley | Equal-Weight | $144 | 5/14/26 |
| Goldman Sachs | Buy | $120 (stale) | 9/17/25 |

**Theme:** Nearly everyone *raised* dollar targets after Q1, but the highest-PT names drifted to **valuation-driven Neutral/Hold** — "**great company, stretched stock.**" The stock (~$289) trades **above** most aggregator average PTs. Downgrades-on-valuation: Freedom Capital Buy→Hold (4/13/26); D.A. Davidson Buy→Neutral (5/18/26). Bull/bear spread: major banks **$120 → $287 (~2.4x)**; full extremes **$79 → $380 (~4.8x)** — unusually wide.

---

## 5. OWNERSHIP & POSITIONING

**NVIDIA stake — ~1.2M claim VERIFIED EXACTLY [PRIMARY]:** **1,190,476 Class A shares**, valued **$123,523,790** as of 3/31/26, per NVIDIA's 13F-HR (accession 0001045810-26-000042, filed 5/15/26). At ~$289 ≈ **~$344M**. **Critical caveat:** captures only NVIDIA's **original Dec 2024 equity stake**; the **separate $2B March 2026 pre-funded warrants** are not reportable common stock, so the 13F **understates** NVIDIA's true exposure.

**Largest 13G holder [PRIMARY]:** Situational Awareness LP (Aschenbrenner) — **12,410,060 sh = 5.6% of Class A** (13G filed 5/27/26).

**Top institutions [SECONDARY, ~3/31/26]:** BlackRock 9.94M (3.9%), Fred Alger 9.60M (3.8%), Orbis 8.31M (3.3%), Accel 6.83M (2.7%). Institutional ownership ≈ **52–54%.**

**Insider/control [PRIMARY 20-F]:** Dual-class (A=1 vote, B=10 votes). Founder Volozh via LASTAR trust holds Class B ≈ **~52–55% of voting power on ~11–13% economic**. All insiders ≈ **~60–65% voting**. **Founder retains majority voting control far above economic stake.**

**Short interest [SECONDARY, Nasdaq, settle 5/29/26]:** **44.3M shares short ≈ 17.5% of float**, ~2.6 days to cover, declining. Elevated SI + Nasdaq-100 inclusion = squeeze fuel.

---

## 6. IMPLIED EXPECTATIONS (reverse sanity-check, EV ≈ $72.5B)

**(a) Reverse EV/Sales — embedded steady-state revenue?** At a *mature* ~5–10x EV/Sales: 10x → ~$7.2B revenue; 7x → ~$10.3B; 5x → ~$14.4B. FY26 consensus is only $3.44B, so the EV implies the market has **already underwritten the FY27–28 ramp toward $10B+ revenue** at a mature multiple applied today.

**(b) Reverse EV/ARR — exit ARR to justify price?** $72.5B at 10x EV/ARR → ~$7B ARR; at 8x → ~$9B. **This brackets management's exact $7–9B YE-2026 guide** — i.e., the price **fully capitalizes the YE26 ARR target as if already achieved** at a mature multiple, leaving little margin for slippage. The guide implies a ~540% ARR jump in 2026 alone, which the price assumes lands.

**(c) Forward-return check:** For 12%/yr over 3 years, EV must reach ~$101B by end-2028 → $14–20B revenue at 5–7x (consensus FY28 ~$21.3B *just* clears). Over 5 years to end-2030: ~$127B EV → $18–25B revenue at 5–7x.

**Bottom line on expectations:** At ~$289, the market prices NBIS to (i) hit the high end of $7–9B exit-2026 ARR, (ii) scale revenue to ~$14–20B by 2028 at a mature ~40%+ EBITDA margin, all valued at a mature ~5–7x EV/Sales **applied today**. That is roughly **consensus-to-slightly-above** — trades above most average PTs and embeds near-flawless execution of the Meta/Microsoft backlog. **Downside risk concentrated in FY27 revenue conversion (consensus itself spans $4–11B) and the multi-year deeply-negative FCF / ~$20–25B-a-year capex funding need.** *(Derived sanity-checks, not a formal DCF.)*

---

## COULD NOT VERIFY
- **FY2026 capex dollar guidance ($20–25B).** Nebius's *written* materials guide on **contracted power (>4 GW)**, not a capex $ figure; $20–25B is call-/secondary-sourced only.
- **FY2027 consensus revenue.** Spans $4.3B / $7.8B / $11.2B — no reliable single consensus.
- **Exact current-second price.** Fresh ATHs intraday 6/18/26; figures here are 6/18 morning ($287.73) / 6/17 close ($280.91).
- **SEC.gov direct fetch (HTTP 403)** — figures cross-confirmed via filing-text indexes + Business Wire/EQS mirrors; SEC HTML not rendered directly.
- **Diluted vs basic market cap** is a material (~$16B / ~22%) fork — both reported; EV anchored on basic 253.9M count.

**Key primary sources:** Q1'26 SEC 6-K Ex.99.2 (`sec.gov/Archives/edgar/data/1513845/000110465926064092/nbis-20260331xex99d2.htm`); FY2025 20-F (`.../nbis-20251231x20f.htm`); NVIDIA 13F (`sec.gov/Archives/edgar/data/1045810/000104581026000042/information_table.xml`); Situational Awareness 13G; Nebius shareholder letters (Q4'25, Q1'26 PDFs at assets.nebius.com).
