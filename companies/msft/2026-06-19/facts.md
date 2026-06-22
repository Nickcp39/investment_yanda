# MSFT Facts

最后更新: 2026-06-19 (cold-start; as_of=2026-06-19)
来源纪律: `../../../sources/source_policy.md`。仅 A1/A2 一手或明确标注 derived 的进 EVIDENCE;社媒/commentary 只进 SENTIMENT/OPEN。

---

## EVIDENCE (A1/A2 一手已验证)

### 价格 / 市值
- E1. 最新收盘 **$379.40**(2026-06-18,Yahoo chart API)[MSFT.A1.PRICE.001]
- E2. 52 周高 **$555.45** / 52 周低 **$356.28** → 现价**距高点 −31.7%,距低点 +6.5%**(near 52w low)[MSFT.A1.PRICE.002/.003]
- E3. 流通股 ~**7.428B**(2026-04-23 dei cover)[MSFT.A1.SHARES.001]
- E4. (derived) 市值 ~**$2.82T**;P/E(TTM)~**22.5×**;P/FCF(TTM)~**38.7×**;**TTM 收益率 ~4.44%**,FCF 收益率 ~2.59% [MSFT.DERIVED.*]

### 损益 / 现金流(FY25 + 最新季)
- E5. FY25 营收 **$281.7B**、营业利润 **$128.5B(45.6% 营业利润率)**、净利 **$101.8B** [MSFT.A1.*.FY25]
- E6. FY25 OCF **$136.2B**、capex **$64.6B**(FY23 $28.1B→FY24 $44.5B→FY25 $64.6B)、FCF **~$71.6B** [MSFT.A1.OCF/CAPEX.FY25]
- E7. FY25 buyback **$18.4B**(FY22 峰值 $32.7B 回落)、dividend **$24.1B**(单调上升,连续 20+ 年增派)[MSFT.A1.BUYBACK/DIV.FY25]
- E8. Q3 FY26(end 2026-03-31)营收 **$82.9B(+18%)**、营业利润 **$38.4B(+20%,46.3% margin)**、净利 **$31.8B(+23%)**、EPS **$4.27(+23%)** [MSFT.A1.*.Q3FY26]
- E9. 9mFY26 营收 **$241.8B(+17.8% YoY)**、OCF **$127.5B**、capex(PP&E)**$80.1B** [MSFT.A1.*.9MFY26]

### 分部 / 云 / AI
- E10. Q3 FY26 分部:Productivity & Business Processes **$35.0B(+17%)** · Intelligent Cloud **$34.7B(+30%)** · More Personal Computing **$13.2B(−1%)** [MSFT.A1.SEG.*]
- E11. **Azure +40% YoY(+39% cc)**,超 37–38% 指引,逆转此前多季减速 [MSFT.A1.AZURE.Q3FY26]
- E12. **Microsoft Cloud 营收 $54.5B(+29%)**,单季首破 $50B [MSFT.A1.MSCLOUD.Q3FY26]
- E13. **Commercial RPO $627B,+99% YoY**(已签约未确认订单)[MSFT.A1.RPO.Q3FY26]
- E14. **AI 业务年化 run-rate >$37B,+123% YoY** [MSFT.A2.AIRR.Q3FY26]

### 资产负债表 / 治理
- E15. 现金+短期投资 **$78.3B**、长期债务 **$31.4B**(下降中)、股东权益 **$414.4B**;**净现金 ~$47B** [MSFT.A1.*.Q3FY26]
- E16. **一股一票,无双层股权,无创始人投票控制**(治理标准化)[MSFT.A1.GOV.VOTE]
- E17. CEO Nadella(2014 起 + 2021 起董事长)FY25 薪酬 ~$96.5M,~90% 股权挂钩 [MSFT.A1.CEO.COMP.FY25]

---

## INTERPRETATION (derived / 判断,带依据)

- I1. **质量记分卡满分级**:45.6% 营业利润率 + 净现金 + 三引擎(M365/Azure/AI)同向增长 + RPO $627B → 生意质量 = `exceptional`,非仅 good。
- I2. **现价是"capex 冲击后的二次定价",非高位追涨**:股价从 $555 跌到 $379(−32%),市场已把 FY26 ~$190B capex 指引(+61%)的惊吓打进价格。TTM 收益率 4.44% vs GOOGL 1.45% — **同因子(AI capex)但起始收益率档次高一截**。
- I2b. capex 口径必须分清:电话会 $190B 含**融资租赁产能**;现金流量表自有 PP&E 9mo $80.1B(年化 ~$107B)。FCF 用 $107B 口径算,$190B 是承诺产能不是现金支出。
- I3. **owner earnings 与报表净利的缺口比 GOOGL 小**:MSFT TTM 净利 $125.2B、FCF $72.9B,差额主要是 capex(可观测),不像 GOOGL 含大额不可重复股权收益。报表利润质量更高。
- I4. **binding constraint = capex 回报兑现 + AI 折旧周期**:$190B 量级投入若 ROIC 达不到,FCF 会被长期压制;但 RPO $627B(+99%)+ Azure 重新加速 +40% + AI run-rate +123% 提供了"需求是真的"的早期证据 — 这是 MSFT 与纯 capex 黑洞的关键区别。
- I5. **下行保护强于多数 Mega7**:净现金 + 持续 dividend + 三引擎分散(若 AI 慢,M365/Azure 基本盘仍在)+ 一股一票(出错有纠错杠杆)。

---

## SENTIMENT (D1/C2 仅情绪,不支撑 thesis)

- S1. 媒体叙事:Q3 "Azure 重回 40%" 被视作 AI 需求确认;但 $190B capex 指引引发"capex 见顶担忧",股价当日下跌(coindcx / CNBC commentary)。仅情绪,数字已回 A1 校验。

---

## OPEN (待补 / 未验证)

- O1. **FY26 capex 指引 ~$190B 与 ~$25B 组件涨价拆分**:来自电话会(B2 commentary),**未拿到官方 transcript 逐字**。属 OPEN,不进 BUY 直接支撑。
- O2. **维护 vs 成长 capex 拆分 / AI 资产折旧年限假设**:与 GOOGL 同一不可观测变量;10-Q/10-K 段注本轮未逐字提取。这是 owner earnings 收敛与 binding constraint 的核心,标 monitoring。
- O3. **OpenAI 关系经济学**:MSFT 与 OpenAI 的股权/算力/收入分成安排、对 Azure 增长贡献的拆分、近期重组后的口径 — 未在本轮一手提取,影响 Azure 增长的可持续性判断。OPEN,重大。
- O4. **分部营业利润率拆分**(各 segment operating income)未本轮提取;只有合并 op margin 46.3%。
- O5. **MSFT-8K-2026-06(event 2026-06-02)具体 item** 未读;可能含债务/治理/重大事项,需核。
- O6. **回购授权剩余额度 + FY26 全年 buyback 节奏** 未提取。
- O7. 10 年完整序列里 FY16/FY17 的 OCF/capex 未拉(只拉到 FY18 起);不影响近 8 年趋势判断。

---

## Contradictions / 口径冲突登记

- C#1. **capex 两个口径**:电话会 $190B(含租赁产能)vs 现金流量表 9mo PP&E $80.1B(年化 ~$107B)。两者皆真,destination 分别为 OPEN(指引)/ EVIDENCE(现金支出)。FCF 计算一律用 $107B 口径。
- C#2. Azure +40% 来自官方 IR press release(A1);AI run-rate $37B 同为官方 IR(A1);二者非二手。但"逆转减速趋势"的归因属解读(I 区)。
