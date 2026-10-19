"""日本泡沫后资产回报 vs 中国现在：从 markets/data/ 的原始数据计算所有数字（不联网）。

数据（先运行 fetch_markets.py；部分文件为手工 curl 下载，见 japan_post_bubble_markets.md 附录）：
  Yahoo v8 日线 JSON（^N225、^HSI、个股、ETF），东方财富日线（上证综指 1.000001），
  中证指数公司 index-perf API（000300/H00300/000922/H00922，含 peg=市盈率），
  日本财务省 jgbcm_all.csv（国债各期限日度收益率，1974–），中债国债收益率曲线年度 xlsx（2006–2026），
  FRED 缓存（BIS 住宅价格 QJPN628BIS/QCNN628BIS，日本贴现率 INTDSRJPM193N，日本隔夜拆借 IRSTCI01JPM156N，
  H.10 美元兑日元 DEXJPUS），世界银行 CPI 通胀（FP.CPI.TOTL.ZG），Ken French Japan.Dat（日元计价组合回报与估值比率），
  日经平均总回报指数月度 CSV（2016–）。
运行：python analyze_markets.py  → 打印并写 results_markets.txt 与 aligned_table.csv
"""
import csv
import datetime as dt
import io
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE / "data"
OUT = []


def p(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s)


# ---------------- loaders ----------------
def yahoo(tk, field="close"):
    f = D / f"yahoo_{tk.replace('^', 'IDX_').replace('=', '_')}.json"
    r = json.loads(f.read_text())["chart"]["result"][0]
    off = r["meta"].get("gmtoffset", 0) or 0
    q = r["indicators"]["quote"][0]
    s = [(dt.datetime.utcfromtimestamp(t + off).date(), c) for t, c in zip(r["timestamp"], q[field]) if c]
    divs = {}
    for v in (r.get("events", {}).get("dividends", {}) or {}).values():
        divs[dt.datetime.utcfromtimestamp(v["date"] + off).date()] = v["amount"]
    return s, divs


def eastmoney(secid):
    j = json.loads((D / f"em_{secid}.json").read_text(encoding="utf-8"))
    out = []
    for k in j["data"]["klines"]:
        a = k.split(",")
        out.append((dt.date.fromisoformat(a[0]), float(a[2]), float(a[3])))  # date, close, high
    return out


def csi(code):
    d = json.loads((D / f"csi_{code}.json").read_text(encoding="utf-8"))["data"]
    return [(dt.datetime.strptime(r["tradeDate"], "%Y%m%d").date(), r["close"], r["peg"]) for r in d if r["close"]]


def fred(sid):
    out = []
    for r in csv.reader(io.StringIO((D / f"{sid}.csv").read_text(errors="replace"))):
        if len(r) == 2 and r[0][:1].isdigit() and r[1] not in ("", "."):
            out.append((dt.date.fromisoformat(r[0]), float(r[1])))
    return out


def mof_jgb():
    era = {"S": 1925, "H": 1988, "R": 2018}
    out = []
    txt = (D / "mof_jgbcm_all.csv").read_bytes().decode("cp932")
    for r in csv.reader(io.StringIO(txt)):
        m = re.match(r"([SHR])(\d+)\.(\d+)\.(\d+)$", r[0] if r else "")
        if m and r[10] not in ("-", ""):
            out.append((dt.date(era[m[1]] + int(m[2]), int(m[3]), int(m[4])), float(r[10])))
    return out


def chinabond10():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    out = []
    for f in sorted((D / "chinabond").glob("cgb_*.xlsx")):
        ws = openpyxl.load_workbook(f).active
        for r in ws.iter_rows(min_row=2, values_only=True):
            if r[2] in (10, 10.0):
                out.append((dt.datetime.strptime(r[0], "%Y/%m/%d").date(), float(r[3])))
    return sorted(out)


def wb_cpi():
    j = json.loads((D / "wb_cpi.json").read_text())
    return {(r["country"]["id"], int(r["date"])): r["value"] for r in j[1] if r["value"] is not None}


def ff_japan(section_title):
    """Ken French Japan.Dat: 返回 {yyyymm: [Mkt, BMH, BML, EPH, EPL, CEPH, CEPL, YH, YL, Y0]}（%）"""
    lines = (D / "ff_intl" / "Japan.Dat").read_text().splitlines()
    out, on = {}, False
    for ln in lines:
        if section_title in ln:
            on, out = True, {}
            continue
        if on:
            a = ln.split()
            if a and re.fullmatch(r"\d{6}", a[0]):
                out[a[0]] = [float(x) for x in a[1:]]
            elif out and a and re.fullmatch(r"\d{4}", a[0]):
                break
            elif out and not a:
                break
    return out


def ff_ratios():
    lines = (D / "ff_intl" / "Japan.Dat").read_text().splitlines()
    i = next(k for k, l in enumerate(lines) if "Average of Annual Value-Weight Averages" in l)
    out = {}
    for ln in lines[i:]:
        a = ln.split()
        if a and re.fullmatch(r"\d{4}", a[0]):
            out[int(a[0])] = dict(zip(["firms", "BM", "EP", "CEP", "Yld"], map(float, a[1:])))
        elif out and "Average of Annual" in ln:
            break
    return out


# ---------------- helpers ----------------
def at(s, d):
    d = dt.date.fromisoformat(d) if isinstance(d, str) else d
    w = [x for x in s if x[0] <= d]
    return w[-1] if w else None


def win(s, a, b):
    return [x for x in s if a <= x[0].isoformat() <= b]


def ymax(s, a, b):
    return max(win(s, a, b), key=lambda x: x[1])


def ymin(s, a, b):
    return min(win(s, a, b), key=lambda x: x[1])


def yrs(a, b):
    return (b - a).days / 365.25


def tr_series(px, divs):
    """收盘价 + 分红事件 → 总回报指数（分红按除息日收盘价再投资）"""
    out, idx, prev = [], 1.0, None
    for d, c in px:
        if prev is not None:
            idx *= (c + divs.get(d, 0.0)) / prev
        out.append((d, idx))
        prev = c
    return out


def cum(rets):
    v = 1.0
    for r in rets:
        v *= 1 + r / 100
    return v


# =====================================================================
p("# results_markets.txt  生成：", dt.date.today().isoformat())

# ---------- 1. 日经 225 ----------
p("\n## 1. 日经225（Yahoo ^N225 日线收盘）")
n225, _ = yahoo("^N225")
pk = ymax(n225, "1985-01-01", "1999-12-31")
p("泡沫顶（收盘）:", pk)
for a, b, lab in [("1990-01-01", "1992-12-31", "1992 低点"), ("1993-01-01", "2003-12-31", "2003 低点"),
                  ("2007-01-01", "2009-12-31", "2008-09 低点"), ("1990-01-01", "2024-01-01", "全程最低")]:
    t = ymin(n225, a, b)
    p(f"{lab}: {t[0]} {t[1]:.2f}  距顶 {t[1]/pk[1]-1:+.1%}  距顶 {yrs(pk[0], t[0]):.1f} 年")
reg = next(x for x in n225 if x[0] > pk[0] and x[1] > pk[1])
p(f"首次收盘超过 1989 顶: {reg[0]} {reg[1]:.2f}，距顶 {yrs(pk[0], reg[0]):.1f} 年")
last = n225[-1]
p(f"最新: {last[0]} {last[1]:.2f}  相对 1989 顶 {last[1]/pk[1]:.2f} 倍；价格年化 {(last[1]/pk[1])**(1/yrs(pk[0], last[0]))-1:+.2%}")
p("年末收盘 / 相对 1989 顶:")
n225_ye = {}
for y in range(1989, 2027):
    x = at(n225, f"{y}-12-31")
    n225_ye[y] = x
    p(f"  {y} {x[0]} {x[1]:9.2f} {x[1]/pk[1]:.2f}")

# ---------- 1b. 日经总回报（月度，2016–） ----------
p("\n## 1b. 日经平均总回报指数（日经官方月度 CSV，2016-01 起；基准 1979-12-28=6569.47）")
trm = []
for r in csv.reader(io.StringIO((D / "nikkei225_tr_monthly_en.csv").read_text(errors="replace"))):
    if r and re.match(r"\d{4}/\d{2}/\d{2}", r[0]):
        trm.append((dt.datetime.strptime(r[0], "%Y/%m/%d").date(), float(r[1])))
# 日经 2019-10-04 文章（更新自 2019-09-19 电子版）：总回报约为 1989 顶的 "8割弱"，价格指数 "5割強"
px_0919 = at(n225, "2019-09-19")[1]
tr_0930 = [v for d, v in trm if d == dt.date(2019, 9, 1)][0]
px_0930 = at(n225, "2019-09-30")[1]
tr_0919 = tr_0930 * px_0919 / px_0930
p(f"2019-09-19 日经价格 {px_0919:.2f}（={px_0919/pk[1]:.1%} 顶）；估 TR {tr_0919:.0f}")
for ratio in (0.75, 0.78, 0.80):
    tr89 = tr_0919 / ratio
    cross = next((d for d, v in trm if v > tr89), None)
    p(f"  若 2019-09 TR = 1989 顶的 {ratio:.0%} → 1989 顶 TR≈{tr89:.0f}；首个月末 TR 超过它: {cross}")
tr_last = trm[-1]
p(f"TR 最新月度值 {tr_last}；TR/价格 比 2016-01 = {trm[0][1]/at(n225,'2016-01-29')[1]:.3f}，最新 = {tr_last[1]/last[1]:.3f}")
tr89 = tr_0919 / 0.78
p(f"以 1989 顶 TR≈{tr89:.0f} 计：至 {last[0]} TR 约 {tr_last[1]/tr89:.2f} 倍，年化 {(tr_last[1]/tr89)**(1/yrs(pk[0], last[0]))-1:+.2%}（价格年化见上）")

# ---------- 2. JGB 10Y ----------
p("\n## 2. 日本 10 年国债收益率（财务省 jgbcm_all.csv，日度，1986-07 起）")
jgb = mof_jgb()
p("区间:", jgb[0], jgb[-1])
mx = ymax(jgb, "1989-01-01", "1992-12-31")
p("1989–92 最高:", mx)
for th in (5, 4, 3, 2, 1.66, 1.5, 1, 0.5, 0):
    f1 = next((x for x in jgb if x[0] > mx[0] and x[1] < th), None)
    p(f"  首次 < {th}%: {f1}  （距 1989-12-29 股市顶 {yrs(dt.date(1989,12,29), f1[0]):.1f} 年；距 1991 地价顶 {yrs(dt.date(1991,1,1), f1[0]):.1f} 年）" if f1 else f"  首次 < {th}%: 无")
# 最后一次低于 2% 之后再也没回到 2% 以上的时点
above2 = [x for x in jgb if x[0] > dt.date(1995, 1, 1) and x[1] >= 2]
p("  1995 后最后一个 ≥2% 交易日（直到再次回升前）:", next((x for x in above2 if x[0] < dt.date(2000, 1, 1) and not any(y[1] >= 2 for y in jgb if x[0] < y[0] < dt.date(2020, 1, 1))), None))
p("  最低:", min(jgb, key=lambda x: x[1]), "  首次 <0:", next((x for x in jgb if x[1] < 0), None))
back1 = next((x for x in jgb if x[0] > dt.date(2013, 1, 1) and x[1] >= 1), None)
back2 = next((x for x in jgb if x[0] > dt.date(2013, 1, 1) and x[1] >= 2), None)
back3 = next((x for x in jgb if x[0] > dt.date(2013, 1, 1) and x[1] >= 3), None)
p("  2013 后首次 ≥1%:", back1, " ≥2%:", back2, " ≥3%:", back3, " 最新:", jgb[-1])
jgb_ye = {y: at(jgb, f"{y}-12-31") for y in range(1989, 2027)}
p("  年末:", " ".join(f"{y}:{v[1]:.2f}" for y, v in jgb_ye.items()))

# ---------- 3. 中国 10Y ----------
p("\n## 3. 中国 10 年国债收益率（中债国债收益率曲线，10 年期，日度 2006–）")
cgb = chinabond10()
p("区间:", cgb[0], cgb[-1])
p("2007 最高:", ymax(cgb, "2007-01-01", "2008-12-31"), " 2013 最高:", ymax(cgb, "2013-01-01", "2014-12-31"))
p("2021 起最高:", ymax(cgb, "2021-01-01", "2026-12-31"), " 历史最低:", min(cgb, key=lambda x: x[1]))
cgb_ye = {y: at(cgb, f"{y}-12-31") for y in range(2018, 2027)}
p("  年末:", " ".join(f"{y}:{v[0]}={v[1]:.3f}" for y, v in cgb_ye.items()))
for th in (2.5, 2.0, 1.8, 1.7):
    f1 = next((x for x in cgb if x[0] > dt.date(2021, 1, 1) and x[1] < th), None)
    p(f"  2021 后首次 < {th}%: {f1}")

# ---------- 4. 日元 ----------
p("\n## 4. 美元兑日元（FRED DEXJPUS = 美联储 H.10 中午买入价）")
fx = fred("DEXJPUS")
for y in (1985, 1989, 1990, 1995, 2000, 2007, 2011, 2012, 2015, 2020, 2022, 2024, 2025):
    p(f"  {y} 年末 {at(fx, f'{y}-12-31')}")
p("  1990–2012 日元最强:", ymin(fx, "1990-01-01", "2012-12-31"), " 1995 最强:", ymin(fx, "1995-01-01", "1995-12-31"))
p("  2021 后日元最弱:", ymax(fx, "2021-01-01", "2026-12-31"), " 最新:", fx[-1])

# ---------- 5. 房价 ----------
p("\n## 5. BIS 名义住宅价格（FRED 缓存 QJPN628BIS / QCNN628BIS，2010=100，季度）")
jph, cnh = fred("QJPN628BIS"), fred("QCNN628BIS")
jpk = ymax(jph, "1980-01-01", "1999-12-31")
jtr = ymin(jph, jpk[0].isoformat(), "2020-12-31")
p(f"日本 顶 {jpk}，底 {jtr}，跌 {jtr[1]/jpk[1]-1:+.1%}，历时 {yrs(jpk[0], jtr[0]):.1f} 年；最新 {jph[-1]} = 顶的 {jph[-1][1]/jpk[1]:.0%}")
cpk = max(cnh, key=lambda x: x[1])
p(f"中国 顶 {cpk}，最新 {cnh[-1]}，跌 {cnh[-1][1]/cpk[1]-1:+.1%}，历时 {yrs(cpk[0], cnh[-1][0]):.1f} 年")

# ---------- 6. 中国股市 ----------
p("\n## 6. 中国 / 香港股市")
sse = eastmoney("1.000001")
s07 = ymax([(d, c) for d, c, h in sse], "2007-01-01", "2007-12-31")
h07 = max(((d, h) for d, c, h in sse if d.year == 2007), key=lambda x: x[1])
s15 = ymax([(d, c) for d, c, h in sse], "2015-01-01", "2015-12-31")
s_last = sse[-1]
p(f"上证综指（东方财富日线）2007 顶收盘 {s07}，盘中 {h07}；2015 顶收盘 {s15}；最新 {s_last[0]} {s_last[1]:.2f} = 2007 收盘顶的 {s_last[1]/s07[1]:.1%}（距顶 {yrs(s07[0], s_last[0]):.1f} 年）")
s_lo = ymin([(d, c) for d, c, h in sse], "2021-01-01", "2026-12-31")
p(f"  2021 后最低收盘 {s_lo}；2021 后最高收盘 {ymax([(d, c) for d, c, h in sse], '2021-01-01', '2026-12-31')}")
sse_ye = {y: at([(d, c) for d, c, h in sse], f"{y}-12-31") for y in range(2007, 2027)}
p("  年末:", " ".join(f"{y}:{v[1]:.0f}" for y, v in sse_ye.items()))

c300 = [(d, c) for d, c, pe in csi("000300")]
c300pe = {d: pe for d, c, pe in csi("000300")}
c3tr = [(d, c) for d, c, pe in csi("H00300")]
cdiv = [(d, c) for d, c, pe in csi("000922")]
cdtr = [(d, c) for d, c, pe in csi("H00922")]
cdpe = {d: pe for d, c, pe in csi("000922")}
k07, k21 = ymax(c300, "2007-01-01", "2007-12-31"), ymax(c300, "2021-01-01", "2021-12-31")
klo = ymin(c300, "2021-03-01", "2026-12-31")
p(f"沪深300（中证指数公司）2007 顶 {k07}，2021 顶 {k21}（PE {c300pe.get(k21[0])}），2021 后最低 {klo}（{klo[1]/k21[1]-1:+.1%}，PE {c300pe.get(klo[0])}）")
p(f"  最新 {c300[-1]}（{c300[-1][1]/k21[1]-1:+.1%} vs 2021 顶；PE {c300pe.get(c300[-1][0])}）")
c300_ye = {y: at(c300, f"{y}-12-31") for y in range(2020, 2027)}
t21 = at(c3tr, k21[0]); tl = c3tr[-1]
p(f"  沪深300全收益 H00300：2021 顶日 {t21} → {tl}：{tl[1]/t21[1]-1:+.1%}")
d21 = at(cdtr, k21[0]); dl = cdtr[-1]
p(f"  中证红利全收益 H00922：同期 {d21} → {dl}：{dl[1]/d21[1]-1:+.1%}；中证红利价格 000922 同期 {at(cdiv, k21[0])[1]:.2f} → {cdiv[-1][1]:.2f}（{cdiv[-1][1]/at(cdiv, k21[0])[1]-1:+.1%}），PE {cdpe.get(cdiv[-1][0])}")
p("  年度（全收益）：年份  沪深300TR  中证红利TR")
for y in range(2021, 2027):
    a0, a1 = at(c3tr, f"{y-1}-12-31"), at(c3tr, f"{y}-12-31")
    b0, b1 = at(cdtr, f"{y-1}-12-31"), at(cdtr, f"{y}-12-31")
    p(f"   {y}{'(至'+str(a1[0])+')' if y == 2026 else ''}  {a1[1]/a0[1]-1:+.1%}  {b1[1]/b0[1]-1:+.1%}")
a0, a1, b0, b1 = at(c3tr, "2020-12-31"), c3tr[-1], at(cdtr, "2020-12-31"), cdtr[-1]
p(f"  2020 年末→最新累计：沪深300TR {a1[1]/a0[1]-1:+.1%}，中证红利TR {b1[1]/b0[1]-1:+.1%}")

hsi, _ = yahoo("^HSI")
h18, h21 = ymax(hsi, "2018-01-01", "2018-12-31"), ymax(hsi, "2021-01-01", "2021-12-31")
hlo = ymin(hsi, "2021-03-01", "2026-12-31")
p(f"恒生指数（Yahoo）2018 顶 {h18}，2021 顶 {h21}，之后最低 {hlo}（{hlo[1]/h18[1]-1:+.1%} vs 2018 顶），最新 {hsi[-1]}（{hsi[-1][1]/h18[1]-1:+.1%} vs 2018 顶）")
p(f"  恒指历史最高收盘 {max(hsi, key=lambda x: x[1])}")

p("\n地产股（Yahoo 收盘，已含拆股调整，不含分红）：")
for tk, nm in [("000002.SZ", "万科A"), ("0688.HK", "中国海外发展"), ("2007.HK", "碧桂园")]:
    s, _ = yahoo(tk)
    m = ymax(s, "2015-01-01", "2026-12-31")
    p(f"  {nm} {tk}: 2015 后最高 {m[0]} {m[1]:.2f} → 最新 {s[-1][0]} {s[-1][1]:.2f}（{s[-1][1]/m[1]-1:+.1%}）")

# ---------- 7. 日本个股与组合 ----------
p("\n## 7. 日本代表性个股（Yahoo 日线，收盘+分红再投资；Yahoo 日本个股数据始于 1999–2005）")
names = {"7203.T": "丰田", "4063.T": "信越化学", "6861.T": "基恩士", "7974.T": "任天堂", "9983.T": "迅销(优衣库)",
         "8801.T": "三井不动产", "1801.T": "大成建设", "8306.T": "三菱UFJ"}
p("  名称  起点  起点→2012-11-14(安倍行情前)  2012-11-14→最新  （价格；总回报）")
for tk, nm in names.items():
    s, dv = yahoo(tk)
    t = tr_series(s, dv)
    st = s[0][0] if s[0][0] > dt.date(2000, 12, 29) else at(s, "2000-12-29")[0]
    mid = at(s, "2012-11-14")[0]
    def r(a, b, ser):
        return at(ser, b)[1] / at(ser, a)[1] - 1
    p(f"  {nm} {tk} 起 {st}: 价 {r(st, mid, s):+.0%} / TR {r(st, mid, t):+.0%}；之后 价 {r(mid, s[-1][0], s):+.0%} / TR {r(mid, s[-1][0], t):+.0%}（{s[-1][0]}）")
p(f"  对照 日经225 价格：2000-12-29→2012-11-14 {at(n225,'2012-11-14')[1]/at(n225,'2000-12-29')[1]-1:+.0%}；2012-11-14→最新 {last[1]/at(n225,'2012-11-14')[1]-1:+.0%}")
ewj, ewd = yahoo("EWJ")
ewt = tr_series(ewj, ewd)
p(f"  EWJ（MSCI Japan ETF，美元，总回报）1996-03→2012-11-14 {at(ewt,'2012-11-14')[1]/ewt[0][1]-1:+.0%}；2012-11-14→最新 {ewt[-1][1]/at(ewt,'2012-11-14')[1]-1:+.0%}")

p("\n## 8. Ken French 日本组合（日元计价、市值加权、含分红；Japan.Dat 'Value-Weight Local Returns, All 4 Data Items Not Reqd'）")
loc = ff_japan("Value-Weight Local  Returns      All 4 Data Items Not Reqd")
cols = ["市场", "高B/M(价值)", "低B/M(成长)", "高E/P", "低E/P", "高CE/P", "低CE/P", "高股息", "低股息", "零股息"]
for a, b in [("199001", "201212"), ("199001", "200312"), ("200401", "201212"), ("201301", "202512"), ("199001", "202512")]:
    ks = [k for k in sorted(loc) if a <= k <= b]
    n = len(ks) / 12
    line = []
    for i, c in enumerate(cols):
        v = cum([loc[k][i] for k in ks])
        line.append(f"{c} {v-1:+.0%}({v**(1/n)-1:+.1%}/年)")
    p(f"  {a}–{b}: " + "；".join(line))
rat = ff_ratios()
p("  估值（French 年度比率；行 t = t-1 年末组合形成时点，市值加权）：年份 P/B P/E 股息率")
for y in (1988, 1989, 1990, 1991, 1992, 1993, 1995, 1998, 2000, 2003, 2008, 2009, 2012, 2013, 2020, 2024, 2025):
    r_ = rat[y]
    p(f"   {y}(={y-1}年末) P/B {100/r_['BM']:.2f}  P/E {100/r_['EP']:.1f}  股息率 {r_['Yld']:.2f}%")

# 6 组合（美元）：小盘 vs 大盘
txt = (D / "ff" / "Japan_6_Portfolios_ME_BE-ME.csv").read_text()
blk = txt.split("Average Value Weighted Returns -- Monthly")[1].split("Average Equal Weighted")[0]
six = {}
for ln in blk.splitlines():
    a = [x.strip() for x in ln.split(",")]
    if a and re.fullmatch(r"\d{6}", a[0]):
        six[a[0]] = [float(x) for x in a[1:]]
c6 = ["小盘成长", "小盘中性", "小盘价值", "大盘成长", "大盘中性", "大盘价值"]
for a, b in [("199007", "201212"), ("201301", "202512")]:
    ks = [k for k in sorted(six) if a <= k <= b]
    n = len(ks) / 12
    p(f"  6 组合（美元计价）{a}–{b}: " + "；".join(f"{c} {cum([six[k][i] for k in ks])-1:+.0%}({cum([six[k][i] for k in ks])**(1/n)-1:+.1%}/年)" for i, c in enumerate(c6)))

# ---------- 9. 日本现金 / 国债（估算） ----------
p("\n## 9. 日本现金与 10 年国债 1990–2012（估算）")
call = fred("IRSTCI01JPM156N")  # OECD 隔夜拆借（月均，%）
cash = 1.0
for y in range(1990, 2013):
    for m in range(1, 13):
        v = at(call, f"{y}-{m:02d}-28")
        cash *= 1 + v[1] / 100 / 12
p(f"  隔夜拆借滚存 1990-01→2012-12：{cash-1:+.0%}（{cash**(1/23)-1:+.2%}/年）")
# 10 年国债恒定期限总回报近似：月回报 = y/12 + 价格变动（按平价债券修正久期）
mend = [at(jgb, dt.date(y, m, 28) if m != 12 else dt.date(y, 12, 31)) for y in range(1989, 2013) for m in range(1, 13)]
mend = [x for x in mend if x and x[0] >= dt.date(1989, 12, 1)]
idx = 1.0
for (d0, y0), (d1, y1) in zip(mend, mend[1:]):
    yy = y0 / 100
    dur = (1 - (1 + yy / 2) ** -20) / (yy if yy > 1e-6 else 1e-6) if yy > 1e-6 else 10.0
    idx *= 1 + yy / 12 - dur * (y1 - y0) / 100
p(f"  10 年国债恒定期限总回报（近似）{mend[0][0]}→{mend[-1][0]}：{idx-1:+.0%}（{idx**(1/yrs(mend[0][0], mend[-1][0]))-1:+.2%}/年）")
cpi = wb_cpi()
pl = 1.0
for y in range(1990, 2013):
    pl *= 1 + cpi[("JP", y)] / 100
p(f"  日本 CPI 1990–2012 累计 {pl-1:+.1%}（世界银行 FP.CPI.TOTL.ZG）")
ks = [k for k in sorted(loc) if "199001" <= k <= "201212"]
p(f"  对照：日本股市（French 市场组合，日元，含分红）同期 {cum([loc[k][0] for k in ks])-1:+.0%}")

# ---------- 10. 对齐表 ----------
p("\n## 10. 对齐表：日本 T=1991（住宅/地价顶）vs 中国 T=2021（BIS 住宅价格顶 2021Q3）")
disc = fred("INTDSRJPM193N")
rows = [["T", "日本年份", "日10Y年末%", "日贴现率年末%", "日隔夜拆借12月%", "日经年末/1989顶", "日本住宅价(BIS Q4)/顶", "日本CPI%",
         "中国年份", "中10Y年末%", "上证年末/2007顶", "沪深300年末/2021顶", "中国住宅价(BIS Q4)/顶", "中国CPI%"]]
for k in range(0, 11):
    yj, yc = 1991 + k, 2021 + k
    jh = at(jph, f"{yj}-10-01")
    r = [k, yj, f"{jgb_ye[yj][1]:.2f}", f"{at(disc, f'{yj}-12-01')[1]:.2f}", f"{at(call, f'{yj}-12-01')[1]:.2f}",
         f"{n225_ye[yj][1]/pk[1]:.2f}", f"{jh[1]/jpk[1]:.2f}", f"{cpi[('JP', yj)]:.1f}"]
    if yc <= 2026:
        ch = at(cnh, f"{yc}-10-01")
        r += [yc, f"{cgb_ye[yc][1]:.2f}" + ("*" if yc == 2026 else ""), f"{sse_ye[yc][1]/s07[1]:.2f}", f"{c300_ye[yc][1]/k21[1]:.2f}",
              f"{ch[1]/cpk[1]:.2f}" + (f"({ch[0]})" if ch[0].year != yc or ch[0].month != 10 else ""), f"{cpi.get(('CN', yc), float('nan')):.1f}"]
    rows.append(r)
with open(HERE / "aligned_table.csv", "w", newline="", encoding="utf-8-sig") as f:
    csv.writer(f).writerows(rows)
for r in rows:
    p("  " + " | ".join(str(x) for x in r))

(HERE / "results_markets.txt").write_text("\n".join(OUT), encoding="utf-8")

# ---------- 11. 补充 ----------
p("\n## 11. 补充")
t07 = at(c3tr, k07[0])
p(f"沪深300全收益：2007 顶日 {t07} → {c3tr[-1]}：{c3tr[-1][1]/t07[1]-1:+.1%}（{(c3tr[-1][1]/t07[1])**(1/yrs(t07[0], c3tr[-1][0]))-1:+.2%}/年）；价格 {c300[-1][1]/k07[1]-1:+.1%}")
dt07 = at(cdtr, k07[0])
p(f"中证红利全收益：2007 顶日 {dt07} → {cdtr[-1]}：{cdtr[-1][1]/dt07[1]-1:+.1%}（{(cdtr[-1][1]/dt07[1])**(1/yrs(dt07[0], cdtr[-1][0]))-1:+.2%}/年）")
p(f"同在顶后 19.0 年：日经 {n225_ye[2008][0]} = 1989 顶的 {n225_ye[2008][1]/pk[1]:.0%}；上证 {s_last[0]} = 2007 顶的 {s_last[1]/s07[1]:.0%}")
p(f"同在顶后约 5.7 年（CSI300 2021-02 → 2026-10）：日经 1995-09 末 = {at(n225,'1995-09-29')[1]/pk[1]:.0%} 顶")
for d in ("2021-07-01", "2021-02-10", "2007-10-16"):
    p(f"  中国 10Y 首次 <1.7%（2024-12-27）距 {d}: {yrs(dt.date.fromisoformat(d), dt.date(2024,12,27)):.1f} 年")
p(f"  日本 10Y 首次 <1.66%（1998-05-08）距 1990-09（六大城市地价顶）: {yrs(dt.date(1990,9,1), dt.date(1998,5,8)):.1f} 年")
lpk = ymax(n225, "2000-01-01", "2000-12-31")
p(f"日经 1990–2012 年度回报为正的年数: {sum(1 for y in range(1990, 2013) if n225_ye[y][1] > n225_ye[y-1][1])}/23")
