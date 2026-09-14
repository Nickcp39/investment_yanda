# EROC Research Status

as_of: 2026-08-13 · **本次跑未完成，可跨会话恢复**

---

## Pipeline 状态

| Stage | 状态 | 产出 |
|---|---|---|
| **Stage 0 — Identify** | ✅ done | `step0_plan.md` §已确认的事实 |
| **Stage 1 — Plan** | ✅ done | `step0_plan.md` 完整 block 列表 |
| **Stage 2 — Execute by block** | ❌ **BLOCKED / 未完成** | 见下 |
| Stage 3 — Synthesize (facts.md) | ⏸ 不可进入 | 缺 Stage 2 输入 |
| Stage 4 — Audit | ⏸ | |
| Stage 5+ — souls / decision card | ⏭ **跳过，出 NO-VERDICT 卡** | `decision_card.md` |

## Stage 2 为什么没跑完

**两层阻断，叠加：**

1. **一手源全部被出口代理拦截**（SEC EDGAR / businesswire / 公司 IR）——
   结构性问题，与 `../../nbis/2026-08-12/` 同因。详见 `source_register.md`。
2. **二手源检索在本次会话中途被 API 额度上限中断**（session limit，
   UTC 06:10 重置）。四个并行取数任务（身份与商业模式 / Q2财报与订单质量 /
   竞争格局 / 估值与股东结构）**全部在返回结果前终止**，
   `raw/block02–05` 因此为空。

> **本次没有用模型知识补齐缺口。** EROC 是 2026-06 IPO 的新公司，
> 不在训练知识可靠覆盖范围内；此处任何"看起来合理"的数字都会是编造。
> 按 lab 规则记为 OPEN，不记为 fact。

## 已落盘的东西（可用）

- `step0_plan.md` — Stage 0 身份 + 完整搜索计划（**下次直接从 Block 2 续跑**）
- `claim_ledger.csv` — 15 条 claim + **7 条 OPEN**，每条标了状态与置信度
- `source_register.md` — 源可达性 + **美股投资网定级依据 + 该来源的电力主题谱系**
- `decision_card.md` — **NO VERDICT**（完整度不足，不出裁决）

## 恢复指令（下次会话直接照做）

```
1. 读 step0_plan.md 的 Block 2–5 列表
2. 按 block 跑 WebSearch，产出落 raw/block0N_*.md
3. 优先级（按对裁决的影响排序）：
   OPEN-2 backlog 构成  >  OPEN-1 设备供应链  >  OPEN-3 锁定期
   >  OPEN-4 估值倍数  >  OPEN-5 竞争格局  >  OPEN-6 环保  >  OPEN-7 管理层
4. 三个停止条件（step0_plan.md §停止条件）能答上再进 Stage 3
5. 即使全部答上，因一手源不可达，裁决仍封顶在 WATCH
```

## 本次跑真正有价值的产出（不依赖被阻断的取数）

1. **E006 冲突的初步拆解**：二手标题"revenue surge +23%"与"Revenue Falls 42%"
   看似矛盾，实为**环比 +26% 与同比 −41.7% 并存**。
   → 真正要问的不是"哪个对"，而是**"去年同期 $68.5M 是什么业务"**。
   一家做 AI 电力的公司在 AI 电力最热的一年收入腰斩，
   这个基数问题是整个多头叙事的地基。
2. **E010 联动**：Anthropic 470MW 订单 = Anthropic 在本 lab 数据里
   **第二次以电力买家身份出现**（第一次是 WULF 的 20 年 ~$19B 肯塔基租约）。
   → 值得单独拉一条"Anthropic 电力采购地图"，比单看 EROC 信息量大。
3. **E014 媒体谱系**：该来源的 AI 电力主题已跑 2.5 年三代标的
   （公用事业 → 核能/SMR → 分布式发电），标的一代比一代早期。
   → 直接进 `studies/…/舆论热度轨迹_2026-08-13.md` 第五条规律作新样本。
