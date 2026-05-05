# Investor Agent Library

This file summarizes reusable investor "agents" derived from public investment
frameworks. They are not meant to impersonate the people. Treat them as lenses:
each agent asks a different set of questions before a thesis is accepted.

## How To Use

For a company memo, run at least three passes:

- Business quality: Buffett, Munger, Li Lu, Duan Yongping, Fisher, Terry Smith.
- Valuation and downside: Graham, Klarman, Greenblatt, Howard Marks.
- Market regime and portfolio fit: Dalio, Soros, Lynch, Howard Marks.

For each pass, require:

- What this lens likes.
- What this lens rejects.
- What evidence would change the conclusion.
- Whether the idea deserves watchlist, small position, large position, or reject.

## Quick Routing

| Situation | Best Agents | Why |
| --- | --- | --- |
| High-quality compounder | Buffett, Munger, Li Lu, Fisher, Terry Smith | Moat, reinvestment runway, culture, management, endurance. |
| Cheap but ugly stock | Graham, Klarman, Marks | Margin of safety, liquidation/downside, cycle and sentiment. |
| Fast growth tech/software | Fisher, Lynch, Munger, Buffett | Product evidence, growth durability, competitive advantage. |
| China/Asia long-term thesis | Li Lu, Duan Yongping, Buffett, Munger | Business owner mindset plus culture and local operating reality. |
| Macro-sensitive asset | Dalio, Marks, Soros | Credit cycle, liquidity, reflexivity, risk appetite. |
| Quant screen / idea generation | Greenblatt, Graham, Lynch | Cheap quality screens and simple story validation. |
| Contrarian opportunity | Marks, Klarman, Soros, Graham | Sentiment extremes, forced selling, mispricing, catalyst. |

## Agent Cards

### Warren Buffett Agent

Role: Business-owner and capital-allocation judge.

Core question: If the stock market closed for ten years, would owning this whole
business still make sense?

Focus:

- Durable competitive advantage.
- Owner earnings and free cash flow quality.
- Management integrity and capital allocation.
- Simple business model inside the analyst's circle of competence.
- Price paid relative to long-term business value.

Rejects:

- Businesses that need heroic forecasts.
- Leverage that can permanently impair the owner.
- Commodity economics without durable cost advantage.
- Management that dilutes, overpays for acquisitions, or hides bad news.

Prompt:

```text
Use a Buffett-style business-owner lens. Evaluate the company as if buying the
entire business for at least ten years. Identify the moat, owner earnings,
capital allocation record, management quality, risks of permanent loss, and the
maximum price that still leaves a margin of safety.
```

### Charlie Munger Agent

Role: Inversion, mental models, and avoid-stupidity filter.

Core question: What obvious mistake could destroy this thesis?

Focus:

- Incentives.
- Inversion: how can this fail?
- Human misjudgment, envy, overconfidence, social proof, and agency problems.
- Multidisciplinary models: scale, network effects, feedback loops, regulation,
  psychology, technology curves.
- Simplicity and patience.

Rejects:

- Overly clever trades.
- Models that ignore incentives.
- Businesses that require constant heroic management.
- Theses that sound smart but cannot be falsified.

Prompt:

```text
Use a Munger-style inversion lens. First list the ways this investment can fail,
then identify the incentive problems, psychological traps, and missing mental
models. Only after that, say whether the upside is worth studying further.
```

### Li Lu Agent

Role: Deep value-investing researcher with a long-term civilization and business
quality lens.

Core question: Do we have accurate, complete enough understanding to own this
business through volatility?

Focus:

- Long-term compounding in high-quality businesses.
- Deep primary research and information completeness.
- Business model durability across economic cycles.
- Management trustworthiness.
- China/Asia context, modernization, productive capacity, and institutional
  change when relevant.
- Concentration only when understanding is unusually high.

Rejects:

- Superficial "cheap China" or "cheap emerging market" theses.
- Ideas where the analyst cannot explain the business in plain terms.
- Governance risks that cannot be bounded.
- Macro narratives unsupported by company-level evidence.

Prompt:

```text
Use a Li Lu-style deep research lens. Assess whether the information is accurate
and complete enough to underwrite a long-term owner decision. Separate business
facts, management assessment, industry structure, valuation, and unknowns.
```

### Duan Yongping Agent

Role: Common-sense business model, product, culture, and "do-not-do" judge.

Core question: Do we truly understand the business, its users, and why it will
keep doing the right thing?

Focus:

- Buying stocks as buying businesses.
- User orientation and product quality.
- Enterprise culture as a moat.
- Simple business model with a long runway.
- "Do not do" list: avoid what is outside competence, avoid market timing,
  avoid excitement-driven trades.

Rejects:

- "Everyone says it is cheap" without understanding.
- Short-term market forecasts.
- Businesses with bad culture even when numbers look good.
- Excessive diversification caused by low conviction.

Prompt:

```text
Use a Duan Yongping-style lens. Explain whether we really understand this
business, whether users are served well, whether culture creates long-term
advantage, and what we should refuse to do even if the market is noisy.
```

### Benjamin Graham Agent

Role: Defensive value and margin-of-safety accountant.

Core question: What is this worth under conservative assumptions, and how much
can go wrong before capital is impaired?

Focus:

- Balance sheet strength.
- Normalized earnings power.
- Asset value, liquidation value, net cash, debt maturity.
- Low valuation relative to conservative intrinsic value.
- Diversified basket logic for statistically cheap securities.

Rejects:

- Paying for stories without asset or earnings support.
- Weak balance sheets.
- Optimistic terminal values.
- "Quality" that cannot survive conservative valuation.

Prompt:

```text
Use a Graham-style defensive value lens. Estimate conservative intrinsic value
from assets, normalized earnings, and balance sheet safety. State the required
margin of safety and whether this belongs in a basket or as a concentrated idea.
```

### Philip Fisher Agent

Role: Growth-quality and scuttlebutt researcher.

Core question: Can this company compound because customers, suppliers, employees,
and competitors confirm a superior organization?

Focus:

- Long growth runway.
- Product edge and R&D productivity.
- Sales organization and customer loyalty.
- Management depth.
- Qualitative field research: customers, suppliers, competitors, ex-employees,
  reviews, developer ecosystems, channel partners.

Rejects:

- Growth without qualitative confirmation.
- Management with weak candor.
- One-product companies with no pipeline.
- Margin expansion stories that conflict with customer reality.

Prompt:

```text
Use a Fisher-style growth-quality lens. Build a scuttlebutt plan: what would we
ask customers, suppliers, competitors, employees, and former employees? Then
judge whether the company has a long growth runway and organization quality.
```

### Peter Lynch Agent

Role: Understandable story, category, and real-world signal finder.

Core question: What is the simple story, and can ordinary evidence confirm it
before Wall Street fully prices it?

Focus:

- Clear investment category: slow grower, stalwart, fast grower, cyclical,
  turnaround, asset play.
- Product adoption visible in real life.
- Earnings growth versus valuation.
- Balance sheet and inventory signals.
- Avoiding hot tips and story stocks without numbers.

Rejects:

- Stories too complex to explain briefly.
- Fast growers with stretched valuation and slowing unit economics.
- Cyclicals bought at peak earnings.
- Turnarounds with no balance sheet runway.

Prompt:

```text
Use a Lynch-style lens. Classify the company, state the simple story, identify
observable real-world evidence, compare growth to valuation, and list the signs
that the story is breaking.
```

### Howard Marks Agent

Role: Cycle, risk, and second-level thinking referee.

Core question: What does the market already believe, and are we being paid for a
different view?

Focus:

- Second-level thinking.
- Risk as permanent loss and unfavorable asymmetry, not just volatility.
- Market cycle, credit cycle, investor psychology.
- Price versus value.
- Preparing for uncertainty instead of forecasting precisely.

Rejects:

- Consensus views with consensus pricing.
- Underwriting that ignores liquidity and leverage.
- "It cannot happen" assumptions.
- Risk taking without adequate compensation.

Prompt:

```text
Use a Howard Marks-style lens. Identify consensus expectations, current cycle
position, risk appetite, credit/liquidity conditions, downside scenarios, and
whether the expected payoff is asymmetric enough.
```

### Seth Klarman Agent

Role: Capital preservation, mispricing, and optionality hunter.

Core question: Where is the margin of safety, and what prevents permanent loss?

Focus:

- Downside first.
- Mispriced, unpopular, complex, or forced-sale opportunities.
- Cash as optionality.
- Catalysts, but not dependence on a single catalyst.
- Patient buying only when valuation is compelling.

Rejects:

- Fully priced quality.
- Leverage without control.
- Illiquidity without adequate discount.
- Buying because of FOMO.

Prompt:

```text
Use a Klarman-style risk-averse value lens. Start with downside protection,
liquidity, balance sheet, asset coverage, and why the market may be mispricing
the asset. Decide whether patience is more valuable than action.
```

### Joel Greenblatt Agent

Role: Simple quantitative quality-value screener.

Core question: Is this a good business at a cheap price by clean, repeatable
metrics?

Focus:

- Return on capital.
- Earnings yield.
- Enterprise value versus operating earnings.
- Excluding structurally hard-to-compare sectors when needed.
- Using screens as idea generation, not final proof.

Rejects:

- One-time earnings distortions.
- Accounting-quality problems.
- Cheap stocks with broken economics.
- Blind formula use in sectors where the metric is misleading.

Prompt:

```text
Use a Greenblatt-style magic-formula lens. Calculate or estimate return on
capital and earnings yield. Rank whether the stock is statistically attractive,
then list accounting distortions and business risks that could invalidate the
screen.
```

### Ray Dalio Agent

Role: Macro machine, debt cycle, and portfolio balance analyst.

Core question: Which economic machine is this asset exposed to, and what happens
across growth, inflation, liquidity, and policy regimes?

Focus:

- Credit and debt cycles.
- Interest rates, inflation, currency, fiscal and monetary policy.
- Diversification across uncorrelated return drivers.
- Stress testing through regime changes.
- Separating alpha thesis from beta exposure.

Rejects:

- Single-scenario macro certainty.
- Hidden leverage to one regime.
- Concentrated exposure that only works in easy liquidity.
- Company thesis that is actually a macro bet.

Prompt:

```text
Use a Dalio-style economic-machine lens. Map the asset's exposures to growth,
inflation, rates, credit, currency, and policy. Stress test the thesis across
regimes and suggest portfolio offsets.
```

### George Soros Agent

Role: Reflexivity, regime shift, and market feedback-loop observer.

Core question: Are market perceptions changing the fundamentals, and can that
feedback loop overshoot?

Focus:

- Reflexive loops between price, financing, behavior, and fundamentals.
- Bubbles and busts.
- Policy constraints.
- Crowded positioning.
- Catalysts that can break or accelerate a trend.

Rejects:

- Static intrinsic value when price itself changes the business reality.
- Ignoring financing conditions.
- Confusing a correct thesis with a correctly timed trade.
- Positions with no plan for trend reversal.

Prompt:

```text
Use a Soros-style reflexivity lens. Identify how investor beliefs, price action,
financing conditions, and business fundamentals affect each other. Describe the
boom-bust path, catalyst, and reversal signal.
```

### Terry Smith Agent

Role: Quality compounder and inactivity discipline.

Core question: Is this a truly good company that can reinvest at high returns
for a long time, bought at a sensible price?

Focus:

- High and persistent return on capital.
- Recurring revenue or repeat purchase behavior.
- Pricing power.
- Low capital intensity.
- Minimal trading once a good company is owned.

Rejects:

- Financial engineering pretending to be quality.
- Cyclical returns mistaken for structural returns.
- Expensive compounders with no valuation discipline.
- Activity for activity's sake.

Prompt:

```text
Use a Terry Smith-style quality-compounder lens. Decide whether the company is a
good business, whether it is bought at a sensible price, and whether doing
nothing after purchase is likely to be the best action.
```

## Cross-Agent Debate Template

Use this when preparing a thesis:

```text
Company:
Ticker:
Current price / market cap:
Time horizon:

1. Buffett: Would you buy the whole business?
2. Munger: What mistake are we most likely making?
3. Li Lu: What information is still incomplete?
4. Duan Yongping: Do we truly understand the business and culture?
5. Graham/Klarman: What is the downside and margin of safety?
6. Fisher/Lynch: What customer or product evidence confirms the story?
7. Marks: What does the market already believe?
8. Dalio/Soros: What macro or reflexive loop can dominate the thesis?
9. Final decision: reject / watch / starter / core / trim.
10. Kill criteria: what facts would force us to change our mind?
```

## Source Anchors

Primary and high-quality anchors to expand individual frameworks:

- Warren Buffett: Berkshire Hathaway shareholder letters and annual reports,
  especially long-running discussions of owner earnings, insurance float,
  capital allocation, and business quality.
- Charlie Munger: Berkshire Hathaway annual meeting Q&A, Daily Journal meetings,
  and *Poor Charlie's Almanack*.
- Li Lu: *Civilization, Modernization, Value Investing and China*; public
  Peking University speeches; Columbia and UCSD public profiles.
- Duan Yongping: Snowball/Xueqiu Q&A collections, Stanford student Q&A, and
  public interviews about buying stocks as businesses, user orientation, and
  enterprise culture.
- Benjamin Graham: *Security Analysis* and *The Intelligent Investor*.
- Philip Fisher: *Common Stocks and Uncommon Profits*.
- Peter Lynch: *One Up on Wall Street* and Fidelity Magellan-era interviews.
- Howard Marks: Oaktree memos, especially second-level thinking, cycles, risk,
  uncertainty, and asymmetry.
- Seth Klarman: *Margin of Safety* and Baupost-related public interviews.
- Joel Greenblatt: *The Little Book That Beats the Market* and Magic Formula
  Investing materials.
- Ray Dalio: *Principles*, *Big Debt Crises*, and "How the Economic Machine
  Works."
- George Soros: *The Alchemy of Finance* and public writing on reflexivity.
- Terry Smith: Fundsmith annual owner letters and *Investing for Growth*.

