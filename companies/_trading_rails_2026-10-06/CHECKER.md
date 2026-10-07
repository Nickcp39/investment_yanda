# 交易通道批次 2026-10-06 — 验收 (CHECKER, self-check)

⚠️ Runner 自检（PROTOCOL §3 Checker ≠ Runner 未满足）→ 13 张卡 `clean=false`。本批**没有卡提议 STARTER**（完整度全部 < 60%，按 PIPELINE.md 上限为 WATCH），按 2026-09-05 以来的规矩现在无需派独立 Checker；但 7 家"价格已过 8% 线"的名字在任何升级前**必须**先补完整度并派独立 Checker。

## P0 基准
| 检查 | 状态 |
|---|---|
| `git fetch` + 比对 ticker 路径 | ✔ 落后 0 个提交；13 个 dated 目录均为新建 |

## P1 价格与新鲜度
| 检查 | 状态 |
|---|---|
| 价格双源（Yahoo + Nasdaq） | ✔ 13/13 差 0.00% |
| `verify_freshness.py` 在线独立回抓 | ✔ **13/13 PASS**，`refetched_yahoo` 均非空且等于卡片值 |
| T3 市值恒等式 / T4 距高点 / T5 单一价格 | ✔ 13/13 |
| T6 指引时效 | ⚠ 13/13 WARN（47–77 天）：最新为 Q2 财报，Q3 财报在 10 月中旬至 11 月 |
| 市值与 Nasdaq 的差异 | 口径差：卡片用估值股数（IBKR 全部转换 1,703.8M vs Nasdaq 仅 A 类，差 290%；其余 0.1–10.6%），已写入 `delta_note` |

## P2 财务一手性
| 检查 | 状态 |
|---|---|
| 财报原文本地检索 | ✔ 13 家全部下载（10-K / 20-F、10-Q、8-K / 6-K）；表格逐行压平后人工读取 |
| IBKR 全部转换股数 | ✔ 8-K 表：Holdings 1,250,737,416 单位（73.5%）+ 10-Q 封面 A 类 453,077,771 |
| HOOD / COIN / CRCL / BTGO 多类股 | ✔ 10-Q 封面逐类相加（XBRL 抓取遗漏，已手工替换） |
| FUTU | ✔ 6-K 季度新闻稿 + 20-F 年报；Q1 罚款金额来自二手报道（引用公司公告），**待用 Q1 6-K 原文复核** |
| VIRT TTM 正常化 EPS $6.96 | ⚠ 二手汇总（Barchart / allinvestview）；Q2 与 H1 来自一手 8-K；**待补 Q3/Q4 2025 原文** |
| CME FY2025 调整后净利润 | ⚠ 用 GAAP TTM（XBRL $4.29B）+ 上半年调整后差额推算，未取 FY2025 调整后原值 |
| COIN 周期中位 OE | `derived`：8-K 附录 10 个季度调整后 EBITDA 均值 − SBC − 折旧 − 税 |
| 操作者履历 | 全部 `unsourced_background`（本批未逐人核实） |

## P3 估值一致性
| 检查 | 状态 |
|---|---|
| 与佩洛西 / 石油 / 电力批次同一公式 | ✔ `valuation_model.py` 复制，只换输入；新增 ramp 情景的"8% 所需第 10 年 OE" |
| 卡片数字只读估值 JSON 与 freshness.json | ✔ `make_dossiers.py` 生成，无手填价格 |

## P4 本批已知弱点（交给独立 Checker 时重点看）
1. 交易所（CBOE / CME / ICE / NDAQ）的 base 增速 6–8%、退出 21–22x 是否偏乐观 —— 四家 bear IRR 仍为 +1% 到 +3.5%，结论对退出倍数敏感
2. BR 的 AI / 代币化替代风险只用了二手报道定性，**没有做替代测试**（委托书处理量、合同续签、分布式账本回购平台规模）
3. FUTU 的存量内地客户占比未量化 —— 这是它 bear 情景的核心变量
4. VIRT 的周期中位 OE（$0.75B）是判断，不是统计；应补 2018–2025 年逐年正常化净利润
