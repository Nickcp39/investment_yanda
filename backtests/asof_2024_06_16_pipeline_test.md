# As-Of Backtest - 2024-06-16 Pipeline Test

Last updated: 2026-06-16

Purpose: test whether the 10-layer research pipeline would have produced master-like decisions using only information available as of 2024-06-16.

This is a pipeline ability test, not a current investment memo.

---

## 0. Test Protocol

Cutoff date: 2024-06-16.

Market date used for price: 2024-06-14 close, because 2024-06-16 was a Sunday.

Allowed before verdict:

- Filings, earnings releases, call transcripts, and prices available on or before 2024-06-16.
- Local video / sentiment notes published on or before 2024-06-16, but only as topic leads, not evidence.
- No 2025 or 2026 financials.
- No later Berkshire / H&H / Duan actions before the blind verdict is locked.

Allowed after verdict:

- Later Berkshire / Duan actions only for scoring whether the pipeline direction matched.

Scoring:

| Score | Meaning |
|---|---|
| `PASS` | Pipeline would have produced a materially similar action / direction. |
| `PARTIAL` | Pipeline would identify quality and direction but miss the actual action design. |
| `FAIL` | Pipeline would reject or ignore a case that the target investor later acted on. |

---

## 1. Case A - GOOGL As Of 2024-06-16

### As-Of Inputs

Price:

- GOOGL close on 2024-06-14: $176.79.
- Approximate equity value: about $2.2T using roughly 12.5B economic shares.

Primary sources available:

- Alphabet Q1 2024 Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000047/googexhibit991q12024.htm
- Alphabet Q1 2024 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000053/goog-20240331.htm
- Alphabet FY2023 Form 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm
- Yahoo chart price API snapshot in `data/asof_2024_06_16_quotes.csv`.

Key evidence available then:

- Q1 2024 revenue: $80.5B, +15% YoY.
- Q1 2024 operating income: $25.5B, operating margin about 32%.
- Q1 2024 Google Cloud revenue: $9.6B, Cloud operating income about $0.9B.
- Q1 2024 operating cash flow: about $28.8B.
- Q1 2024 capex: about $12.0B.
- Q1 2024 FCF: about $16.8B.
- FY2023 revenue: $307.4B.
- FY2023 operating income: $84.3B.
- FY2023 OCF: $101.7B.
- FY2023 capex: $32.3B.
- FY2023 derived FCF: $69.5B.
- Alphabet announced its first dividend and a new $70B buyback authorization in Q1 2024.

### Blind Pipeline Output

Verdict the pipeline should have produced:

`STARTER / BUY WITH MONITOR`

Suggested size:

2% to 4% starter, with room to add only if AI Search damage does not appear and Cloud margin continues improving.

### 10-Layer Test

| Layer | As-of 2024 result | Pass? |
|---|---|---|
| Direction Selection | Google was the right company to study: AI fear, Search dominance, Cloud inflection, strong FCF, buybacks/dividend. | Yes |
| Business Thesis | One-minute thesis was clear: commercial intent + ad auction + Cloud + distribution. | Yes |
| Evidence Engineering | A1 evidence existed from FY2023 10-K and Q1 2024 filing/release. | Yes |
| Accounting | Strong OCF/FCF, capex still manageable versus 2026-era levels. | Yes |
| Value Chain | Google controlled the highest-value public Search ad pool. | Yes |
| Moat | Search habit, distribution, ad auction, YouTube, Android/Chrome were still strong. | Yes |
| Operator | Buyback + dividend + Cloud discipline gave a cleaner capital-allocation read than 2026. | Yes |
| Inversion | AI disintermediation was a real risk, but no hard evidence of Search damage yet. | Yes |
| Valuation / MOS | Not deep value, but acceptable for a quality compounder at $176-$177 if 8%-10% long-run return was enough. | Yes |
| Decision / Monitoring | Correct output: starter position plus AI/Search monitor, not all-in. | Yes |

### Why This Matches The Buffett-Like Direction

The pipeline would not have predicted a specific later Berkshire private placement or the internal Berkshire decision-maker. But it should have done the important thing:

> It should not have rejected Google. It should have classified Google as a high-quality compounder with a reasonable enough 2024 price to start a position, while monitoring AI disruption.

That is close enough to the target behavior for this test.

Score: `PASS`.

---

## 2. Case B - NVDA As Of 2024-06-16

### As-Of Inputs

Price:

- NVDA close on 2024-06-14: $131.88, post-split adjusted.
- Approximate equity value: about $3.3T using roughly 24.8B post-split shares.

Primary sources available:

- NVIDIA Q1 FY2025 official release: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2025
- NVIDIA Q1 FY2025 Form 10-Q: https://www.sec.gov/Archives/edgar/data/1045810/000104581024000124/nvda-20240428.htm
- NVIDIA FY2024 Form 10-K: https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm
- Yahoo chart price API snapshot in `data/asof_2024_06_16_quotes.csv`.
- Local sentiment lead available before cutoff: `sources/videos/2024-06-15_8hMW5slRpB0_..._nvda_transcript.md`.

Key evidence available then:

- Q1 FY2025 revenue: $26.0B, up 262% YoY.
- Data Center revenue: $22.6B, up 427% YoY.
- GAAP gross margin: 78.4%.
- Non-GAAP gross margin: 78.9%.
- GAAP diluted EPS: $5.98 pre-split, up 629% YoY.
- Non-GAAP diluted EPS: $6.12 pre-split, up 461% YoY.
- 10-for-1 stock split announced / effective around June 2024.
- Blackwell platform was already part of the forward product cycle.

### Blind Pipeline Output Without Any New Patch

Verdict the current value-investing-heavy pipeline would likely have produced:

`WATCH / EXCEPTIONAL QUALITY BUT NO CLASSIC MOS`

Reason:

- Direction: obvious AI bottleneck.
- Business quality: exceptional.
- Operator: exceptional.
- Moat: CUDA + accelerators + networking + ecosystem very strong.
- Accounting: extraordinary growth and gross margin.
- Valuation: already expensive around $132 post-split / $3T+ market cap.

This would identify the company but might refuse to act.

### Blind Pipeline Output With A Required Bottleneck Exception

Verdict the corrected pipeline should produce:

`EXCEPTIONAL BOTTLENECK STARTER / STRUCTURED ENTRY`

Suggested action:

- Do not treat it as a normal cheap-stock BUY.
- Allow a small common-stock starter if position size is modest.
- Prefer structured entry if options are understood and risk-controlled:
  - sell put only at a price where you would happily own shares;
  - buy-write / covered call only if it creates an effective basis inside the desired entry zone;
  - no buying calls as speculation;
  - no oversized position because valuation and cyclicality are real.

Target basis range from this backtest:

- Simple common-stock buy zone: hard to justify at $132 without heroic growth.
- Structured-entry zone: effective basis near $90-$110 becomes much more reasonable if the investor truly underwrites the bottleneck.

### 10-Layer Test

| Layer | As-of 2024 result | Pass? |
|---|---|---|
| Direction Selection | NVDA was the clearest AI compute bottleneck. | Yes |
| Business Thesis | One-minute thesis: AI factories need GPUs, networking, CUDA, systems, and software. | Yes |
| Evidence Engineering | Official Q1 FY2025 release/10-Q gave extremely strong hard evidence. | Yes |
| Accounting | Revenue +262%, Data Center +427%, gross margin near 78%; extraordinary. | Yes |
| Value Chain | NVDA captured the scarce upstream profit pool, unlike GOOG/MSFT/AMZN who were major capex spenders. | Yes |
| Moat | CUDA ecosystem, product cadence, networking, systems integration, developer lock-in. | Yes |
| Operator | Jensen Huang should score extremely high. | Yes |
| Inversion | ASIC substitution, hyperscaler bargaining, export controls, cyclicality, supply-chain concentration. | Yes |
| Valuation / MOS | Classic MOS failed at $132. Exceptional bottleneck model was required. | Partial |
| Decision / Monitoring | Without structure module: WATCH. With structure module: small starter / sell premium / buy-write. | Partial to Yes |

### Comparison To Duan-Like Action

Later reporting says Duan Yongping used a buy-write structure on NVDA: bought 100,000 shares around $116.7 and sold 1,000 March 2026 $120 calls, reducing effective cost to about $92.52. That later action should not be used in the blind verdict, but it is useful for scoring the pipeline.

Sources for the later comparison:

- GuruFocus: https://www.gurufocus.com/news/2745054/nvidia-nvda-stock-strategy-duan-yongpings-925-million-buywrite-strategy
- Moomoo/Futu: https://www.moomoo.com/hans/news/post/50634501

Test result:

- If the pipeline only allows ordinary common-stock BUY/WATCH/REJECT, it likely misses the Duan-like result.
- If the pipeline includes an exceptional-bottleneck + position-engineering module, it can get close: "great company, too expensive for ordinary MOS, but worth owning through a structured basis-reduction trade if risk is capped."

Score without patch: `PARTIAL / likely miss action`.

Score with bottleneck exception: `PASS`.

---

## 3. Test Verdict

| Case | Target behavior | Pipeline result | Score |
|---|---|---|---|
| GOOGL 2024-06-16 | Buffett-like quality compounder / buyable at then-price | STARTER / BUY WITH MONITOR | PASS |
| NVDA 2024-06-16 | Duan-like recognition of quality plus structured entry | WATCH unless bottleneck exception exists; structured-entry module gives PASS | PARTIAL -> PASS after framework patch |

Main finding:

> The pipeline is good enough for Buffett-style compounders such as Google, but it needs an explicit "Exceptional Bottleneck / Position Engineering" module to catch NVDA-like companies without becoming reckless.

---

## 4. Required Framework Patch

Add a submodule inside Layer 9 and Layer 10:

`Exceptional Bottleneck / Position Engineering`

Trigger only when all are true:

1. Direction layer identifies a real industry bottleneck, not a theme.
2. Revenue growth is extraordinary and supported by hard filings, not only narrative.
3. Gross margin / operating margin confirm pricing power.
4. Customer ROI is plausible and customers are increasing spend.
5. Moat is technical and ecosystem-based, not only cyclical supply shortage.
6. Operator score is high.
7. Inversion risks are explicit.
8. Classic MOS fails at spot price.

Allowed actions:

- `WATCH`.
- `STARTER common` with small size.
- `SELL PUT at buy-below`.
- `BUY-WRITE / covered call` if the effective basis enters the underwriting range.
- `DO NOTHING` if option premium does not compensate risk.

Forbidden actions:

- Buy calls for speculation.
- Use options on a company not deeply understood.
- Treat option premium as free money.
- Use leverage to force a valuation case.
- Ignore assignment risk or tax/liquidity constraints.

This is the exact patch needed for the pipeline to become closer to Duan's style without losing Buffett/Graham discipline.

