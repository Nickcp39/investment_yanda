# -*- coding: utf-8 -*-
"""Mine both corpora (videos transcripts + wechat articles) to characterise
TradesMax/美股投资网's stock-picking 'edge': ticker universe & frequency,
first-mention timeline for key winners/themes, and method/marketing keyword tallies.
Read-only."""
import json, re
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VID = ROOT / "sources/videos"
ART_MANIFEST = ROOT / "sources/news/wechat_mp/manifest.jsonl"

STOP = set("""AI IPO US USA VIP ETF CEO CFO SEC FED PC GPU CPU AWS API UI UX SAAS MSCI
PE PS EPS FSD ALL STOCKWE VC II III IV TD DRAM HBM LLM DC TV OK AM PM QE QT GDP CPI PPI
FOMC Q1 Q2 Q3 Q4 NO OF TO IN ON AT BY OR AND THE FOR DOW SPX ETN WTF IRA DFM ID URL NRC
ITAR LEU OVD ROSA NASA GB TB KV GW DM SSD PCB RF IC FPD HDI SDA PUE OLED NVL LTPS BR ZT
SOX GAAP FDA FAA GD MRDIMM DDR ZPE NYSE OS NATO EV CES GTC ESG SPAC YOY QOQ ROE ROIC FCF
CN UK EU AI'S US'S OEM ODM IDM TAM SAM CAGR YTD WSJ CNBC TSM PHD MIT KV""".split())

# documents: list of (date, title, text, source)
docs = []
for f in sorted(VID.glob("*.md")):
    name = f.name
    m = re.match(r"(\d{4}-\d{2}-\d{2})_", name)
    if not m: continue
    date = m.group(1)
    txt = f.read_text(encoding="utf-8", errors="ignore")
    title = txt.split("\n",1)[0].replace("# Transcript:","").strip()
    docs.append((date, title, txt, "video"))

for line in ART_MANIFEST.read_text(encoding="utf-8").splitlines():
    line=line.strip()
    if not line: continue
    r=json.loads(line)
    pt=(r.get("publish_time","") or "")[:10]
    body=""
    mp=r.get("markdown_path","")
    if mp and (ROOT/mp).exists():
        body=(ROOT/mp).read_text(encoding="utf-8",errors="ignore")
    docs.append((pt, r.get("title","") or "", body, "wechat"))

docs.sort(key=lambda d: d[0])
print(f"文档总数: {len(docs)} (视频 {sum(1 for d in docs if d[3]=='video')} + 微信 {sum(1 for d in docs if d[3]=='wechat')})")
print(f"时间跨度: {docs[0][0]} → {docs[-1][0]}")

def tickers(text):
    return set(t for t in re.findall(r"[A-Z]{2,5}", text) if t not in STOP)

# frequency: in how many DOCS each ticker appears; and first mention
doc_count = Counter()
first = {}
for date,title,text,src in docs:
    for t in tickers(text):
        doc_count[t]+=1
        if t not in first:
            first[t]=(date,title,src)

print(f"\n出现过的不同代号(>=2 字母, 去常见缩写后): {len(doc_count)} 个")
print(f"只出现 1 次的代号: {sum(1 for t,c in doc_count.items() if c==1)} 个  (撒网宽度指标)")
print("\n=== 复用最多的代号 Top 30 (出现在多少篇里) ===")
for t,c in doc_count.most_common(30):
    fd=first[t]
    print(f"  {t:6s} {c:3d} 篇   首提 {fd[0]} [{fd[2]}]")

# first mention of 2026-series winners + 2025-cited winners + theme leaders
WATCH = ["MU","NBIS","GLW","TTMI","INOD","SANM","RMBS","RDW","PLAB","AEP","NVDA","ONDS","SMR",
         "CRDO","CLS","HIMS","AVGO","CRWV","LITE","COHR","OKLO","ARM","CRCL","ASTS"]
print("\n=== 关键标的首次提及 (踩点早不早) ===")
for t in WATCH:
    if t in first:
        fd=first[t]
        print(f"  {t:6s} 首提 {fd[0]} [{fd[2]:6s}] 共{doc_count[t]:3d}篇  | {fd[1][:46]}")
    else:
        print(f"  {t:6s} (未出现)")

# method & marketing keyword tallies (繁简都算)
def count_kw(variants):
    n=0; hits=set()
    for date,title,text,src in docs:
        if any(v in text for v in variants):
            n+=1
    return n
KW = {
    "量化/大数据":     ["量化","大數據","大数据"],
    "主力资金/资金流": ["主力資金","主力资金","資金流","资金流","資金流向","资金流向"],
    "期权大单/异动":   ["期權","期权","大單","大单","異動","异动"],
    "机构持仓/机构":   ["機構持倉","机构持仓","機構","机构"],
    "评分/多因子":     ["評分","评分","多因數","多因子","因數模型","因子模型"],
    "胜率/全部上涨":   ["勝率","胜率","全部上漲","全部上涨","100%"],
    "区间最高/最高涨幅":["區間","区间","最高漲幅","最高涨幅","一年內","一年内"],
    "VIP/Top Stock":   ["VIP","Top Stock","TopStock"],
    "FOMO(错过/晚一天)":["錯過","错过","晚一天","多付","立即","限時","限时"],
    "目标价/入场价":   ["目標價","目标价","入場價","入场价","合理"],
}
print("\n=== 方法/营销关键词出现在多少篇里 (共{}篇) ===".format(len(docs)))
for k,v in KW.items():
    print(f"  {k:18s} {count_kw(v):3d} 篇")
