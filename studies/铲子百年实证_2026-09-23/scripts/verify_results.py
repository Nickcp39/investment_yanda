"""验收研究产物。检查算术/边界，不把检查通过当成投资结论成立。"""
import hashlib
import json
import math
import pathlib
import re

BASE=pathlib.Path(__file__).resolve().parents[1]

def main():
    errors=[]; checks=[]
    def check(ok,message):
        checks.append({'check':message,'pass':bool(ok)})
        if not ok: errors.append(message)
    d=json.loads((BASE/'data/rebuilt_returns.json').read_text(encoding='utf-8'))
    series=json.loads((BASE/'data/normalized_usd_monthly.json').read_text(encoding='utf-8'))
    manifest=json.loads((BASE/'data/audit_fetch_manifest.json').read_text(encoding='utf-8'))
    check(d['original_companies']==33 and d['original_with_prices']==32,'原数据公司数33，有价格32')
    check(d['candidate_companies']==41 and d['with_prices']==40,'扩展41候选，40有价格')
    original_sha=hashlib.sha256((BASE/'data/shovel_prices.json').read_bytes()).hexdigest()
    check(original_sha==d['raw_snapshot_sha256'],'原价格快照未改变')
    for rec in manifest:
        if 'path' in rec:
            p=BASE/rec['path']
            check(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256'],f'原始响应哈希 {p.name}')
    check(d['results']['APTV']['status']=='quarantined','APTV分拆隔离')
    check(d['results']['SPR']['status']=='missing','SPR缺失，没有记成零回报')
    check(min(series['HUBB'])>='1995-01','HUBB异常早期序列隔离')
    check(min(series['VRT'])>='2020-03','VRT不把SPAC阶段算作经营历史')
    for tk,values in series.items():
        check(max(values)<='2026-08' and all(v>0 and math.isfinite(v) for v in values.values()),f'完整月和有限正财富 {tk}')
    for tk,r in d['results'].items():
        if 'longest' not in r: continue
        for label,m in [('longest',r['longest'])]+list(r['fixed_years'].items()):
            if m is None: continue
            a,b=series[tk],series['SPY']; n=m['months']
            x=100*((a[m['end']]/a[m['start']])**(12/n)-1)
            y=100*((b[m['end']]/b[m['start']])**(12/n)-1)
            check(abs(x-y-m['excess_pp'])<1e-8,f'同端点独立复算 {tk} {label}')
            if label!='longest':
                check(n==int(label)*12 and m['missing_months']==0,f'共同窗口完整 {tk} {label}')
    raw=json.loads((BASE/'data/audit_raw/KRW_daily.json').read_text(encoding='utf-8'))['chart']['result'][0]
    fx=[v for v in raw['indicators']['adjclose'][0]['adjclose'] if v is not None]
    check(all(100<v<10000 for v in fx),'韩元日线无月线数量级异常；范围检查不代替独立核验')
    report=(BASE/'report.md').read_text(encoding='utf-8')
    for tk in ['HUBB','TDG','ENPH','CIEN','ASML','LRCX','KLAC','CAT','ETN','HEI','SLB','HAL','FLR','MGA','WAB','ROK','DE','AMAT']:
        value=d['results'][tk]['fixed_years']['10']['excess_pp']
        check(f'{abs(value):.2f}' in report,f'正文十年数字对应输出 {tk}')
    for name in ['report.md','README.md','DATA_AUDIT.md','claim_ledger.md','section19_replacement.md']:
        text=(BASE/name).read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if not target.startswith(('http:','https:','#')):
                check((BASE/target.split('#')[0]).exists(),f'本地链接 {name} -> {target}')
    for name in ['report.md','fig1_excess_return_by_lock.svg','scripts/fetch_data.py','scripts/analyze.py','scripts/gen_chart.py']:
        check((BASE/'archive/v1'/name).exists(),f'原稿归档 {name}')
    for name in ['fig2_common_window.svg','fig2_common_window.png','fig3_cisco_entry_sensitivity.svg','fig3_cisco_entry_sensitivity.png']:
        check((BASE/name).stat().st_size>1000,f'生成图非空 {name}')
    output={'status':'PASS' if not errors else 'FAIL','checks':len(checks),'errors':errors,
            'scope':'计算与本地工件验收；不验证护城河因果、供应商全部复权、完整历史总回报或投资建议',
            'known_open_items':['HUBB早期复权异常','RR配股现金流','APTV及其他分拆财富','SPR历史序列','韩华重组','同源价格尚未全面独立核验','幸存者/时点分类/估值与风险因子控制'],
            'details':checks}
    (BASE/'data/verification.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k!='details'},ensure_ascii=True,indent=2))
    raise SystemExit(bool(errors))

if __name__=='__main__': main()
