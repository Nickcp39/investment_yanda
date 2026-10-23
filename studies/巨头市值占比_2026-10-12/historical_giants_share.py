# -*- coding: utf-8 -*-
"""
历史上「市场霸主」的市值占比峰值对比
口径：1932/1929/1955 为占全部上市美股(当时无标普500)，1967 起为占标普500
来源：historyofmarket.com (Top10 SPX share)、NYT、Benzinga/Kobeissi
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/studies/巨头市值占比_2026-10-12'
os.makedirs(OUT, exist_ok=True)

# (公司, 峰值年份, 占比%, 结局, 是否高亮)
data = [
    ('AT&T（贝尔系统）', 1932, 13.0, '1984 反垄断拆分', False),
    ('标准石油（Exxon 前身）', 1929, 9.8, '1911 反垄断拆成34家', False),
    ('英伟达 NVDA', 2025, 8.5, '当前（AI 周期）', True),
    ('通用汽车 GM', 1955, 7.7, '2009 破产重组', False),
    ('IBM', 1967, 7.4, '被 PC 革命侵蚀、长期横盘', False),
    ('苹果 Apple', 2024, 7.1, '仍处顶部', False),
    ('微软 Microsoft', 2024, 7.0, '2000后横盘16年再创新高', False),
    ('埃克森 Exxon', 1980, 6.2, '长期慢牛（能源）', False),
    ('微软 Microsoft', 1999, 4.9, '见顶后横盘', False),
    ('思科 Cisco', 2000, 4.2, '24年未回前10', False),
    ('柯达 Kodak', 1972, 2.9, '2012 破产', False),
]

data.sort(key=lambda x: -x[2])
names = [d[0] + f'（{d[1]}）' for d in data]
vals = [d[2] for d in data]
colors = ['#ffd166' if d[4] else '#4da6ff' for d in data]
endings = [d[3] for d in data]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 7.5), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

bars = ax.barh(names, vals, color=colors, height=0.62, zorder=3)
for b, v, e in zip(bars, vals, endings):
    ax.text(v + 0.15, b.get_y() + b.get_height()/2, f'{v:.1f}%', va='center',
            color='#e8eaed', fontsize=10.5, fontweight='bold')
    ax.text(v + 1.6, b.get_y() + b.get_height()/2, e, va='center',
            color='#9aa0a6', fontsize=8.5)

ax.set_xlim(0, 17)
ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
ax.set_xticklabels([f'{t}%' for t in [0, 2, 4, 6, 8, 10, 12, 14]])

ax.set_title('历史上「市场霸主」的市值占比峰值：英伟达 8.5% 并非历史最高',
             color='#e8eaed', fontsize=14.5, fontweight='bold', pad=14)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.tick_params(axis='y', colors='#e8eaed', labelsize=10.5)
ax.set_xlabel('峰值时占市场指数市值比例', color='#9aa0a6', fontsize=11)
ax.invert_yaxis()
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7, axis='x')
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

note = ('口径：1932/1929/1955 为占「全部上市美股」（当时标普500尚未成立）；1967 起为占「标普500」。\n'
        '黄色=英伟达当前；蓝色=历史上各代霸主。来源：historyofmarket.com、NYT、Benzinga/Kobeissi(2025)。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8.5)

plt.tight_layout()
p = os.path.join(OUT, '历史巨头市值占比峰值.png')
plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('已保存:', p)
