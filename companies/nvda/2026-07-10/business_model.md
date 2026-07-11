# NVDA Business Model (M2) — as_of 2026-06-19

## 一句话生意
NVIDIA 卖的是**加速计算的全栈平台**——不是一颗 GPU，而是 "芯片(Blackwell) + 互联(NVLink/InfiniBand/Spectrum-X) + 软件(CUDA) + 系统(整机柜/AI 工厂)" 打包的、AI 训练与推理必须绕过的基础设施层。客户为"每瓦/每美元产出的 AI 算力"付费，转换成本来自十几年积累的 CUDA 生态锁定。

## 营收引擎（Q1 FY27 拆解 [S001/S002]）
| 引擎 | Q1 FY27 营收 | 占比 | Y/Y | 性质 |
|---|---|---|---|---|
| Data Center 合计 | $75.25B | ~92% | +92% | 主引擎；AI 训练+推理 |
| └ DC Compute | $60.4B | ~74% | +77% | Blackwell GPU/系统 |
| └ DC Networking | $14.8B | ~18% | +199% | InfiniBand/Spectrum-X/NVLink，第二增长腿 |
| Graphics (Gaming+ProViz 等) | $7.07B | ~9% | +58% | 周期性消费/专业可视化 |

- **客户结构**: Hyperscale ~50% of DC；另 50% = AI Clouds、industrial、enterprise、sovereign → 较 2023 更**多元**，主权 AI 与企业是新需求来源。
- **变现**: 一次性硬件销售为主（非订阅），但 CUDA + 每代架构（Hopper→Blackwell→Blackwell 300）形成**重复采购节奏**；网络与软件提升 attach 与单系统 ASP。

## 10 年测试（十年后这门生意还在、还更强吗？）
- **看多**: AI 推理需求长期化（agentic AI 进入生产）、CUDA 生态网络效应、每代架构性能跃升维持升级周期、网络/系统层扩展 TAM、主权 AI 是结构性新池。
- **看空/不确定**: ①AI capex 是否 pull-forward（hyperscaler 资本开支周期回撤）；②custom silicon（CSP 自研 ASIC，如 TPU/Trainium/MTIA）+ AMD 在推理侧蚕食；③China 永久关闭（已归零）；④推理向更便宜/更专用芯片迁移压缩 GPU 份额。
- **判断**: 生意**十年大概率还在且仍是核心**，但"份额与利润率能否守在当前极值"是开放问题 → 耐久性给 high 但**带 custom-silicon/周期 haircut**，不是无限外推。

## 质量记分卡
| 维度 | 评分 | 依据 |
|---|---|---|
| 毛利率 | A | 74.9% GAAP（Q1 FY27），软件+全栈定价权 [S001] |
| 现金转化 | A | FCF/OCF ~96%，capex 极轻（FY26 $6.1B vs 营收 $215.9B）[S002/S003] |
| 资产负债表 | A+ | 净现金 ~$72B，债务微 [S001] |
| 营收质量 | B+ | 一次性硬件为主、非订阅；但架构升级节奏制造重复采购 |
| 客户集中 | B− | Hyperscale ~50% DC，少数大客户主导 → 周期/议价尾部 |
| 周期性 | B− | DC 需求与 AI capex 周期高度相关；历史 Gaming 周期波动大（FY23 营收 flat、$4.5B H20 计提示范尾部）|
| 可持续性 | B | 取决于 AI 推理需求长期化 vs custom silicon 替代（O4 OPEN）|

**结论**: 质量极高的**周期成长股 + 真实 bottleneck**——非稳态消费垄断（如可乐），利润率与份额处历史极值，耐久性强但需对"极值能否维持"打 haircut。按 METHODOLOGY 周期股纪律，**size 天花板封在 Confirmed 以下**。
