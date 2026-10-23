# -*- coding: utf-8 -*-
"""
纳斯达克100 单一公司历史权重峰值（1998-2026）
数据来源：纳斯达克官方(special rebalance 数据)、新浪财经/Wind、ChartRow、QQQ SEC持仓
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

OUT = r'D:/work/investment/financial-analysis-lab/studies/巨头市值占比_2026-10-12'
os.makedirs(OUT, exist_ok=True)

# (标签, 权重%, 风口, 结局, 高亮)
data = [
    ('微软 1998', 25.0, '互联网/PC 革命前夜', '2000后横盘16年', False),
    ('苹果 2011', 20.5, '移动/iPhone 现金机器', '被rebalance压到12%', False),
    ('苹果 2014', 13.6, '移动巅峰', '长期10-13%区间', False),
    ('微软 2023', 13.0, 'AI+云计算', 'rebalance压到9.8%', False),
    ('微软 2019', 11.5, '云计算', '—', False),
    ('思科 2000', 10.0, '互联网基建(市值全球第一)', '一年跌85%、24年未回前10', False),
    ('英伟达 2026', 9.0, 'AI 算力', '当前', True),
    ('微软 2004', 9.0, 'PC 软件', '长期横盘', False),
]

data.sort(key=lambda x: -x[1])
names = [d[0] for d in data]
vals = [d[1] for d in data]
colors = ['#ffd166' if d[4] else '#4da6ff' for d in data]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(12, 7), dpi=130)
fig.patch.set_facecolor('#121417')
ax.set_facecolor('#121417')

bars = ax.barh(names, vals, color=colors, height=0.6, zorder=3)
for b, d in zip(bars, data):
    v = d[1]
    ax.text(v + 0.3, b.get_y() + b.get_height()/2, f'{v:.1f}%', va='center',
            color='#e8eaed', fontsize=11, fontweight='bold')
    ax.text(v + 1.7, b.get_y() + b.get_height()/2, f'{d[2]}  ·  {d[3]}', va='center',
            color='#9aa0a6', fontsize=8.5)

ax.set_xlim(0, 30)
ax.set_xticks([0, 5, 10, 15, 20, 25])
ax.set_xticklabels([f'{t}%' for t in [0, 5, 10, 15, 20, 25]])

ax.set_title('纳指100 单一公司权重历史峰值：英伟达 9% 远未到历史极端（微软曾 25%、苹果曾 20.5%）',
             color='#e8eaed', fontsize=13.5, fontweight='bold', pad=14)
ax.tick_params(colors='#9aa0a6', labelsize=10)
ax.tick_params(axis='y', colors='#e8eaed', labelsize=10.5)
ax.set_xlabel('单一公司占纳指100 权重（%）', color='#9aa0a6', fontsize=11)
ax.invert_yaxis()
ax.grid(color='#2a2e33', linewidth=0.6, alpha=0.7, axis='x')
for spine in ax.spines.values():
    spine.set_color('#2a2e33')

note = ('注：纳指100 有「特殊再平衡」机制(1998/2011/2023 三次)，权重超4.5%的公司合计超48%即强制调低——'
        '微软25%、苹果20.5%都是触发再平衡前的高点。黄色=英伟达当前。')
fig.text(0.01, 0.01, note, color='#6b7280', fontsize=8)

plt.tight_layout()
p = os.path.join(OUT, '纳指100_单一公司权重峰值.png')
plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches='tight')
print('已保存:', p)
