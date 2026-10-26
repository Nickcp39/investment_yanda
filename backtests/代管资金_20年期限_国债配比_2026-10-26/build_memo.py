#!/usr/bin/env python
"""memo_template.md (f-string) + stats.json -> memo.md. Template kept outside .py because CPython 3.9 chokes on long UTF-8 lines."""
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
D = Path(__file__).resolve().parent
S = json.load(open(D / "stats.json", encoding="utf-8"))
yp, Y = S["yield_pct"], S["yields_now"]


def hz(h):
    sp, nd = S[f"spx_{h}y"], S["ndx_windows"][str(h)]
    a = f"| {h} 年 | {sp['nom_min']:+.1f}%（{sp['nom_min_start'][:7]}） | {sp['nom_median']:.1f}% | {sp['share_negative_nom']:.0f}% "
    b = f"| {sp['share_below_bond']:.0f}% / {sp['share_below_bond_since_1980']:.0f}% "
    c = f"| {nd['min']:+.1f}%（{nd['min_start'][:7]}） | {nd['median']:.1f}% | {nd['share_negative']:.0f}% |"
    return a + b + c


rows_h = "\n".join(hz(h) for h in (5, 10, 20))
nd15 = S["ndx_windows"]["15"]
named = "\n".join(
    f"| {k[:7]} | {v['stock_nom']:.1f}% | {v['bond_lock']:.1f}% | {v['stock_nom'] - v['bond_lock']:+.1f} | ×{v['stock_mult']:.1f} vs ×{v['bond_mult']:.1f} |"
    for k, v in S["spx_20y_named"].items())
bs = "\n".join(f"| {h} 年 | {v['yield_used']:.2f}% | **{v['bond_share']:.0f}%** | {v['equity_share']:.0f}% |" for h, v in S["bond_share_table"].items())
st = S["structure_20y"]
P = st["principal_usd"]
outc = "\n".join(f"| {k} | {v['cagr']:.1f}% | {v['total']:,.0f}（×{v['total'] / P:.1f}） |" for k, v in st["outcomes"].items())
mix = "\n".join(
    f"| {k} | {v['最差']:,.0f}（×{v['最差'] / P:.1f}） | {v['5分位']:,.0f} | {v['中位']:,.0f}（×{v['中位'] / P:.1f}） |"
    for k, v in S["mix_20y"].items())
ndn = S["ndx_20y_named"]
tpl = (D / "memo_template.md").read_text(encoding="utf-8").replace("\r\n", "\n")
md = eval('f"""' + tpl + '"""')
(D / "memo.md").write_text(md, encoding="utf-8")
print("memo.md written", len(md), "chars")
