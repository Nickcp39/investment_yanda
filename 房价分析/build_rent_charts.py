# -*- coding: utf-8 -*-
"""售租比(房价/年租金)图: R1 中国四城时序, R2 峰值vs现值哑铃图"""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data/numbeo_p2r_history.csv')
p = df.pivot_table(index='year', columns='city', values='p2r_center')

COL = {'深圳': '#2a78d6', '北京': '#e34948', '上海': '#eda100', '广州': '#8a8a8a',
       '首尔': '#4a3aa7', '台北': '#008300', '新加坡': '#1baf7a', '东京': '#555555',
       '旧金山': '#b0b0b0', '纽约': '#c9c9c9', '香港': '#e87ba4'}

# ---------- R1: 中国四城 + 关键参照 时序 ----------
fig, ax = plt.subplots(figsize=(11.5, 6.5), dpi=150)
fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
DY = {'深圳': 4, '北京': -5, '上海': 3, '广州': 10}
for c in ['深圳', '北京', '上海', '广州']:
    s = p[c].dropna()
    ax.plot(s.index, s.values, lw=2.2, color=COL[c], zorder=3)
    ax.annotate(f'{c} {s.iloc[-1]:.0f}', (s.index[-1], s.iloc[-1]),
                textcoords='offset points', xytext=(6, DY[c]), fontsize=9.5,
                color=COL[c], va='center', fontweight='bold')
for c, dy in [('东京', 0), ('旧金山', 0)]:
    s = p[c].dropna()
    ax.plot(s.index, s.values, lw=1.5, ls='--', color=COL[c], zorder=1)
    ax.annotate(f'{c} {s.iloc[-1]:.0f}', (s.index[-1], s.iloc[-1]),
                textcoords='offset points', xytext=(6, dy), fontsize=8.5,
                color='#666', va='center')
ax.axhspan(15, 25, color='#008300', alpha=0.06)
ax.text(2011.2, 16.5, '国际"租金定价"区间 15-25倍(回报率4-6.7%)', fontsize=8, color='#008300')
# 深圳峰标注
ax.annotate('深圳峰95倍\n=租金回报率1.1%', (2022, 95), textcoords='offset points',
            xytext=(-70, -4), fontsize=9, color=COL['深圳'], fontweight='bold')
ax.set_xlim(2011, 2029); ax.set_ylim(0, 105)
ax.set_xticks(range(2011, 2027, 3))
ax.set_xlabel('年份', fontsize=10.5)
ax.set_ylabel('售租比(房价 ÷ 年租金,倍)', fontsize=10.5)
ax.set_title('中国一线售租比(2011-2026):比房价收入比更极端的泡沫口径', fontsize=14.5, fontweight='bold', pad=22)
ax.text(0, 1.012, '售租比=买下这套房要收多少年租金 | 房价跌但租金同跌,售租比修复(-26%)慢于PIR(-38%)',
        transform=ax.transAxes, fontsize=9.5, color='#777')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e8e8e4', lw=0.7)
plt.tight_layout()
plt.savefig('output/p2r_china_trend.png', facecolor='#fcfcfb')
plt.close()
print('R1 saved')

# ---------- R2: 峰值 vs 现值 哑铃图 ----------
CITIES = ['深圳', '首尔', '广州', '台北', '北京', '上海', '香港', '东京', '新加坡', '纽约', '旧金山']
rows = []
for c in CITIES:
    s = p[c].dropna()
    w = s[(s.index >= 2019) & (s.index <= 2024)]   # 本轮周期峰窗口
    rows.append({'city': c, 'peak': w.max(), 'peak_yr': int(w.idxmax()), 'now': s.iloc[-1]})
d = pd.DataFrame(rows).sort_values('now', ascending=True).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(11.5, 7), dpi=150)
fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
for i, r in d.iterrows():
    col = COL[r['city']]
    ax.plot([r['now'], r['peak']], [i, i], color=col, lw=2, alpha=0.45, zorder=2)
    ax.plot(r['peak'], i, 'o', ms=8, color=col, alpha=0.45, zorder=3)
    ax.plot(r['now'], i, 'o', ms=9, color=col, zorder=4)
    ax.annotate(f"{r['now']:.0f}", (r['now'], i), textcoords='offset points',
                xytext=(0, 9), fontsize=9, color=col, ha='center', fontweight='bold')
    ax.annotate(f"峰{r['peak']:.0f}({r['peak_yr']})", (r['peak'], i), textcoords='offset points',
                xytext=(8, -3), fontsize=8, color='#888')
ax.set_yticks(range(len(d))); ax.set_yticklabels(d['city'], fontsize=11)
# 历史泡沫参照
ax.axvline(33, color='#c9553d', lw=1.2, ls='--')
ax.text(33, len(d) - 0.25, '美国2006泡沫顶≈33\n(Numbeo2009×CS指数推算)', fontsize=8, color='#c9553d', ha='center', va='top')
ax.axvspan(40, 60, color='#555', alpha=0.08)
ax.text(50, -0.55, '日本1990泡沫顶估计区间40-60(文献估计,仅参考)', fontsize=8, color='#666', ha='center')
ax.axvspan(15, 25, color='#008300', alpha=0.06)
ax.text(20, len(d) - 0.25, '租金定价区间\n15-25', fontsize=8, color='#008300', ha='center', va='top')
ax.set_xlim(0, 108); ax.set_ylim(-0.9, len(d) - 0.1)
ax.set_xlabel('售租比(房价 ÷ 年租金,倍) — 实心=2026现值, 空心=本轮峰值', fontsize=10.5)
ax.set_title('全球主要城市售租比:峰值 vs 现在(2026)', fontsize=14.5, fontweight='bold', pad=14)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.grid(axis='x', color='#e8e8e4', lw=0.7)
plt.tight_layout()
plt.savefig('output/p2r_dumbbell.png', facecolor='#fcfcfb')
plt.close()
print('R2 saved')
print(d.to_string())
