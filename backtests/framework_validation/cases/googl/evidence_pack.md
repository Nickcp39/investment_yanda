# Evidence Pack — GOOGL as-of 2024-06-14  [ANCHOR EXEMPLAR]

Status: `DRAFT — verified from repo-cited sources` · this is the **format template** for the other 9 cases.
Prepared: 2026-06-16 · Sources reused from `../../../asof_2024_06_16_pipeline_test.md` (already EDGAR-cited).

> Sections 0–3 are **Runner-visible** (only info dated ≤ as-of).
> Sections 4–5 are **SEALED — Scorer only**. Never pass to the Runner.

---

## 0. As-of frame  · Runner-visible

| Field | Value | Source |
|---|---|---|
| Company / ticker | Alphabet Inc. / GOOGL | — |
| as_of date | 2024-06-14 (2024-06-16 was a Sunday; use Fri close) | — |
| Anchor event | Q1 2024 earnings (reported 2024-04-25) | A1.2024Q1 |
| as_of price | $176.79 | quotes: `data/asof_2024_06_16_quotes.csv` |
| Equity value | ~$2.2T (≈12.5B economic shares) | derived |
| Context (preclassified for Scorer) | `quality_compounder` | §4 |

## 1. Primary sources available as of 2024-06-14  · Runner-visible (only ≤ as-of)

| source_id | type | title | date | url |
|---|---|---|---|---|
| A1.2024Q1.991 | earnings release | Alphabet Q1 2024 Exhibit 99.1 | 2024-04-25 | sec.gov/Archives/edgar/data/1652044/000165204424000047/googexhibit991q12024.htm |
| A1.2024Q1.10Q | 10-Q | Alphabet Q1 2024 Form 10-Q | 2024-04 | sec.gov/Archives/edgar/data/1652044/000165204424000053/goog-20240331.htm |
| A1.2023K.10K | 10-K | Alphabet FY2023 Form 10-K | 2024-01 | sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm |

## 2. Key financials as of 2024-06-14  · Runner-visible (each cited)

| metric | value | source_id |
|---|---|---|
| Q1 2024 revenue | $80.5B (+15% YoY) | A1.2024Q1.991 |
| Q1 2024 operating income | $25.5B (~32% margin) | A1.2024Q1.991 |
| Q1 2024 Google Cloud revenue | $9.6B | A1.2024Q1.991 |
| Q1 2024 Cloud operating income | ~$0.9B | A1.2024Q1.991 |
| Q1 2024 operating cash flow | ~$28.8B | A1.2024Q1.991 |
| Q1 2024 capex | ~$12.0B | A1.2024Q1.991 |
| Q1 2024 FCF (derived) | ~$16.8B | derived |
| FY2023 revenue | $307.4B | A1.2023K.10K |
| FY2023 operating income | $84.3B | A1.2023K.10K |
| FY2023 OCF | $101.7B | A1.2023K.10K |
| FY2023 capex | $32.3B | A1.2023K.10K |
| FY2023 FCF (derived) | $69.5B | A1.2023K.10K |
| Capital return | first dividend + new $70B buyback authorization | A1.2024Q1.991 |

## 3. Point-in-time narrative context  · Runner-visible (leads only, no outcome)

- Market debate in mid-2024: does generative-AI answer-search **disintermediate** Google's commercial-intent search, or
  deepen query monetization? Is rising AI/datacenter capex a moat or an FCF drain? Cloud margin inflection durability.
- No hard evidence of Search ad damage in the filings as of this date.

---

## 4. SEALED — Scorer only  · DO NOT pass to Runner

```json
{
  "case_id": "googl_2024-06-14",
  "context_label": "quality_compounder",
  "dominant_layers": [2, 5, 6],
  "veto_expected": false,
  "correct_size_band": "STARTER..CORE",
  "mechanical_label": "WINNER",
  "forward": {
    "as_of_price": 176.79,
    "to_2026-06-16": 373.0,        "total_return": 1.11,
    "+12m": null, "+24m": null,    "bench_SPY_+24m": null, "bench_QQQ_+24m": null
  }
}
```

- **Key variable (right reason):** commercial-intent gateway intact + Cloud margin inflection + heavy FCF;
  AI-Search damage is a *risk*, not yet a *fact*. Price is full but not a veto for a compounder.
- **Why it tests the disease:** the framework's live v2 run capped this at `WATCH / 0%` on valuation + open questions.
  Correct behavior = price modulates size, does not zero it.
- Forward: $176.79 → ~$373 by 2026-06-16 (~+111%); intermediate prices + benchmark `TO VERIFY` at run time.

### Ground-truth per-layer signals (the target the tuned engine should roughly reproduce)

| # | Layer | role | target signal | note |
|---|---|---|---|---|
| 1 | Direction | context | `quality_compounder` | AI-fear dislocation on a dominant franchise |
| 2 | Business Thesis | conviction | +2 | commercial-intent ad gateway, crystal clear |
| 3 | Evidence Eng. | confidence | high | A1 filings, hard numbers |
| 4 | Accounting Trend | conviction | +1.5 | strong OCF/FCF; capex still manageable vs later |
| 5 | Value Chain | conviction | +1.5 | controls highest-value public search-ad pool |
| 6 | Moat | conviction | +2 | search habit, distribution, auction, YouTube, Android/Chrome |
| 7 | Operator | conviction | +1 | buyback+dividend+Cloud discipline; founder control = mild caveat |
| 8 | Inversion | risk | −1 | AI disintermediation real but unproven; **below** θ_veto |
| 9 | Valuation/MOS | price | ~0 (full, not cheap) | modulator in compounder context → trims size, not to zero |

→ Expected engine output: conviction high, no veto, price haircuts size but `STARTER..CORE`, **not** WATCH/0%.

---

## 5. Verification status

- Financials & sources: reused from repo backtest, originally EDGAR-cited → `VERIFIED (secondary-to-repo)`; re-pull at run time to confirm.
- Forward endpoint (~$373 / +111%): established in working session; `TO VERIFY` against a price series.
- Intermediate forward prices + SPY/QQQ benchmark: `TO FETCH`.
