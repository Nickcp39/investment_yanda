#!/usr/bin/env python3
"""fetch_oil_prices.py — 一手油气价格（EIA），可原地重跑。

输出 data/：
  eia_monthly_spot.json  : WTI 现货（RWTC，1986-）、Brent 现货（RBRTE，1987-）、Henry Hub 天然气（RNGWHHD，1997-）月度均价
  eia_mer_T09.01.csv     : EIA《月度能源评论》表 9.1 原油价格汇总（国内首购价 1949 年起年度、1974 年起月度等）
FRED 在本环境不可达（HTTP 000），故全部改用 EIA。
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0"}
DATA = Path(__file__).resolve().parents[1] / "data"
SERIES = {
    "WTI_spot": "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RWTC&f=M",
    "Brent_spot": "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RBRTE&f=M",
    "HenryHub_spot": "https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm",
}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def parse(h):
    ser = {}
    for y, rest in re.findall(r"<td class='B4'>(?:&nbsp;)*\s*(\d{4})\s*</td>(.*?)</tr>", h, re.S):
        vals = re.findall(r"<td class='B3'>([^<]*)</td>", rest)
        for i, v in enumerate(vals[:12]):
            v = v.replace("&nbsp;", "").strip()
            if v:
                ser[f"{y}-{i + 1:02d}"] = float(v)
    return ser


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    out = {}
    for k, u in SERIES.items():
        out[k] = parse(get(u))
        ks = sorted(out[k])
        print(k, len(ks), ks[0] if ks else None, "->", ks[-1] if ks else None, out[k][ks[-1]] if ks else None)
    (DATA / "eia_monthly_spot.json").write_text(json.dumps(out, indent=0), encoding="utf-8")
    mer = get("https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T09.01")
    (DATA / "eia_mer_T09.01.csv").write_text(mer, encoding="utf-8")
    print("MER T09.01 rows", mer.count("\n"))


if __name__ == "__main__":
    main()
