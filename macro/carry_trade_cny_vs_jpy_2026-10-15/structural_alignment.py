"""日本（泡沫顶点 1991）vs 中国（房价顶点 2021）：结构性指标对齐。

数据：世界银行 WDI API（年度）、FRED 上的 BIS 债务序列（季度，% GDP）。下载到 data/wb_*.json、data/*.csv（已有不重下）。
零点：日本 T0 = 1991（BIS 名义住宅价格峰值 1991Q1；日经顶点 1989-12），中国 T0 = 2021（BIS 名义住宅价格峰值 2021Q3）。
运行：python structural_alignment.py → 打印对齐表，并写 structural_alignment.json、structural_alignment.png
"""
import csv
import datetime as dt
import io
import json
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.font_manager import FontProperties  # noqa: E402

HERE = Path(__file__).resolve().parent
D = HERE / "data"
T0 = {"JPN": 1991, "CHN": 2021}
WB = {  # 指标: (中文, 单位)
    "NY.GDP.PCAP.PP.KD": ("人均 GDP（PPP，2021 年不变国际元）", "元"),
    "NY.GDP.PCAP.CD": ("人均 GDP（现价美元）", "美元"),
    "SP.URB.TOTL.IN.ZS": ("城镇化率", "%"),
    "SP.POP.1564.TO": ("劳动年龄人口（15–64 岁）", "人"),
    "SP.POP.TOTL": ("总人口", "人"),
    "SP.POP.65UP.TO.ZS": ("65 岁以上占比", "%"),
    "SP.DYN.TFRT.IN": ("总和生育率", "孩/妇女"),
    "NE.CON.PRVT.ZS": ("居民消费占 GDP", "%"),
    "NE.GDI.TOTL.ZS": ("资本形成（投资）占 GDP", "%"),
    "NY.GDP.DEFL.KD.ZG": ("GDP 平减指数涨幅", "%"),
    "FP.CPI.TOTL.ZG": ("CPI 涨幅", "%"),
    "NY.GDP.MKTP.KD.ZG": ("实际 GDP 增长", "%"),
    "BN.CAB.XOKA.GD.ZS": ("经常账户占 GDP", "%"),
    "NE.EXP.GNFS.ZS": ("出口占 GDP", "%"),
}
BIS = {  # FRED 上的 BIS 信贷序列（% GDP，按市场价值，调整断点）
    "居民债务": {"CHN": "QCNHAM770A", "JPN": "QJPHAM770A"},
    "非金融企业债务": {"CHN": "QCNNAM770A", "JPN": "QJPNAM770A"},
    "政府债务": {"CHN": "QCNGAM770A", "JPN": "QJPGAM770A"},
    "私人非金融部门合计": {"CHN": "QCNPAM770A", "JPN": "QJPPAM770A"},
}


def wb(ind):
    f = D / f"wb_{ind}.json"
    if not f.exists() or f.stat().st_size < 500:
        url = f"https://api.worldbank.org/v2/country/CHN;JPN;USA/indicator/{ind}?format=json&per_page=3000&date=1960:2026"
        f.write_bytes(subprocess.run(["curl", "-s", "-m", "120", url], capture_output=True).stdout)
    js = json.loads(f.read_text(encoding="utf-8"))
    out = {"CHN": {}, "JPN": {}, "USA": {}}
    for r in js[1] if len(js) > 1 and js[1] else []:
        if r["value"] is not None:
            out[r["countryiso3code"]][int(r["date"])] = r["value"]
    return out


def fred(sid):
    f = D / f"{sid}.csv"
    if not f.exists() or f.stat().st_size < 200:
        f.write_bytes(subprocess.run(["curl", "-s", "-m", "90", f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"],
                                     capture_output=True).stdout)
    out = {}
    for r in csv.reader(io.StringIO(f.read_text(errors="replace"))):
        if len(r) == 2 and r[0][:1].isdigit() and r[1] not in ("", "."):
            d = dt.date.fromisoformat(r[0])
            out.setdefault(d.year, []).append(float(r[1]))
    return {y: sum(v) / len(v) for y, v in out.items()}  # 年均


res = {"wb": {}, "bis": {}}
offsets = [-5, 0, 3, 5, 10, 20]
print("指标".ljust(28), "日本 T-5 / T0 / T+3 / T+5 / T+10 / T+20（1986/1991/1994/1996/2001/2011）", "| 中国 T-5 / T0 / T+3 / T+5（2016/2021/2024/2026）")
for ind, (name, unit) in WB.items():
    data = wb(ind)
    res["wb"][ind] = data
    row = []
    for c in ("JPN", "CHN"):
        vals = []
        for k in offsets:
            y = T0[c] + k
            v = data[c].get(y)
            if ind == "SP.POP.1564.TO" or ind == "SP.POP.TOTL":
                v = v / 1e6 if v else None
            vals.append("—" if v is None else (f"{v:,.0f}" if abs(v) >= 1000 else f"{v:.1f}"))
        row.append(" / ".join(vals[:6] if c == "JPN" else vals[:4]))
    print(name.ljust(28), row[0], "|", row[1])

# 人均收入相对美国（PPP）
pp = res["wb"]["NY.GDP.PCAP.PP.KD"]
for c in ("JPN", "CHN"):
    y = T0[c]
    if pp[c].get(y) and pp["USA"].get(y):
        print(f"{c} T0 人均 GDP（PPP）相对美国：{pp[c][y] / pp['USA'][y] * 100:.0f}%")
latest = max(pp["CHN"])
print(f"中国最新（{latest}）人均 GDP（PPP）相对美国：{pp['CHN'][latest] / pp['USA'][latest] * 100:.0f}%")
# 劳动年龄人口峰值年
for c in ("JPN", "CHN"):
    w = res["wb"]["SP.POP.1564.TO"][c]
    pk = max(w, key=w.get)
    print(f"{c} 劳动年龄人口峰值：{pk} 年 {w[pk] / 1e6:,.1f} 百万；最新 {max(w)} 年 {w[max(w)] / 1e6:,.1f} 百万")
    t = res["wb"]["SP.POP.TOTL"][c]
    tp = max(t, key=t.get)
    print(f"{c} 总人口峰值：{tp} 年 {t[tp] / 1e6:,.1f} 百万")
# 平减指数转负
for c in ("JPN", "CHN"):
    g = res["wb"]["NY.GDP.DEFL.KD.ZG"][c]
    neg = [y for y in sorted(g) if y >= T0[c] - 2 and g[y] < 0]
    print(f"{c} T0 之后 GDP 平减指数为负的年份：{neg[:25]}")

print("\nBIS 债务（% GDP，年均）")
for name, ids in BIS.items():
    out = {}
    for c, sid in ids.items():
        s = fred(sid)
        out[c] = s
        vals = [f"{s[T0[c] + k]:.0f}" if s.get(T0[c] + k) else "—" for k in (offsets if c == "JPN" else offsets[:4])]
        print(f"  {name:12s} {c} {' / '.join(vals)}  最新 {max(s) if s else '—'} {s[max(s)]:.0f}" if s else f"  {name} {c} 无数据")
    res["bis"][name] = out

(HERE / "structural_alignment.json").write_text(json.dumps(res, ensure_ascii=False, default=str), encoding="utf-8")

# ---------- 图：按 T0 对齐的 6 个结构指标
font = FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
plt.rcParams.update({"font.family": font.get_name(), "axes.unicode_minus": False, "font.size": 8.5,
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 160})
panels = [
    ("人均 GDP（PPP）相对美国 %", lambda c, y: (pp[c].get(y) / pp["USA"][y] * 100) if pp[c].get(y) and pp["USA"].get(y) else None),
    ("城镇化率 %", lambda c, y: res["wb"]["SP.URB.TOTL.IN.ZS"][c].get(y)),
    ("劳动年龄人口（T0 = 100）", lambda c, y: (res["wb"]["SP.POP.1564.TO"][c].get(y) / res["wb"]["SP.POP.1564.TO"][c][T0[c]] * 100)
     if res["wb"]["SP.POP.1564.TO"][c].get(y) else None),
    ("居民消费占 GDP %", lambda c, y: res["wb"]["NE.CON.PRVT.ZS"][c].get(y)),
    ("GDP 平减指数涨幅 %", lambda c, y: res["wb"]["NY.GDP.DEFL.KD.ZG"][c].get(y)),
    ("私人非金融部门债务 % GDP（BIS）", lambda c, y: res["bis"]["私人非金融部门合计"][c].get(y)),
]
fig, axs = plt.subplots(2, 3, figsize=(11.5, 6.6))
for ax, (title, fn) in zip(axs.flat, panels):
    for c, col, lab in (("JPN", "#b9484a", "日本（T0 = 1991）"), ("CHN", "#235e7c", "中国（T0 = 2021）")):
        xs, ys = [], []
        for k in range(-20, 31):
            v = fn(c, T0[c] + k)
            if v is not None:
                xs.append(k)
                ys.append(v)
        ax.plot(xs, ys, color=col, lw=1.6, label=lab)
    ax.axvline(0, color="#999", lw=0.8, ls="--")
    if "平减" in title:
        ax.axhline(0, color="#555", lw=0.7)
    ax.set_title(title, loc="left", fontweight="bold", fontsize=9.5)
    ax.grid(alpha=0.25)
    ax.set_xlabel("距房价顶点的年数")
axs[0][0].legend(fontsize=7.5, frameon=False)
fig.suptitle("以房价顶点为零点对齐：日本（1991）vs 中国（2021）的结构性指标", x=0.01, ha="left", fontweight="bold", fontsize=11)
fig.text(0.01, 0.004, "来源：世界银行 WDI（NY.GDP.PCAP.PP.KD、SP.URB.TOTL.IN.ZS、SP.POP.1564.TO、NE.CON.PRVT.ZS、NY.GDP.DEFL.KD.ZG），BIS 经 FRED（QJPPAM770A、QCNPAM770A）。",
         fontsize=7, color="#666")
fig.tight_layout(rect=(0, 0.02, 1, 0.95))
fig.savefig(HERE / "structural_alignment.png")
print("图：", HERE / "structural_alignment.png")
