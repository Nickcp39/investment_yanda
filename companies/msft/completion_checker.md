# MSFT Completion Checker（公司级 A–F gate）

最后更新: 2026-06-19 · 依据 `frameworks/research_completion_checker.md`

## 状态标签: `DECISION_DRAFT`（completeness ~65%）— **非 COMPLETE**

## A. Scope And Definition
- [x] 范围冻结:MSFT,普通股(一股一票,无 share class 区分),as_of 2026-06-19,决策=新钱是否建仓 + 仓位,horizon 10yr。
- [x] 完成标准在最终答案前写明(本文件 + research_status)。
- [x] 状态标签不 stale(cold-start,无旧版本)。

## B. Evidence Engineering
- [x] source_register 含 memo/model 用到的每个来源。
- [~] raw 摘录:财务序列 + Q3 IR 已存;**10-K/10-Q 全文段注未逐字提取**(用 XBRL 聚合 + IR 替代)。
- [x] claim_ledger 含 tier/验证状态/source_id。
- [x] facts 仅从已验证或明确标 derived 的 claim 更新;社媒进 SENTIMENT。
- [x] memo 无裸 claim(均挂 source_id 或标 OPEN)。
- [x] 无旧版 stale claim(cold-start)。

## C. Ten-Layer Research
- [x] 1 方向 · [x] 2 生意/质量门 · [x] 3 证据 · [x] 4 会计趋势 · [x] 5 价值链 · [x] 6 护城河/瓶颈 · [x] 7 operator · [x] 8 反演 · [x] 9 估值/MOS · [x] 10 决策/监控
  - 注:5/8/9 层存在但深度受 O2/O3/O4 缺口限制。

## D. Model And Math
- [x] 收入驱动(分部 + Azure/AI)挂证据。
- [~] 费用/capex 模型:capex 序列有;**维护/成长拆分缺(O2)**。
- [x] owner earnings 桥(本版重建,区间 $73–125B)。
- [x] 隐含预期/IRR 从现价重建(三情景)。
- [x] 情景输出与来源/假设勾稽。
- [x] 关键公式可审计(scenario_model.csv + PowerShell 计算)。

## E. Open Questions And Blockers
- [x] 每个 open 分类:O2 capex 拆分=monitoring/可上修;O3 OpenAI=**blocking CORE**;O4 分部利润率=non-blocking STARTER;O1 $190B transcript=monitoring;O5 8-K=monitoring。
- [x] blocking 问题封顶 verdict(O3+完整度 → 封 STARTER,堵 CORE)。
- [x] non-blocking 给了不阻塞理由。
- [x] evidence backlog 见 monitor 证据触发器。

## F. Audit And Consistency
- [x] audit 检查 stale 自述(无)。
- [x] 文件索引/status 反映当前状态。
- [x] 旧版本标记(无,cold-start)。
- [~] 内容一致性检查:JSON 已 ConvertFrom-Json 验证通过;数字全文一致(市值/股数/价格)。
- [x] 最终答案报告真实状态(DECISION_DRAFT),非更好听状态。

## 必答自检
1. 状态标签? **DECISION_DRAFT(~65%)**
2. 哪些 gate 未过? **B(raw 全文段注)、D(capex 拆分)、E(OpenAI blocking)** → 完整度 <80%。
3. 升 COMPLETE 需要什么? **OpenAI 经济学(O3)+ capex 维护/成长拆分(O2)+ 分部利润率(O4)一手化 + 10-K/10-Q 段注逐字。**
4. 有 stale 文件吗? **无(cold-start)。**
5. 措辞匹配状态吗? **是,全程用 STARTER/DECISION_DRAFT/草案,未用"完成"。**
