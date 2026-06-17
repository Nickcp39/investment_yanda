# Position And Cash Management Source Notes

Date: 2026-06-17

Status: source collection / preliminary synthesis only. This is not the final portfolio-construction design.

Purpose: collect verifiable public notes from well-known real-money trading competitions and durable public traders to inform later changes to the research pipeline's sizing and cash controller.

## 1. Source Quality Filter

Use higher weight for sources that meet most of these conditions:

- Real-money competition or audited / independently tracked account.
- Multiple-year record or known long-term practitioner, not only one spectacular year.
- Explicit discussion of cash, exposure, position sizing, or drawdown control.
- Publicly accessible source that can be rechecked.

Lower weight for:

- Pure social-media summaries without primary support.
- One-year winners with little public process disclosure.
- Futures / forex championship examples that depend heavily on leverage and may not transfer cleanly to a long-only equity portfolio.

## 2. Competitions Worth Tracking

### United States Investing Championship / USIC

Useful because it is stock-market focused, real money, and public.

Notes:

- USIC has separate stock and enhanced-growth divisions. The stock division permits long/short, leverage, ETFs, foreign stocks, and written options; long options and futures move participants into enhanced growth.
- The official site lists current and prior standings, including Money Manager Verified Ratings for $1M+ accounts.
- BusinessWire's 2019 release says participants specify an account at the beginning of the year and brokerage statements verify performance claims.
- Prior participants listed by USIC / BusinessWire include Paul Tudor Jones, Mark Minervini, David Ryan, Edward Thorp, Mark Strome, Doug Kass, Marty Schwartz, Tom Basso, and others.

Sources:

- USIC official site: https://financial-competitions.com/
- USIC previous standings: https://financial-competitions.com/previousstandings
- 2019 BusinessWire final standings: https://www.businesswire.com/news/home/20200120005078/en/United-States-Investing-Championship-2019-Final-Standings
- 2025 BusinessWire final standings: https://www.businesswire.com/news/home/20260202090143/en/Multiple-World-Records-Set-in-International-Investing-Competition

### World Cup Trading Championships

Useful as a real-money performance reference, but less directly transferable.

Notes:

- It is famous and long-running, especially in futures / forex.
- Larry Williams and Andrea Unger are important historical names.
- The strategy and sizing lessons often involve leverage, margin, and short-term systems, so use cautiously for our stock research pipeline.

Sources:

- Official standings: https://www.worldcupchampionships.com/world-cup-trading-championship-standings
- Official site: https://www.worldcupchampionships.com/

## 3. Practitioner Notes

### Mark Minervini

Why relevant:

- Two-time US Investing Champion and long-term public momentum practitioner.
- His useful concept for us is not a fixed cash percentage. It is progressive exposure.

Observed method:

- Start smaller when coming out of cash or uncertainty.
- Increase exposure only after trades work and the market confirms.
- Cut exposure when recent trades fail or the market environment becomes hostile.
- Cash is an output of the opportunity set and recent feedback, not a permanent badge of prudence.

Sources:

- IBD position sizing / scaling discussion: https://www.youtube.com/watch?v=X8fHoK0U4so
- Chartmill summary of progressive exposure: https://www.chartmill.com/documentation/trading-and-investing/money-and-risk-management/473-Mastering-Market-Dynamics-The-Benefits-of-Progressive-Exposure

### David Ryan

Why relevant:

- Three-time US Investing Champion and long-term CAN SLIM / growth-stock practitioner.
- Useful for concentration and sizing positions large enough to matter while controlling defined risk.

Observed method:

- Position sizing should help capture large moves that move the portfolio needle.
- Concentration matters, but risk must be defined first.
- Adds should happen after a position proves itself, not by averaging down.

Sources:

- Investing With IBD podcast: https://podcasts.apple.com/us/podcast/david-ryan-how-to-size-positions-like-a-three-time/id1454868999?i=1000626316655
- IBD video: https://www.investors.com/ibd-videos/videos/david-ryan-how-to-size-positions-like-a-three-time-u-s-investing-champion

### Sean Ryan

Why relevant:

- Not just a one-year result. BusinessWire 2025 notes he entered every USIC competition since the 2019 restart and reported profits each year.
- Business Insider profile gives explicit risk-control rules.

Observed method:

- Hard maximum loss per position around 1% of total trading portfolio.
- If a stock rises meaningfully, he may move a stop to breakeven to reduce remaining risk.
- He scales into positions and trims / shaves profits while maintaining a core.
- His process is chart-driven and highly responsive to market feedback.

Sources:

- Business Insider interview: https://www.businessinsider.com/stock-market-investor-indicators-profitable-trader-huge-returns-2023-2
- 2025 USIC final standings: https://www.businesswire.com/news/home/20260202090143/en/Multiple-World-Records-Set-in-International-Investing-Competition

### J Law / Law Wai-Sum

Why relevant:

- 2024 and 2025 USIC $1M+ stock division winner; BusinessWire describes a two-year record in the million-plus division.
- Public free material gives useful high-level process but not enough detailed sizing formulas.

Observed method:

- In slumps, he exits positions, reduces position size, reviews trades, and resets.
- Concentration is valuable only when market conditions justify it.
- The best time to concentrate is typically after a major correction or early in a bull market.
- He can add to winners, but add-on buys are smaller than the initial position and shrink as price rises.

Sources:

- TraderLion interview: https://traderlion.com/profile/j-law/11-lessons-from-j-law/
- 2025 USIC final standings: https://www.businesswire.com/news/home/20260202090143/en/Multiple-World-Records-Set-in-International-Investing-Competition
- JLawStock Academy page, useful only as supporting context: https://www.jlawstock.com/jla

### Clement Ang

Why relevant:

- USIC top performer and public process writer.
- Especially useful for the idea of earning the right to increase exposure.

Observed method:

- Concentration over broad diversification when the setup is strong.
- Progressive exposure: from cash, start with a first buy; increase exposure only when that first buy is working.
- Use unrealized or realized profits as a cushion to finance later risk.
- Trade larger in good environments and smaller in poor environments.

Source:

- Trading Resource Hub guest post: https://tradingresourcehub.substack.com/p/6-lessons-from-competing-usic-2024-clement-ang

### Christian Flanders

Why relevant:

- Strong 2024 USIC result and detailed public post on drawdown control.
- More one-year-performance dependent than Sean Ryan / David Ryan, so use as supporting evidence rather than core authority.

Observed method:

- Reduce trade size and frequency when market conditions turn hostile.
- His key question was what the performance would look like if no month lost more than 5% of equity.
- When repeatedly stopped out, the market is telling the trader to reduce size, cut risk, or stop trading.
- For rare high-conviction opportunities, he sized aggressively after conditions aligned.

Source:

- Trading Resource Hub guest post: https://tradingresourcehub.substack.com/p/christian-flanders-usic-2024-outperformance

### IBD SwingTrader / CAN SLIM-Style Model Portfolio

Why relevant:

- Not a competition winner, but a professional rule-based trading product with explicit position-sizing language.
- Useful as a bridge between champion anecdotes and implementable rules.

Observed method:

- Full position size is around 10% in their swing-trading context, with smaller initial positions when risk is higher.
- A flexible approach allows adding when a position is working.
- The key tension is that too large a position creates unmanageable losses, while too small a position dilutes returns.

Sources:

- IBD SwingTrader position-sizing article: https://www.investors.com/research/swing-trading/risk-management-position-sizing-swingtrader/
- IBD SwingTrader FAQ / position sizing context: https://www.investors.com/research/swing-trading/swing-trading-strategy-position-sizing-tips-ibd-swingtrader-platform/

## 4. Repeated Patterns Across Sources

### Pattern A: Cash Is An Exposure State

Cash rises when:

- Setups are poor.
- Current positions are not working.
- The market is choppy or hostile to the strategy.
- The trader is in a drawdown or losing streak.

Cash falls when:

- Initial positions show profit.
- The market confirms the theme.
- More high-quality setups appear in related themes.
- There is a cushion of unrealized or realized gains.

### Pattern B: Initial Size Tests The Idea

The first entry is often not the final desired exposure. It tests:

- Thesis quality.
- Market acceptance.
- Timing.
- Whether the stock behaves as expected.

### Pattern C: Add Only After Evidence Improves

Professional-style notes repeatedly reject averaging down. They favor:

- Adding to winners.
- Adding after price / volume / business confirmation.
- Reducing add-on size as the position matures or price becomes extended.

### Pattern D: Risk Is Defined By Portfolio Loss, Not Just Position Percent

Several sources think in terms of portfolio risk per trade:

- Example: 1% of total portfolio risk per position.
- Position weight then depends on stop distance, volatility, gap risk, and conviction.

This is different from saying every idea should be 1% of capital.

### Pattern E: Too-Small Sizing Is Also A Failure

IBD's framing is especially useful: positions that are too large are dangerous, but positions that are too small dilute returns. This directly applies to the SNDK pipeline issue.

## 5. Preliminary Implications For Our Pipeline

Do not finalize yet, but these are the working hypotheses:

- M6 should not be the final owner of portfolio size. It should output attractiveness, asymmetry, stage, and risk.
- A separate portfolio controller should later combine M6 with cash policy, current holdings, drawdown state, and theme exposure.
- SNDK 2025 exposed a conservative sizing failure: direction was correct, but the test did not punish under-sizing enough.
- The better professional analogy is progressive exposure:
  - initial position to test,
  - add after confirmation,
  - cut or stop if the market / business does not confirm.
- Our standing 25% cash target can fit this structure, but it should be managed as a cash band and funding sleeve, not as a reason to permanently cap good ideas.

## 6. Open Questions Before Design

- What should count as confirmation for fundamental research cases where price action is not the primary signal?
- Should our risk budget be based on mark-to-market drawdown, thesis failure loss, or expected downside to kill price?
- How should a 25% cash target interact with high-conviction periods?
- How should we rank funding sources when adding to a winner: cash first, weakest holding, overextended winner trim, or theme rebalance?
- How should scoring penalize "right direction, too small" separately from "wrong direction"?

