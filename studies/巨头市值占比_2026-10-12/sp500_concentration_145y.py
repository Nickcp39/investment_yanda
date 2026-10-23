# -*- coding: utf-8 -*-
"""
标普500 前10大权重 145年(1880-2025)：现在的 38% 并非史无前例，等于 1965 年
来源：Visual Capitalist/Finaeon/S&P/Citi(1880-1960)；S&P Dow Jones Indices(1965-2025 官方季度)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/studies/巨头市值占比_2026-10-12'
os.makedirs(OUT, exist_ok=True)

# (年份, 前10大占标普500权重%)
years = [1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960,
         1965, 1971, 1977, 1980, 1986, 1989, 1995, 2001, 2010, 2016, 2019, 2022, 2025]
share = [27, 22, 28, 26, 19, 20, 28, 26, 28,
         38, 34, 30, 28, 20, 18, 17, 26, 20, 19, 22, 30, 38]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 7), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

ax.plot(years, share, color='#4da6ff', linewidth=2.6, marker='o', markersize=4.5, zorder=3)

# 两个 38% 高点
ax.scatter([1965, 2025], [38, 38], color='#ffd166', s=140, zorder=4, edgecolor='#121417')
ax.annotate('1965 年 · 38%\n工业巨头时代\n(AT&T/GM/Exxon/IBM)',
            xy=(1965, 38), xytext=(1928, 35),
            color='#ffd166', fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#ffd166', lw=1))
ax.annotate('2025 年 · 38%\nAI 时代\n(苹果/微软/英伟达等)',
            xy=(2025, 38), xytext=(1998, 34),
            color='#ffd166', fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#ffd166', lw=1))

# 分散期标注
ax.annotate('1980s–1990s 分散期\n(前10大仅 17–18%)',
            xy=(1989, 18), xytext=(1945, 12),
            color='#9aa0a6', fontsize=9,
            arrowprops=dict(arrowstyle='->', color='#9aa0a6', lw=0.8))

ax.axhline(38, color='#ffd166', linewidth=1, linestyle='--', alpha=0.5)

ax.set_title('标普500 前十大权重 · 145 年：现在 38% = 1965 年 38%，并非「史无前例」',
             color='#e8eaed', fontsize=14.5, fontweight='bold', pad=14)
ax.set_xlabel('年份', color='#9aa0a6', fontsize=11)
ax.set_ylabel('前十大公司占标普500 权重（%）', color='#9aa0a6', fontsize=11)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.set_xlim(1875, 2030)
ax.set_ylim(10, 44)
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7)
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

note = ('来源：1880-1960 为 Visual Capitalist/Finaeon/S&P/Citi；1965-2025 为 S&P Dow Jones Indices 官方季度数据。\n'
        '注意：1960 年代(38%)和现在(38%)是两个峰值，中间的 1980-1990s 是史上最分散时期。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

plt.tight_layout()
p = os.path.join(OUT, '标普500前十大权重_145年.png')
plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('已保存:', p)
