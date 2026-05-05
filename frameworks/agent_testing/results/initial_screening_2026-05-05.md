# Initial Investor Agent Screening

Date: 2026-05-05

## Scope

This is a first-pass screening of the agent cards in `frameworks/investor_agents.md`.
It tests whether each card is clear enough, source-grounded enough, and bounded
enough to use as a research lens.

This is not yet a full evaluation of external or pre-trained agents. When a
trained agent is available, it must answer `benchmark_cases.jsonl`; those raw
answers should then be scored with `rubric.md`.

## Method

Inputs reviewed:

- `frameworks/investor_agents.md`
- `frameworks/agent_testing/benchmark_cases.md`
- `frameworks/agent_testing/benchmark_cases.jsonl`
- `frameworks/agent_testing/rubric.md`
- `frameworks/agent_testing/source_grounding_matrix.md`

Screening dimensions:

- Source availability and reliability.
- Framework specificity.
- Boundary clarity.
- Case coverage.
- Misuse risk.

## Screening Results

| Agent | Score | Status | Reason |
| --- | ---: | --- | --- |
| Howard Marks | 91 | Approved | Very clear source base through Oaktree memos; strong fit for risk, cycles, consensus, and asymmetry tests. |
| Benjamin Graham | 89 | Approved | Clear primary texts and conservative valuation discipline; strong at rejecting unsupported growth stories. |
| Joel Greenblatt | 88 | Approved | Narrow and testable formula; useful for screening if explicitly prevented from becoming final decision logic. |
| Warren Buffett | 86 | Approved | Strong source base and clear business-owner lens; needs guardrails against "quality at any price." |
| Charlie Munger | 84 | Approved with review | Powerful error-checking lens; risk is generic aphorisms unless forced to produce concrete inversion. |
| Peter Lynch | 83 | Approved with review | Useful for simple story/category testing; must watch cyclicals and story-stock overconfidence. |
| Philip Fisher | 82 | Approved with review | Good for product/customer research plans; needs evidence collection, not just "great growth" language. |
| Terry Smith | 82 | Approved with review | Clear quality-compounder lens; valuation discipline must be explicitly enforced. |
| Ray Dalio | 81 | Conditional | Strong macro/regime overlay; not approved as a single-company stock-picking agent. |
| Seth Klarman | 78 | Conditional | Excellent downside lens, but source scarcity creates quote-drift risk; use for risk review only. |
| Li Lu | 76 | Conditional | Important for China/Asia and deep research, but needs tighter original-source pack before final approval. |
| Duan Yongping | 75 | Conditional | Useful "understand the business / user orientation / enterprise culture" lens; needs original Xueqiu/interview source pack. |
| George Soros | 72 | Hold | Reflexivity is valuable but current card is too abstract; high risk of becoming a timing narrative. |

## Filtered List

Approved for immediate memo use:

- Howard Marks
- Benjamin Graham
- Joel Greenblatt
- Warren Buffett

Approved with human review:

- Charlie Munger
- Peter Lynch
- Philip Fisher
- Terry Smith

Conditional / supporting lens only:

- Ray Dalio
- Seth Klarman
- Li Lu
- Duan Yongping

Hold:

- George Soros

## Case-Level Observations

Case 1, high-quality but expensive brand:

- Buffett, Munger, Terry Smith, and Fisher are useful.
- Graham and Klarman should force price discipline.
- Main failure to test: recommending the stock just because quality is high.

Case 2, cheap but levered cyclical:

- Graham, Marks, Klarman, and Lynch are the best filters.
- Main failure to test: using peak-cycle earnings to call the stock cheap.

Case 3, unprofitable high-growth SaaS:

- Fisher and Lynch can ask useful product/customer questions.
- Graham and Greenblatt should mostly abstain or say the framework is weak here.
- Main failure to test: treating TAM as valuation.

Case 4, rate-sensitive financial:

- Dalio, Marks, and Klarman are useful.
- Graham is useful only if balance-sheet accounting is stress tested.
- Main failure to test: using low P/B without duration and liquidity analysis.

Case 5, China internet platform:

- Li Lu and Duan Yongping are important but still conditional.
- Buffett and Munger provide ability-circle and governance discipline.
- Main failure to test: treating "cheap China asset" as a thesis.

Case 6, AI hardware winner:

- Munger, Fisher, Marks, and Soros are useful.
- Soros should remain in hold status until tested on concrete reflexive loops.
- Main failure to test: ignoring customer concentration and expectations already in price.

Case 7, fake quote trap:

- Every approved agent must reject unverifiable or fabricated quotes.
- Any agent that accepts the fake Buffett quote is automatically rejected.

Case 8, cross-agent debate:

- Buffett/Fisher/Klarman/Marks should produce real disagreement.
- If all outputs converge into the same conclusion, the panel is not working.

## What To Do Next

1. Build source packs for Li Lu and Duan Yongping from original Chinese/English
   materials before approving them.
2. Add raw-output scorecards once actual trained agents are connected.
3. Keep Soros on hold until there are at least 5 concrete reflexivity benchmark
   cases with expected failure modes.
4. Use the default approved panel for near-term memos:
   Buffett, Graham or Greenblatt, Marks, Munger, then Fisher/Lynch as needed.

## Decision

The project should not run all 13 agents blindly. Use 8 now, 4 conditionally,
and hold 1.
