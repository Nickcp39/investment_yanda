#!/usr/bin/env python3
"""fetch_brk_13f.py — 伯克希尔（CIK 1067983）历年 13F-HR 中石油相关持仓的逐季序列（一手，SEC）。

说明：13F 只含美国上市的股票（不含 OXY 优先股、认股权证、港股中石油 H 股）。
2013Q3 起 13F 采用 XML 信息表；此前为文本表，本脚本只处理 XML 时代。
输出 data/brk_13f_oil.csv：report_date, issuer, shares, value_usd, implied_price
"""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.request
from pathlib import Path

UA = {"User-Agent": "financial-analysis-lab research admin@financial-analysis-lab.org"}
OUT = Path(__file__).resolve().parents[1] / "data" / "brk_13f_oil.csv"
NAMES = {"CHEVRON": "CVX", "OCCIDENTAL": "OXY", "EXXON": "XOM", "CONOCOPHILLIPS": "COP", "PHILLIPS 66": "PSX",
         "SUNCOR": "SU"}


def get(url, as_json=False):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                b = r.read()
            return json.loads(b) if as_json else b.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


def filings():
    j = get("https://data.sec.gov/submissions/CIK0001067983.json", as_json=True)
    blocks = [j["filings"]["recent"]] + [get(f"https://data.sec.gov/submissions/{f['name']}", as_json=True)
                                         for f in j["filings"].get("files", [])]
    out = []
    for r in blocks:
        for i in range(len(r["form"])):
            if r["form"][i] == "13F-HR" and r["reportDate"][i] >= "2013-09-30":
                out.append((r["reportDate"][i], r["filingDate"][i], r["accessionNumber"][i]))
    return sorted(set(out))


def main():
    rows = []
    for rep, filed, acc in filings():
        base = f"https://www.sec.gov/Archives/edgar/data/1067983/{acc.replace('-', '')}"
        idx = get(base + "/index.json", as_json=True)
        xmls = [it["name"] for it in idx["directory"]["item"]
                if it["name"].lower().endswith(".xml") and "primary" not in it["name"].lower()]
        if not xmls:
            continue
        x = get(f"{base}/{xmls[0]}")
        tables = re.findall(r"<(?:\w+:)?infoTable>(.*?)</(?:\w+:)?infoTable>", x, re.S)
        # 2022 年前 13F 的 value 单位为千美元，之后为美元：用总额判断
        tot = sum(int(re.search(r"<(?:\w+:)?value>(\d+)<", t).group(1)) for t in tables)
        mult = 1000 if tot < 5e9 else 1
        agg = {}
        for t in tables:
            nm = re.search(r"nameOfIssuer>(.*?)<", t).group(1).upper()
            for key, tk in NAMES.items():
                if nm.startswith(key):
                    v = int(re.search(r"<(?:\w+:)?value>(\d+)<", t).group(1)) * mult
                    s = int(re.search(r"sshPrnamt>(\d+)<", t).group(1))
                    a = agg.setdefault(tk, [0, 0])
                    a[0] += v
                    a[1] += s
        for tk, (v, s) in agg.items():
            rows.append({"report_date": rep, "filed": filed, "ticker": tk, "shares": s, "value_usd": v,
                         "implied_price": round(v / s, 2) if s else None})
        print(rep, {k: (v[1], round(v[0] / 1e9, 2)) for k, v in agg.items()})
        time.sleep(0.3)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
