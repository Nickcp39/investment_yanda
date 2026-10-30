# 补充：Howmet（HWM）燃机叶片收入（2026-10-30）

- 补的是 `report.md` 的设备层。主报告已提交（a135288），不改；本文件与 `../data/howmet_gas_turbines.csv`、`../raw/hwm_*.txt` 一起新增。不构成投资建议。
- 起因：用户记得 6 月那批"AI 缺电"卡里，除了 GEV 还有一家"发动机公司"。那批是 GEV（06-19）与 Vertiv、Constellation、Howmet（06-22）。Vertiv 已在主研究里；Constellation 截至 10-30 只出了 Q2（08-06），Q3 未出；**Howmet 是那家发动机公司**，主研究漏了，这里补上。
- 另一个容易混的：GE Aerospace（`companies/ge_aerospace/2026-10-28`）卡里写明，数据中心燃机故事属于 GE Vernova，不属于 GE Aerospace。

## 1. Howmet 是哪一环

做航空发动机和燃气轮机的单晶高温合金涡轮叶片，卖给发动机和燃机厂，也卖存量机组的备件。10-K 原话：燃机业务"serve growing demand for electricity generation, driven by accelerating data center build-out"。

所以它的收入反映的是**燃机厂的产量和存量机组的备件**，属于出货层，不是订单层。GEV 的"每季新签 GW"是订单层。两者不能直接对冲。

## 2. 燃机收入（全部 P，SEC 10-Q / 10-K 分市场表）

| 季度 | 收入（百万美元） | 同比 | 环比增量 |
|---|---:|---:|---:|
| 2024Q3 | 191 | | |
| 2024Q4 | 201（推算） | | +10 |
| 2025Q1 | 204 | | +3 |
| 2025Q2 | 233 | | +29 |
| 2025Q3 | 241 | +26%（推算） | +8 |
| 2025Q4 | 266（推算） | +32% | +25 |
| 2026Q1 | 284 | +39% | +18 |
| 2026Q2 | 321 | +38% | +37 |
| **2026Q3** | **349** | **+45%** | +28 |

- 同比数字取自各季新闻稿原话；2025Q3 的 +26% 是按表格推算的。2026Q3 按 10-Q 表格是 349 / 241 − 1 = 44.8%。
- 推算方法：2024Q4 = 全年 755 − 前三季 554；2025Q4 = 全年 944 − 前三季 678。
- 2026Q3 的 349 里只有 1 来自收购的 CAM（Fastening Systems），其余 348 在 Engine Products，基本是内生增长。
- 燃机占公司收入从 11.5%（2025Q3）升到 12.9%（2026Q3）。全年口径 2023 年 674，2024 年 755，2025 年 944。

## 3. 怎么读

1. **和主报告的框架一致，属于"远端仍在加速"那一侧。** GEV 积压 64 GW、预留排到 2032 年，燃机厂在扩产交付，叶片先行出货，Howmet 的收入因此逐季加速（+26% → +32% → +39% → +38% → +45%）。这与 GEV 第三季新签只有 11 GW 不矛盾：新签少，不影响已经在积压里的机组生产。
2. **管理层第三季说需求还在加强**，原话"customers looking to increase volumes beyond previous expectations"，并说这支撑 2028 年以后的展望。资本开支 1.47 亿（上年同季 1.08 亿），说 2027 年以后还要维持高位。这是公司自己的说法（P），不是订单数字。
3. **三个限制：**
   - 这个类别包含石油天然气。2025Q4 起两类合并披露，之前 2025Q3 是工业燃机 152、石油天然气 89，后者约占 37%，不全是数据中心。
   - 45% 里有一部分是份额提升，CEO 原话是"the increase in market share"，不全是市场在长。
   - Howmet 不披露燃机订单和积压。它能告诉我们产量在加速，不能告诉我们新订单在加速。
4. **对 NBIS 的含义不变**：发电设备这条链的远端在加速，近端的算力新签在放缓。Howmet 加强的是前一半，不改后一半。

## 4. 价格与旧卡（只记录，不重跑）

- Yahoo v8 收盘价：10-29 为 **$205.94**，财报当天 +5.5%。近 6 个月高点 $292.65（08-18），低点 $185.91（10-23）。stockanalysis 被 Cloudflare 拦截，本条为单一来源。
- 06-22 的卡：as-of $280.36，WATCH，buy_below 约 $174，base 5 年 IRR −1.6%。那张卡用的是 Q1 数据（燃机 +39%），已过时。
- 股价从高点跌约 30%，燃机收入同期在加速，说明下跌不是燃机业务造成的。Q3 新闻稿专门说"We do not expect any material impact on our spares demand from the Middle East conflict"，下跌可能与航空备件担忧有关，这是推断，没有核实。
- 要不要重跑，看用户。

## 5. 来源

| ID | 文件 | URL | 日期 | 类型 |
|---|---|---|---|---|
| HWM_PR_3Q26 | 3Q26 新闻稿（8-K EX-99.1） | https://www.sec.gov/Archives/edgar/data/4281/000110465926119857/tm2628456d1_ex99-1.htm | 2026-10-29 | P |
| HWM_10Q_3Q26 | 3Q26 10-Q | https://www.sec.gov/Archives/edgar/data/4281/000000428126000036/hwm-20260930.htm | 2026-10-29 | P |
| HWM_10Q_2Q26 | 2Q26 10-Q | https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm | 2026-08-06 | P |
| HWM_10Q_1Q26 | 1Q26 10-Q | https://www.sec.gov/Archives/edgar/data/4281/000000428126000019/hwm-20260331.htm | 2026-05-07 | P |
| HWM_10K_2025 | FY2025 10-K | https://www.sec.gov/Archives/edgar/data/4281/000000428126000012/hwm-20251231.htm | 2026-02-12 | P |
| HWM_10Q_3Q25 | 3Q25 10-Q（工业燃机 / 石油天然气分列） | https://www.sec.gov/Archives/edgar/data/4281/000162828025047584/hwm-20250930.htm | 2025-10-30 | P |
| HWM_PR_4Q25 / 1Q26 / 2Q26 | 各季新闻稿（同比口径） | 见 CSV `source_url` | | P |

纯文本副本：`../raw/hwm_3q26_press_release.txt`；五份文件的燃机表格摘录在 `../raw/hwm_gas_turbine_tables.txt`。
