#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, sys, pandas as pd
from pathlib import Path
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
HERE = Path(__file__).resolve().parent
S = json.load(open(HERE/"stats_conc.json", encoding="utf-8")); N = S["now"]; P = S["ndx_share_proxy"]
ap = pd.read_csv(HERE/"data"/"apollo_largest_weight_by_year.csv").sort_values("weight_pct", ascending=False).head(14)
CN = {"Apple": "苹果", "NVIDIA": "英伟达", "IBM": "IBM", "AT&T": "AT&T", "Exxon Mobil": "埃克森美孚", "General Electric": "通用电气", "Microsoft": "微软", "Walmart": "沃尔玛"}
AP_ROWS = "\n".join(f"| {CN.get(r.company, r.company)} | {r.year} | {r.weight_pct:.1f}% | {r.pe:.0f} |" for r in ap.itertuples())
tpl = open(HERE/"report_template.md", encoding="utf-8").read()
md = eval('f"""' + tpl + '"""')
open(HERE/"report.md", "w", encoding="utf-8", newline="\n").write(md); print("report.md written", len(md))
