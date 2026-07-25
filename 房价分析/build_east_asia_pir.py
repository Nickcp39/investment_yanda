# -*- coding: utf-8 -*-
"""
东亚房价收入比(PIR)跨国对比 — 数据整合与出图
运行目录: 房价分析/
产出: output/pir_east_asia_aligned.png, output/pir_east_asia_absolute.png,
      data/computed_pir_series.csv
"""
import json, sys, math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

sys.path.insert(0, 'data')
from anchors_and_chains import (CN_DEC_YOY, CN_2026_JUN_YOY, TW_TAIPEI_PIR,
                                JP_TOKYO_PIR, US_PIR_ANCHOR)

plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

OUT = {}   # name -> (x_years[np.array], pir[np.array])  x in calendar years (float)

# ---------------- 中国一线 (易居口径锚点 + 统计局二手房年度链) ----------------
CN_ANCH_2015 = {'深圳': 27.7, '北京': 18.1, '上海': 20.8, '广州': 11.1}  # 易居2015榜
CN_PEAK_2021 = {'深圳': 37.0, '北京': 25.0, '上海': 24.0, '广州': 17.0}  # 易居口径峰
G_POST = 0.04  # 2021后名义收入增速假设

for city in ['深圳', '北京', '上海', '广州']:
    years = [2014] + list(range(2015, 2026))
    P = [100.0]
    for y in range(2015, 2026):
        P.append(P[-1] * CN_DEC_YOY[y][city] / 100.0)
    # 2026H1: P(Jun26) = P(Jun25) * YoY;  P(Jun25) ~ 几何插值(Dec24, Dec25)
    p_jun25 = math.sqrt(P[-2] * P[-1])
    p_jun26 = p_jun25 * CN_2026_JUN_YOY[city] / 100.0
    years.append(2026.5); P.append(p_jun26)
    P = np.array(P); years = np.array(years, dtype=float)
    i15 = list(years).index(2015); i21 = list(years).index(2021)
    # 峰前收入增速: 由2015与2021两锚点校准
    ratio_price = P[i21] / P[i15]
    ratio_pir = CN_PEAK_2021[city] / CN_ANCH_2015[city]
    g_pre = (ratio_price / ratio_pir) ** (1 / 6.0) - 1
    pir = np.zeros_like(P)
    for k, y in enumerate(years):
        if y <= 2021:
            pir[k] = CN_PEAK_2021[city] * (P[k] / P[i21]) / ((1 + g_pre) ** (y - 2021))
        else:
            pir[k] = CN_PEAK_2021[city] * (P[k] / P[i21]) / ((1 + G_POST) ** (y - 2021))
    m = years >= 2015
    OUT[city] = (years[m], pir[m])
    print(f'{city}: g_pre={g_pre*100:.1f}%/yr  2015={pir[i15]:.1f} 峰2021={pir[i21]:.1f} 2026H1={pir[-1]:.1f}')

# ---------------- 韩国首尔 (KB公寓指数 + KB中位收入, 锚2021-12 PIR=19.0) ----------------
kr_p = pd.read_csv('data/kr_kb_seoul_apt_index.csv', dtype={'date': str})
kr_p['dt'] = pd.to_datetime(kr_p['date'], format='%Y%m')
kr_i = pd.read_csv('data/kr_kb_income_raw.csv')
kr_i['dt'] = pd.to_datetime(kr_i['날짜'])
kr = kr_p.merge(kr_i[['dt', '중위가구월소득금액']], on='dt', how='left')
kr = kr[kr['dt'] >= '2009-01-01'].copy()
kr['inc'] = kr['중위가구월소득금액'].ffill()
a = kr[kr['dt'] == '2021-12-01'].iloc[0]
kr['pir'] = 19.0 * (kr['idx'] / a['idx']) / (kr['inc'] / a['inc'])
kr = kr.dropna(subset=['pir'])
kr['q'] = kr['dt'].dt.to_period('Q')
krq = kr.groupby('q', as_index=False).agg(pir=('pir', 'mean'))
krq['x'] = krq['q'].map(lambda p: p.year + (p.quarter - 0.5) / 4)
OUT['首尔'] = (krq['x'].values, krq['pir'].values)
pk = kr.loc[kr['pir'].idxmax()]
print(f"首尔: 峰 {pk['dt'].date()} PIR={pk['pir']:.1f}  最新 {kr['dt'].iloc[-1].date()} PIR={kr['pir'].iloc[-1]:.1f}")

# ---------------- 台湾台北 (内政部改版口径锚点, 线性插值到季度) ----------------
tw_pts = sorted(TW_TAIPEI_PIR.items())
tw_x = np.union1d(np.arange(2015.0, 2026.01, 0.25), [p[0] for p in tw_pts])
tw_y = np.interp(tw_x, [p[0] for p in tw_pts], [p[1] for p in tw_pts])
OUT['台北'] = (tw_x, tw_y)

# ---------------- 新加坡 (HDB转售指数 / URA私宅指数 + SingStat中位收入) ----------------
hdb = pd.DataFrame(json.load(open('data/sg_HDB_RPI.json')))
hdb['index'] = hdb['index'].astype(float)
hdb['x'] = hdb['quarter'].map(lambda q: int(q[:4]) + (int(q[-1]) - 0.5) / 4)
ura = pd.DataFrame(json.load(open('data/sg_URA_PPI.json')))
ura = ura[ura['property_type'] == 'All Residential'].copy()
ura['index'] = ura['index'].astype(float)
ura['x'] = ura['quarter'].map(lambda q: int(q[:4]) + (int(q[-1]) - 0.5) / 4)
inc_rows = json.load(open('data/sg_income_key_indicators.json'))
med = [r for r in inc_rows if r['DataSeries'].startswith('Median Monthly Household Employment Income Including')][0]
sg_inc_y = {int(k): float(v) for k, v in med.items() if k.isdigit()}
sg_inc_y[2026] = sg_inc_y[2025] * 1.04


def sg_income(x):
    yrs = sorted(sg_inc_y)
    return np.interp(x, [y + 0.5 for y in yrs], [sg_inc_y[y] for y in yrs])


for name, df_, anchor in [('新加坡组屋', hdb, 4.35), ('新加坡私宅', ura, 13.0)]:
    d = df_[df_['x'] >= 2000].copy()
    a_idx = d[(d['x'] > 2025) & (d['x'] < 2026)]['index'].mean()  # 2025均值为锚
    a_inc = sg_inc_y[2025]
    d['pir'] = anchor * (d['index'] / a_idx) / (sg_income(d['x']) / a_inc)
    OUT[name] = (d['x'].values, d['pir'].values)
    pk = d.loc[d['pir'].idxmax()]
    print(f"{name}: 峰 {pk['quarter']} PIR={pk['pir']:.2f}  最新 {d['quarter'].iloc[-1]} PIR={d['pir'].iloc[-1]:.2f}")

# ---------------- 美国 (Case-Shiller + 3%/yr收入, 背景) ----------------
cs = pd.read_csv('data/us_case_shiller.csv', parse_dates=['Date'])
for name, col, pk_pir in [('旧金山', 'CA-San Francisco', 9.2), ('纽约', 'NY-New York', 7.0)]:
    d = cs[['Date', col]].dropna().copy()
    d = d[d['Date'] >= '1998-01-01']
    d['x'] = d['Date'].dt.year + (d['Date'].dt.month - 0.5) / 12
    win = d[(d['x'] > 2005) & (d['x'] < 2008)]
    pk_row = win.loc[win[col].idxmax()]
    d['pir'] = pk_pir * (d[col] / pk_row[col]) / (1.03 ** (d['x'] - pk_row['x']))
    OUT[name] = (d['x'].values, d['pir'].values)
    print(f"{name}: CS峰 {pk_row['Date'].date()}  谷PIR={d[(d['x']>2008)&(d['x']<2013)]['pir'].min():.1f}  最新PIR={d['pir'].iloc[-1]:.1f}")

# ---------------- 日本东京圈 (锚点插值, 背景) ----------------
jp_pts = sorted(JP_TOKYO_PIR.items())
jp_x = np.arange(1985.0, 2025.01, 0.5)
jp_y = np.interp(jp_x, [p[0] for p in jp_pts], [p[1] for p in jp_pts])
OUT['东京圈'] = (jp_x, jp_y)

# ---------------- 序列落盘 ----------------
rows = []
for name, (x, y) in OUT.items():
    for xi, yi in zip(x, y):
        rows.append({'series': name, 'year': round(float(xi), 3), 'pir': round(float(yi), 3)})
pd.DataFrame(rows).to_csv('data/computed_pir_series.csv', index=False, encoding='utf-8-sig')

# ---------------- 峰值信息 ----------------
PEAKS = {}
for name, (x, y) in OUT.items():
    if name in ('旧金山', '纽约'):
        w = (x > 2004) & (x < 2008)
    elif name == '东京圈':
        w = (x > 1988) & (x < 1993)
    elif name == '新加坡组屋':
        w = (x > 2011) & (x < 2016)          # 2013调控周期峰
    elif name == '新加坡私宅':
        w = (x > 2007) & (x < 2014)          # 真实PIR峰=2008(其后靠收入增长消化)
    elif name == '台北':
        w = (x > 2022) & (x < 2026)
    elif name == '首尔':
        w = (x > 2018) & (x < 2023)
    else:
        w = (x > 2019) & (x < 2023)          # 中国 2021
    xi, yi = x[w], y[w]
    k = int(np.argmax(yi))
    PEAKS[name] = (float(xi[k]), float(yi[k]))
    print(f'PEAK {name}: {xi[k]:.2f}  PIR={yi[k]:.2f}')

COL = {'深圳': '#2a78d6', '北京': '#e34948', '上海': '#eda100', '广州': '#8a8a8a',
       '首尔': '#4a3aa7', '台北': '#008300', '新加坡私宅': '#e87ba4', '新加坡组屋': '#1baf7a',
       '旧金山': '#b0b0b0', '纽约': '#c9c9c9', '东京圈': '#555555'}

# ============ 图A: 峰值对齐 ============
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
MAIN = ['深圳', '北京', '上海', '首尔', '台北', '新加坡私宅', '新加坡组屋']
BG = ['旧金山', '纽约', '东京圈']
for name in BG:
    px, pv = PEAKS[name]
    x, y = OUT[name]
    t = x - px; m = (t >= -6) & (t <= 18)
    ax.plot(t[m], y[m] / pv * 100, ls='--', lw=1.6, color=COL[name], zorder=1)
    xe, ye = t[m][-1], (y[m] / pv * 100)[-1]
    lbl = {'旧金山': '旧金山(峰9.2, 2006)', '纽约': '纽约(峰7.0, 2006)', '东京圈': '东京圈(峰18.1, 1990)'}[name]
    ax.annotate(lbl, (xe, ye), textcoords='offset points', xytext=(6, 0),
                fontsize=8.5, color=COL[name], va='center')
LBL_DY = {'深圳': 0, '北京': -4, '上海': 5, '首尔': -4, '台北': 10,
          '新加坡私宅': 0, '新加坡组屋': 0}
for name in MAIN:
    px, pv = PEAKS[name]
    x, y = OUT[name]
    t = x - px; m = (t >= -6) & (t <= 18)
    ax.plot(t[m], y[m] / pv * 100, lw=2.2, color=COL[name], zorder=3,
            solid_capstyle='round')
    xe, ye = t[m][-1], (y[m] / pv * 100)[-1]
    lbl = {'深圳': '深圳(峰38, 2020-21)', '北京': '北京(峰25, 2021)', '上海': '上海(峰24, 2021)',
           '首尔': '首尔(峰19, 2021)',
           '台北': '台北(峰16.6, 2024)',
           '新加坡私宅': f'新加坡私宅(峰{PEAKS["新加坡私宅"][1]:.1f}, 2008)',
           '新加坡组屋': f'新加坡组屋(峰{PEAKS["新加坡组屋"][1]:.1f}, 2013)'}[name]
    ax.annotate(lbl, (xe, ye), textcoords='offset points', xytext=(6, LBL_DY[name]),
                fontsize=9, color=COL[name], va='center', fontweight='bold')
ax.axvline(0, color='#999', lw=0.8, ls=':')
ax.axhline(100, color='#999', lw=0.8, ls=':')
ax.set_xlim(-6.3, 24.5); ax.set_ylim(25, 118)
ax.set_xlabel('距各自PIR峰值的年数', fontsize=11)
ax.set_ylabel('房价收入比(峰值=100%)', fontsize=11)
ax.set_title('东亚 vs 美日:房价收入比完整周期,按各自峰值对齐', fontsize=15, fontweight='bold', pad=14)
ax.text(0, 1.005, '峰前段高于100%处为上一轮周期顶(如上海2016) | 美日为背景虚线',
        transform=ax.transAxes, fontsize=9, color='#777')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e8e8e4', lw=0.7)
ax.text(-6.1, 27.5, '数据:易居/国家统计局(中) · KB国民银行(韩) · 内政部(台) · HDB/URA/SingStat(新) · Case-Shiller(美) · 不动产研究所(日) | 收入增长已校正',
        fontsize=7.5, color='#888')
plt.tight_layout()
plt.savefig('output/pir_east_asia_aligned.png', facecolor='#fcfcfb')
plt.close()

# ============ 图B: 绝对PIR水平(日历时间) ============
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
DY_B = {'深圳': 0, '北京': 9, '上海': -1, '广州': 0, '首尔': -11,
        '台北': 0, '新加坡私宅': 0, '新加坡组屋': 0}
for name in ['深圳', '北京', '上海', '广州']:
    x, y = OUT[name]
    ax.plot(x, y, lw=2.2, color=COL[name], zorder=3)
    ax.annotate(name, (x[-1], y[-1]), textcoords='offset points', xytext=(6, DY_B[name]),
                fontsize=9.5, color=COL[name], va='center', fontweight='bold')
for name in ['首尔', '台北', '新加坡私宅', '新加坡组屋']:
    x, y = OUT[name]
    m = x >= 2008
    ax.plot(x[m], y[m], lw=2.2, color=COL[name], zorder=3)
    ax.annotate(name, (x[m][-1], y[m][-1]), textcoords='offset points', xytext=(6, DY_B[name]),
                fontsize=9.5, color=COL[name], va='center', fontweight='bold')
for name in ['旧金山', '纽约']:
    x, y = OUT[name]
    m = x >= 2008
    ax.plot(x[m], y[m], ls='--', lw=1.5, color=COL[name], zorder=1)
    ax.annotate(name, (x[m][-1], y[m][-1]), textcoords='offset points', xytext=(6, 0),
                fontsize=8.5, color=COL[name], va='center')
ax.axhspan(4, 6, color='#008300', alpha=0.06)
ax.text(2008.3, 4.6, '世界银行"合理区间" 4-6倍', fontsize=8, color='#008300')
ax.set_xlim(2008, 2029.5); ax.set_ylim(0, 40)
ax.set_xticks(range(2008, 2027, 2))
ax.set_xlabel('年份', fontsize=11)
ax.set_ylabel('房价收入比(倍)', fontsize=11)
ax.set_title('东亚各地房价收入比绝对水平(2008-2026):量级差距一目了然', fontsize=15, fontweight='bold', pad=14)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e8e8e4', lw=0.7)
ax.text(2008.2, 1.0, '注:跨经济体绝对倍数受口径影响(收入统计/面积/持有成本),形状与相对高低比绝对值更可靠',
        fontsize=7.5, color='#888')
plt.tight_layout()
plt.savefig('output/pir_east_asia_absolute.png', facecolor='#fcfcfb')
plt.close()

# ============ 一对一绝对值对比图(峰值对齐横轴, 绝对PIR纵轴, 统一0-40) ============
CN3 = ['深圳', '北京', '上海']

PAIRS = [
    ('cn_vs_us', ['旧金山', '纽约'],
     '中国 vs 美国(2008):同样的下坡,不同的海拔',
     '美国泡沫顶(7-9倍)还不到中国出清5年后水平(17-24倍)的一半;美国跌到4-5倍是真便宜,V型有起点优势'),
    ('cn_vs_jp', ['东京圈'],
     '中国 vs 日本(1990):唯一在同一海拔的对手',
     '东京圈峰18.1→谷6.8用了14年;中国峰后5年的跌速与日本相当,日本的教训不是深度,是时间'),
    ('cn_vs_kr', ['首尔'],
     '中国 vs 韩国首尔(2021):同年见顶,两种命运',
     '首尔急跌25%后三年收复至九成(供给短缺+人口流入);中国一线没有这个引擎,收复无从谈起'),
    ('cn_vs_tw', ['台北'],
     '中国 vs 台湾台北(2024):软着陆模板,但起点差一倍',
     '台北30年未崩、峰值16.6,政策压降每年约-1倍;中国即便复制这个斜率,回到15倍也要5年以上'),
    ('cn_vs_sg', ['新加坡私宅', '新加坡组屋'],
     '中国 vs 新加坡:双轨制的降维打击',
     '组屋(80%人口)全程4-6倍,私宅15.9→12.9靠收入涨了18年;"不跌价靠收入消化"需要一代人的时间'),
]

for fname, comps, title, subtitle in PAIRS:
    fig, ax = plt.subplots(figsize=(11.5, 6.5), dpi=150)
    fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
    for name in CN3:
        px, pv = PEAKS[name]
        x, y = OUT[name]
        t = x - px; m = (t >= -6) & (t <= 18)
        ax.plot(t[m], y[m], lw=2.2, color=COL[name], zorder=3)
        xe, ye = t[m][-1], y[m][-1]
        ax.annotate(f'{name} {ye:.0f}', (xe, ye), textcoords='offset points',
                    xytext=(6, {'深圳': 0, '北京': 5, '上海': -6}[name]), fontsize=9,
                    color=COL[name], va='center', fontweight='bold')
        ax.plot([0], [pv], 'o', ms=5, color=COL[name], zorder=4)
        if name == '深圳':
            ax.annotate(f'峰{pv:.0f}', (0, pv), textcoords='offset points', xytext=(-2, 8),
                        fontsize=9, color=COL[name], fontweight='bold', ha='right')
    for name in comps:
        px, pv = PEAKS[name]
        x, y = OUT[name]
        t = x - px; m = (t >= -6) & (t <= 18)
        ax.plot(t[m], y[m], lw=2.4, color=COL[name], zorder=3,
                ls='-' if name not in ('旧金山', '纽约', '东京圈') else '--')
        xe, ye = t[m][-1], y[m][-1]
        ax.annotate(f'{name} {ye:.1f}', (xe, ye), textcoords='offset points',
                    xytext=(6, 0), fontsize=9, color='#333' if name in ('旧金山','纽约','东京圈') else COL[name],
                    va='center', fontweight='bold')
        ax.plot([0], [pv], 'o', ms=5, color=COL[name], zorder=4)
        ax.annotate(f'峰{pv:.1f}', (0, pv), textcoords='offset points', xytext=(4, -11),
                    fontsize=9, color='#333' if name in ('旧金山','纽约','东京圈') else COL[name])
    ax.axvline(0, color='#999', lw=0.8, ls=':')
    ax.axhspan(4, 6, color='#008300', alpha=0.06)
    ax.text(17.9, 4.6, '世行合理区间4-6', fontsize=7.5, color='#008300', ha='right')
    ax.set_xlim(-6.3, 22); ax.set_ylim(0, 40)
    ax.set_xlabel('距各自PIR峰值的年数(深圳/北京/上海 峰=2020-21)', fontsize=10.5)
    ax.set_ylabel('房价收入比(倍,绝对值)', fontsize=10.5)
    ax.set_title(title, fontsize=14.5, fontweight='bold', pad=22)
    ax.text(0, 1.012, subtitle, transform=ax.transAxes, fontsize=9.5, color='#777')
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#e8e8e4', lw=0.7)
    plt.tight_layout()
    plt.savefig(f'output/pir_{fname}.png', facecolor='#fcfcfb')
    plt.close()
    print(f'pairwise saved: output/pir_{fname}.png')

print('charts saved.')
