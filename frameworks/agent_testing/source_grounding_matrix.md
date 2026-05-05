# Source Grounding Matrix

这个文件记录每类 agent 的来源层级。测试时优先使用 primary source；二手整理
只能作为导航，不能当作最终证据。

## 来源等级

- A: 一手来源。本人书籍、股东信、公司官网、本人公开演讲原文/视频。
- B: 高质量转录或授权整理。可靠媒体、机构页面、课程转录。
- C: 第三方总结。可用于发现线索，但不能直接当作证据。

## Agent 来源表

| Agent | A 级来源 | B 级来源 | C 级来源 | 测试注意 |
| --- | --- | --- | --- | --- |
| Warren Buffett | Berkshire Hathaway shareholder letters, annual reports, annual meeting Q&A | CNBC Berkshire meeting archive | Media summaries | 不允许编造语录；重点测 owner earnings、moat、capital allocation、能力圈。 |
| Charlie Munger | Berkshire/Daily Journal meeting Q&A, *Poor Charlie's Almanack* | CNBC Daily Journal streams/transcripts | Quote compilations | 重点测 inversion、incentives、psychology；不要让它只输出鸡汤。 |
| Li Lu | *Civilization, Modernization, Value Investing and China*; public speeches where original text is available | University profiles; translated speech archives | Profiles and blog summaries | 重点测信息完整性、深度研究、中国语境和治理风险。 |
| Duan Yongping | Xueqiu posts/interviews where original text is available; Stanford Q&A if transcript traceable | Public interview transcripts | Wiki/quote compilations | 重点测“懂生意”、用户导向、企业文化、不为清单；不要神化。 |
| Benjamin Graham | *Security Analysis*; *The Intelligent Investor* | Columbia value investing course materials | Book summaries | 重点测保守估值和安全边际；不要把 Graham 变成成长股叙事。 |
| Philip Fisher | *Common Stocks and Uncommon Profits* | Interviews and course materials | Book summaries | 重点测 scuttlebutt 和 15-point 质性研究。 |
| Peter Lynch | *One Up on Wall Street*; Fidelity-era public talks | Fidelity educational materials | Book summaries | 重点测分类、简单故事、增长和估值匹配。 |
| Howard Marks | Oaktree memos and books | Talks at GS and interviews | Media summaries | 重点测 second-level thinking、cycle、risk、asymmetry。 |
| Seth Klarman | *Margin of Safety*; Baupost letters if available to user | Public interviews | Book summaries | 重点测 capital preservation；注意他的材料很多是非公开或盗版，不要乱引用。 |
| Joel Greenblatt | *The Little Book That Beats the Market*; Magic Formula Investing site | Lectures/interviews | Strategy summaries | 重点测筛选不是结论，避免机械公式化。 |
| Ray Dalio | *Principles*; *Big Debt Crises*; official Principles site/videos | Bridgewater research where public | Media summaries | 重点测 regime、debt cycle、portfolio balance。 |
| George Soros | *The Alchemy of Finance*; public essays | Interviews | Summaries | 重点测 reflexivity 和 boom-bust feedback。 |
| Terry Smith | Fundsmith owner letters and reports; *Investing for Growth* | Fundsmith interviews | Media summaries | 重点测高质量复利、合理价格、低交易频率。 |

## 已确认公开来源入口

- Berkshire Hathaway annual reports and shareholder letters:
  https://www.berkshirehathaway.com/reports.html
- Berkshire Hathaway shareholder letters archive:
  https://www.berkshirehathaway.com/letters/letters.html
- Oaktree Howard Marks memos:
  https://www.oaktreecapital.com/insights
- Oaktree "The Best of..." memo collection:
  https://www.oaktreecapital.com/insights/memo/the-best-of
- Ray Dalio Principles:
  https://www.principles.com/principles/
- Fundsmith official site:
  https://www.fundsmith.com/
- Magic Formula Investing:
  https://www.magic-formula-investing.com/
- Li Lu public profile, UC San Diego:
  https://china.ucsd.edu/policy/china-forum/participants/li-lu.html
- Li Lu speech translation archive, Longriver:
  https://www.longriverinv.com/thought/the-practice-of-value-investing-by-li-lu
- Duan Yongping third-party navigation wiki:
  https://duanyongping.wiki/

## 测试集使用原则

- 如果测试的是来源忠实度，必须把具体来源片段放进 prompt。
- 如果测试的是案例应用，案例包必须自包含，不依赖 agent 自己搜索。
- 如果 agent 使用了未提供来源，必须标注为 external claim，并扣分。
- 如果 agent 给出直接引号但没有可核验来源，视为严重失败。

