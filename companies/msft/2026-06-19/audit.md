# MSFT Audit (Stage 7 · 质量门)

最后更新: 2026-06-19 · 审计本轮 cold-start dossier 的完整度、内部一致性、verdict 封顶

## 1. 完整度评估

| 维度 | 状态 | 说明 |
|---|---|---|
| 一手证据底座 | 强 | 10 年审计序列(SEC XBRL)+ Q3 FY26 官方 IR;~30 条 claim 入 ledger,载荷性数字基本回挂 A1 |
| 财务模型 | 中强 | 10 年史 + owner earnings 桥 + 三情景 IRR + 价格带,算术勾稽;但 OE 区间宽($73–125B),取决于 capex 拆分(不可观测) |
| 8 分析模块 | 齐全 | business/value_chain/moat/bottleneck/operator/inversion/financial_quality/valuation 全部存在 |
| 缺口 | 见下 | OpenAI 经济学(O3)、capex 维护/成长拆分(O2)、分部利润率(O4)、8-K 2026-06 内容(O5)未一手提取 |

**完整度估计:~65%**(GOOGL pilot 用整天到 ~75%;本轮 cold-start 一遍 ~65% 合理)。

## 2. 硬规则封顶检查
- "缺模块封顶":8 模块齐全 → **不触发**。
- "来源不足封顶 INFO-GAP/WATCH":载荷性数字回挂 A1,但存在 3 个**重大信息缺口(O2/O3/O4)**,其中 OpenAI 经济学(O3)直接影响 Azure 增长可持续性判断。
- **verdict 上限 = 完整度**:~65% → 落在 **60–80 = STARTER 区间**(铁律2)。**不可上 CORE**(需 >80% 完整度 + 缺口补强)。

## 3. ceiling 来源(与 GOOGL 案的关键不同)
- GOOGL 案:ceiling=WATCH,来源是**价格无安全边际**(实质发现)。
- **MSFT 案:ceiling=STARTER,来源是完整度(~65%)+ 信息缺口(OpenAI/capex 拆分)**,**不是**价格 —— 因为估值端 MSFT 有正安全边际(base 8% 公允价 ~$436 > 现价 $379)。
- 即:GOOGL 是"好公司错价格"(价格封顶);**MSFT 是"好公司对价格,但研究未做完"(完整度封顶)**。补强 O2/O3/O4 后可上修讨论 CORE。

## 4. 内部一致性检查
- ✅ 各模块信号与 facts 一致;capex 两个口径($190B 含租赁 / $107B 自有 PP&E)在 facts C#1、raw Block3、financial_quality §2 一致登记,FCF 一律用 $107B 口径。
- ✅ 估值用 7.428B 股 + $379.40,市值 $2.82T 全文一致。
- ✅ 无 stale 文件声称不同状态(cold-start,无旧版本)。

## 5. 给 IC 的质询点(panel 须正面回应)
1. **OpenAI 黑箱(最硬)**:Azure +40% 含多少 OpenAI 算力贡献?关系/经济学未一手验证(O3)——这是 thesis 的隐藏依赖,STARTER 而非 CORE 的核心原因之一。
2. **capex ROI 框架缺失**:$190B 量级投入无管理层披露的 ROIC 门槛(O2/O4),与 GOOGL 同病。
3. **OE 区间宽($73–125B)**:base $112B 是 ~40% capex 为成长的假设,非证据。
4. **价格有 MOS 但完整度封顶**:估值支持 STARTER+,但研究缺口(O2/O3)按铁律2 把 verdict 封在 STARTER,不可 CORE。
5. **FY26 capex 指引来自电话会(B2)**未拿官方 transcript 逐字(O1)。

## 6. 完整度结论
**~65% · ceiling = STARTER(完整度+信息缺口封顶,非价格)· 价格端有正安全边际。** 上修 CORE 的路径:补 OpenAI 经济学 + capex 维护/成长拆分 + 分部利润率,使 OE 区间收敛、Azure 增长可持续性可独立验证。
