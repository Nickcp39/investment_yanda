# Source Policy

创建: 2026-06-15

这份文件定义所有公司、行业、主题、投资人框架研究的来源分级。原则很简单:
**没有可追溯来源的结论，不进入 thesis；社交媒体只能生成线索，不能直接证明线索。**

---

## Source Tiers

| Tier | 名称 | 典型来源 | 可否支撑 thesis |
|---|---|---|---|
| A1 | 官方一手披露 | SEC/交易所文件、年报、季报、8-K、招股书、proxy、公司 IR、监管公告、法院/专利/标准文件 | 可以 |
| A2 | 一手经营/技术证据 | 官方电话会 transcript、公司公告、客户/供应商公告、项目备案、政府采购、临床/认证数据库、行业协会原始数据 | 可以 |
| B1 | 高质量二手事实报道 | Reuters、Bloomberg、WSJ、FT、财新、财联社等有采编责任的媒体 | 可以辅助，关键数字需回溯到 A |
| B2 | 专业解读/行业研究 | Sell-side、产业研究机构、咨询报告、专业媒体、专家访谈整理 | 只作解读；引用时应回到 A/B1 事实 |
| C1 | 方法/工具/开源仓库 | GitHub skill、agent 项目、方法论文章、公开 prompt、第三方资料整理 | 只能启发流程或生成检查清单 |
| C2 | 市场评论 | 博客、公众号、YouTube、播客、雪球长帖、Substack | 只能作为 signal，不能单独支撑结论 |
| D1 | 社交媒体/社区情绪 | X、小红书、Reddit、股吧、Discord、微信群转述 | 只能作为 lead generation 或 sentiment |
| E1 | AI 输出/模型估计 | LLM 总结、自动打分、未审计 scrape、无法复核的估算 | 不可作事实；只能标为 estimate/scenario |

---

## Decay Class（决期分级）— 与 tier 正交（2026-06-21 新增，lean-6module-v1.1）

来源 **tier**(A1–E1)衡量**可信度**；**decay class** 衡量**时效**。二者**正交**——一个高 tier 的一手来源,其描述的状态仍可能快速过期。

| Decay | 含义 | 字段 | 复核要求 |
|---|---|---|---|
| **LIVE** | 快衰减,每次跑必须当 as_of 重新取并交叉验证 | 股价、市值、52 周高/低、流通股；**LIVE-定性**:出口管制/监管状态、在审诉讼、guidance、analyst consensus | 进 `freshness.json`,≥2 独立源,过 `scripts/verify_freshness.py`(机械) |
| **FILED** | 慢衰减,锚定带日期的归档即可 | 10-K/10-Q/8-K 行项:营收、利润、毛利、资产负债表、capex、回购授权、股息 | 一手来源 + `public_date ≤ as_of`(现有 claim_ledger 纪律) |

> **关键陷阱(INC-001)**: NVDA 的 China 出口管制是 **A2 一手** 却是 **LIVE**——"永久损失"措辞过期了(2026-02 H200 许可已重发)。价格是 **B1** 也是 **LIVE**——单源+只验日期漏掉了 45% 错价。**"一手来源" ≠ "无需刷新"。tier 高不代表不会过期。**

---

## Hard Rules

1. 每个关键 claim 必须有 `source_id`、URL/path、日期、tier、原文摘录或 close paraphrase。
2. 每个数字必须记录 `value`、`unit`、`as_of`、`source_id`；冲突数字全部入库，不提前择优。
3. A1/A2 是事实锚点；B/C/D 只能帮助发现问题、构建假设、理解共识。
4. D1 社交媒体不能进入 EVIDENCE 区，只能进 SENTIMENT 或 OPEN QUESTIONS。
5. E1 AI 输出不能作为来源；AI 只能帮助整理、提取、建模、提出待验证问题。
6. 任何 quote 都必须能回到原文或可靠 transcript；不能凭记忆补引号。
7. 如果来源不足，结论上限是 `INFO-GAP` 或 `WATCH`，不能给 `STARTER` / `CORE`。
8. **LIVE 数据(见 Decay Class)必须经 `scripts/verify_freshness.py` 机械交叉验证(≥2 独立源)方可进入 `decision_card`。date-only 检查不足;无 passing `freshness_check.json` 的 run = void/non-comparable(同版本戳缺失)。**

---

## Claim Ledger Fields

用于 `sources.csv`、`claim_ledger.csv` 或 facts.md 的最小字段:

| 字段 | 说明 |
|---|---|
| source_id | 稳定 ID，如 `GOOG.A1.2026Q1.001` |
| claim | 一句话事实或信号 |
| value | 如果是数字，填数字 |
| unit | USD、shares、%、MW、days 等 |
| as_of | 事实对应日期，不是抓取日期 |
| retrieved_at | 抓取/阅读日期 |
| source_type | A1/A2/B1/B2/C1/C2/D1/E1 |
| source_url_or_path | URL 或本地路径 |
| original_excerpt | 短摘录或 close paraphrase |
| reliability_note | 冲突、估算、口径差异、是否二手 |
| destination | EVIDENCE / INTERPRETATION / SENTIMENT / OPEN_QUESTION |

