# NBIS Completion Checker（公司级 A–F gate）

最后更新: 2026-06-18 · 依据 `frameworks/research_completion_checker.md`（packaged 2026-06-21 under lean-6module-v1.1）

## 状态标签: `DECISION_DRAFT`（completeness ~70%）— **非 COMPLETE**

## A. Scope And Definition
- [x] 范围冻结:NBIS(Nebius Group N.V.),Nasdaq、Amsterdam-domiciled、US GAAP foreign private issuer(20-F/6-K,无 10-Q);as_of 2026-06-18;决策=(主)电力/buildout 是否 bottleneck + (决策)存量 +~50% 仓位 hold/trim/add + 新钱是否建仓;horizon 10yr。
- [x] 完成标准在最终答案前写明(本文件 + research_status)。
- [x] 状态标签不 stale(cold-start;旧单视频 brief `../../nbis.md` 明确标 C 级、仅对照)。

## B. Evidence Engineering
- [x] source_register 含 memo/model 用到的每个来源(21 源,A1/A2/B1/B2/C 分层)。
- [~] raw 摘录:6 份子代理 raw(电力/财务/operator/估值/商业模式/合同质量,~547k tokens)已存;**20-F/6-K 全文部分段注未逐字提取**(用 XBRL/IR/transcript 替代;active MW、集中度 % 段注未拉)。
- [x] claim_ledger 含 tier/验证状态/source_id(51 条)。
- [x] facts 仅从已验证或明确标 derived 的 claim 更新;KOL(旧 nbis.md)进 SENTIMENT/对照,核出老视频 3 处错。
- [x] memo 无裸 claim(均挂 claim_id 或标 OPEN)。
- [x] 无旧版 stale claim(cold-start)。
- [x] **LIVE 数据(price/mcap/52wk/shares + 合同/电力/ARR/Russia 定性)入 freshness.json,≥2 独立源,verify_freshness.py PASS**。

## C. Ten-Layer Research
- [x] 1 方向 · [x] 2 生意/质量门 · [x] 3 证据 · [x] 4 会计趋势 · [x] 5 价值链 · [x] 6 护城河/瓶颈(主)· [x] 7 operator · [x] 8 反演 · [x] 9 估值/MOS · [x] 10 决策/监控
  - 注:6(bottleneck,LEAD)深度高;9 估值受 active MW(O-A)/集中度(O-B)/capex(O-C)缺口限制。

## D. Model And Math
- [x] 收入驱动(3-tier:锚合同 / reserved / self-service + Token Factory)挂证据。
- [~] 费用/capex 模型:capex 序列有;**FY26 capex actual($20–25B vs $31–35B)缺(O-C)**;active MW 转化曲线缺(O-A)。
- [x] owner-earnings DCF **显式判定不可用**(FCF 负至 ≥2028)→ 改 EV/forward-sales 三角 + implied-expectations,理由写明。
- [x] 隐含预期从现价 $286.69 重建(EV ≈ 2.2× RPO ≈ 8–10× YE26 exit-ARR 当兑现)。
- [x] 三情景(bear/base/bull)输出与假设/来源勾稽(scenario_model.csv + model_assumptions.md)。
- [x] 关键公式可审计(implied_price = implied_ev / assumed_shares;标注忽略后续稀释)。

## E. Open Questions And Blockers
- [x] 每个 open 分类:**O-A active MW = blocking STARTER(转化证明缺)**;O-B 集中度 % = monitoring/可上修;O-C FY26 capex = monitoring;O-D Russia indemnity = non-blocking(低-中 severity)。
- [x] blocking 问题封顶 verdict:**价格(无 MOS)→ 新钱 WATCH** 为主;**O-A + 完整度 → 堵 STARTER** 为次;二者共同把新钱钉在 WATCH。
- [x] non-blocking 给了不阻塞理由(O-B/O-C 季度可解;O-D 多为声誉/已剥离)。
- [x] evidence backlog 见 monitor 事件日历(Q2'26 6-K ~Aug 解 O-A/O-C)。

## F. Audit And Consistency
- [x] audit 检查 stale 自述(无)。
- [x] 文件索引/status 反映当前状态。
- [x] 旧版本标记(旧 `../../nbis.md` = 单视频、结论 Watch、C 级对照)。
- [~] 内容一致性检查:JSON 已 json.load 验证通过;**canonical as_of_price $286.69 跨 decision_card.json/.md、valuation.md、facts.md、scenario_model.csv 一致**(T5 PASS);市值 $72.79B basic / 股数 253.9M 一致(T3 0.00%)。
- [x] 最终答案报告真实状态(DECISION_DRAFT),非更好听状态;新钱用 WATCH、存量用 HOLD,未用"COMPLETE/建仓"。

## 必答自检
1. 状态标签? **DECISION_DRAFT(~70%)**
2. 哪些 gate 未过? **B(20-F/6-K 全文段注:active MW、集中度)、D(FY26 capex actual + active MW 转化曲线)、E(O-A blocking STARTER)** → 完整度 <80%。
3. 升 COMPLETE 需要什么? **active MW 一手披露(O-A)+ 客户集中度精确 %(O-B)+ FY26 capex actual(O-C)+ Russia indemnity/或有(O-D)一手化 + 20-F/6-K 段注逐字。**
4. 有 stale 文件吗? **无(cold-start;旧单视频 brief 明确标对照)。**
5. 措辞匹配状态吗? **是,全程用 WATCH(新钱)/ HOLD(存量)/ DECISION_DRAFT/草案,未用"完成/建仓"。**

> **封顶逻辑提醒**:本案与 MSFT **镜像**——MSFT 价格有正 MOS、被**完整度**封顶(STARTER);**NBIS 被价格封顶(WATCH,无 MOS)**,完整度(active MW)为次级封顶。两者都 ≤ 各自 ceiling、都诚实自承非 COMPLETE。
