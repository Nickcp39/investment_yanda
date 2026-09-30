import json, pathlib, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
BASE=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((BASE/'data/industry_analysis.json').read_text(encoding='utf-8'))
names={'Mach':'机械','ElcEq':'电气设备','Aero':'航空器及零件','Ships':'造船与铁路设备','Cnstr':'建筑施工','Util':'公用事业'}
def cagr(r): return math.expm1(sum(math.log1p(x) for x in r)*12/len(r))*100
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'---|'*len(headers)]+['| '+' | '.join(map(str,r))+' |' for r in rows])
rows=[]
for k,n in names.items():
 s=d['summary'][k];rows.append([n,f"{s['cagr']:.2f}%",f"{s['excess']:+.2f}pp",f"{s['win_count']}/91",f"{s['maxdd']:.1f}%"])
summary=table(['行业组合','百年年化','相对市场','十年胜出次数','月末最大回撤'],rows)
era=table(['时期','市场年化','机械差值','电气差值','航空差值','船铁差值','施工差值'],[[e['label'],f"{e['cagr']['Market']:.2f}%",*[f"{e['excess'][k]:+.2f}" for k in ['Mach','ElcEq','Aero','Ships','Cnstr']]]for e in d['eras']])
idx=d['dates'].index('195001');market=cagr(d['monthly']['Market'][idx:])
robust=table(['行业','1926起市值加权','1950起市值加权','1926起等权'],[[n,f"{d['summary'][k]['cagr']:.2f}%",f"{cagr(d['monthly'][k][idx:]):.2f}%",f"{d['summary'][k]['ew_cagr']:.2f}%"]for k,n in names.items()])
(BASE/'data/research_tables.json').write_text(json.dumps({'century':summary,'eras':era,'robustness':robust},ensure_ascii=False,indent=2),encoding='utf-8')
(BASE/'industry_appendix.md').write_text('# 百年行业计算附表\n\n月收益区间 1926-07 至 2026-07，共 1,201 个月。年化为复利年化；收益差是两个 CAGR 相减。\n\n'+summary+'\n\n## 时代收益差（百分点）\n\n'+era+'\n\n## 起点与权重稳健性\n\n'+robust+f'\n\n1950-01 至 2026-07 的市场年化为 {market:.2f}%。等权组合会增加小公司权重，也增加再平衡影响；未经交易成本、规模因子和风险调整，不能称为可实现 alpha。\n',encoding='utf-8')
facts={
 'GE_power':{'years':[2001,2002],'revenue':[20.211,22.926],'orders':[24.5,14.2],'profit':[4.860,6.255],'unit':'USD billion','source':['https://www.ge.com/news/press-releases/ge-2002-earnings-grow-7-151-billion-cashflow-ex-progress-grows-10-152-billion','https://www.sec.gov/Archives/edgar/data/40545/000004054503000016/frm10k.htm']},
 'AMAT_EES':{'years':[2011,2012,2013],'revenue':[1.990,.425,.173],'profit':[.453,-.668,-.433],'unit':'USD billion','source':['https://ir.appliedmaterials.com/static-files/26df7d1f-2c60-4d72-a1ed-3955c633692a']},
 'ASML':{'years':[2008,2009],'equipment':[2.517,1.175],'service':[.437,.421],'unit':'EUR billion','source':['https://www.asml.com/en/news/press-releases/2010/asml-announces-2009-fourth-quarter-and-full-year-results']},
 'CAT':{'years':[2012,2013,2014,2015,2016,2017],'revenue':[65.9,55.7,55.2,47.0,38.5,45.5],'adjusted_margin':[13.9,11.5,11.1,9.6,7.2,12.5],'unit':'USD billion / % adjusted','source':['https://www.caterpillar.com/content/dam/caterpillarDotCom/releases/2Q18%20Caterpillar%20Inc.%20Results%20Presentation%20Slides.pdf']}}
(BASE/'data/case_facts.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2),encoding='utf-8')
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc');plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':190})
fig,axes=plt.subplots(2,2,figsize=(10,7));blue='#235e7c';gold='#d28a36'
ax=axes[0,0]; ax.plot([2001,2002],[20.211,22.926],'-o',label='收入',color=blue);ax.plot([2001,2002],[24.5,14.2],'-o',label='新订单',color=gold);ax.set_title('GE 动力：订单先于收入反转');ax.set_xticks([2001,2002]);ax.set_ylabel('十亿美元');ax.legend()
ax=axes[0,1];x=[0,1,2];ax.bar([i-.18 for i in x],[1.990,.425,.173],width=.35,label='收入',color=blue);ax.bar([i+.18 for i in x],[.453,-.668,-.433],width=.35,label='分部营业利润',color=gold);ax.set_xticks(x,[2011,2012,2013]);ax.axhline(0,c='gray',lw=.6);ax.set_title('AMAT 能源环保：上游也会亏损');ax.set_ylabel('十亿美元');ax.legend(fontsize=8)
ax=axes[1,0];ax.bar([-.18,.82],[2.517,1.175],width=.35,label='设备',color=blue);ax.bar([.18,1.18],[.437,.421],width=.35,label='服务与升级',color=gold);ax.set_xticks([0,1],[2008,2009]);ax.set_title('ASML：存量业务缓冲新增设备衰退');ax.set_ylabel('十亿欧元');ax.legend(fontsize=8)
ax=axes[1,1];ax.plot(range(2012,2018),facts['CAT']['revenue'],'-o',color=blue);ax.set_title('卡特彼勒：强渠道也有四年收入收缩');ax.set_ylabel('十亿美元');ax.set_xticks(range(2012,2018));
for ax in axes.flat: ax.grid(axis='y',alpha=.18)
fig.suptitle('图 4｜看见利润形成的过程，才知道“铲子”是哪一种生意',x=.06,ha='left',fontsize=14,fontweight='bold');fig.tight_layout(rect=(0,0,1,.95));fig.savefig(BASE/'fig7_case_cycles.png');plt.close(fig)
print('Tables and operating-cycle charts built')
