# GOOGL Research Status — as_of 2026-08-28

最后更新: 2026-08-28（价格 + 资金结构重定价 refresh）

真实状态标签: **DECISION_DRAFT**（不是 COMPLETE）· completeness ~72%

Decision question:
Alphabet 是否仍是十年后值得拥有的高质量生意？$340.65 是否有安全边际？
7/28 之后的发债行为与伯克希尔 13F 如何改变裁决？（答：都不改变。）

---

## 这一轮做了什么（focused refresh，非从零重研究）

| 项 | 状态 |
|---|---|
| M2/M3 thesis-breaking 复核 | ✅ 无破坏性事件；伯克希尔 +83% 加仓反向强化"好生意" |
| M4 资金结构增量 | ✅ 8/10 $25B 发债 8-K 入库（raw/block13 + claim_ledger_addendum） |
| M5 kill_criteria 复核 | ✅ K-B 强化、K-C 边际恶化、K-D 无新裁决（检索日志） |
| M6 重算 IRR @ $340.65 | ✅ `valuation.md`；**模型独立复现验证通过**（7/24 csv 逐位一致） |
| 两轴裁决 | ✅ new_money=WATCH / existing=HOLD / 0% |
| 价格双源交叉验证 | ✅ Yahoo $340.65 + Nasdaq $340.65（delta 0.0%） |
| freshness 机械门 | 见 `freshness.json` / `freshness_check.json` |

## Final Verdict 摘要
**WATCH · 0% 仓位 · HOLD · 好生意，价格仍不要，杠杆还更重了。**
- $340.65 三情景 10y IRR：bear −12.0% / base −1.7% / **bull +7.4%**——全部 <8%。
- mktcap/TTM FCF 78.2x，比 7/28（76.6x）更贵。
- buy-below ~$117 不变；avoid above ~$322，现价在其上 $18+。
- 新变量：伯克希尔 Q2 加仓 +83%（13F A1 源）——承保生意与低价格带，不承保 $340。

**解除 WATCH / 上修路径**：① 价格回 ~$99–117 重开 IC 讨论 starter（届时伯克希尔 Q2
行为是最有力一票）；或 ② capex 见顶 + FCF/share 回升 + ROI 框架出现。

## 完整度封顶（~72%，未到 COMPLETE 的原因）
- O1 维护 vs 成长 capex 拆分仍未披露。
- O2 capex ROI 门槛第三个周期未给。
- O3 Cloud 35.5% 利润率可持续性（Q3 第三方算力桥接）未验。
- O4 DOJ adtech 最终救济形态未定（窗口内无裁决，检索日志）。
- O5 利率路径 vs 新 30/40 年债（6.375%/6.5% 档）双重敏感。
- O6 完整 owner-earnings 桥/十年逐年序列待 Q3 数据重建。

> 措辞纪律：本 dossier 为 **DECISION_DRAFT**，非"完成/彻底跑完"。verdict 由**价格**
> 封顶 WATCH；完整度 ~72%（<80%）另将新钱 ceiling 封在 STARTER，价格封得更低。

## Next Review
- Q3-2026 财报（~10 月下旬）：capex 是否见顶、FCF/share、Cloud 利润率 30%+、Search 增速。
- 事件触发：DOJ adtech 救济裁决、数据中心/TPU 减值（→ K-C 升 🔴）、FOMC 利率路径。
- 价格触发：~$139 进观察、~$117 重开 panel、~$250–280（regime 轮动）提前重开。
