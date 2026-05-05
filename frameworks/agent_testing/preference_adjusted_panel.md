# Preference-Adjusted Investor Panel

Date: 2026-05-05

This file separates two ideas:

- Evaluation score: how source-grounded and testable an agent currently is.
- Usage weight: how much influence the agent should have in our actual research
  workflow.

The current preference is to move newer, business-operator, product, user-value,
and culture-oriented lenses forward. Older value frameworks remain useful, but
they should act more like guardrails than the main engine.

## Default Equity Memo Weights

| Rank | Agent / Lens | Weight | Role |
| ---: | --- | ---: | --- |
| 1 | Duan Yongping | 22% | Understand the business, user value, product quality, culture, and what not to do. |
| 2 | Li Lu | 15% | Deep research discipline, long-term ownership, China/Asia context when relevant. |
| 3 | Buffett | 14% | Business-owner lens, moat, owner earnings, capital allocation. |
| 4 | Munger | 10% | Inversion, incentives, psychology, and mistake prevention. |
| 5 | Howard Marks | 10% | Cycle, risk compensation, market consensus, and downside asymmetry. |
| 6 | Peter Lynch | 8% | Simple story, category, real-world adoption evidence. |
| 7 | Graham / Greenblatt | 8% | Valuation floor, balance sheet safety, quantitative cheapness check. |
| 8 | Fisher / Terry Smith | 7% | Growth-quality and quality-compounder verification, optional when the business fits. |
| 9 | Ray Dalio | 4% | Macro regime overlay: rates, liquidity, credit, inflation, policy. |
| 10 | Seth Klarman | 2% | Extra downside-first review for distressed, illiquid, or complex cases. |

Total: 100%

George Soros remains on hold. Reflexivity is useful, but the current card needs
more concrete tests before it gets weight in the default panel.

## Why Duan Yongping Moves Up

Duan Yongping's lens is especially useful for modern companies where the key
question is not only "is it statistically cheap?" but:

- Do users genuinely like the product?
- Is the company doing the right things for the right reasons?
- Is culture helping the business compound?
- Do we understand the business well enough to sit through volatility?
- What should we refuse to do, even when the market is exciting?

This matches the project's intended bias: fewer pure screens, more business
understanding.

Control: Duan remains source-pack conditional. His weight is high because the
lens is valuable, not because the source pack is already complete.

## Reduced Role For Old-School Value

Graham and Greenblatt are still useful, but they should not dominate the panel.

Use them to answer:

- Is the balance sheet dangerous?
- Is the valuation obviously excessive?
- Is the stock cheap for a reason?
- Are we paying too much for a story?

Do not use them to reject every modern compounder just because it fails a simple
low-multiple screen.

## Optional Modern-Quality Slot

Fisher and Terry Smith are not required names in the main workflow if the user
does not like them. Keep their combined slot as a "modern quality / growth
verification" role.

For most memos, this slot can be filled by one of:

- Fisher, when product, customer, channel, and R&D scuttlebutt matter.
- Terry Smith, when testing high-ROIC recurring compounders.
- A future newer investor/operator lens after it passes source and case tests.

## Panel By Situation

### U.S. Large-Cap Compounder

| Lens | Weight |
| --- | ---: |
| Duan Yongping | 18% |
| Buffett | 18% |
| Munger | 12% |
| Terry Smith / Fisher | 12% |
| Marks | 12% |
| Lynch | 10% |
| Graham / Greenblatt | 10% |
| Li Lu | 5% |
| Dalio | 3% |

### China / Asia Platform Or Consumer Company

| Lens | Weight |
| --- | ---: |
| Duan Yongping | 25% |
| Li Lu | 22% |
| Buffett | 12% |
| Munger | 10% |
| Marks | 9% |
| Lynch | 8% |
| Graham / Greenblatt | 7% |
| Fisher / Terry Smith | 5% |
| Dalio | 2% |

### AI / Technology Growth Company

| Lens | Weight |
| --- | ---: |
| Duan Yongping | 20% |
| Fisher / Terry Smith | 15% |
| Munger | 13% |
| Buffett | 12% |
| Lynch | 12% |
| Marks | 10% |
| Li Lu | 8% |
| Graham / Greenblatt | 6% |
| Dalio | 4% |

### Cheap / Distressed / Cyclical

| Lens | Weight |
| --- | ---: |
| Marks | 20% |
| Graham / Greenblatt | 18% |
| Klarman | 14% |
| Munger | 12% |
| Buffett | 10% |
| Duan Yongping | 10% |
| Dalio | 8% |
| Lynch | 5% |
| Li Lu | 3% |

## Updated Default Prompt Order

Run the panel in this order:

1. Duan Yongping: Do we understand the business, users, culture, and do-not-do list?
2. Li Lu: What information is missing before we can own it long term?
3. Buffett: Is the business durable and worth owning as a whole company?
4. Munger: Where are we fooling ourselves?
5. Marks: Are we being paid for the risk and cycle position?
6. Lynch: What is the simple story and real-world evidence?
7. Graham / Greenblatt: What is the valuation and balance-sheet guardrail?
8. Fisher / Terry Smith: Only if growth quality or high-ROIC compounding needs a deeper check.
9. Dalio: Only if macro regime exposure could dominate the thesis.

## Approval Rule

An agent can have high usage weight and still be conditional. In that case:

- Its output must be labeled "preferred lens, source-pack conditional."
- It cannot be the only reason for a buy/watch/core decision.
- It must be paired with at least one approved guardrail agent.

