# -*- coding: utf-8 -*-
"""Build the TradesMax 2026 必买14只股 performance scorecard (HTML) from
logs/mg2026_prices.json (Yahoo data) + episode/entry/target metadata.
As-of: latest close in the price data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRICES = json.loads((ROOT / "logs/mg2026_prices.json").read_text(encoding="utf-8"))
OUT = ROOT / "sources/channels/tradesmax/track_record_2026.html"

EP = {  # ticker -> (episode, video_url)
    "RMBS":("上集","https://www.youtube.com/watch?v=GDzegfS0ZPE"),
    "HROW":("上集","https://www.youtube.com/watch?v=GDzegfS0ZPE"),
    "SANM":("上集","https://www.youtube.com/watch?v=GDzegfS0ZPE"),
    "ONDS":("上集","https://www.youtube.com/watch?v=GDzegfS0ZPE"),
    "NVDA":("上集","https://www.youtube.com/watch?v=GDzegfS0ZPE"),
    "AEP":("中集","https://www.youtube.com/watch?v=TaX5DM5dQlg"),
    "MU":("中集","https://www.youtube.com/watch?v=TaX5DM5dQlg"),
    "GLW":("中集","https://www.youtube.com/watch?v=TaX5DM5dQlg"),
    "RDW":("中集","https://www.youtube.com/watch?v=TaX5DM5dQlg"),
    "TTMI":("下集","https://www.youtube.com/watch?v=JoBRgakmD58"),
    "INOD":("下集","https://www.youtube.com/watch?v=JoBRgakmD58"),
    "PLAB":("下集","https://www.youtube.com/watch?v=JoBRgakmD58"),
    "NBIS":("下集","https://www.youtube.com/watch?v=JoBRgakmD58"),
    "SMR":("下集","https://www.youtube.com/watch?v=JoBRgakmD58"),
}
# recommended / VIP entry price stated in the video/post (None = not given -> use pub close)
ENTRY = {"ONDS":7.60,"RDW":7.66,"TTMI":66.86,"INOD":60.0,"PLAB":30.0,"NBIS":80.0,"SMR":18.0}
TARGET = {"TTMI":120,"INOD":150,"PLAB":53,"NBIS":200,"SMR":50}  # 下集 stated targets
NOTE = {"MU":"二次推荐(2025已+240%)","INOD":"二次推荐(2025+168%)","NBIS":"二次推荐(2025翻3倍)",
        "NVDA":"大盘价值重估 bonus","ONDS":"VIP $7.60 介入","RDW":"VIP $7.66 介入",
        "TTMI":"VIP 12-26 $66.86"}
COMPANY_CN = {"RMBS":"Rambus 内存接口","HROW":"Harrow 眼科药","SANM":"Sanmina EMS制造",
    "ONDS":"Ondas 国防无人机","NVDA":"英伟达 AI GPU","AEP":"美国电力 AEP","MU":"美光 存储/HBM",
    "GLW":"康宁 光纤/材料","RDW":"Redwire 太空基建","TTMI":"TTM 高端PCB","INOD":"Innodata AI数据",
    "PLAB":"Photronics 掩模版","NBIS":"Nebius AI云","SMR":"NuScale 小型核电"}

# benchmark blended (equal-weight by episode date) — computed in chat
BENCH = {"SPY":8.6,"QQQ":19.7}
SPY_BY_EP = {"上集":9.5,"中集":8.3,"下集":7.9}
QQQ_BY_EP = {"上集":20.6,"中集":19.4,"下集":19.1}

rows=[]
for r in PRICES:
    t=r["t"]; ep,url=EP[t]
    pc=r["pub_close"]; today=r["today"]; ret=r["ret"]; hi=r["hi"]; lo=r["lo"]
    entry=ENTRY.get(t) or pc
    ret_entry=(today-entry)/entry*100
    maxgain=(hi-pc)/pc*100
    tgt=TARGET.get(t)
    tgt_hit = (today>=tgt) if tgt else None
    tgt_hit_ever = (hi>=tgt) if tgt else None
    rows.append({"t":t,"co":COMPANY_CN.get(t,r["co"]),"ep":ep,"url":url,"pub_date":r["pub_date"],
        "pub_close":pc,"today":today,"today_date":r["today_date"],"ret":ret,"hi":hi,"lo":lo,
        "entry":entry,"entry_given":t in ENTRY,"ret_entry":ret_entry,"maxgain":maxgain,
        "target":tgt,"tgt_hit":tgt_hit,"tgt_hit_ever":tgt_hit_ever,
        "spy":SPY_BY_EP[ep],"qqq":QQQ_BY_EP[ep],"note":NOTE.get(t,"")})

rows.sort(key=lambda x:x["ret"], reverse=True)
asof = max(r["today_date"] for r in PRICES)
rets=[r["ret"] for r in rows]
winners=[r for r in rows if r["ret"]>0]
n=len(rows)
avg=sum(rets)/n
srt=sorted(rets); med=(srt[n//2-1]+srt[n//2])/2 if n%2==0 else srt[n//2]
summary={"asof":asof,"n":n,"win":len(winners),"hit":len(winners)/n*100,"avg":avg,"med":med,
         "spy":BENCH["SPY"],"qqq":BENCH["QQQ"],"best":rows[0],"worst":rows[-1],
         "over50":sum(1 for r in rows if r["ret"]>=50)}
payload=json.dumps({"summary":summary,"rows":rows},ensure_ascii=False)

HTML=r"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TradesMax 2026 必买14只股 · 战绩复盘</title>
<style>
:root{--bg:#0f1419;--panel:#1a2029;--panel2:#222b36;--line:#2c3744;--ink:#e6edf3;--muted:#8b98a5;
--accent:#4ca3ff;--green:#3fb950;--red:#f85149;--gold:#ffb454}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-size:14px;line-height:1.6;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif}
.wrap{max-width:1200px;margin:0 auto;padding:24px 20px 80px}
h1{margin:0 0 4px;font-size:22px}.sub{color:var(--muted);font-size:13px;margin-bottom:18px}
.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:18px 0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.card .k{color:var(--muted);font-size:12px}.card .v{font-size:24px;font-weight:700;margin-top:3px}
.card .v small{font-size:12px;color:var(--muted);font-weight:400}
.up{color:var(--green)}.dn{color:var(--red)}.gold{color:var(--gold)}
section{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:16px 0}
h2{margin:0 0 14px;font-size:15px;color:var(--accent)}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:8px 9px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
th{color:var(--muted);font-weight:600;cursor:pointer;user-select:none;position:sticky;top:0;background:var(--panel)}
th:hover{color:var(--accent)}td.l,th.l{text-align:left}
tr:hover td{background:var(--panel2)}
.tk{font-weight:700}.tk a{color:var(--ink);text-decoration:none}.tk a:hover{color:var(--accent)}
.ep{font-size:11px;color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:1px 6px}
.bar{display:flex;align-items:center;gap:2px}
.barfill{height:14px;border-radius:3px;min-width:2px}
.note{color:var(--muted);font-size:11px}
.pill{display:inline-block;border-radius:4px;padding:1px 7px;font-size:11px;font-weight:600}
.pill.hit{background:rgba(63,185,80,.15);color:var(--green)}
.pill.miss{background:rgba(248,81,73,.12);color:var(--red)}
.legend{color:var(--muted);font-size:12px;margin-top:10px}
ul.notes{color:#cdd9e5;font-size:13px;margin:6px 0 0;padding-left:18px}
ul.notes li{margin:4px 0}
.win{color:var(--green)}.lose{color:var(--red)}
</style></head><body><div class="wrap">
<h1>TradesMax「2026 必买股」战绩复盘</h1>
<div class="sub">美股投资网 / StockWe · 上中下集 14 只 · 发布日收盘→<b id="asof"></b> 收盘 · 数据 Yahoo Finance · 等权、未计股息</div>
<div class="cards" id="cards"></div>
<section><h2>个股收益(发布日→今天,按涨幅排序)</h2><div id="chart"></div>
<div class="legend">绿=涨 红=跌 · 灰条=区间最高(若止盈可达的涨幅)</div></section>
<section><h2>明细表(点表头排序)</h2>
<div style="overflow-x:auto"><table id="tbl"><thead><tr>
<th class="l" data-k="t">代码</th><th class="l" data-k="ep">集</th><th data-k="pub_date">发布日</th>
<th data-k="pub_close">发布close</th><th data-k="today">今日</th><th data-k="ret">收益%</th>
<th data-k="maxgain">区间最高%</th><th data-k="ret_entry">按建议入场%</th>
<th data-k="spy">同期SPY</th><th data-k="target">目标价</th><th class="l">备注</th>
</tr></thead><tbody></tbody></table></div></section>
<section><h2>结论</h2><ul class="notes" id="concl"></ul></section>
</div>
<script>
const D=/*PAYLOAD*/;const S=D.summary,R=D.rows;
document.getElementById("asof").textContent=S.asof;
const f1=x=>(x>=0?"+":"")+x.toFixed(1);
const cls=x=>x>=0?"up":"dn";
document.getElementById("cards").innerHTML=[
 ["命中率",`<span class="${S.hit>=50?'up':'dn'}">${S.win}/${S.n}</span> <small>${S.hit.toFixed(0)}%</small>`],
 ["等权平均收益",`<span class="${cls(S.avg)}">${f1(S.avg)}%</span>`],
 ["中位数",`<span class="${cls(S.med)}">${f1(S.med)}%</span>`],
 ["同期 SPY / QQQ",`<span class="up" style="font-size:18px">+${S.spy}% / +${S.qqq}%</span>`],
 [">50% 大涨",`<span class="gold">${S.over50}</span> <small>只</small>`],
].map(c=>`<div class="card"><div class="k">${c[0]}</div><div class="v">${c[1]}</div></div>`).join("");
// chart
const mx=Math.max(...R.map(r=>Math.max(Math.abs(r.ret),r.maxgain)));
document.getElementById("chart").innerHTML=R.map(r=>{
 const w=Math.abs(r.ret)/mx*100, wm=r.maxgain/mx*100;
 const col=r.ret>=0?"var(--green)":"var(--red)";
 return `<div style="display:grid;grid-template-columns:120px 1fr 70px;gap:10px;align-items:center;margin:3px 0">
  <div class="l" style="text-align:left"><span class="tk">${r.t}</span> <span class="note">${r.ep}</span></div>
  <div class="bar"><div class="barfill" style="width:${wm}%;background:#33404d" title="区间最高 +${r.maxgain.toFixed(0)}%"></div>
   <div class="barfill" style="width:${w}%;background:${col};margin-left:-${wm>w?(wm-w):0}%"></div></div>
  <div style="text-align:right;font-weight:700;color:${col}">${f1(r.ret)}%</div></div>`;
}).join("");
// table
function render(rows){
 document.querySelector("#tbl tbody").innerHTML=rows.map(r=>`<tr>
 <td class="l tk"><a href="${r.url}" target="_blank" title="点开视频">${r.t}</a><div class="note">${r.co}</div></td>
 <td class="l"><span class="ep">${r.ep}</span></td>
 <td>${r.pub_date.slice(5)}</td><td>$${r.pub_close.toFixed(2)}</td><td>$${r.today.toFixed(2)}</td>
 <td class="${cls(r.ret)}" style="font-weight:700">${f1(r.ret)}%</td>
 <td class="gold">+${r.maxgain.toFixed(0)}%</td>
 <td class="${cls(r.ret_entry)}">${f1(r.ret_entry)}%${r.entry_given?'':'<span class="note">*</span>'}</td>
 <td class="note">+${r.spy}%</td>
 <td>${r.target?('$'+r.target+' '+(r.tgt_hit?'<span class="pill hit">达标</span>':(r.tgt_hit_ever?'<span class="pill hit">曾达</span>':'<span class="pill miss">未到</span>'))):'<span class="note">—</span>'}</td>
 <td class="l note">${r.note}</td></tr>`).join("");
}
render(R);
let asc={};
document.querySelectorAll("#tbl th[data-k]").forEach(th=>th.onclick=()=>{
 const k=th.dataset.k;asc[k]=!asc[k];
 const s=[...R].sort((a,b)=>{let x=a[k],y=b[k];if(typeof x==="string")return asc[k]?x.localeCompare(y):y.localeCompare(x);return asc[k]?x-y:y-x;});
 render(s);
});
document.querySelector('#tbl th[data-k="ret_entry"]').insertAdjacentHTML('beforeend','');
// conclusions
const big=R.filter(r=>r.ret>=50).map(r=>r.t+" "+f1(r.ret)+"%").join("、");
const lose=R.filter(r=>r.ret<0).map(r=>r.t+" "+f1(r.ret)+"%").join("、");
document.getElementById("concl").innerHTML=[
 `<b>命中率 ${S.win}/${S.n} (${S.hit.toFixed(0)}%)</b>,等权平均 <span class="win">${f1(S.avg)}%</span>(约 5.4 个月),中位数 ${f1(S.med)}%。`,
 `<b>大幅跑赢大盘</b>:同窗口 SPY 仅 +${S.spy}%、QQQ +${S.qqq}%;这个篮子等权 ${f1(S.avg)}%,是 QQQ 的约 3 倍。`,
 `<b>典型幂律分布</b>:收益主要来自 5 只 >50% 的大牛(${big});其余贡献有限——他们的真本事在"挑出大牛股",不是"颗颗都中"。`,
 `<b>亏损 4 只</b>:${lose}。小盘投机股(SMR/ONDS)和个别二次推荐(无)命中差,大中盘 AI 主题(MU/NBIS/GLW/TTMI)才是 edge 所在。`,
 `<b>二次推荐分化</b>:MU 去年+240%今年再 <span class="win">+247%</span>、NBIS 去年翻3倍今年再 <span class="win">+176%</span>——但同为二次推荐的票也可能哑火,不能闭眼复制。`,
 `<span class="note">* 按建议入场%:仅 ONDS/RDW/TTMI/INOD/PLAB/NBIS/SMR 视频给了入场价,其余用发布日 close 代替。未计股息;"区间最高%"为发布日后盘中最高,用于检验"若止盈"的口径。</span>`,
].map(s=>`<li>${s}</li>`).join("");
</script></body></html>"""
OUT.write_text(HTML.replace("/*PAYLOAD*/",payload),encoding="utf-8")
print("written:",OUT)
print(f"hit {summary['win']}/{summary['n']} ({summary['hit']:.0f}%) avg {summary['avg']:+.1f}% median {summary['med']:+.1f}%")
print("best:",summary['best']['t'],f"{summary['best']['ret']:+.1f}%","worst:",summary['worst']['t'],f"{summary['worst']['ret']:+.1f}%")
