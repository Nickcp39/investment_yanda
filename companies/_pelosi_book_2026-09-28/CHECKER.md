# 佩洛西持仓批次 2026-09-28 — 验收 (CHECKER)

规则：每项必须可机器或人工复核。"感觉完成"不算。
**⚠️ 角色声明：本 CHECKER 由 Runner 本人执行（self-check）。PROTOCOL §3 的 Checker ≠ Runner 未满足** ——
机械层（`verify_freshness.py` 独立回抓 + T1–T6、IRR 独立复算）是真独立的；判断层（信号打分、情景假设、裁决）**不是**。
因此：全部卡 `clean=false`；runner 提议 STARTER 的三张卡**以 WATCH 落锁**。

## P0 基准新鲜度（INC-002 / A0）
| # | 检查项 | 状态 |
|---|---|---|
| 0.1 | 开跑前 `git fetch` + 比对 | ✔ 落后 4 个提交（仅 studies/），已 `pull --ff-only` |
| 0.2 | 8 个 ticker 路径在远端不存在 | ✔ 8/8 首次建档，`refresh_of = null` |

## P1 价格与新鲜度（v1.1 硬门）
| # | 检查项 | 标准 | 状态 |
|---|---|---|---|
| 1.1 | 价格双源 | ≥2 独立源，差 <1% | ✔ Yahoo chart + Nasdaq historical，**8/8 差 0.00%** |
| 1.2 | 独立回抓 | `verify_freshness.py` 在线回抓 last close ≤ as_of | ✔ **8/8 PASS（exit 0）**，回抓值 = 卡片值 |
| 1.3 | 市值双源 | derived vs Nasdaq summary | ✔ 差 0.0–1.5%（INTC 3.4%：Nasdaq 用增发前股数，已注明） |
| 1.4 | 52 周高低双源 | Yahoo meta vs Nasdaq | ✔ 高点 8/8 一致；低点 BE/INTC 因窗口起点差 >1%，已加 `delta_note` |
| 1.5 | T2 贴近高/低点 | 触发须有机械理由 | ✔ 仅 AB 触发（+2.4% 距低点），已用独立回抓证明为真实收盘 |
| 1.6 | T4 距高点叙述 | 与卡片隐含值差 ≤1pt | ✔ 8/8 gap 0.0pt |
| 1.7 | T5 单一真值 | as_of_price 出现在所有带价文件 | ✔ 8/8 |
| 1.8 | T6 定性新鲜度 | 指引来源 ≤45 天 | ⚠ **4/8 WARN**：BE 62 天、INTC 67 天、UBER 54 天、VST 52 天 —— 下一次财报均在 10 月底–11 月初，**当前已是最新权威事件** |
| 1.9 | 股数口径 | 注明来源 | ✔ 见各 `freshness.json` note；INTC 用 424B5 增发后股数（含绿鞋假设） |

## P2 财务一手性
| # | 检查项 | 状态 |
|---|---|---|
| 2.1 | TTM 来自 SEC XBRL | ✔ 7/8；**BE 的 Q2 未进 companyfacts**，Q2 数字取自 8-K，TTM 为推算（已标注）；AB Holding 用分配口径 |
| 2.2 | 最新季度 headline 来自公司原文 | ✔ 8/8 8-K EX-99.1 原文存于各 `raw/` |
| 2.3 | 一次性项目识别 | ✔ INTC 托管股重估 −$12.53B；UBER 股权重估 +$1.6B；VST 未实现对冲损失 −$472M；AVGO/CRWD/PANW 用 FCF−SBC 回避 |
| 2.4 | SBC 扣除（库规：SBC 是真实股东成本） | ✔ 8/8；AB 以分配为 OE（SBC 已在 AB LP 层费用中） |
| 2.5 | 深度一手（仅价格友好者） | ✔ UBER：10-Q + Form 4；AB：10-Q + qualified notice；VST：10-Q 本地全文检索 |

## P3 估值一致性
| # | 检查项 | 状态 |
|---|---|---|
| 3.1 | 8 家同一公式 | ✔ `valuation_model.py`，三种 OE 路径同一 IRR/门槛价函数 |
| 3.2 | 与库口径的差异已声明 | ✔ PLAN §4 + 每张卡并列"库口径 IRR" |
| 3.3 | **IRR 独立复算**（不同实现：多项式求根） | ✔ AB 13.09% / UBER 12.83% / VST 10.37% / AVGO 2.54%，与模型差 <0.01pp |
| 3.4 | 卡片 JSON 数字只来自模型输出 | ✔ `make_cards.py` 读取 `data/valuation_*.json`，不手抄 |
| 3.5 | 敏感性数字为实算 | ✔ UBER、VST 的敏感性表均由模型函数计算 |
| 3.6 | 不跨名排名"距 buy_below %" | ✔ synthesis 明示 |

## P4 裁决完整性
| # | 检查项 | 状态 |
|---|---|---|
| 4.1 | 每家有 facts + 5 个模块文件 + valuation + decision_card.md/.json + freshness 两件 | ✔ 8/8 |
| 4.2 | verdict 上限 = 完整度 | ✔ 三张 STARTER 提议卡完整度 62–65%（>60 允许 STARTER）；其余 55–60% |
| 4.3 | 价格先于完整度封顶 | ✔ 5 张价格封顶卡注明"补完整度不改变裁决" |
| 4.4 | kill criteria 红/黄/绿 | ✔ 8/8 |
| 4.5 | 单因子检查 | ✔ 8/8 写入组合层一节 |
| 4.6 | 持有载体检查（用户 2028 年非居民路径） | ✔ AB 专门建模（税后 IRR +10.4%）；UBER/VST 注明摩擦小；佩洛西的 LEAPS 形式在 5 张卡中标注"本库不允许" |

## P5 已知未闭合项（诚实清单）
| 名字 | 未闭合 |
|---|---|
| UBER | AV >$10B 计划无一手量化（O-U1）；Waymo 合同条款（O-U2） |
| AB | 私募信贷 AUM 占比（O-AB1）；**用户专属 PTP 税务需 CPA（O-AB3）**；Q3/Q4'25 分配经检索摘要读取 |
| VST | 2027–28 对冲价格水平（O-V1）；9 月次级票据用途（O-V3） |
| AVGO | 客户集中度未披露（O-A1） |
| BE | Q2 未进 XBRL；积压订单无一手数字；做空报告指控未独立核实 |
| INTC | 托管 1.43 亿股是否已计入股数（O-I1） |
| CRWD / PANW | GRR/NRR、有机 vs 并购 ARR 拆分 |
| 全批 | 操作者生平均为 `unsourced_background`；**佩洛西交易数据全部为 secondary（众议院 PTR 原件未取）** |

## P6 结论标签
**`DECISION_DRAFT (self-checked)`** —— 机械层 CLEAN，判断层未经独立审查。
**解锁三张 STARTER 提议卡的唯一动作：一个与 Runner 隔离的 Checker 过一遍 P3/P4 的判断项**（尤其 UBER 的 g、AB 的 D₀ 与退出倍数、VST 的 OE₀）。
