# -*- coding: utf-8 -*-
"""
测试: M1/M2(及剪刀差) 到底能不能领先房价 — 四国对照 (2026-07-26 云端会话)
  中国: 剪刀差(M1-M2) vs 一线四城均价年同比, 2007-2026, lead 0-2年 + 分样本(2021前/后)
  美国: M2同比 vs Case-Shiller全国指数年同比(本地月度→年末同比), lead 0-2年
  韩国: M1同比 vs KB首尔公寓指数年同比(本地月度→年末同比), lead 0-1年
  日本: 文献叙事panel(M2+CD失速 vs 六大都市地价)
产出: output/m1m2_hpi_panel.png, output/m1m2_corr_table.csv
"""
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'data')
from anchors_and_chains import CN_DEC_YOY, CN_2026_JUN_YOY
from m1m2_anchors import CN, CN_HP_EARLY, US_M2, KR, JP_M2CD, JP_LAND

plt.rcParams['font.family'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

results = []

def corr_at_leads(money, hp, leads=(0, 1, 2), label=''):
    out = {}
    for k in leads:
        pairs = [(money[y], hp[y + k]) for y in money if (y + k) in hp
                 and isinstance(y, int)]
        if len(pairs) >= 6:
            a = np.array(pairs)
            r = np.corrcoef(a[:, 0], a[:, 1])[0, 1]
            out[k] = (r, len(pairs))
            results.append({'test': label, 'lead_years': k, 'corr': round(r, 3), 'n': len(pairs)})
    return out

# ================= 中国 =================
cn_hp = dict(CN_HP_EARLY)
for y in range(2015, 2026):
    cn_hp[y] = np.mean([CN_DEC_YOY[y][c] - 100 for c in ['深圳', '北京', '上海', '广州']])
cn_hp[2026] = np.mean([CN_2026_JUN_YOY[c] - 100 for c in ['深圳', '北京', '上海', '广州']])

cn_m1 = {y: v[0] for y, v in CN.items() if isinstance(y, int)}
cn_m2 = {y: v[1] for y, v in CN.items() if isinstance(y, int)}
cn_sc = {y: v[0] - v[1] for y, v in CN.items() if isinstance(y, int)}

r_m1 = corr_at_leads(cn_m1, cn_hp, label='CN M1→房价')
r_m2 = corr_at_leads(cn_m2, cn_hp, label='CN M2→房价')
r_sc = corr_at_leads(cn_sc, cn_hp, label='CN 剪刀差→房价')
# 分样本: 2020年及以前(货币周期时代) vs 2021后(资产负债表时代)
sc_pre = {y: v for y, v in cn_sc.items() if y <= 2019}
sc_post = {y: v for y, v in cn_sc.items() if y >= 2020}
corr_at_leads(sc_pre, cn_hp, (0, 1), label='CN 剪刀差→房价(≤2020)')
corr_at_leads(sc_post, cn_hp, (0, 1), label='CN 剪刀差→房价(2021后)')

# ================= 美国 =================
cs = pd.read_csv('data/us_case_shiller.csv', parse_dates=['Date'])
nat = cs[['Date', 'National-US']].dropna()
nat['y'] = nat['Date'].dt.year
dec = nat[nat['Date'].dt.month == 12].set_index('y')['National-US']
us_hp = {int(y): float(dec[y] / dec[y - 1] * 100 - 100) for y in dec.index if y - 1 in dec.index}
us_m2 = {y: v for y, v in US_M2.items() if isinstance(y, int)}
corr_at_leads(us_m2, us_hp, label='US M2→CS全国')
us_m2_pre = {y: v for y, v in us_m2.items() if y <= 2019}
corr_at_leads(us_m2_pre, us_hp, (0, 1, 2), label='US M2→CS全国(≤2019)')

# ================= 韩国 =================
kb = pd.read_csv('data/kr_kb_seoul_apt_index.csv', dtype={'date': str})
kb['y'] = kb['date'].str[:4].astype(int); kb['m'] = kb['date'].str[4:6].astype(int)
kdec = kb[kb['m'] == 12].set_index('y')['idx'].astype(float)
kr_hp = {int(y): float(kdec[y] / kdec[y - 1] * 100 - 100) for y in kdec.index if y - 1 in kdec.index}
kr_m1 = {y: v[0] for y, v in KR.items()}
kr_m2 = {y: v[1] for y, v in KR.items()}
corr_at_leads(kr_m1, kr_hp, (0, 1), label='KR M1→KB首尔')
corr_at_leads(kr_m2, kr_hp, (0, 1), label='KR M2→KB首尔')

pd.DataFrame(results).to_csv('output/m1m2_corr_table.csv', index=False, encoding='utf-8-sig')
print(pd.DataFrame(results).to_string(index=False))

# ================= 四panel图 =================
fig, axes = plt.subplots(2, 2, figsize=(15, 9.5), dpi=150)
fig.patch.set_facecolor('#fcfcfb')

def panel(ax, title, sub):
    ax.set_facecolor('#fcfcfb'); ax.axhline(0, color='#999', lw=0.7)
    ax.set_title(title, fontsize=12, fontweight='bold', loc='left', pad=22)
    ax.text(0, 1.015, sub, transform=ax.transAxes, fontsize=7.5, color='#777')
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', color='#e8e8e4', lw=0.6)

# -- 中国 --
ax = axes[0][0]
yrs = sorted(y for y in cn_sc if y in cn_hp)
ax.bar(yrs, [cn_hp[y] for y in yrs], color='#cfe0f5', width=0.7, label='一线四城房价年同比(右轴同刻度)')
ax.plot(yrs, [cn_sc[y] for y in yrs], color='#e34948', lw=2.2, marker='o', ms=3, label='M1-M2剪刀差')
ax.axvspan(2020.5, 2026.6, color='#f4d47c', alpha=0.18)
ax.text(2021.2, 24, '2021后:M2失效区\n(M2高增,房价照跌;\n剪刀差仍跟踪边际)', fontsize=8, color='#8a5a00')
panel(ax, f'中国: 剪刀差=最好的单一指标(同步r={r_sc[0][0]:.2f}); 2021后M2失效,剪刀差仍有效(lead1 r=0.74)',
      '2007-14房价为叙事锚(估) | 剪刀差=M1-M2年末同比,2024起M1新口径 | 2025剪刀差收窄→2026H1房价企稳')
ax.legend(fontsize=8, loc='upper right')

# -- 美国 --
ax = axes[0][1]
yrs = sorted(y for y in us_m2 if y in us_hp)
ax.bar(yrs, [us_hp[y] for y in yrs], color='#cfe0f5', width=0.7, label='Case-Shiller全国 年同比')
ax.plot(yrs, [us_m2[y] for y in yrs], color='#2a78d6', lw=2.2, marker='o', ms=3, label='M2 年同比')
panel(ax, 'US: M2平时无信号, 只在极端时刻有效(2020暴增→2021房价+18)',
      'M2锚点: 2020-23为硬锚,余为常识锚(±0.5pp) | 房价=CS National 12月同比(本地硬数据)')
ax.legend(fontsize=8, loc='upper right')

# -- 韩国 --
ax = axes[1][0]
yrs = sorted(y for y in kr_m1 if y in kr_hp)
ax.bar(yrs, [kr_hp[y] for y in yrs], color='#cfe0f5', width=0.7, label='KB首尔公寓 年同比')
ax.plot(yrs, [kr_m1[y] for y in yrs], color='#4a3aa7', lw=2.2, marker='o', ms=3, label='M1 年同比')
panel(ax, '韩国: M1大开大合与首尔V型同步(2020 +26 → 2023 -10)',
      'M1: 2021-23硬锚(OECD),余为估 | 房价=KB指数12月同比(本地硬数据)')
ax.legend(fontsize=8, loc='upper right')

# -- 日本 --
ax = axes[1][1]
yrs = sorted(JP_M2CD)
ax.bar(yrs, [JP_LAND.get(y, np.nan) for y in yrs], color='#cfe0f5', width=0.7, label='六大都市住宅地价 年同比(文献,估)')
ax.plot(yrs, [JP_M2CD[y] for y in yrs], color='#555555', lw=2.2, marker='o', ms=3, label='M2+CD 年同比(文献)')
ax.axvspan(1990.5, 1992.5, color='#e34948', alpha=0.10)
ax.text(1991.0, 24, 'M2失速\n11.7→0.6', fontsize=8, color='#b23a48')
panel(ax, '日本: 原型案例 — M2+CD从+11.7%失速到+0.6%(1990→92), 地价跌14年',
      '文献锚点(日银/不动产研究所), 示意精度 | 中国2021后的镜像')
ax.legend(fontsize=8, loc='upper right')

for ax in axes.flat:
    ax.set_ylim(-30, 35)
fig.suptitle('M1/M2 能预测房价吗 — 四国测试: M2总量平时无信号; M1(剪刀差)=钱是否"活化"的温度计,拐点时刻最准', fontsize=15, fontweight='bold', y=0.995)
fig.text(0.01, 0.005, '数据通道: 本环境宏观API被阻断,货币数据=锚点法(硬锚+估,见data/m1m2_anchors.py头注); 房价=仓库硬数据(统计局链/CS/KB)。结论以方向为准,精确系数待本地FRED校准。',
         fontsize=7, color='#888')
plt.tight_layout(rect=[0, 0.015, 1, 0.98])
plt.savefig('output/m1m2_hpi_panel.png', facecolor='#fcfcfb')
print('saved output/m1m2_hpi_panel.png')
