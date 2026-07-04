# MSFT Refresh Note — as_of 2026-07-04

**Type**: LIGHT REFRESH(not a rebuild)of the 2026-06-19 lean-6module-v1 dossier.
**Pipeline**: lean-6module-v1 · weights none · original run_date 2026-06-19.
**Scope**: verify the 2-week delta (2026-06-18 → 2026-07-01),confirm/re-stamp verdict。40+ 文件 dossier 保留,未重跑。

## 1. Current price (last daily close ≤ as_of)
- **$384.28** — 2026-07-01 close(Yahoo chart API,`macro/market_panel/data/MSFT.csv`)。
- 市值 ~**$2.85T**(7.428B 流通股 × $384.28)。
- 距 pipeline 定价 $379.40 = **+1.3%**,基本原地。

## 2. 2-week delta 观察(2026-06-18 → 2026-07-01)

| Date | Close | 备注 |
|---|---:|---|
| 2026-06-18 | $379.40 | pipeline as_of |
| 2026-06-22 | $367.34 | 阶段回调开始 |
| 2026-06-25 | **$352.83** | **窗口最低点,一度回到 STARTER 深端(接近 12% IRR 区上沿 ~$303,但未触)** |
| 2026-06-26 | $372.97 | 反弹 |
| 2026-06-30 | $373.02 | 稳住 |
| 2026-07-01 | $384.28 | as_of,回升 |

- 窗口内价格波动区间:$352.83 – $384.28(振幅 ~9%),**没有跌破 12% IRR 加仓锚 $303**,也没有突破 8% no-chase 上沿 $436。**全程在 STARTER 区间内。**
- 2026-06-25 低点 $352.83 对应 IRR ~10.5% —— 是"更好的 STARTER 入场点",但不构成 CORE 触发(需 ≤ $303 + 补 O2/O3 缺口双条件)。

## 3. 3-week delta 事件扫描
- **8-K / 一手 filings**:窗口内无重大 8-K。
- **Q4 FY2026 财报**:仍预期 **~2026-07 下旬**(距 as_of ~3 周)—— 主要 catalyst,pipeline 已列。此财报是 **CAPEX 拆分 / OpenAI 口径 / Azure FY27 指引** 的兑现窗口,可能触发 memo v2 而非 light refresh。
- **10-K FY2026** 也在 ~2026-07 末,决定 O2/O3/O4 三缺口能否收敛。
- **监管/AI 政策**:无重大变化。
- **组合层因子提醒**:MSFT 与已持有 GOOGL / NBIS / BTC 同骑 "AI capex + 流动性" 因子。这 3 周该因子在其他持仓上无重大反证。

## 4. 结论:verdict 是否成立?
**YES — 无实质变化。** 从 memo-v1 起 verdict / size / ceiling / buy-below 全部不变:

- new_money **STARTER**(初始 3–5%),existing **ADD**(现价区可加至 starter 目标)。
- max size **暂封 9%**(待 O2/O3 补强)。
- 完整度 **~65%**,binding_constraint 仍是"研究完整度 + 两个信息缺口",**非价格**。
- buy_below **$436**(no-chase),加仓/评 CORE 锚 **$303**,deep value **$250**。
- 状态标签 **DECISION_DRAFT**(非 COMPLETE)。

## 5. 相对 pipeline 日的 IRR 更新(基于 $384.28)

| 情景 | 原(as_of $379.40)| 现(as_of $384.28)| 10y IRR 变动 |
|---|---:|---:|---:|
| Base | **9.5%** | **~9.4%** | −0.1pp,可忽略 |
| Bull | **15.2%** | **~15.0%** | −0.2pp,可忽略 |
| Bear | **~0.1%** | **~−0.1%** | ~0,基本 breakeven |

Base 案 IRR ~9.4%,仍**高于 8% 门槛**,MOS 正但被小幅侵蚀。

## 6. 下一次 refresh 或 re-open 的触发

- **Re-open panel(memo v2)**:Q4 FY26 财报 or 10-K FY26 落地 → 触发 IC panel 重开,主要看 (a) FY26 capex 是否坐实 $190B (b) 是否首次拆维护/成长 (c) OpenAI 关系新披露 (d) Azure FY27 指引。
- **Kill 触发**:价格 > $436(丧失 MOS)或 K-A/B/C/D 任一转红 → 立即重审。
- **Light refresh 触发**:另有 2–3 周价格漂移无重大事件 → 继续 light 模式即可,不重跑 dossier。

*本次为 light refresh,不改动 dossier 其余部分。*
