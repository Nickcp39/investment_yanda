# UBER + ADBE 全量刷新批次 · 2026-10-20 — 运行计划 (PLAN)

**批次 ID** `refresh_uber_adbe_2026-10-20` · **as_of** 2026-10-20 收盘（2026-10-20 23:35 EDT 收盘后运行）· `lean-6module-v1.1` · weights `none` · 两家均为**刷新**（`refresh_of`：`uber/2026-09-28`、`adbe/2026-08-07`）

## 触发
用户 2026-10-20："跑 uber 和 adobe，全部重新完整的，我要看具体情况。" 前因：同日问"最近跌得惨的科技巨头有没有机会"，交叉比对后 ADBE（现价在 12% 锚下 16%）与 UBER（现价在 8% 线下、且 09-28 独立 Checker 的 6 条修正一直没落实）是距离本库买入线最近、也最需要重跑的两张卡。

## 0. 两张卡各自要补的东西
| 公司 | 上一版 | 本次必须做 |
|---|---|---|
| UBER | 2026-09-28（佩洛西批次，WATCH 落锁，runner 提 STARTER 3%；独立 Checker CONFIRM WITH FIXES） | 落实 Checker 全部 6 条：① Delivery Hero $13.7B 要约入卡；② OE₀ 改完税口径；③ "扣一半 AV"真扣；④ p 下调；⑤ 关闭 O-U3 / O-U4；⑥ 区间改库惯例。另补：保险浮存、VIE 敞口、Aurora 减持、"C 类"错误、净现金过时 |
| ADBE | 2026-08-07（被杀大科技批次，STARTER 3% 自检） | 并入 Q3 FY26（2026-09-10 8-K / 09-22 10-Q）：TTM 滚到 Q3；重判 K-A..K-H、O1..O10；CEO 任命（09-08 8-K）；内部人交易；采购义务（O3）；Figma / Canva 数据（O8） |

## 1. A0 基准新鲜度门（INC-002）
`git fetch origin` → 本地不落后远端；远端 `companies/uber/` 最新为 `2026-09-28`、`companies/adbe/` 最新为 `2026-08-07`，与两张卡的 `refresh_of` 一致。

## 2. 本批特有的方法
1. **Delivery Hero 现金流叠加层**（`valuation_model.py` 新增 `extra_cf`）：第 2 年（2027 下半年交割）流出 $11.1B（$13.7B 扣 Q2 已付 $2.3B 增持、再扣 TRS 可实物交割部分，粗估），第 2 年起并入 DH 的 FCF（bear 0 / base $0.3B 起同增速 / bull $0.6B 起）。不改 OE₀，不改退出倍数。
2. **UBER 完税 OE₀**：FCF − SBC − 现金税正常化（TTM 已付现金税 $0.46B vs 正常化约 $1.9B；NOL 递延税资产 $3.18B 约 3 年用完）− 一半 AV（$1.25B）= $5.5B；余约 3 年税盾按 10 年摊回 +$0.4B → **$5.9B**，与 09-28 Checker 盲估相同。
3. **ADBE 改用库统一 10 年公式**（08-07 用的是 EV 口径 5y + 10y），便于与其他卡横比；新增 **harvest 情景**（g 2%、退出 10x）作为"净新增 ARR −36% 延伸十年"的下限测试。
4. 价格双源：Yahoo chart + Nasdaq historical；`fetch_filings.py` 新增"自 2026-08-01 起所有 8-K"下载（并购融资、人事 8-K 都在这里）。

## 3. 脚本
| 脚本 | 产物 |
|---|---|
| `fetch_data.py` | `data/snapshot_2026-10-20.json / .md`（价格、52 周、XBRL TTM） |
| `fetch_filings.py` | `companies/{uber,adbe}/2026-10-20/raw/*.txt`（10-K、10-Q、财报与并购 / 融资 / 人事 8-K） |
| `valuation_model.py` | `data/valuation_2026-10-20.json / .md` |
| `make_freshness.py` | 两家 `freshness.json` |
| `make_cards.py` | 两家 `decision_card.json`（数字只读估值 JSON 与 freshness.json） |
| `scripts/verify_freshness.py` | 两家 `freshness_check.json / .txt`（2/2 PASS） |

七个 md 模块本次手写（刷新卡每家的叙事差异大，不走 `dossier_content.py` 模板）。

## 4. 进度
| 公司 | 完整度 | 落锁 | runner 提议 | base IRR | buy_below | 现价 | binding |
|---|---:|---|---|---:|---:|---:|---|
| UBER | 72% | WATCH 0% | STARTER 2%（等 11-04 / 11-05） | +8.9% | $74.48（8% 线） | $68.94 | 垫子 0.9pt + DH 结果 + Checker 未复核修正版 |
| ADBE | 74% | WATCH 0% | STARTER 3%（建议等 12 月中） | +14.6% | $306.17（12% 锚） | $256.73 | 可验证性 + 交接期 |
