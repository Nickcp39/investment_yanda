# TSLA Financial Quality (M4) — as_of 2026-06-19

来源: FY2025 数据 [S008 回挂 10-K] / Q1 2026 [S005/S006/S008] / 官方运营 [S004]。SEC 逐行 403 未直取（O1）。模型见 `model/*.csv`。

## 1. 盈利能力与趋势（核心警告）
- **营收见顶回落**: FY23 $96.8B → FY24 $97.7B → FY25 **$94.8B（−2.9%）**。汽车交付 FY25 **−9%**。
- **营业利润率连续三年腰斩**: FY22 **16.8%** → FY23 9.2% → FY24 7.2% → **FY25 4.6%**。这是本案最硬的负面事实——核心生意盈利能力在结构性塌缩。
- **GAAP 净利**: FY22 峰 $12.6B → FY25 **$3.79B（−70% off peak，−46% Y/Y）**。
- **Q1 2026 的"改善"要打折**: GM 21.1%（+477bps）、营业利润 $941M——但官方 + B1 明示**部分来自一次性 warranty/tariff 收益**，且监管积分仍贡献 [C1]。**不应外推为结构性利润率回升。**

## 2. 现金流与 owner earnings 桥
- FY25: OCF $14.7B − capex $8.5B = **FCF $6.22B**。但 **FCF 上升主要因 capex 从 $11.3B 砍到 $8.5B**，非经营改善 [C2]。
- **capex 指引重新上调（2025-26 >$25B，AI/Optimus/robotaxi [S012]）→ 未来 FCF 将被增长 capex 吃回去**。当前 FCF 是"capex 低谷年"的美化值，不可持续外推。
- **owner earnings 锚**: 经营 owner earnings ≈ GAAP 净利量级 ~$3.8B（剔一次性后更低），**远小于报表 FCF**，因为 (a) FCF 含 capex 周期性低谷，(b) SBC $2.83B 是真实股东成本（且 Musk $1T 包将大幅放大未来 SBC/稀释）。
- 保守 owner earnings run-rate 取 **~$4–6B/年**（DELIVERED 口径，不计 robotaxi/Optimus 期权）。

## 3. 资产负债表（唯一的 A）
- 净现金 ~**$35.5B**（现金+短投 $44.7B − 债务 $9.2B）→ **fortress**，可存活汽车下行周期。这是 thesis 里最强的一点：**死不了**。
- 存货升至 $14.4B（vs $12.4B FY25 末）→ 与产>交、库存 27 天一致，需求侧走弱。
- **股本悬顶**: Musk $1T 包 **423.7M 股 ≈ 12% 稀释**若解锁 → 现有股东被显著摊薄；SBC 已 $2.83B/年并将放大。

## 4. 三情景（DELIVERED owner earnings 起点，NARRATIVE 期权严格区隔）
见 `model/scenario_model.csv`。owner earnings 起点用 **DELIVERED 口径 ~$5B**（汽车 + 能源，不计未兑现 robotaxi/Optimus）：
- **Bull**: robotaxi/Optimus **部分兑现**为真利润腿 + 能源继续翻倍 + 汽车利润率回升 → owner earnings 量级跃升。但即便如此，从 $1.41T / 0.44% 起始 yield 出发，5y IRR 仅中个位数（估值起点太高）。
- **Base**: 汽车持续低增/低利润率、能源成第二腿、robotaxi 缓慢扩张但单位经济一般、Optimus 仍未规模化 → owner earnings 缓慢爬升；现价 P/E 371x **无法被 DELIVERED 增长消化** → de-rate → **5y IRR 显著为负**。
- **Bear**: 汽车份额/利润率进一步塌（中国 EV + 需求弱）、robotaxi/Optimus 落空或大幅延后、narrative 溢价崩 → 估值向 DELIVERED 基本面回归（即便给 30–40x owner earnings 也意味腰斩级 de-rate）。**但资产负债表存活，非破产。**

## 5. 与 Mega7 同侪对照（关键差异）
- 与 NVDA 相反: NVDA owner earnings 干净、forward 19x、价格友好；**TSLA owner earnings 薄（汽车利润率塌）、P/E 371x / P/FCF 227x，价格是最极端的卡点**。
- 与 GOOGL 类似但更甚: GOOGL 是"好生意 + 价格无 MOS（WATCH-0%）"；**TSLA 是"减速制造业 + 极端价格 + 故事溢价"——价格封顶比 GOOGL 更紧**。
- binding constraint = **极端估值无安全边际（价格封顶）+ 核心利润池收缩 + Musk key-man/稀释**——三重，而非单一前瞻不确定。

## OPEN
- O1 SEC 10-Q/10-K 逐行（**分部利润是关键缺口**——能源/AI 到底赚不赚钱）；O5 能源分部真实利润率；O6 capex 明细对 FCF 的精确 haircut。
