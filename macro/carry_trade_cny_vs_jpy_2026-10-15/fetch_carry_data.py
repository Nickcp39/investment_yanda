"""套息交易：下载 FRED（curl）与 Yahoo 数据到 scratchpad/carry/data。"""
import json
import subprocess
import urllib.request
from pathlib import Path

D = Path(__file__).resolve().parent / "data"
D.mkdir(parents=True, exist_ok=True)
FRED = {
    "DEXJPUS": "日元/美元 日度（美联储 H.10）", "DEXCHUS": "人民币/美元 日度（美联储 H.10）",
    "FEDFUNDS": "联邦基金利率 月度", "DFF": "联邦基金利率 日度", "DGS2": "美国 2 年期国债", "DGS10": "美国 10 年期国债",
    "IRSTCI01JPM156N": "日本 隔夜拆借利率（OECD 月度）", "IR3TIB01JPM156N": "日本 3 个月银行间利率（OECD）",
    "IRLTLT01JPM156N": "日本 10 年期国债（OECD）",
    "IR3TIB01CNM156N": "中国 3 个月银行间利率（OECD）", "IRSTCI01CNM156N": "中国 隔夜拆借利率（OECD）",
    "IRLTLT01CNM156N": "中国 长期国债收益率（OECD）", "INTDSRCNM193N": "中国 贴现率（IMF）",
    "IR3TIB01USM156N": "美国 3 个月银行间利率（OECD）",
}
for sid, name in FRED.items():
    out = D / f"{sid}.csv"
    if out.exists() and out.stat().st_size > 200:
        continue
    raw = subprocess.run(["curl", "-s", "-m", "90", f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"], capture_output=True).stdout
    out.write_bytes(raw)
for sid in FRED:
    t = (D / f"{sid}.csv").read_text(errors="replace").strip().splitlines()
    good = [l for l in t[1:] if "," in l and not l.endswith(",") and not l.endswith(".")]
    print(f"{sid:18s} {FRED[sid]:24s} {len(good):6d} 行  {good[0] if good else '无'} … {good[-1] if good else ''}")

for tk in ("JPY=X", "CNY=X", "CNH=X", "^N225", "AUDJPY=X", "DX-Y.NYB"):
    out = D / f"yahoo_{tk.replace('^', 'IDX_').replace('=', '_')}.json"
    if not out.exists():
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{tk.replace('^', '%5E')}?period1=0&period2=9999999999&interval=1d"
        out.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read())
    r = json.loads(out.read_text())["chart"]["result"][0]
    ts = r["timestamp"]
    print(f"Yahoo {tk:10s} {len(ts)} 行，最新价 {r['meta'].get('regularMarketPrice')}")
