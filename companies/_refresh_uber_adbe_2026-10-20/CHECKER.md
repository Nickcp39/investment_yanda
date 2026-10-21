# UBER + ADBE 刷新批次 2026-10-20 — 验收 (CHECKER, self-check)

⚠️ Runner 自检（PROTOCOL §3 Checker ≠ Runner 未满足）→ 两张卡 `clean=false`。两家 runner 都提议 STARTER（UBER 2%、ADBE 3%），按 2026-09-05 以来的规矩**一律以 WATCH 落锁**，升级前必须派独立 Checker。UBER 的特殊情况：09-28 版本经过独立 Checker（CONFIRM WITH FIXES），本版本把 6 条修正全部落实，但**修正后的版本本身没有经过第二次独立复核**。

## P0 基准
| 检查 | 状态 |
|---|---|
| `git fetch origin` + 比对 `companies/uber/`、`companies/adbe/` 远端目录 | ✔ 本地不落后远端；远端最新为 `uber/2026-09-28`、`adbe/2026-08-07`，与两张卡的 `refresh_of` 一致（INC-002） |

## P1 价格与新鲜度
| 检查 | 状态 |
|---|---|
| 价格双源（Yahoo + Nasdaq） | ✔ 2/2 差 0.00%（UBER $68.94、ADBE $256.73） |
| `verify_freshness.py` 在线独立回抓 | ✔ **2/2 PASS**，`refetched_yahoo` 等于卡片值 |
| T3 市值恒等式 / T4 距高点 / T5 单一价格 | ✔ 2/2 |
| T6 指引时效 | UBER ⚠ WARN（最新指引 2026-08-05 Q2，76 天；Q3 在 11-04，**仍是最新权威指引**）；ADBE ✔ 40 天 |
| 市值与 Nasdaq 的差异 | UBER 卡 $141.3B（摊薄 2,050.2M）vs Nasdaq $140.8B（0.4%）；ADBE $101.4B（摊薄 395M）vs $99.9B（1.5%），口径差写入 `delta_note` |

## P2 财务与事实的一手性
| 项 | 状态 |
|---|---|
| UBER 财务 | ✔ 无新季度；TTM 与 09-28 同（XBRL）；现金税、VIE 敞口、回购剩余授权来自 10-Q / 10-K 原文（本地检索） |
| UBER Delivery Hero | ✔ 条款 / 融资 / 分手费 / 长停日：8-K 07-16 EX-99.1；接受期与持股比例：Uber IR 新闻稿 08-27；定期贷款与过桥削减：8-K 08-07；票据：8-K 09-15。**二手**：DH 自身 2025 / 2026 财务（业绩报道）；DH 董事会推荐（Bloomberg） |
| UBER AV 承诺 | ✔ Lucid 2 万辆 + "现金需求未定"：10-K 原文；**二手**：Rivian $1.25B 条款（Reuters 转述）、Tesla / Waymo 车队与时间表、AV 高管离职（Bloomberg，未具名） |
| UBER 内部人 | ✔ Form 4 逐条解析（CEO / COO 9 月买入；10-16 全为 RSU 归属）；Aurora 减持：Form 4 + 13D/A |
| UBER CFO 变更 | ✔ 8-K 2026-02-04；"三年第三任"由 8-K 序列得出 |
| ADBE Q3 FY26 | ✔ 8-K EX-99.1 + 10-Q 原文（收入、利润、OCF、回购、ARR、RPO、股数、债务、采购义务） |
| ADBE 净新增 ARR −36% | ⚠ **推算 + 电话会分析师口径**（公司不披露；管理层未否认）—— 这是本卡最重要的单一数字，也是最弱的一手性 |
| ADBE CEO 任命 | ✔ 8-K 09-08 EX-99.1；Wadhwani 离开：电话会逐字稿（Motley Fool，二手） |
| ADBE 内部人 | ✔ Form 4（Narayen 9/16 公开市场卖出 74,500 股；10/15 全员 RSU）；**10b5-1 计划状态未核** |
| ADBE 竞争 | 二手：Figma 新闻稿转述、Canva 高管访谈 / SaaStr |
| 操作者履历 | `unsourced_background`（Khosrowshahi、Narayen、Chakravarthy 早年经历未逐条核） |

## P3 估值一致性
| 检查 | 状态 |
|---|---|
| 与库同一公式 | ✔ `valuation_model.py` 复制自交易通道批次，只换输入；新增 `extra_cf` 叠加层（默认全 0，对 ADBE 无影响） |
| UBER OE₀ 与 09-28 Checker 盲估对账 | ✔ 本卡 $5.9B = Checker $5.9B；base IRR 本卡 +8.9%（含 DH）vs Checker +8.5–10.1%（含 DH 敏感性）—— 在区间内 |
| ADBE 08-07 → 本卡 | ✔ OE₀ 8.20 → 8.52（TTM 滚一季）；buy_below $306 → $306.17（公式换了但 12% 锚几乎不动，说明两套公式在 ADBE 的参数下一致） |
| 卡片数字只读 JSON | ✔ `make_cards.py`；md 内价格字符串经 T5 校验 |

## P4 本批已知弱点（交给独立 Checker 时重点看）
1. **UBER DH 叠加层的 $11.1B 是粗估**：未扣 TRS 实物交割、未计 Blacklane、未计交割前利息；交割时点（第 2 年）若推迟到 2028，base IRR 会略升。叠加层对 base 的影响是 −0.6pt（+9.5% → +8.9%），方向明确、量级小。
2. **UBER 税盾摊回 +$0.4B 是 runner 的判断**：若按 Checker 的严格口径不摊回，OE₀ $5.5B → base 约 +8.0%，刚好在线上。**这一项决定 UBER 是"过线"还是"压线"。**
3. **ADBE harvest 情景的 p=0.9**：若公司在收割期把回购降到 FCF 的 60%，harvest IRR 会低于 8%。
4. **ADBE 净新增 ARR 是推算**：Semrush 的 ARR 贡献（约 $0.48B）来自 Q2 披露，Q3 有机 / 无机拆分没有一手。
5. **两家的操作者评级都带主观**：UBER 3/5（财务型 CEO 做大并购 + 关键岗位流失），ADBE 22/40（销售型新 CEO + 创意负责人离开）—— 独立 Checker 可能给出不同分数。

## P5 裁决处理
| 公司 | runner 提议 | 落锁 | 理由 |
|---|---|---|---|
| UBER | STARTER 2% | **WATCH 0%** | Checker ≠ Runner 未满足；垫子 0.9pt；11-04 / 11-05 两个事件在两周内 |
| ADBE | STARTER 3% | **WATCH 0%** | Checker ≠ Runner 未满足；K-I 要到 12 月中才能判 |
