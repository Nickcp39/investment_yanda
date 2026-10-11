#!/usr/bin/env python
"""Macro inputs for the market-temperature report.
BLS public API v1 (no key, 10-year chunks, 25 req/day): CPI-U NSA (CUUR0000SA0), unemployment rate SA (LNS14000000).
LBMA gold PM fix (USD) daily since 1968. M2 + CAPE copied from earlier batches (FRED unreachable from this machine).
Outputs data/bls_cpi_unrate_monthly.csv, data/gold_lbma_pm_daily.csv, data/macro_manifest.json"""
import csv, json, sys, datetime as dt, urllib.request, shutil
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent; D = HERE/"data"; D.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (research-lab market-temperature)"}
man = {"fetched_utc": dt.datetime.utcnow().isoformat(timespec="seconds"), "series": []}


def get(url, data=None, headers=None, timeout=90):
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r: return r.read()


# ---- BLS ----
BLS = "https://api.bls.gov/publicAPI/v1/timeseries/data/"; SERIES = {"CUUR0000SA0": "cpi_u_nsa", "LNS14000000": "unrate_sa"}
out = {}
year = 1978; end_year = dt.date.today().year
while year <= end_year:
    chunk_end = min(year + 9, end_year)
    payload = json.dumps({"seriesid": list(SERIES), "startyear": str(year), "endyear": str(chunk_end)}).encode()
    body = json.loads(get(BLS, data=payload, headers={"Content-Type": "application/json"}).decode())
    if body.get("status") != "REQUEST_SUCCEEDED": raise RuntimeError(f"BLS {year}-{chunk_end}: {body.get('message')}")
    for s in body["Results"]["series"]:
        col = SERIES[s["seriesID"]]
        for o in s["data"]:
            if not o["period"].startswith("M") or o["period"] == "M13": continue
            try: v = float(o["value"])
            except ValueError: continue
            out.setdefault(f"{o['year']}-{o['period'][1:]}", {})[col] = v
    print(f"BLS {year}-{chunk_end}: {len(out)} months"); year = chunk_end + 1
rows = sorted(out.items())
with open(D/"bls_cpi_unrate_monthly.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["month", "cpi_u_nsa", "unrate_sa"])
    for m, d in rows: w.writerow([m, d.get("cpi_u_nsa", ""), d.get("unrate_sa", "")])
man["series"].append({"name": "BLS CPI-U NSA + unemployment rate SA", "url": BLS, "rows": len(rows), "first": rows[0][0], "last": rows[-1][0]})
print("BLS last:", rows[-1])

# ---- LBMA gold PM ----
try:
    j = json.loads(get("https://prices.lbma.org.uk/json/gold_pm.json", timeout=120).decode())
    g = [(x["d"], x["v"][0]) for x in j if x.get("v") and x["v"][0]]
    g.sort()
    with open(D/"gold_lbma_pm_daily.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["date", "usd_per_oz"]); w.writerows(g)
    man["series"].append({"name": "LBMA gold PM USD/oz", "url": "https://prices.lbma.org.uk/json/gold_pm.json", "rows": len(g), "first": g[0][0], "last": g[-1][0]})
    print("LBMA", len(g), g[0], g[-1])
except Exception as e:
    src = HERE.parent/"黄金_货币供应_估值_2026-08-07"/"data"/"gold_lbma_pm_daily.csv"; shutil.copy(src, D/"gold_lbma_pm_daily.csv")
    man["series"].append({"name": "LBMA gold PM USD/oz (cached copy, fetch failed)", "error": str(e), "copied_from": str(src)}); print("LBMA fetch failed, copied cache:", e)

# ---- copies ----
for src, dst in [(HERE.parent/"黄金_货币供应_估值_2026-08-07"/"data"/"us_m2_monthly.csv", "us_m2_monthly.csv"),
                 (HERE.parent/"QQQ_现在高不高_2026-10-08"/"data"/"multpl_shiller_pe.csv", "multpl_shiller_pe.csv"),
                 (HERE.parent/"QQQ_现在高不高_2026-10-08"/"data"/"multpl_sp500_pe.csv", "multpl_sp500_pe.csv"),
                 (HERE.parent/"QQQ_现在高不高_2026-10-08"/"data"/"ndx_forward_pe_weekly.csv", "ndx_forward_pe_weekly.csv")]:
    shutil.copy(src, D/dst); man["series"].append({"name": dst, "copied_from": str(src)})
json.dump(man, open(D/"macro_manifest.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("manifest written")
