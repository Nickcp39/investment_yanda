# CAPITAL_CYCLE — 供给/需求资本周期(可选横切 lens)

**类型**: 可选 lens · **weight = none**(定性、诚实标不确定) · **条件触发**(不是每个 case 都用)。
**一句话**: 超额回报是一种不均衡,它自己会引来供给把自己填平(高回报→吸引资本/产能/人→供给涌入→卷平)。
这个 lens **不改 6 模块机械分**,是一个**单独变量 + 额外思考层**:只在"供给能响应的不均衡型生意"上触发,输出定性判断 + **单向 caution**,**不带权重**——因为我们既不知道拐点时点、也不知道该给多少权重。

> 出处:Edward Chancellor / Marathon《Capital Returns》的资本周期;也是 IC 面板 **Marks"我们在周期哪个位置"** 的内核。

---

## 0. 适用门(先判 N/A,别硬套)
必答一个门:**这家的超额回报是否依赖一个"供给可以响应"的供需不均衡?**
- **YES(适用)**:商品/产能/周期型 —— memory(DRAM/NAND/HBM)、GPU、晶圆代工、neocloud/算力出租、能源、航运、大宗、某类劳动力供给。
- **NO(标 N/A,跳过)**:回报来自**供给填不进来**的结构 —— 网络效应、品牌、转换成本、监管特许、心智垄断(如搜索、支付网络、强品牌消费)。
- **PARTIAL**:部分业务适用 —— 如 NVDA:算力供需有周期性,但 CUDA/生态是结构壁垒 → 只对**适用段**用。

> **天真守卫(本 lens 存在的首要理由)**:能看见的 demand>supply 是**共识**,资本已经在路上。**可见稀缺 + 高价 + ATH margin 默认是 late-cycle,不是买点**。天真版"需求>供给就买"= 买在顶。

## 1. 四问(定性;不确定就写"不知道",别装精确)
1. **当前不均衡 & 超额回报**:margin/定价权 vs **mid-cycle 正常化**水平(看偏离,不看绝对)。
2. **供给响应**:谁在加供给、量级、**lead-time**、announced capex 是否在**加速**?(产能公告 = 顶部信号)
3. **供给壁垒(HIGH→LOW)= 耐久性的真来源**:填平这个缺口难不难 —— 资本强度 / know-how / 稀缺投入(EUV、电力、先进制程产能)/ 时间 / 监管。**壁垒高=不均衡持久(真 bottleneck);壁垒低=周期,必均值回归。**
4. **周期位置**:`trough / early / mid / late / peak / rolling-over / unknown`(**允许且鼓励 unknown**)。

## 2. 输出:一个单独字段(不进核心 6 模块分)
`decision_card` 可选块 `capital_cycle`:
```
applicable:     yes | no | partial
stage:          trough | early | mid | late | peak | rolling | unknown
supply_barrier: high | med | low | unknown
read:           <一两句定性,包含"我们不知道 X">
caution:        <单向旗标,见 §3>
```

## 3. 单向 caution 规则(**能减不能加**,不机械翻 verdict)
- **只降不升**:诊断 `late/peak` + 壁垒低 + 价格外推峰值 → `caution=PEAK`,把 verdict 往 **WATCH/TRIM 压(封顶/haircut)**。这是一个 ceiling,**不是精确权重**。
- **trough 侧只作机会提示,不自动升 verdict**:诊断 `trough` + 供给在收缩 → `caution=TROUGH-WATCHLIST`,写进 `monitor.md` 当**布局观察**;但**不**因此加 size —— 仍需 M1–M6 常规举证 + 价格 MOS(**时点不可知,不赌拐点**)。
- **unknown 就写 unknown**:不确定不硬判,记为 open,既不封也不升。
- **weight = none**:它**永远不单独决定 verdict**;它只做三件事 —— 给人一个 caution、给 M5 一个 trap 输入、给 context_label 一个候选。

## 4. 与现有模块的关系(不重复造轮子)
- **M5(反演/陷阱)**:`capital_cycle_peak` 是一种 trap 类型的输入。
- **context_label**:新增两个**候选**(非强制)`capital_cycle_peak` / `durable_bottleneck`。
- **monitor.md**:把**行业总 capex/产能增速**列作 leading 监控项 —— 高 margin 上还在加速扩产 = late-cycle 警报。(现有 MU/SNDK/NBIS 卡的 kill 项已隐含此意:"SK Hynix HBM 扩产""capacity coming online"。)
- **IC 灵魂**:天然由 **Marks** 主问(周期位置)。

## 5. 治理(为什么现在不进核心)
- 这是 **optional lens,不改 6 模块机械分 → 不强制版本 bump**。某 case 实际用到就在该卡记 `capital_cycle` 块 + `caution`。
- **要正式纳入核心(带 weight、进聚合)必须先按 [`PATCH_LEDGER.md`](PATCH_LEDGER.md) 回测 ≥8 案验证 —— 当前明确不做**(我们不知道权重,不裸奔)。
- 验证设想:拿已知周期案例(memory 2018/2022 顶、2023 底;航运 2021 顶)——它该在**顶**给 `PEAK` caution、在**底**进 `TROUGH-WATCHLIST`,且**不因此单独翻 verdict**。

## 6. 应用示例(今天的三只)
| 名字 | applicable | stage | supply_barrier | caution | 一句话 |
|---|---|---|---|---|---|
| **MU/SNDK** | yes | late/peak | med-low(商品段) | **PEAK** | 三大厂 HBM/DRAM 扩产在路上 → 卡在 ATH 判 WATCH/TRIM 正是此 lens |
| **NVDA** | **partial** | late? | **high**(CUDA/full-stack)vs low(裸算力) | 视段而定 | 胜负手=壁垒能否扛住 custom silicon + 扩产;lens 把 M3 争点钉死,不给结论 |
| **NBIS** | yes | mid-late | low(neocloud 出租) | PEAK-lean | 高回报引来供给(CoreWeave、Meta 卖过剩算力)= 供给信号,非孤立利空 |
