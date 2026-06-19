# -*- coding: utf-8 -*-
"""Build a self-contained HTML dashboard for the wechat_mp archive (美股投资网).

Reads sources/news/wechat_mp/manifest.jsonl + the article .md bodies and emits a
single offline HTML file with summary stats, a monthly chart, and a searchable /
filterable / full-text article browser.
"""
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSONL = ROOT / "sources/news/wechat_mp/manifest.jsonl"
OUT = ROOT / "sources/news/wechat_mp/dashboard.html"

STOP = {
    "AI","IPO","US","USA","VIP","ETF","CEO","CFO","SEC","FED","PC","GPU","CPU",
    "AWS","API","UI","UX","SAAS","MSCI","PE","PS","EPS","FSD","ALL","STOCKWE",
    "VC","II","III","IV","TD","DRAM","HBM","LLM","DC","TV","OK","AM","PM",
    "QE","QT","GDP","CPI","PPI","FOMC","Q1","Q2","Q3","Q4","NO","OF","TO","IN",
    "ON","AT","BY","OR","AND","THE","FOR","DOW","SPX","ETN","WTF","IRA","DFM",
}

def pdate(s):
    try:
        return datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
    except Exception:
        return None

def extract_body(md_path):
    """Strip YAML frontmatter + boilerplate header lines, return article body."""
    try:
        txt = (ROOT / md_path).read_text(encoding="utf-8")
    except Exception:
        return ""
    # drop frontmatter
    if txt.startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) == 3:
            txt = parts[2]
    lines = txt.splitlines()
    body = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("# ") or s.startswith("Account:") or s.startswith("Source:") or s.startswith("> "):
            continue
        body.append(ln)
    return "\n".join(body).strip()

def tickers_of(text):
    out = []
    for tok in re.findall(r"[A-Z]{2,6}", text):
        if tok not in STOP and tok not in out:
            out.append(tok)
    return out

rows = []
for line in JSONL.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line:
        rows.append(json.loads(line))

articles = []
all_ticks = Counter()
for r in rows:
    d = pdate(r.get("publish_time", ""))
    body = extract_body(r.get("markdown_path", ""))
    blob = (r.get("title","") or "") + " " + (r.get("description","") or "")
    ticks = tickers_of(blob)
    for t in ticks:
        all_ticks[t] += 1
    articles.append({
        "title": r.get("title","") or "(无标题)",
        "date": d.strftime("%Y-%m-%d") if d else "",
        "ym": d.strftime("%Y-%m") if d else "",
        "time": r.get("publish_time","") or "",
        "author": r.get("author","") or "",
        "desc": r.get("description","") or "",
        "url": r.get("url","") or "",
        "path": r.get("markdown_path","") or "",
        "len": r.get("text_length",0) or 0,
        "ticks": ticks,
        "body": body,
    })

articles.sort(key=lambda a: a["time"], reverse=True)

# summary stats
dated = [a for a in articles if a["date"]]
months = Counter(a["ym"] for a in dated)
month_keys = sorted(months)
total_chars = sum(a["len"] for a in articles)
top_ticks = [t for t, _ in all_ticks.most_common(24)]

summary = {
    "count": len(articles),
    "date_min": min(a["date"] for a in dated) if dated else "",
    "date_max": max(a["date"] for a in dated) if dated else "",
    "total_chars": total_chars,
    "avg_chars": total_chars // max(len(articles), 1),
    "months": [{"m": m, "n": months[m]} for m in month_keys],
    "top_ticks": [{"t": t, "n": all_ticks[t]} for t, _ in all_ticks.most_common(24)],
    "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
}

payload = json.dumps({"summary": summary, "articles": articles}, ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>美股投资网 · 公众号文章库</title>
<style>
  :root{
    --bg:#0f1419; --panel:#1a2029; --panel2:#222b36; --line:#2c3744;
    --ink:#e6edf3; --muted:#8b98a5; --accent:#4ca3ff; --accent2:#ffb454;
    --green:#3fb950; --red:#f85149;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
    line-height:1.6;font-size:14px}
  .wrap{max-width:1180px;margin:0 auto;padding:24px 20px 80px}
  header h1{margin:0 0 4px;font-size:22px}
  header .sub{color:var(--muted);font-size:13px}
  .cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:20px 0}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
  .card .k{color:var(--muted);font-size:12px;margin-bottom:4px}
  .card .v{font-size:22px;font-weight:700}
  .card .v small{font-size:12px;font-weight:400;color:var(--muted)}
  section{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:16px 0}
  section h2{margin:0 0 14px;font-size:15px;color:var(--accent)}
  /* monthly chart */
  .chart{display:flex;align-items:flex-end;gap:4px;height:160px;overflow-x:auto;padding-bottom:4px}
  .bar{flex:1 0 26px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
  .bar .col{width:100%;background:linear-gradient(180deg,var(--accent),#2b6cb0);border-radius:4px 4px 0 0;min-height:2px;transition:.2s}
  .bar .col:hover{background:var(--accent2)}
  .bar .n{font-size:11px;color:var(--muted);margin-bottom:3px}
  .bar .lab{font-size:10px;color:var(--muted);margin-top:5px;writing-mode:vertical-rl;white-space:nowrap}
  /* ticker chips */
  .chips{display:flex;flex-wrap:wrap;gap:8px}
  .chip{background:var(--panel2);border:1px solid var(--line);border-radius:20px;padding:4px 12px;cursor:pointer;font-size:13px;user-select:none}
  .chip:hover{border-color:var(--accent)}
  .chip.active{background:var(--accent);color:#06121f;border-color:var(--accent);font-weight:600}
  .chip b{color:var(--accent2);margin-left:5px;font-weight:700}
  .chip.active b{color:#06121f}
  /* controls */
  .controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:6px}
  input[type=search],select{background:var(--panel2);border:1px solid var(--line);color:var(--ink);
    border-radius:8px;padding:8px 12px;font-size:14px;font-family:inherit}
  input[type=search]{flex:1;min-width:220px}
  .hint{color:var(--muted);font-size:12px}
  /* list */
  .item{border:1px solid var(--line);border-radius:10px;margin:10px 0;overflow:hidden;background:var(--panel2)}
  .item .head{padding:12px 14px;cursor:pointer;display:flex;gap:12px;align-items:flex-start}
  .item .head:hover{background:#27313d}
  .item .meta{flex:0 0 96px;color:var(--muted);font-size:12px}
  .item .meta .len{display:block;margin-top:3px}
  .item .ti{flex:1;font-weight:600}
  .item .ti .d{display:block;color:var(--muted);font-weight:400;font-size:12.5px;margin-top:4px}
  .item .ti .tk{display:inline-block;background:#13202e;color:var(--accent);border:1px solid var(--line);
    border-radius:4px;padding:0 6px;font-size:11px;margin:4px 4px 0 0;font-weight:600}
  .item .body{display:none;padding:0 16px 16px;border-top:1px solid var(--line);white-space:pre-wrap;
    color:#cdd9e5;font-size:13.5px;max-height:520px;overflow:auto}
  .item.open .body{display:block}
  .item .links{margin:10px 0 0;font-size:12.5px}
  .item .links a{color:var(--accent);text-decoration:none;margin-right:16px}
  .item .links a:hover{text-decoration:underline}
  .empty{color:var(--muted);text-align:center;padding:40px}
  mark{background:var(--accent2);color:#06121f;border-radius:2px}
  .note{color:var(--muted);font-size:12px;margin-top:6px}
  a.clean{color:var(--accent);text-decoration:none}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>美股投资网 · 公众号文章库</h1>
    <div class="sub">来源 StockWe.com / TradesMax &nbsp;·&nbsp; 微信公众号本地存档 &nbsp;·&nbsp; 生成于 <span id="gen"></span></div>
  </header>

  <div class="cards" id="cards"></div>

  <section>
    <h2>月度发文量</h2>
    <div class="chart" id="chart"></div>
    <div class="note">提示:2025-05 之前为零星缓存命中,非连续存档;2025-05 起为连续逐篇归档。</div>
  </section>

  <section>
    <h2>高频标的 (点击筛选)</h2>
    <div class="chips" id="ticks"></div>
  </section>

  <section>
    <h2>文章浏览 · 检索 · 查全文</h2>
    <div class="controls">
      <input type="search" id="q" placeholder="搜索标题 / 摘要 / 正文全文…">
      <select id="month"><option value="">全部月份</option></select>
      <select id="sort">
        <option value="date_desc">按时间↓ (新→旧)</option>
        <option value="date_asc">按时间↑ (旧→新)</option>
        <option value="len_desc">按字数↓</option>
      </select>
    </div>
    <div class="hint" id="count"></div>
    <div id="list"></div>
  </section>
</div>

<script>
const DATA = /*PAYLOAD*/;
const S = DATA.summary, A = DATA.articles;
let activeTick = "", openSet = new Set();

document.getElementById("gen").textContent = S.generated;

// stat cards
const fmt = n => n.toLocaleString("en-US");
document.getElementById("cards").innerHTML = [
  ["文章总数", fmt(S.count) + " <small>篇</small>"],
  ["时间跨度", '<span style="font-size:15px">'+S.date_min+'<br>→ '+S.date_max+'</span>'],
  ["正文总量", fmt(S.total_chars) + " <small>字</small>"],
  ["篇均字数", fmt(S.avg_chars) + " <small>字</small>"],
].map(c => '<div class="card"><div class="k">'+c[0]+'</div><div class="v">'+c[1]+'</div></div>').join("");

// monthly chart
const maxN = Math.max.apply(null, S.months.map(m=>m.n));
document.getElementById("chart").innerHTML = S.months.map(m =>
  '<div class="bar" title="'+m.m+': '+m.n+' 篇"><div class="n">'+m.n+'</div>'+
  '<div class="col" style="height:'+(m.n/maxN*100)+'%"></div>'+
  '<div class="lab">'+m.m+'</div></div>').join("");

// ticker chips
document.getElementById("ticks").innerHTML = S.top_ticks.map(t =>
  '<span class="chip" data-t="'+t.t+'">'+t.t+'<b>'+t.n+'</b></span>').join("");
document.querySelectorAll(".chip").forEach(c => c.onclick = () => {
  const t = c.dataset.t;
  activeTick = (activeTick === t) ? "" : t;
  document.querySelectorAll(".chip").forEach(x => x.classList.toggle("active", x.dataset.t === activeTick));
  render();
});

// month dropdown
const msel = document.getElementById("month");
S.months.slice().reverse().forEach(m => {
  const o = document.createElement("option"); o.value = m.m; o.textContent = m.m+" ("+m.n+")"; msel.appendChild(o);
});

const esc = s => s.replace(/[&<>]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
function hl(s, q){ if(!q) return esc(s); const i = s.toLowerCase().indexOf(q.toLowerCase());
  if(i<0) return esc(s); return esc(s.slice(0,i))+"<mark>"+esc(s.slice(i,i+q.length))+"</mark>"+esc(s.slice(i+q.length)); }

function render(){
  const q = document.getElementById("q").value.trim();
  const mon = document.getElementById("month").value;
  const sort = document.getElementById("sort").value;
  const ql = q.toLowerCase();
  let list = A.filter(a => {
    if(mon && a.ym !== mon) return false;
    if(activeTick && !a.ticks.includes(activeTick)) return false;
    if(ql){ const hay = (a.title+" "+a.desc+" "+a.body).toLowerCase(); if(hay.indexOf(ql)<0) return false; }
    return true;
  });
  if(sort==="date_asc") list.sort((x,y)=> x.time<y.time?-1:1);
  else if(sort==="len_desc") list.sort((x,y)=> y.len-x.len);
  else list.sort((x,y)=> x.time>y.time?-1:1);

  document.getElementById("count").textContent =
    "共 "+list.length+" 篇" + (activeTick?(" · 标的 "+activeTick):"") + (mon?(" · "+mon):"") + (q?(" · 含「"+q+"」"):"");

  const box = document.getElementById("list");
  if(!list.length){ box.innerHTML = '<div class="empty">没有匹配的文章</div>'; return; }
  box.innerHTML = list.map(a => {
    const id = a.path;
    const op = openSet.has(id) ? " open" : "";
    const tks = a.ticks.slice(0,6).map(t=>'<span class="tk">'+t+'</span>').join("");
    let body = a.body || "(正文未抓取)";
    if(q && body.toLowerCase().indexOf(ql)>=0){
      const i = body.toLowerCase().indexOf(ql);
      const start = Math.max(0, i-400);
      body = (start>0?"…":"") + body.slice(start, i+q.length+1200);
    } else { body = body.slice(0, 1600) + (a.body.length>1600?" …":""); }
    return '<div class="item'+op+'" data-id="'+esc(id)+'">'+
      '<div class="head"><div class="meta">'+a.date+'<span class="len">'+fmt(a.len)+' 字</span></div>'+
      '<div class="ti">'+hl(a.title,q)+
        '<span class="d">'+hl(a.desc||"",q)+'</span>'+tks+'</div></div>'+
      '<div class="body">'+esc(body)+
        '<div class="links"><a href="'+esc(a.url)+'" target="_blank" rel="noopener">↗ 原文链接</a>'+
        '<a href="'+esc(a.path.split("sources/news/wechat_mp/")[1]||a.path)+'" target="_blank">📄 本地 Markdown</a></div>'+
      '</div></div>';
  }).join("");
  box.querySelectorAll(".item .head").forEach(h => h.onclick = () => {
    const it = h.parentElement, id = it.dataset.id;
    it.classList.toggle("open");
    if(it.classList.contains("open")) openSet.add(id); else openSet.delete(id);
  });
}

document.getElementById("q").addEventListener("input", render);
document.getElementById("month").addEventListener("change", render);
document.getElementById("sort").addEventListener("change", render);
render();
</script>
</body>
</html>
"""

OUT.write_text(HTML.replace("/*PAYLOAD*/", payload), encoding="utf-8")
print(f"written: {OUT}")
print(f"size: {OUT.stat().st_size/1024:.0f} KB")
print(f"articles embedded: {len(articles)}")
