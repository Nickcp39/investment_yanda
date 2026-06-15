# Buffett Research Checklist

创建: 2026-06-15

用途: 公司研究进入 memo 前，必须用这份清单做一次 business-owner 检查。它不是“像巴菲特说话”，而是把长期股权研究中最硬的几个问题问清楚。

---

## 0. Core Question

如果股市明天关门十年，我是否愿意按今天这个价格拥有这家公司的一部分？

如果答案依赖“下个月会涨”“市场会重新评级”“别人也在买”，则不通过 Buffett lens。

---

## 1. 十年视角

必须回答:

- 这家公司十年后大概率还在做同一门好生意吗？
- 十年前、五年前、今天，收入结构和利润池是否一致？变化是增强还是削弱 moat？
- 十年收入、毛利率、营业利润率、FCF、ROIC、股本数、债务、回购、capex 如何变化？
- 过去一次逆风期，公司是保持定价权、现金流和客户关系，还是靠融资/叙事撑过去？
- 管理层过去十年的 capital allocation 是加分还是扣分？

最低资料:

- 10 年 10-K/年报数字时间序列，或 since IPO。
- 最近 4 季 call transcript。
- 最近 10-K/10-Q 的业务、风险、MD&A。
- proxy/股东信/回购并购历史。

---

## 2. 生意是否足够好

必须回答:

- 客户为什么付钱？这个价值是否会持续？
- 护城河来自哪里: 品牌、网络效应、成本优势、规模经济、监管、分销、数据、习惯、生态锁定？
- 护城河的具体机制是什么？证据指标是什么？攻击路径是什么？
- 毛利率和 ROIC 是结构性优势，还是周期/会计/一次性因素？
- 增长是否需要越来越多资本？如果增长吃掉 owner earnings，不算好生意。
- 这门生意是否在能力圈内，能否用两句话讲清楚赚钱机制？

红灯:

- 只看 TAM，不看实际 monetization。
- 只看 revenue growth，不看 incremental ROIC。
- 护城河解释依赖模糊词，比如“生态”“AI”“平台”，但没有可验证指标。

护城河细节按 [moat_technical_analysis.md](../moat_technical_analysis.md) 处理。任何 memo 里出现“有护城河”，都必须同时给出:

- moat type
- mechanism
- evidence
- attack surface
- durability test
- monitor metric

---

## 3. Owner Earnings

必须回答:

- 会计利润到 owner earnings 的桥是什么？
- 维护性 capex 和成长性 capex 能否分开？
- SBC、重组、一次性收益、资本化费用、递延收入、折旧摊销是否扭曲利润？
- 如果停止发股/发债/并购，公司是否仍能自我融资增长？
- 十年累计 FCF 有多少真正回到股东手里，多少被 capex、并购、SBC 稀释吃掉？

建议表:

| Year | Revenue | Operating income | Net income | OCF | Capex | FCF | SBC | Buyback | Shares | Debt | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|

---

## 4. 价格是否足够便宜

必须回答:

- 当前价格隐含了什么增长、利润率和 terminal multiple？
- 保守情景、基准情景、乐观情景下，10 年 IRR 分别是多少？
- 如果估值倍数回到历史中位或行业合理区间，回报是否仍可接受？
- 好公司是否已经贵到没有 margin of safety？
- 如果今天买入后估值压缩 30%-50%，基本面能否弥补？

标准输出:

```text
Current price:
Market cap / EV:
Owner earnings yield:
Base-case 10y IRR:
Downside-case 10y IRR:
Required buy price for margin of safety:
Verdict at current price:
```

---

## 5. 安全边际

安全边际不是“这个公司很好”，而是:

- 保守估值明显高于价格。
- 或者 business quality 极高、可预测性极强，即使低增长也不容易永久亏损。
- 或者资产/现金流/资本结构能保护下行。

必须回答:

- 需要多大折扣才足够？20%、30%、40%？
- 下行情景中永久亏损来自哪里？
- 现金、债务、到期结构、回购、稀释是否提供保护还是增加风险？
- 如果未来三年没有增长，今天价格是否仍合理？

结论上限:

- 没有安全边际: 最高 `WATCH`。
- 安全边际来自乐观假设: 最高 `WATCH`。
- 安全边际来自保守现金流/资产/极强护城河: 可以讨论 `STARTER`。

---

## 6. 风险与死亡路径

必须写至少 5 条:

| Risk | Mechanism | Evidence | Early warning | Severity |
|---|---|---|---|---|

至少覆盖:

- 需求风险
- 竞争风险
- 技术替代风险
- 监管/反垄断风险
- 资本配置风险
- 财务杠杆/稀释风险
- 管理层/文化风险
- 估值风险

---

## 7. 技术颠覆检查

这个模块对 Google、Apple、Microsoft、NVIDIA、支付、广告、云、医疗科技尤其重要。

必须回答:

- 有没有新技术降低客户 switching cost？
- 有没有新技术让现有产品的边际成本/定价权下降？
- 有没有新入口绕过公司原有分发渠道？
- 现有公司是被颠覆者，还是能用资金、数据、分销、生态把新技术吸收进来？
- 新技术提升 owner earnings，还是只是迫使公司用更高 capex 保住旧利润？
- 技术路线是否可能换轨，导致现有资产/能力过时？

输出:

| Technology shift | Threatens what | Helps what | Evidence | Net effect | Watch item |
|---|---|---|---|---|---|

---

## 8. Capital Allocation

必须回答:

- 管理层过去十年是买回便宜股票，还是高价回购？
- 并购是否创造价值？
- 是否为了增长牺牲 ROIC？
- SBC 是否实质上把利润转给员工、再用回购掩盖稀释？
- 管理层是否在好年份保守、坏年份有弹药？

---

## 9. Verdict

Buffett lens 的输出不应该是长篇散文，而是:

```text
Business quality: poor / average / good / exceptional
Predictability: low / medium / high
Owner earnings quality: poor / average / good
Technology disruption risk: low / medium / high / unknown
Management/capital allocation: poor / average / good
Balance sheet risk: low / medium / high
Margin of safety: none / thin / adequate / large
Verdict: REJECT / INFO-GAP / WATCH / STARTER / CORE
Max price for STARTER:
Max price for CORE:
Top 3 kill criteria:
```

---

## 10. Google-Specific Prompts

用于 Alphabet/Google:

- Search 广告十年后是否仍是高 ROIC 生意，还是 AI answer interface 降低广告 load？
- YouTube 的用户时间和广告/订阅 monetization 是否能对冲 Search 风险？
- Cloud 的高增长和 margin 改善是否是真正的平台质量，还是 capex 周期里的暂时结果？
- TPU、数据中心、电力、AI capex 是护城河，还是 owner earnings 的消耗？
- 反垄断、默认搜索分销、Chrome/Android、广告市场结构的监管风险是否可量化？
- Berkshire 买入时的隐含价格和交易结构是否提供安全边际，还是只是优质资产补票？
