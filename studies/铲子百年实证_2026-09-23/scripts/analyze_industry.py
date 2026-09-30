"""Preselected FF49 industry proxies; monthly total returns, nominal USD.
No claim that industry SIC portfolios identify a causal upstream premium.
"""
import csv, io, json, math, pathlib, statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
BASE=pathlib.Path(__file__).resolve().parents[1]
RAW=BASE/'data/industry_raw'
NAMES={'Mach':'机械','ElcEq':'电气设备','Aero':'航空器及零件','Ships':'造船与铁路设备','Cnstr':'建筑施工','Util':'公用事业'}
def parse(path, marker=None):
    lines=path.read_text().splitlines()
    if marker: lines=lines[next(i for i,x in enumerate(lines) if marker in x)+1:]
    start=next(i for i,x in enumerate(lines) if x.strip().startswith(','))
    header=[s.strip() for s in lines[start].split(',')][1:]
    rows={}
    for line in lines[start+1:]:
        if not line.strip(): continue
        bits=[x.strip() for x in line.split(',')]
        if len(bits[0])==6 and bits[0].isdigit():
            rows[bits[0]]={k:float(v)/100 for k,v in zip(header,bits[1:]) if float(v) not in (-99.99,-999)}
        elif rows: break
    return rows
vw=parse(RAW/'ff49.txt','Average Value Weighted Returns -- Monthly')
ew=parse(RAW/'ff49.txt','Average Equal Weighted Returns -- Monthly')
fac=parse(RAW/'factors.txt')
dates=sorted(set(vw)&set(fac))
assert dates[0]=='192607' and all(k in vw[d] for d in dates for k in NAMES)
assert len(dates)==(int(dates[-1][:4])-1926)*12+int(dates[-1][4:])-7+1
series={k:[vw[d][k] for d in dates] for k in NAMES}
series['Market']=[fac[d]['Mkt-RF']+fac[d]['RF'] for d in dates]
def cagr(r): return math.expm1(sum(math.log1p(x) for x in r)*12/len(r))*100
def stats(r):
    wealth=peak=1.; maxdd=0.; peakidx=-1; trough=-1; start=-1
    for i,x in enumerate(r):
        wealth*=1+x
        if wealth>peak: peak=wealth; peakidx=i
        dd=wealth/peak-1
        if dd<maxdd: maxdd=dd; start=peakidx; trough=i
    return {'cagr':cagr(r),'multiple':wealth,'maxdd':maxdd*100,'peak':dates[start] if start>=0 else '192606','trough':dates[trough]}
summary={k:stats(r) for k,r in series.items()}
rolling={k:[] for k in NAMES}
for i,d in enumerate(dates):
    if d.endswith('07') and i+120<=len(dates):
        for k in NAMES:
            rolling[k].append({'start':d,'end':dates[i+119],'excess':cagr(series[k][i:i+120])-cagr(series['Market'][i:i+120])})
for k in NAMES:
    s=summary[k]; s['excess']=s['cagr']-summary['Market']['cagr']; s['ew_cagr']=cagr([ew[d][k] for d in dates])
    s['win_count']=sum(x['excess']>0 for x in rolling[k]); s['window_count']=len(rolling[k]); s['win_pct']=100*s['win_count']/s['window_count']
    s['rolling_median']=statistics.median(x['excess'] for x in rolling[k])
eras=[]
for a,b,label in [(1926,1929,'1926-1929'),(1930,1949,'1930-1949'),(1950,1969,'1950-1969'),(1970,1981,'1970-1981'),(1982,1999,'1982-1999'),(2000,2002,'2000-2002'),(2003,2007,'2003-2007'),(2008,2019,'2008-2019'),(2020,2022,'2020-2022'),(2023,2026,'2023-2026.07')]:
    idx=[i for i,d in enumerate(dates) if a<=int(d[:4])<=b]
    vals={k:cagr([r[i] for i in idx]) for k,r in series.items()}
    eras.append({'label':label,'start':dates[idx[0]],'end':dates[idx[-1]],'months':len(idx),'cagr':vals,'excess':{k:vals[k]-vals['Market'] for k in NAMES}})
out={'start':dates[0],'end':dates[-1],'months':len(dates),'summary':summary,'eras':eras,'rolling':rolling,'dates':dates,'monthly':series}
(BASE/'data/industry_analysis.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
with (BASE/'data/industry_monthly.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['month',*series]); w.writerows([[d,*[series[k][i] for k in series]] for i,d in enumerate(dates)])
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':180})
colors=['#235e7c','#d28a36','#378575','#8c698d','#b95b56','#8c929d']
fig,ax=plt.subplots(figsize=(10,4.8))
xx=[int(d[:4])+(int(d[4:])-1)/12 for d in dates]
for k,c in zip(NAMES,colors):
    rel=[]; v=1
    for a,b in zip(series[k],series['Market']): v*=(1+a)/(1+b); rel.append(v)
    ax.plot(xx,rel,label=NAMES[k],color=c,lw=1.5)
ax.set_yscale('log'); ax.axhline(1,color='#555555',lw=.8,ls='--'); ax.set_ylabel('相对市场财富倍数（起点=1，对数刻度）'); ax.set_xlim(1926,2027); ax.grid(alpha=.18); ax.legend(ncol=3,loc='upper left',fontsize=9)
ax.set_title('图 1｜上游相关行业并没有一条共同的百年赢家曲线',loc='left',fontweight='bold',pad=12)
fig.tight_layout();fig.savefig(BASE/'fig4_century_relative.png');plt.close(fig)
fig,ax=plt.subplots(figsize=(10,5.4)); matrix=[[e['excess'][k] for e in eras] for k in NAMES]
im=ax.imshow(matrix,cmap='RdYlGn',vmin=-20,vmax=20,aspect='auto')
ax.set_yticks(range(6),list(NAMES.values()));ax.set_xticks(range(len(eras)),[e['label'] for e in eras],rotation=35,ha='right')
for y,row in enumerate(matrix):
    for x,v in enumerate(row): ax.text(x,y,f'{v:+.1f}',ha='center',va='center',fontsize=9,color='black')
ax.set_title('图 2｜时代切换会改写赢家：各时期年化收益差（百分点）',loc='left',pad=12,fontweight='bold');fig.colorbar(im,ax=ax,label='相对美国股票市场的年化收益差');fig.tight_layout();fig.savefig(BASE/'fig5_era_heatmap.png');plt.close(fig)
fig,ax=plt.subplots(figsize=(10,4.6))
for k,c in zip(NAMES,colors):ax.plot([int(r['start'][:4]) for r in rolling[k]],[r['excess'] for r in rolling[k]],label=NAMES[k],color=c,lw=1.4)
ax.axhline(0,color='#555555',lw=.8);ax.set_xlabel('持有期起始年份（每年 7 月；持有 120 个月）');ax.set_ylabel('十年年化收益差（百分点）');ax.legend(ncol=3,fontsize=9);ax.grid(alpha=.18);ax.set_title('图 3｜同一个行业，换一代投资者就可能换一个结论',loc='left',pad=12,fontweight='bold');fig.tight_layout();fig.savefig(BASE/'fig6_rolling_decade.png');plt.close(fig)
print(json.dumps({'months':len(dates),'end':dates[-1],'summary':summary,'eras':eras},ensure_ascii=False,indent=2))
