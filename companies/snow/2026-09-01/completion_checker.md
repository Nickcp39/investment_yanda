# SNOW — 完整度自检

**状态：`DECISION_DRAFT`** —— **禁称 COMPLETE / 跑完了 / 完整重跑完成**
（`frameworks/research_completion_checker.md` Non-Negotiable Language Rule）

## Gate 检查（对 `_mega7_2026-06-19/CHECKER.md` A–F）

| Gate | 要求 | 结果 |
|---|---|---|
| **A 证据** | 关键 claim 有 source_id 或标 OPEN | ✅ 37/37 有归属 |
| **A' 一手** | 核心财务有一手来源 | ❌ **0 条**。全部二手转述 |
| **B freshness** | `freshness_check.json` status=PASS | ❌ **无法运行**（INC-004） |
| **C 模块** | M1–M6 齐全且有分 | ✅ |
| **D 反演** | kill criteria 三态 | ✅ 6 条 |
| **E IC** | 五灵魂，无伪造引语 | ✅ |
| **F 卡** | decision_card.md + .json 带版本戳 | ✅ |
| **G 监控** | monitor.md 有阈值和动作规则 | ✅ |
| **H 自审** | audit.md 含敏感性 | ✅ |

## 完整度计算

| 维度 | 权重 | 得分 | 说明 |
|---|---:|---:|---|
| 一手证据 | 30% | **0%** | A' 全失 |
| 财务完整性 | 20% | 60% | 有损益/毛利/SBC；缺现金流表、资产负债表、股数序列 |
| 价格可验证 | 15% | **0%** | INC-004 |
| 分析模块 | 20% | 95% | 六模块 + 反演 + IC 齐全 |
| 命题回答 | 15% | 40% | T2 答了；**T1 未答**；T3 全答 |
| **加权** | | **≈45%** | |

## 封顶

```
完整度 45%  →  40–60 区间  →  verdict 上限 = WATCH
实际 verdict = WATCH ✅ 未越界
```

## 要升到 STARTER 需要（缺一不可）
1. 恢复行情源，`verify_freshness.py` exit 0
2. 读到一手 10-Q / 8-K，把 ≥15 条 claim 转成 `verified`
3. 关闭 **O-S1**（单一 AI 买家）与 **O-S3**（FY26 调整后 FCF）
4. 价格 ≤ $173

> **第 4 条今天离得最远（−48%），但第 1–3 条才是真正的门。**
