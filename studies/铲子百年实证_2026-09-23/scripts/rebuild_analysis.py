"""描述性收益重建。精确月份交集、完整月、SPY复权、外币换美元、沿革限制。
不把供应商复权当作已审核的全部分拆/退市现金流，不推断因果或组合业绩。
"""
import datetime as dt
import hashlib
import json
import math
import pathlib
import statistics

BASE = pathlib.Path(__file__).resolve().parents[1]
END = '2026-08'
EXTRA = ['ASML', 'LRCX', 'KLAC', 'HEI', 'WAB', 'FLR', 'ROK', 'DE']
# Conservative business-identity start dates, not corrections to legal shareholder TSR.
FLOORS = {'GE':'2024-04','RTX':'2020-04','HWM':'2020-04','GEV':'2024-04',
          'VRT':'2020-03','BKR':'2017-08','APTV':'2017-12','HUBB':'1995-01'}
NOTES = {'GE':'2024分拆后；不是1970年以来纯航空', 'RTX':'2020合并/分拆后',
         'HWM':'2020分拆后', 'GEV':'2024独立上市后', 'VRT':'2020经营资产合并后，去除SPAC',
         'BKR':'2017合并后', 'APTV':'2017分拆后；后续沿革仍须审核',
         'HUBB':'1994异常月跳变前数据隔离；非已修复',
         'RR.L':'2020配股/认购权现金流未独立重建',
         '042660.KS':'重组/停牌/增资历史待核',
         '329180.KS':'2021上市，短窗口', 'ROK':'早期集团沿革不等于当前自动化业务',
         'WAB':'并购改变业务组合；不是19世纪铁路回报',
         'ASML':'美元交易证券；股息税/费用未单列'}
FX = {'GBP':('GBPUSD=X',False,1), 'GBp':('GBPUSD=X',False,0.01),
      'EUR':('EURUSD=X',False,1), 'JPY':('JPY=X',True,1), 'KRW':('KRW=X',True,1)}

def month_no(s):
    return int(s[:4])*12+int(s[5:7])-1

def load_raw(ticker):
    p = BASE/'data/audit_raw'/(ticker.replace('^','_').replace('=','_')+'.json')
    if ticker == 'KRW=X':
        p = BASE/'data/audit_raw/KRW_daily.json'
    if not p.exists():
        return None
    r = json.loads(p.read_text(encoding='utf-8'))['chart']['result'][0]
    # Fixed current offset preserves month boundaries here (US/Europe winter at >=00:00;
    # Asia fixed zones). Convert exchange local time to avoid previous-month UTC labels.
    tz = dt.timezone(dt.timedelta(seconds=r['meta'].get('gmtoffset',0)))
    adj = r['indicators'].get('adjclose',[{}])[0].get('adjclose')
    if adj is None:
        raise ValueError('missing adjclose '+ticker)
    close = r['indicators']['quote'][0]['close']
    rows = {}
    for t,a,c in zip(r['timestamp'],adj,close):
        m = dt.datetime.fromtimestamp(t,tz).strftime('%Y-%m')
        if m<=END and a is not None and a>0 and math.isfinite(a):
            rows[m] = {'adj':a,'close':c,'timestamp':t}
    return {'currency':r['meta'].get('currency'),'name':r['meta'].get('longName',ticker),
            'rows':rows,'meta':r['meta']}

def cagr(vals, months):
    return (vals[-1]/vals[0])**(12/months)-1

def maxdd(vals):
    peak=vals[0]
    worst=0
    for v in vals:
        peak=max(peak,v)
        worst=min(worst,v/peak-1)
    return worst

def metric(stock,bench,start=None,end=END,exact=False):
    keys=sorted(k for k in stock.keys() & bench.keys() if (not start or k>=start) and k<=end)
    if len(keys)<2 or (exact and (keys[0]!=start or keys[-1]!=end)):
        return None
    months=month_no(keys[-1])-month_no(keys[0])
    if not months:
        return None
    a=[stock[k] for k in keys]; b=[bench[k] for k in keys]
    x=cagr(a,months); y=cagr(b,months)
    return {'start':keys[0],'end':keys[-1],'months':months,'observations':len(keys),
            'missing_months':months+1-len(keys),'cagr_pct':100*x,'spy_cagr_pct':100*y,
            'excess_pp':100*(x-y),'relative_wealth_cagr_pct':100*((a[-1]/a[0]/(b[-1]/b[0]))**(12/months)-1),
            'wealth_multiple':a[-1]/a[0], 'monthly_max_drawdown_pct':100*maxdd(a)}

def main():
    original_path=BASE/'data/shovel_prices.json'
    original=json.loads(original_path.read_text(encoding='utf-8'))
    tickers=[k for k in original if k not in ('SPY','^GSPC')]+EXTRA
    raw={k:load_raw(k) for k in tickers+['SPY','^GSPC']+[v[0] for v in FX.values()]}
    bench={k:v['adj'] for k,v in raw['SPY']['rows'].items() if k>='1993-02'}
    normalized={}; results={}; jumps=[]; differences=[]
    for tk in tickers:
        d=raw[tk]
        if d is None:
            results[tk]={'status':'missing','note':'无价格不代表价值归零；需收购/退市现金流'}
            continue
        if tk == 'APTV':
            results[tk]={'status':'quarantined','note':'2026-04分拆Versigent，1股/3股；股东现金流未重建，暂停收益结论'}
            continue
        local={k:v['adj'] for k,v in d['rows'].items()}
        keys=sorted(local)
        for k0,k1 in zip(keys,keys[1:]):
            ret=local[k1]/local[k0]-1
            if ret>1.5 or ret<-.7:
                jumps.append({'ticker':tk,'from':k0,'to':k1,'return_pct':ret*100})
        # Original comparison only US month labels and sufficiently large stored values;
        # intramonth and rounding differences not treated as corruption.
        if tk in original and d['currency']=='USD':
            old={r[0][:7]:r[1] for r in original[tk]['rows'] if r[0][:7]<=END}
            diffs=[(abs(local[k]/v-1),k) for k,v in old.items() if k in local and v>.01]
            if diffs:
                m,k=max(diffs)
                differences.append({'ticker':tk,'max_abs_relative_diff':m,'month':k})
        currency=d['currency']
        if currency=='USD':
            usd=dict(local)
        elif currency in FX:
            ft,invert,scale=FX[currency]
            f=raw[ft]
            usd={k:v*scale*(1/f['rows'][k]['adj'] if invert else f['rows'][k]['adj'])
                 for k,v in local.items() if f and k in f['rows']}
        else:
            results[tk]={'status':'unsupported_currency','currency':currency}
            continue
        floor=FLOORS.get(tk,'1993-02')
        usd={k:v for k,v in usd.items() if k>=floor}
        normalized[tk]=usd
        longest=metric(usd,bench)
        fixed={str(year):metric(usd,bench,f'{2026-year}-08',exact=True) for year in (5,10,20)}
        common=sorted(usd.keys() & bench.keys())
        rolling=[]
        for k in common:
            end=f'{int(k[:4])+10}-{k[5:7]}'
            if end>END:
                continue
            m=metric(usd,bench,k,end,True)
            if m and not m['missing_months']:
                rolling.append(m['excess_pp'])
        loc=metric(local,bench,longest['start'],longest['end'],True) if longest else None
        results[tk]={'status':'vendor_descriptive','name':d['name'],'currency':currency,
                     'note':NOTES.get(tk,'供应商复权；未逐笔核验公司行动'),
                     'longest':longest,'local_cagr_same_window_pct':loc['cagr_pct'] if loc else None,
                     'fixed_years':fixed,'rolling_10y':{'n':len(rolling),
                     'win_fraction':sum(x>0 for x in rolling)/len(rolling) if rolling else None,
                     'min_excess_pp':min(rolling) if rolling else None,
                     'median_excess_pp':statistics.median(rolling) if rolling else None,
                     'max_excess_pp':max(rolling) if rolling else None}}
    sensitivity={k:metric(normalized['CSCO'],bench,k,exact=True)
                 for k in ['1998-03','1999-03','2000-03','2001-03','2002-03','2003-03']}
    gspc={k:v['adj'] for k,v in raw['^GSPC']['rows'].items()}
    benchmark_gap=metric(bench,gspc,'1993-02',exact=True)
    payload={'cutoff_month':END,'method':'Yahoo adjusted monthly values; SPY adjusted benchmark; USD; no current month',
             'original_companies':len(original)-2,'original_with_prices':sum(bool(v['rows']) for k,v in original.items() if k not in ('SPY','^GSPC')),
             'candidate_companies':len(tickers),'with_prices':sum(raw[k] is not None for k in tickers),
             'raw_snapshot_sha256':hashlib.sha256(original_path.read_bytes()).hexdigest(),
             'floors':FLOORS,'results':results,'cisco_start_sensitivity':sensitivity,
             'spy_vs_price_index':benchmark_gap,'large_monthly_jumps':jumps,
             'original_vs_fresh_usd':differences}
    (BASE/'data/rebuilt_returns.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    (BASE/'data/normalized_usd_monthly.json').write_text(json.dumps({'SPY':bench,**normalized},ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# 收益重算附表（自动生成）','',
           '完整月截止 2026-08；美元口径，外股按月末汇率换算。基准为 SPY 复权序列（ETF费用已内含，非指数本身）。',
           '数据是同一供应商复权的描述性结果，非独立核准的股东全现金流；退市/权利/分拆尚有缺口。不同“可用区间”不能横比排名。',
            '最大回撤仅取月度端点，会漏掉月内极值。股票与外汇收盘存在时区差。韩元月线有五个数量级异常点，改用保存的日线逐月最后有效值；不是手工乘倍率。','',
           '| 标的 | 可用区间 | 年化% | SPY% | 差值pp | 月度最大回撤% | 备注 |',
           '|---|---|---:|---:|---:|---:|---|']
    for tk,r in results.items():
        if 'longest' not in r or not r['longest']:
            lines.append(f'| {tk} | 缺失 | — | — | — | — | {r.get("note",r["status"])} |')
            continue
        m=r['longest']
        lines.append(f'| {tk} | {m["start"]}–{m["end"]} | {m["cagr_pct"]:.2f} | {m["spy_cagr_pct"]:.2f} | {m["excess_pp"]:+.2f} | {m["monthly_max_drawdown_pct"]:.1f} | {r["note"]} |')
    lines+=['','## 共同窗口及滚动敏感性','',
            '5/10/20年要求起止月份都存在；“—”不是零回报。10年滚动窗每月移动，彼此重叠，胜率不是独立样本成功概率。',
            '收益差是两个 CAGR 相减，不是风险调整 alpha，也不是组合 CAGR。','',
            '| 标的 | 5年差值pp | 10年差值pp | 20年差值pp | 滚动10年窗数 | 正差值占比 | 最差/中位/最好pp |',
            '|---|---:|---:|---:|---:|---:|---|']
    for tk,r in results.items():
        if 'fixed_years' not in r: continue
        vals=[f'{r["fixed_years"][str(y)]["excess_pp"]:+.2f}' if r['fixed_years'][str(y)] else '—' for y in (5,10,20)]
        rr=r['rolling_10y']; win=f'{100*rr["win_fraction"]:.1f}%' if rr['n'] else '—'
        rng='/'.join(f'{rr[k]:+.2f}' for k in ('min_excess_pp','median_excess_pp','max_excess_pp')) if rr['n'] else '—'
        lines.append(f'| {tk} | '+ ' | '.join(vals)+f' | {rr["n"]} | {win} | {rng} |')
    lines+=['','## Cisco 起点敏感性','', '| 起点→2026-08 | CSCO年化% | SPY年化% | 差值pp |','|---|---:|---:|---:|']
    for k,m in sensitivity.items():
        lines.append(f'| {k} | {m["cagr_pct"]:.2f} | {m["spy_cagr_pct"]:.2f} | {m["excess_pp"]:+.2f} |')
    lines+=['','## 机器质量检查','',f'- 原始清单：{payload["original_companies"]}家公司，其中{payload["original_with_prices"]}家有价格。',
            f'- 扩展清单：{len(tickers)}家公司，其中{payload["with_prices"]}家有价格。',
            '- 大月跳变仅为人工核查警报，不自动判定错误：','']
    lines += [f'- {j["ticker"]}: {j["from"]}→{j["to"]} {j["return_pct"]:+.1f}%' for j in jumps]
    (BASE/'returns_appendix.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    plot(results,sensitivity)
    print(json.dumps({'original_companies':payload['original_companies'],'candidate_companies':len(tickers),
                      'with_prices':payload['with_prices'],'benchmark_gap':benchmark_gap,
                      'cisco':sensitivity,'jumps':jumps},ensure_ascii=False,indent=2))

def plot(results,sensitivity):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    selected=['TDG','AMAT','ASML','LRCX','KLAC','HEI','CAT','DE','HUBB','ETN','WAB','ROK','CSCO','SLB','HAL','FLR','MGA','ENPH','SEDG']
    selected=[k for k in selected if results[k]['fixed_years']['10']]
    vals=[results[k]['fixed_years']['10']['excess_pp'] for k in selected]
    fig,ax=plt.subplots(figsize=(11,7))
    ax.barh(selected[::-1],vals[::-1],color=['#287d76' if v>=0 else '#ac554e' for v in vals[::-1]])
    ax.axvline(0,color='#777',linewidth=.8)
    ax.set_xlabel('CAGR difference vs dividend-adjusted SPY (percentage points)')
    ax.set_title('Same window: August 2016 - August 2026 | USD returns\nSelected examples; no causal lock-group classification',loc='left')
    ax.spines[['top','right']].set_visible(False)
    fig.text(.08,.015,'Source: saved Yahoo monthly responses. Vendor-adjusted data; corporate-action review incomplete.',fontsize=9)
    fig.tight_layout(rect=(0,.04,1,1))
    for ext in ('svg','png'):fig.savefig(BASE/f'fig2_common_window.{ext}',dpi=170)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,4.8))
    keys=list(sensitivity); xs=list(range(len(keys)))
    ax.bar([x-.18 for x in xs],[sensitivity[k]['cagr_pct'] for k in keys],width=.36,label='CSCO')
    ax.bar([x+.18 for x in xs],[sensitivity[k]['spy_cagr_pct'] for k in keys],width=.36,label='SPY')
    ax.set_xticks(xs,keys);ax.set_ylabel('Annualized return (%)');ax.legend()
    ax.set_title('Cisco: moving the entry date changes the result\nAll windows end August 2026; dividend-adjusted USD')
    fig.tight_layout()
    for ext in ('svg','png'):fig.savefig(BASE/f'fig3_cisco_entry_sensitivity.{ext}',dpi=170)
    plt.close(fig)

if __name__=='__main__':
    main()
