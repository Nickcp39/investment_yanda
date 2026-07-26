# -*- coding: utf-8 -*-
"""
中国 vs 加拿大(温哥华/多伦多) PIR 一对一图 — 追加于 2026-07-25(云端会话)
数据: Demographia 中位数倍数(中位房价/中位家庭年收入),数据年=版次前一年Q3
  温哥华: 2015=10.8(2016版) 2016=11.8(2017版) 2017=12.6(2018版) 2019=11.9(2020版)
          峰2021Q3=13.3(2022版,全球第三,仅次于香港23.2/悉尼15.3)
          2022=12.0(2023版) 2023=12.3(2024版) 2024=11.8(2025版,"impossibly unaffordable")
  多伦多: 2019=8.6(2020版) 峰2021Q3≈10.5(2022版,转引口径,标注为估) 2023=9.3(2024版) 2024=8.4(2025版)
  2025-2026H1 外推: Teranet/NBC 2026年中同比 温哥华-6.8% 多伦多-7.3%,名义收入+3%/年
来源: demographia.com dhi.pdf 各版 / thenewswire·mpamag·fcpp 报道 / housepriceindex.ca
产出: output/pir_cn_vs_ca.png, data/ca_demographia_pir.csv
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['WenQuanYi Zen Hei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# ---------- 中国三城: 直接读已算好的序列 ----------
ser = pd.read_csv('data/computed_pir_series.csv')
CN3 = ['深圳', '北京', '上海']
OUT, PEAKS = {}, {}
for c in CN3:
    d = ser[ser['series'] == c]
    x, y = d['year'].values, d['pir'].values
    OUT[c] = (x, y)
    w = (x > 2019) & (x < 2023)
    k = int(np.argmax(y[w]))
    PEAKS[c] = (float(x[w][k]), float(y[w][k]))

# ---------- 加拿大: Demographia 锚点 + 2026H1 外推 ----------
# (年, PIR, 是否插值/外推)
VAN = [(2015.75, 10.8, 0), (2016.75, 11.8, 0), (2017.75, 12.6, 0),
       (2019.75, 11.9, 0), (2021.75, 13.3, 0), (2022.75, 12.0, 0),
       (2023.75, 12.3, 0), (2024.75, 11.8, 0),
       (2025.75, 11.8 * 0.932 / 1.03, 1),           # Teranet 2026中 同比-6.8%, 收入+3%
       (2026.5, 11.8 * 0.932 * 0.966 / 1.03**1.75, 1)]
TOR = [(2019.75, 8.6, 0), (2021.75, 10.5, 1),        # 2022版转引口径,标为估
       (2023.75, 9.3, 0), (2024.75, 8.4, 0),
       (2025.75, 8.4 * 0.927 / 1.03, 1),             # 同比-7.3%
       (2026.5, 8.4 * 0.927 * 0.963 / 1.03**1.75, 1)]

for name, pts, pk in [('温哥华', VAN, (2021.75, 13.3)), ('多伦多', TOR, (2021.75, 10.5))]:
    xs = np.array([p[0] for p in pts]); ys = np.array([p[1] for p in pts])
    xq = np.arange(xs[0], 2026.51, 0.25)
    yq = np.interp(xq, xs, ys)
    OUT[name] = (xq, yq)
    PEAKS[name] = pk
    print(f'{name}: 峰{pk[1]:.1f}@{pk[0]:.0f}  2026H1={yq[-1]:.1f}')

rows = []
for name, pts in [('温哥华', VAN), ('多伦多', TOR)]:
    for x, y, est in pts:
        rows.append({'series': name, 'year': x, 'pir': round(y, 2), 'estimated': est})
pd.DataFrame(rows).to_csv('data/ca_demographia_pir.csv', index=False, encoding='utf-8-sig')

# ---------- 出图: 与既有一对一图完全同风格 ----------
COL = {'深圳': '#2a78d6', '北京': '#e34948', '上海': '#eda100',
       '温哥华': '#b23a48', '多伦多': '#7a4a9e'}
title = '中国 vs 加拿大(2022):同代泡沫,西方唯一没有V型的对手'
subtitle = '温哥华峰13.3为西方之最,与中国同代见顶(2021-22);移民流入也没换来首尔式反弹,T+4仍在阴跌(2026中 同比-7%)'

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
for name in ['温哥华', '多伦多']:
    px, pv = PEAKS[name]
    x, y = OUT[name]
    t = x - px; m = (t >= -6) & (t <= 18)
    ax.plot(t[m], y[m], lw=2.4, color=COL[name], zorder=3)
    xe, ye = t[m][-1], y[m][-1]
    ax.annotate(f'{name} {ye:.1f}', (xe, ye), textcoords='offset points',
                xytext=(6, 0), fontsize=9, color=COL[name], va='center', fontweight='bold')
    ax.plot([0], [pv], 'o', ms=5, color=COL[name], zorder=4)
    ax.annotate(f'峰{pv:.1f}', (0, pv), textcoords='offset points', xytext=(4, -11),
                fontsize=9, color=COL[name])
ax.axvline(0, color='#999', lw=0.8, ls=':')
ax.axhspan(4, 6, color='#008300', alpha=0.06)
ax.text(17.9, 4.6, '世行合理区间4-6', fontsize=7.5, color='#008300', ha='right')
ax.set_xlim(-6.3, 22); ax.set_ylim(0, 40)
ax.set_xlabel('距各自PIR峰值的年数(深圳/北京/上海 峰=2020-21, 加拿大 峰=2021-22)', fontsize=10.5)
ax.set_ylabel('房价收入比(倍,绝对值)', fontsize=10.5)
ax.set_title(title, fontsize=14.5, fontweight='bold', pad=22)
ax.text(0, 1.012, subtitle, transform=ax.transAxes, fontsize=9.5, color='#777')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e8e8e4', lw=0.7)
ax.text(-6.1, 0.9, '数据:Demographia中位数倍数(温/多,版次前一年Q3) · Teranet/NBC 2026中同比外推 · 中国=易居锚+统计局链(口径不同,形状与相对高低更可靠)',
        fontsize=7, color='#888')
plt.tight_layout()
plt.savefig('output/pir_cn_vs_ca.png', facecolor='#fcfcfb')
plt.close()
print('saved output/pir_cn_vs_ca.png')
