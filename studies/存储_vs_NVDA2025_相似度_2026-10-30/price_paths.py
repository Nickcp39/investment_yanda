"""价格形态对比：各自从高点起算的回撤路径。

对比对象：NVDA 2025（1 月高点 → 4 月低点 → 之后）、MU 2026、SNDK 2026（现在），以及 MU 自己的两次周期顶 2018、2022。
数据：Yahoo v8 日线复权收盘（curl，存 data/yahoo_*.json，已有不重下）。as_of = 最近一个完整交易日。
运行：python price_paths.py → 打印，写 data/price_paths.json、price_paths.png
"""
import datetime as dt
import json
import subprocess
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
D = HERE / "data"
D.mkdir(exist_ok=True)


def yahoo(t):
    f = D / f"yahoo_{t}.json"
    if not f.exists() or f.stat().st_size < 1000:
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1420070400&period2=9999999999"
               "&interval=1d&includeAdjustedClose=true&events=div,split")
        f.write_bytes(subprocess.run(["curl", "-s", "-m", "60", "-A", "Mozilla/5.0", url], capture_output=True).stdout)
    r = json.loads(f.read_text(encoding="utf-8"))["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0)
    out = {}
    for ts, c, a in zip(r["timestamp"], r["indicators"]["quote"][0]["close"], r["indicators"]["adjclose"][0]["adjclose"]):
        if c is not None and a is not None:
            out[dt.datetime.utcfromtimestamp(ts + off).date()] = (c, a)
    return out


px = {t: yahoo(t) for t in ["NVDA", "MU", "SNDK", "SMH", "QQQ"]}
AS_OF = max(px["MU"])
print("as_of（最近完整交易日）:", AS_OF, {t: f"{px[t][max(px[t])][0]:.2f}" for t in px})

# 各段：在窗口内找收盘最高点作为"高点"，然后取高点后的路径
EPISODES = [
    ("NVDA 2025", "NVDA", dt.date(2024, 6, 1), dt.date(2025, 3, 1)),
    ("MU 2026（现在）", "MU", dt.date(2026, 1, 1), AS_OF),
    ("SNDK 2026（现在）", "SNDK", dt.date(2026, 1, 1), AS_OF),
    ("MU 2018 周期顶", "MU", dt.date(2018, 1, 1), dt.date(2018, 9, 1)),
    ("MU 2022 周期顶", "MU", dt.date(2021, 9, 1), dt.date(2022, 6, 1)),
]
res = {"as_of": str(AS_OF), "episodes": {}}
for name, t, w0, w1 in EPISODES:
    s = px[t]
    ds = sorted(s)
    win = [d for d in ds if w0 <= d <= w1]
    peak_d = max(win, key=lambda d: s[d][1])
    after = [d for d in ds if d >= peak_d]
    a = np.array([s[d][1] for d in after])
    rel = a / a[0]
    horizon = min(len(after), 400)
    # 高点后的最低点（只看到 as_of 或之后 400 个交易日）
    lo_i = int(rel[:horizon].argmin())
    rec_i = next((i for i in range(1, len(rel)) if rel[i] > 1), None)
    e = {"ticker": t, "peak_date": str(peak_d), "peak_close": s[peak_d][0], "trough_date": str(after[lo_i]),
         "trough_close": s[after[lo_i]][0], "max_dd": float(rel[:horizon].min() - 1), "days_to_trough": lo_i,
         "recover_days": rec_i, "recover_date": str(after[rec_i]) if rec_i else None,
         "path": [float(x) for x in rel[:horizon]], "dates": [str(d) for d in after[:horizon]]}
    if t in ("MU", "SNDK") and "现在" in name:
        e["now_dd"] = float(rel[-1] - 1)
        e["days_since_peak"] = len(after) - 1
        e["now_close"] = s[after[-1]][0]
    else:
        lo = after[lo_i]
        for k, n in (("6m", 126), ("12m", 252)):
            j = lo_i + n
            e[f"from_trough_{k}"] = float(a[j] / a[lo_i] - 1) if j < len(a) else None
    res["episodes"][name] = e
    msg = (f"{name:16s} 高点 {peak_d} {s[peak_d][0]:9.2f} → 最低 {after[lo_i]} {s[after[lo_i]][0]:9.2f}  回撤 {e['max_dd']:+.1%}，"
           f"用 {lo_i} 个交易日；收复 {e['recover_date'] or '未收复'}")
    if "now_dd" in e:
        msg += f"；现在 {e['now_close']:.2f}，距高点 {e['now_dd']:+.1%}，高点后 {e['days_since_peak']} 个交易日"
    else:
        msg += f"；低点后 6 个月 {e['from_trough_6m']:+.0%}、12 个月 {e['from_trough_12m']:+.0%}" if e.get("from_trough_12m") is not None else ""
    print(msg)

# 同期对照：NVDA 2025 段里 SMH/QQQ 跌了多少；MU/SNDK 现在这段 SMH/QQQ 跌了多少
def window_ret(t, d0, d1):
    s = px[t]
    pick = lambda d: s[max(x for x in s if x <= d)][1]
    return pick(d1) / pick(d0) - 1

nv = res["episodes"]["NVDA 2025"]
mu = res["episodes"]["MU 2026（现在）"]
res["context"] = {
    "NVDA 高点→低点 同期": {t: window_ret(t, dt.date.fromisoformat(nv["peak_date"]), dt.date.fromisoformat(nv["trough_date"])) for t in ("SMH", "QQQ")},
    "MU 高点→现在 同期": {t: window_ret(t, dt.date.fromisoformat(mu["peak_date"]), AS_OF) for t in ("SMH", "QQQ")},
    **{f"{k} 高点→低点 同期": {t: window_ret(t, dt.date.fromisoformat(res["episodes"][k]["peak_date"]), dt.date.fromisoformat(res["episodes"][k]["trough_date"])) for t in ("SMH", "QQQ")} for k in ("MU 2018 周期顶", "MU 2022 周期顶")},
    **{f"{k} 高点后前 88 天 同期": {t: window_ret(t, dt.date.fromisoformat(res["episodes"][k]["peak_date"]), dt.date.fromisoformat(res["episodes"][k]["dates"][88])) for t in ("SMH", "QQQ", "MU")} for k in ("MU 2018 周期顶", "MU 2022 周期顶", "NVDA 2025")},
}
print("同期大盘：", {k: {t: f"{v:+.1%}" for t, v in d.items()} for k, d in res["context"].items()})

# 近期日线（10 月）
print("\n10 月以来收盘：")
for t in ("MU", "SNDK"):
    s = px[t]
    ds = [d for d in sorted(s) if d >= dt.date(2026, 9, 25)]
    print(f"  {t}: " + "  ".join(f"{d:%m-%d} {s[d][0]:.0f}" for d in ds))
(D / "price_paths.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")

# ---- 图
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 9, "text.parse_math": False,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": INK2, "xtick.color": INK2,
                     "ytick.color": INK2, "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.dpi": 170})
STYLE = {"NVDA 2025": ("#2a78d6", "-", 2.2), "MU 2026（现在）": ("#eb6834", "-", 2.2), "SNDK 2026（现在）": ("#1baf7a", "-", 2.2),
         "MU 2018 周期顶": ("#6250d6", (0, (4, 2)), 1.5), "MU 2022 周期顶": ("#e87ba4", (0, (4, 2)), 1.5)}
fig, ax = plt.subplots(figsize=(11.5, 6.2))
for name, e in res["episodes"].items():
    c, ls, lw = STYLE[name]
    y = np.array(e["path"]) * 100
    ax.plot(range(len(y)), y, color=c, ls=ls, lw=lw, label=name)
    end = len(y) - 1
    lab = f"{name}  {y[-1] - 100:+.0f}%" + ("（今天）" if "现在" in name else f"（第 {end} 天）")
    ax.annotate(lab, (end, y[-1]), xytext=(4, 0), textcoords="offset points", fontsize=8, color=INK, va="center")
    ax.plot([end], [y[-1]], "o", color=c, ms=4, mec=SURF, mew=1)
nvl = res["episodes"]["NVDA 2025"]
ax.annotate(f"NVDA 低点 {nvl['trough_date']}\n{nvl['max_dd']:+.0%}，第 {nvl['days_to_trough']} 天", (nvl["days_to_trough"], (1 + nvl["max_dd"]) * 100),
            xytext=(61, 112), textcoords="data", fontsize=8, color=INK, ha="center",
            arrowprops=dict(arrowstyle="-", color="#2a78d6", lw=0.8))
ax.axhline(100, color="#9a9994", lw=0.8)
ax.set_xlim(0, 430)
ax.set_xlabel("高点后的交易日", color=INK2)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v - 100:+.0f}%"))
ax.grid(axis="y", color=GRID, lw=0.8)
ax.legend(loc="upper left", frameon=False, fontsize=8.5, ncol=1)
ax.set_title("从各自高点起算的回撤路径：MU、SNDK 现在 vs NVDA 2025，以及 MU 的 2018、2022 周期顶", loc="left",
             fontweight="bold", fontsize=11, color=INK)
fig.text(0.01, 0.01, f"数据：Yahoo 日线复权收盘，截至 {AS_OF}。高点 = 窗口内最高收盘；历史段画到高点后约 400 个交易日。", fontsize=7.2, color=INK2)
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(HERE / "price_paths.png")
print("\n图：", HERE / "price_paths.png")
