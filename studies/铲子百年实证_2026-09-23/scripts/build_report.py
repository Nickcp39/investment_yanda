import pathlib, json, re
BASE=pathlib.Path(__file__).resolve().parents[1]
src=(BASE/'report_source.md').read_text(encoding='utf-8')
tables=json.loads((BASE/'data/research_tables.json').read_text(encoding='utf-8'))
old=(BASE/'archive/v2_audit/report.md').read_text(encoding='utf-8')
modern=old.split('### 6.2')[1].split('## 7.')[0]
modern='41 家候选公司中，40 家取得价格；APTV 因分拆隔离，SPR 缺少完整序列。下表选取业务相关的对照，不是随机样本或可复制组合。共同窗口为 2016-08 至 2026-08，美元供应商复权回报，基准为 SPY；同源复权尚未逐笔独立核验。\n\n### 12.1'+modern
modern=modern.replace('### 6.3','### 12.2').replace('fig2_common_window.svg','fig8_modern_cn.png')
cisco=old.split('## 7.')[1].split('## 8.')[0].split('\n',1)[1]
cisco=cisco.replace('fig3_cisco_entry_sensitivity.svg','fig9_cisco_cn.png')
valuation=old.split('## 8.')[1].split('## 9.')[0]
valuation='### 13.1'+valuation
returns=(BASE/'returns_appendix.md').read_text(encoding='utf-8').split('\n',1)[1].split('## Cisco')[0]
returns=returns.replace('## 共同窗口及滚动敏感性','### B.1 共同窗口及滚动敏感性')
returns=returns.replace('| APTV | 缺失 |','| APTV | 隔离 |')
for k,v in {**tables,'modern':modern,'cisco':cisco,'valuation':valuation,'returns':returns}.items(): src=src.replace('{{'+k+'}}',v)
assert '{{' not in src
# Use ASCII hyphens throughout to avoid missing glyphs in CJK fonts.
src=src.translate(str.maketrans({'−':'-','–':'-','—':'-','‑':'-'}))
(BASE/'report.md').write_text(src,encoding='utf-8')
# Register the exact URLs used, for review and future verification.
urls={}
for title,url in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)',src): urls.setdefault(url,title)
(BASE/'source_index.md').write_text('# 本版直接来源索引\n\n经营数据由正文所链接财报/公告/监管材料支持；行业回报由官方文件复算。\n\n'+'\n'.join(f'{i}. [{title}]({url})' for i,(url,title) in enumerate(urls.items(),1))+'\n',encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
r=json.loads((BASE/'data/rebuilt_returns.json').read_text(encoding='utf-8'))
selected=['LRCX','KLAC','ASML','AMAT','HEI','TDG','CAT','DE','ETN','HUBB','CSCO','ENPH','CIEN','SLB','HAL','FLR','MGA','WAB','ROK']
vals=[r['results'][k]['fixed_years']['10']['excess_pp'] for k in selected]
fig,ax=plt.subplots(figsize=(10,6.4));ax.barh(selected[::-1],vals[::-1],color=['#378575' if v>=0 else '#b95b56' for v in vals[::-1]]);ax.axvline(0,c='#666666',lw=.8)
for i,v in enumerate(vals[::-1]):ax.text(v+(.35 if v>=0 else -.35),i,f'{v:+.1f}',ha='left' if v>=0 else 'right',va='center',fontsize=8)
ax.set_xlim(min(vals)-5,max(vals)+5);ax.set_xlabel('相对 SPY 的复利年化收益差（百分点）');ax.set_title('图 5｜共同十年窗口的公司对照',loc='left',fontweight='bold',pad=13);ax.grid(axis='x',alpha=.15);fig.tight_layout();fig.savefig(BASE/'fig8_modern_cn.png',dpi=190);plt.close(fig)
s=r['cisco_start_sensitivity'];keys=list(s);x=list(range(len(keys)));fig,ax=plt.subplots(figsize=(10,4.3));ax.bar([i-.18 for i in x],[s[k]['cagr_pct'] for k in keys],width=.36,label='Cisco',color='#235e7c');ax.bar([i+.18 for i in x],[s[k]['spy_cagr_pct'] for k in keys],width=.36,label='SPY',color='#d28a36');ax.set_xticks(x,keys);ax.set_ylabel('复利年化回报（%）');ax.set_xlabel('买入月；所有窗口均持有至 2026-08');ax.legend();ax.set_title('图 6｜Cisco：改变进入月份，就改变长期投资结果',loc='left',fontweight='bold',pad=12);ax.grid(axis='y',alpha=.15);fig.tight_layout();fig.savefig(BASE/'fig9_cisco_cn.png',dpi=190);plt.close(fig)
print(json.dumps({'characters':len(src),'sources':len(urls),'figures':len(re.findall(r'!\[',src))},ensure_ascii=False))
