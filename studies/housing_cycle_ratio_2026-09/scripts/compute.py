# -*- coding: utf-8 -*-
"""
compute.py — 房价周期研究 P3: 从 data/ 重算、交叉印证、情景测算
零参数重跑: python scripts/compute.py  (在 study 根目录或任意目录均可)
输出: analysis/computed_results.md ; 任一印证失败则退出码=1
"""
import csv, sys, io
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
DATA, OUT = ROOT / "data", ROOT / "analysis"
OUT.mkdir(exist_ok=True)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))

fails, lines = [], []
def w(s=""): lines.append(s)

# ---------- 检查1: 价格序列重算最大回撤 vs drawdowns.csv (容差2pp) ----------
series = defaultdict(list)
for r in read("price_series.csv"):
    series[r["series_id"]].append((int(r["t"]), float(r["index"])))
dd_claim = {r["series_id"]: r for r in read("drawdowns.csv") if r["metric"] == "price" and r["series_id"]}

w("## 检查1: 价格回撤重算印证 (容差 ±2pp)\n")
w("| 序列 | 重算回撤 | 谷底t | 汇总表声称 | 偏差 | 结果 |")
w("|---|---|---|---|---|---|")
for sid, pts in series.items():
    pts.sort()
    mins = min(p[1] for p in pts)
    t_min = [t for t, v in pts if v == mins][0]
    recomputed = round(mins - 100, 1)
    claim = float(dd_claim[sid]["drawdown_pct"]) if sid in dd_claim else None
    if claim is None:
        fails.append(f"{sid}: 无对应汇总行"); w(f"| {sid} | {recomputed}% | t={t_min} | 缺失 | — | FAIL |"); continue
    dev = round(abs(recomputed - claim), 1)
    ok = dev <= 2.0
    if not ok: fails.append(f"{sid}: 偏差{dev}pp")
    w(f"| {sid} | {recomputed}% | t={t_min} | {claim}% | {dev}pp | {'PASS' if ok else 'FAIL'} |")

# ---------- 检查2: 成交量 indexed 与原值一致性 (容差2) ----------
w("\n## 检查2: 成交量指数化一致性 (容差 ±2)\n")
vol = defaultdict(list)
for r in read("volume_series.csv"):
    vol[r["series_id"]].append(r)
w("| 序列 | 年份 | 原值推算指数 | 表内指数 | 结果 |")
w("|---|---|---|---|---|")
for sid, rows in vol.items():
    peak = float(rows[0]["value"])
    for r in rows:
        implied = round(float(r["value"]) / peak * 100)
        stated = float(r["indexed_to_peak"])
        ok = abs(implied - stated) <= 2
        if not ok: fails.append(f"volume {sid} {r['year']}: {implied} vs {stated}")
        w(f"| {sid} | {r['year']} | {implied} | {stated} | {'PASS' if ok else 'FAIL'} |")

# ---------- 情景测算: 利差触发网格 ----------
w("\n## 情景网格: 触发『租金回报率>=按揭利率』所需价格变化\n")
yields_now = {r["case_id"]: r for r in read("yields_rates.csv")}
y0 = float(yields_now["cn_now"]["gross_rental_yield_pct"])
w(f"当前一线毛回报率 {y0}% (区间1.8-2.7)。所需价格变化 = y0×(1+租金变动)/目标利率 - 1\n")
rates = [3.0, 2.8, 2.6, 2.4, 2.2]
rents = [-0.05, 0.0, 0.05]
w("| 按揭利率 | 租金-5% | 租金持平 | 租金+5% |")
w("|---|---|---|---|")
for m in rates:
    cells = []
    for dr in rents:
        req = (y0 * (1 + dr) / m - 1) * 100
        cells.append(f"{req:+.0f}%" if req < 0 else "已触发")
    w(f"| {m}% | {cells[0]} | {cells[1]} | {cells[2]} |")
w("\n附加口径: 历史大底并非利差打平而是正利差+1.6~+3.1pp; 若要求+1pp(目标回报率=利率+1), 利率3.0%时需价格再跌 "
  f"{(y0/4.0-1)*100:.0f}%; 利率2.4%时需再跌 {(y0/3.4-1)*100:.0f}%。")

# ---------- 检查3/情绪对齐: 情绪阶段 vs 价格阶段 ----------
w("\n## 检查3: 情绪-价格对齐检验\n")
senti = read("sentiment_timeline.csv")
w("| 年份 | 情绪阶段 | 一线价格状态 |")
w("|---|---|---|")
for r in senti:
    w(f"| {r['year']} | {r['phase']} | {r['price_state_tier1']} |")
phases = [r["phase"] for r in senti]
years = [r["year"] for r in senti]
seq = " → ".join(f"{y}{p}" for y, p in zip(years, phases))
w(f"\n**情绪序列**: {seq}\n")
w("**历史案例情绪底与价格底的时差** (公开史实归纳, S39):\n")
w("| 案例 | 麻木期起点 | 价格底 | 麻木先行时长 | 底部年情绪特征 |")
w("|---|---|---|---|---|")
w("| 东京 | 约1995 | 2002 | ~7年 | 社会性冷漠, 房产话题消失 |")
w("| 香港 | 约2001 | 2003 | ~2年 | 负资产10.5万户, 无人看房 |")
w("| 美国 | 约2010 | 2012 | ~2年 | 'housing is dead'主流化 |")
w("| 中国一线 | 2024 | ? | 已2年 | 2026转入争论期(接近底部时的历史特征, 但也可能是B浪反弹舆论) |")
cn_maimu = sum(1 for p in phases if p == "麻木")
w(f"\n推论: 中国麻木期迄今{cn_maimu}年(2024-2025), 2026出现『争论』。对照: 香港/美国麻木~2年后见底, 东京拖了7年。")
w("情绪维度与估值维度(利差-0.8pp未转正)存在张力: 情绪接近底部特征, 估值尚未到位 —— 与『还差最后一跌或最后一轮降息』的判断相互印证。")

# ---------- 汇总 ----------
w("\n## 汇总\n")
w(f"- 印证失败项: {len(fails)}" + ("" if not fails else " → " + "; ".join(fails)))
w(f"- 数据行数: price={sum(len(v) for v in series.values())}, volume={sum(len(v) for v in vol.values())}, "
  f"sentiment={len(senti)}, monthly={len(read('china_monthly.csv'))}, sources={len(read('sources.csv'))}")

out = OUT / "computed_results.md"
out.write_text("# 计算与交叉印证结果 (compute.py 自动生成)\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
print(f"written: {out}")
print(f"FAILS: {len(fails)}")
for f_ in fails: print("  -", f_)
sys.exit(1 if fails else 0)
