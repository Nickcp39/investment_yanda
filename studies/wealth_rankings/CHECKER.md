# 财富榜研究 — CHECKER(Phase 1 数据质量闸门)

角色:**独立于采集者** 的质量门。对三张 Top100 表逐项核,输出 **CLEAN / FIX-NEEDED** +
真实状态标签。**不改数据,只判。**

---

## Gate A — 完整度
- [ ] 每届恰好 **100 行**,`rank` 1–100 **连续无缺**。
- [ ] 必填字段齐:`rank / name / net_worth_usd_b / source_of_wealth / industry / country`。
- [ ] `age / self_made_score` 允许 2008 部分缺,但缺就标 **UNKNOWN**,不许留空当已知、更不许猜。

## Gate B — 来源纪律(主 > 次,带日期)
- [ ] `sources.csv` 里每个 `source_id` 有:出版方 + **届次日期** + url + 主/次标记。
- [ ] 每行 `net_worth + rank` 能追到一个 **福布斯当届** 来源(主源存档页优先;仅次源时标注)。
- [ ] **Top 10 每届 ≥2 源交叉** 一致(名字 + 净值)。

## Gate C — 数字一致性(机械可验)
- [ ] 同届内 `net_worth` 随 `rank` **单调非增**(允许并列)。
- [ ] 净值量级合理:落在该届 [#100 阈值, #1 峰值] 区间内。
- [ ] 无重复 `rank`;无重复同一人(除非福布斯本身按家族/个人分列 → 需注明)。

## Gate D — 年份纯度(防穿越,回测同款)
- [ ] 2008 行只用 2008 当届估值;**禁止**把某人 2015/2025 的身家、或后来的公司/头衔写进 2008 行。
- [ ] `source_of_wealth / company` 反映 **当届** 状态(如 2008 的 Top100 不该出现 Musk;若出现即错)。

## Gate E — 跨年匹配正确性(P1.5)
- [ ] `master_matched` 的 `person_key` 正确合并同一人(处理音译 / 改名 / “& family”);不同人不得误并。
- [ ] 三届交集(谁都在)可复核:每个交集成员在三张原表里都定位得到行。

## Gate F — 不造数
- [ ] 无凭空捏造的名字 / 数字;不可考的值标 **UNKNOWN**。
- [ ] `industry` 只用 PLAN §3.3 受控词表里的标签,不新造。

---

## 输出
`checker_report.md`:逐 Gate 打勾 + 问题清单 + 每届 **CLEAN / FIX-NEEDED** + 一句总评。
FIX-NEEDED 的表必须回修再验,才准进 Phase 2。
