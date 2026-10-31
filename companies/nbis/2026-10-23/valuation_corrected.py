"""NBIS 估值口径修正 + 「现价隐含了什么」+ 2027 年底情景网格。

输入全部来自 research/balance_sheet_financing_runway.md（SEC 一手：Q2'26 6-K、20-F、8 月可转债与 10-22 Citi 6-K），
另有 research/gpu_cloud_economics_peers.md 的同业倍数。单位：十亿美元（$B）、百万股（M）。
运行：python valuation_corrected.py → 打印，写 data/valuation.json、valuation_grid.png
"""
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
P_NOW, P_CARD, P_PEAK, P_CONV_REF = 159.17, 165.47, 286.69, 223.90

# ---- 股本（M 股）
SH_OUT = 287.7          # A+B 流通股：6/30 271.86 + 8 月换股约 15.8
SH_BASIC = 308.7        # 加 NVIDIA 预融资认股权 21.07（已计入基本 EPS）
SH_CARD = 274.10        # 10-19 卡用的数（错：含将注销的 C 类 2.24，漏换股与 PFW）
SH_JUNE_CARD = 257.5    # 06-18 / 07-10 卡定买入带时用的约 255–260M

# ---- 资产负债（$B，pro-forma = 6/30 + 7 月 ABF + 8 月可转债，未扣 Q3 消耗）
CASH_PF = 14.50         # 现金及等价物 8.04（不含受限 1.056）+ ABF 0.775 + 可转债净额 5.68
CONVERTS = 13.425       # 可转债原始本金合计（到期累积约 15.73）
ABF = 0.775
LEASES = 1.625          # 经营租赁负债（另有已签未起租 12.05 未折现，不计）
CITI = 3.5              # 过桥，提款状态未披露；提了就是现金和债务同时加，EV 不变
ITM_CONV_PRINCIPAL = 0.0875 * 2 + 1.58125 * 2   # 2025 年 6 月、9 月四档（转股价 $51.45 / $138.75）
ITM_CONV_SHARES = 26.2
ARR_JUN, ARR_EXIT = 3.0, (7.0, 8.0, 9.0)
REV_FY26_MID, RPO = 3.2, 37.4906
Q3_BURN = {"A 温和": 3.4, "B 重投": 6.65}   # capex − OCF，见 runway 表


def ev(price, shares=SH_BASIC, leases=False, itm_as_equity=False):
    mcap = price * shares / 1000
    debt = CONVERTS + ABF + (LEASES if leases else 0)
    if itm_as_equity:
        mcap += price * ITM_CONV_SHARES / 1000
        debt -= ITM_CONV_PRINCIPAL
    return mcap, mcap - CASH_PF + debt


out = {"inputs": {k: v for k, v in globals().items() if k.isupper() and isinstance(v, (int, float, tuple, dict))}}
print("=== 1. EV 口径对比 ===")
rows = []
for label, kw, price in [
    ("10-19 卡的算法（274.1M 股，债务约 $6.7B）", None, P_CARD),
    ("修正：基本股 308.7M，可转债按本金，不含租赁", {}, P_CARD),
    ("修正（10-22 收盘）", {}, P_NOW),
    ("修正（10-22）+ 经营租赁", {"leases": True}, P_NOW),
    ("修正（10-22）价内可转债按股权", {"itm_as_equity": True}, P_NOW),
]:
    if kw is None:
        mcap, e = P_CARD * SH_CARD / 1000, 37.3
    else:
        mcap, e = ev(price, **kw)
    r = {"label": label, "price": price, "mcap": mcap, "ev": e, "ev_arr_jun": e / ARR_JUN,
         "ev_exit_mid": e / ARR_EXIT[1], "ev_exit_lo": e / ARR_EXIT[0], "ev_exit_hi": e / ARR_EXIT[2],
         "ev_rev26": e / REV_FY26_MID, "ev_rpo": e / RPO}
    rows.append(r)
    print(f"  {label:34s} 价 {price:7.2f} 市值 {mcap:5.1f} EV {e:5.1f} | EV/6 月 ARR {r['ev_arr_jun']:4.1f}x  "
          f"EV/年底 ARR {r['ev_exit_hi']:.1f}–{r['ev_exit_lo']:.1f}x（中值 {r['ev_exit_mid']:.1f}x）  EV/FY26 收入 {r['ev_rev26']:.1f}x  EV/RPO {r['ev_rpo']:.2f}x")
out["ev_table"] = rows
for k, b in Q3_BURN.items():
    print(f"  Q3 消耗 {k}（−${b}B）后同价 EV ≈ {ev(P_NOW)[1] + b:.1f}，EV/年底 ARR 中值 {(ev(P_NOW)[1] + b) / 8:.1f}x")
_, ev_peak = ev(P_PEAK)
print(f"  对照：6-18 高点 $286.69 时（同口径）EV ≈ {ev_peak:.1f}，EV/年底 ARR 中值 {ev_peak / 8:.1f}x")
out["ev_peak"] = ev_peak

print("\n=== 2. 原卡买入带按同一方法、修正股数后对应的价格 ===")
# 06-18 / 07-10 卡：带 $150–180，按 ~257.5M 股、净现金约 0 → 对应 EV $38.6–46.4B
band_ev = (150 * SH_JUNE_CARD / 1000, 180 * SH_JUNE_CARD / 1000)
net_debt_now = CONVERTS + ABF - CASH_PF            # pro-forma，未扣 Q3
nd_ye26 = {"A 温和": CONVERTS + ABF - 7.6, "B 重投": CONVERTS + ABF - 1.1}   # runway 表 Q4'26 季末流动性（不含 Citi）
band = {"ev": band_ev, "pro_forma": [(e - net_debt_now) / SH_BASIC * 1000 for e in band_ev]}
print(f"  原带对应 EV ${band_ev[0]:.1f}–{band_ev[1]:.1f}B；现 pro-forma 净债务 {net_debt_now:+.2f}B")
print(f"  → 修正股数后同一 EV 对应价格 ${band['pro_forma'][0]:.0f}–{band['pro_forma'][1]:.0f}")
for k, nd in nd_ye26.items():
    band[k] = [(e - nd) / SH_BASIC * 1000 for e in band_ev]
    print(f"  → 若按 2026 年底净债务（{k}：{nd:.1f}B）：${band[k][0]:.0f}–{band[k][1]:.0f}")
out["band"] = band

print("\n=== 3. 补资金缺口的稀释 ===")
GAP = {"A 温和": 13.4, "B 重投": 37.9}   # 到 2027 年底、保留 $2B 现金底线的外部资金需求（runway 表）
out["dilution"] = {}
for k, g in GAP.items():
    d = {}
    for p in (P_NOW, P_CONV_REF):
        n = g / p * 1000
        d[str(p)] = {"shares_m": n, "pct": n / SH_BASIC}
    out["dilution"][k] = d
    print(f"  {k} 缺口 ${g}B：全用股权，按 ${P_NOW} 需 {d[str(P_NOW)]['shares_m']:.0f}M 股（+{d[str(P_NOW)]['pct']:.0%}），"
          f"按 8 月参考价 ${P_CONV_REF} 需 {d[str(P_CONV_REF)]['shares_m']:.0f}M 股（+{d[str(P_CONV_REF)]['pct']:.0%}）")

print("\n=== 4. 2027 年底情景网格：每股价值 =（年底 ARR × EV/ARR − 净债务）÷ 股数 ===")
# 融资假设：缺口一半用有担保/资产担保债，一半按 $159 增发；期末保留 $2B 现金
paths = {}
for k, g in GAP.items():
    nd = CONVERTS + ABF + 0.5 * g - 2.0
    sh = SH_BASIC + 0.5 * g / P_NOW * 1000
    paths[k] = {"net_debt": nd, "shares": sh}
    print(f"  融资路径 {k}：2027 年底净债务 ≈ ${nd:.1f}B，股数 ≈ {sh:.0f}M")
ARRS = [8, 12, 16, 20, 24, 28]
MULTS = [3, 4, 5, 6]
grid = {}
for k, pth in paths.items():
    g = np.array([[(a * m - pth["net_debt"]) / pth["shares"] * 1000 for m in MULTS] for a in ARRS])
    grid[k] = g.round(0).tolist()
    print(f"  【{k}】行 = 2027 年底 ARR，列 = EV/ARR {MULTS}")
    for a, row in zip(ARRS, g):
        print(f"     ${a:>2d}B  " + "  ".join(f"{v:7.0f}" for v in row))
out["grid"] = {"arrs": ARRS, "mults": MULTS, "paths": paths, "values": grid}

# 现价要求的 2027 年底 ARR：持有 1.2 年、年化 12%
target = P_NOW * 1.12 ** 1.2
need = {k: {m: (target * p["shares"] / 1000 + p["net_debt"]) / m for m in MULTS} for k, p in paths.items()}
out["required_arr"] = {"target_price": target, "need": need}
print(f"\n  现价 ${P_NOW} 想在 2027 年底（约 1.2 年）拿到年化 12%，目标价 ≈ ${target:.0f}；需要的 2027 年底 ARR：")
for k, d in need.items():
    print(f"    {k}：" + "  ".join(f"{m}x → ${v:.1f}B" for m, v in d.items()))
# 计划路径：年底 ARR 7–9B + 2027 年部署 >1 GW × $20–25M/MW，年底前约一半时间在产
plan = (8 + 1.0 * 20 * 0.5, 8 + 1.0 * 25 * 0.6)
out["plan_arr_2027"] = plan
print(f"  对照「按计划」的粗算：2026 年底 ARR 约 $8B + 2027 年 1 GW × $20–25M/MW × 50–60% 在产 ≈ ${plan[0]:.0f}–{plan[1]:.0f}B")

(HERE / "data" / "valuation.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

# ---- 图
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 8.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160, "text.parse_math": False})
fig, axs = plt.subplots(1, 2, figsize=(11, 4.6))
for ax, (k, pth) in zip(axs, paths.items()):
    g = np.array(grid[k])
    ratio = g / P_NOW
    im = ax.imshow(np.clip(ratio, 0, 2.5), cmap="RdYlGn", vmin=0, vmax=2, aspect="auto", origin="lower")
    for i in range(len(ARRS)):
        for j in range(len(MULTS)):
            v = g[i][j]
            ax.text(j, i, f"${v:.0f}" if v > 0 else "≤0", ha="center", va="center", fontsize=8,
                    color="#111" if 0.35 < ratio[i][j] < 1.8 else "white")
    ax.set_xticks(range(len(MULTS)), [f"{m}x" for m in MULTS])
    ax.set_yticks(range(len(ARRS)), [f"${a}B" for a in ARRS])
    ax.set_xlabel("2027 年底的 EV / ARR 倍数（同业成熟估值约 4x）")
    ax.set_ylabel("2027 年底 ARR")
    ax.set_title(f"融资路径 {k}：净债务 ≈ ${pth['net_debt']:.0f}B，股数 ≈ {pth['shares']:.0f}M", loc="left",
                 fontweight="bold", fontsize=9.5)
    ax.spines[["left", "bottom"]].set_visible(False)
fig.suptitle(f"2027 年底每股价值网格（颜色 = 相对现价 ${P_NOW} 的倍数；绿色高于现价，红色低于）", x=0.01, ha="left",
             fontweight="bold", fontsize=11)
fig.text(0.01, 0.01, "假设：到 2027 年底的资金缺口（A $13.4B / B $37.9B，见 runway 表）一半用有担保债、一半按 $159 增发；期末留 $2B 现金；可转债按本金计债务。"
         "示意用，不是预测。", fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.04, 1, 0.93))
fig.savefig(HERE / "valuation_grid.png")
print("\n图：", HERE / "valuation_grid.png")
