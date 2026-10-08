# -*- coding: utf-8 -*-
"""
build_report.py — P4: 从 data/*.csv 生成 report.html 的数据块 (==DATA:BEGIN== ~ ==DATA:END==)
用法: python scripts/build_report.py   (先跑 compute.py 确认印证通过再构建)
"""
import csv, json, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORT = ROOT / "report.html"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def js(obj):
    return json.dumps(obj, ensure_ascii=False)

# --- SERIES_A ---
META = {
    "cn_tier1_official": {"k": "cn", "label": "中国一线·官方", "dash": False},
    "cn_tier1_txn":      {"k": "cn", "label": "中国一线·成交估算", "dash": True},
    "tokyo_res_land":    {"k": "tokyo", "label": "东京·住宅地价", "dash": False},
    "hk97":              {"k": "hk97", "label": "香港 1997", "dash": False},
    "us06":              {"k": "us06", "label": "美国 2006", "dash": False},
    "hk21":              {"k": "hk21", "label": "香港 2021", "dash": False},
}
ORDER = ["cn_tier1_official", "cn_tier1_txn", "tokyo_res_land", "hk97", "us06", "hk21"]
grp, base = defaultdict(dict), {}
for r in read("price_series.csv"):
    grp[r["series_id"]][int(r["t"])] = float(r["index"])
    base[r["series_id"]] = int(r["peak_year"])
series_a = []
for sid in ORDER:
    vals = [grp[sid][t] for t in sorted(grp[sid])]
    vals = [int(v) if v == int(v) else v for v in vals]
    m = META[sid]
    series_a.append({"k": m["k"], "label": m["label"], "dash": m["dash"], "base": base[sid], "vals": vals})

# --- DRAW ---
def mkey(row):
    mk, pk = row["market"], row["peak"]
    if mk in ("中国一线", "中国全国"): return "cn"
    if mk == "东京": return "tokyo"
    if mk == "美国": return "us06"
    if mk == "香港": return "hk97" if pk == "1997" else "hk21"
    return None
dd = read("drawdowns.csv")
draw = {"price": [], "rent": [], "volume": []}
for r in dd:
    k = mkey(r)
    if r["metric"] == "price" and r["series_id"] == "cn_tier1_txn":
        continue  # 成交口径并入官方行注释
    note = r["note"]
    if r["metric"] == "price" and r["series_id"] == "cn_tier1_official":
        note = "官方，迄今（成交口径约-30)"
    item = {"k": k, "v": int(float(r["drawdown_pct"])), "note": note}
    if r["basis"] == "est": item["est"] = True
    draw[r["metric"]].append(item)

# --- YIELDS ---
YNAMES = {"tokyo_bottom": "东京 2002-04 底", "hk_bottom": "香港 2003 底",
          "us_bottom": "美国 2012 底", "cn_now": "中国一线 2026 现在"}
yields_ = []
for r in read("yields_rates.csv"):
    if r["case_id"] not in YNAMES: continue
    item = {"name": YNAMES[r["case_id"]], "y": float(r["gross_rental_yield_pct"]), "m": float(r["mortgage_rate_pct"])}
    if r["case_id"] == "cn_now": item["now"] = True
    else: item["est"] = True
    yields_.append(item)

# --- RECOVER ---
recover = [{"k": r["market_key"], "name": r["name"], "v": int(r["years_to_recover"]), "note": r["note"]}
           for r in read("recovery.csv")]

# --- SENTI ---
senti = [{"year": r["year"], "phase": r["phase"], "attitude": r["dominant_attitude"],
          "events": r["key_events"], "words": r["hot_words"], "price": r["price_state_tier1"]}
         for r in read("sentiment_timeline.csv")]

# --- REAL (名义vs实际回撤) ---
real = [{"k": r["market_key"], "name": r["name"], "nom": float(r["nominal_dd_pct"]),
         "cpi": float(r["cpi_cum_pct"]), "real": float(r["real_dd_pct"]), "note": r["note"]}
        for r in read("real_terms.csv")]

block = "\n".join([
    "/* ==DATA:BEGIN== 此块由 scripts/build_report.py 从 data/*.csv 生成，勿手改 */",
    'const MARKETS = {',
    '  cn:   { name: "中国一线 2021", color: "var(--s-cn)" },',
    '  tokyo:{ name: "东京 1991",     color: "var(--s-tokyo)" },',
    '  hk97: { name: "香港 1997",     color: "var(--s-hk97)" },',
    '  us06: { name: "美国 2006",     color: "var(--s-us06)" },',
    '  hk21: { name: "香港 2021",     color: "var(--s-hk21)" },',
    '  uk89: { name: "英国 1989",     color: "var(--s-uk)" },',
    '  cn_official: { name: "中国一线·官方", color: "var(--s-cn)" },',
    '  cn_txn: { name: "中国一线·成交", color: "var(--s-cn)" },',
    '};',
    "const SERIES_A = " + js(series_a) + ";",
    "const DRAW = " + js(draw) + ";",
    "const YIELDS = " + js(yields_) + ";",
    "const RECOVER = " + js(recover) + ";",
    "const SENTI = " + js(senti) + ";",
    "const REAL = " + js(real) + ";",
    "/* ==DATA:END== */",
])

html = REPORT.read_text(encoding="utf-8")
pat = re.compile(r"/\* ==DATA:BEGIN==.*?==DATA:END== \*/", re.S)
if not pat.search(html):
    print("ERROR: data markers not found in report.html"); sys.exit(1)
html = pat.sub(lambda _: block, html, count=1)
REPORT.write_text(html, encoding="utf-8")
print(f"report.html data block rebuilt: SERIES_A={len(series_a)} DRAW={sum(len(v) for v in draw.values())} "
      f"YIELDS={len(yields_)} RECOVER={len(recover)} SENTI={len(senti)}")
