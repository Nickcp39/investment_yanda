# -*- coding: utf-8 -*-
"""
维度③: 名义房价绝对值(峰值=100, 峰值对齐) — 2026-07-25 云端会话
不除收入、不除租金,看名义价格本身跌了多少、跌了多久。
数据:
  中国四城 = 统计局70城二手房12月同比链(data/anchors_and_chains.py, 与PIR同源)
  首尔 = KB公寓指数 / 新加坡 = URA私宅指数 / 美国旧金山 = Case-Shiller
  东京圈 = 不动产研究所六大都市住宅地价指数 文献锚点(1985=54,1991=100,1995=65,2000=48,2005=40,2010=36,插值,标估)
  加拿大 = Teranet锚点(2022.1=100峰; 2023.1 多-8.8%/温-3.9%; 2026中 同比 多-7.3%/温-6.8%; 中段年份=稳态假设,标估)
产出: output/abs_price_aligned.png
"""
import sys, math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'data')
from anchors_and_chains import CN_DEC_YOY, CN_2026_JUN_YOY

plt.rcParams['font.family'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

OUT = {}   # name -> (calendar_x, price_index)
PEAKS = {}

# ---- 中国四城: 价格链(峰=2021末) ----
for city in ['深圳', '北京', '上海', '广州']:
    years = [2014.9] + [y + 0.9 for y in range(2015, 2026)]
    P = [100.0]
    for y in range(2015, 2026):
        P.append(P[-1] * CN_DEC_YOY[y][city] / 100.0)
    p_jun25 = math.sqrt(P[-2] * P[-1])
    p_jun26 = p_jun25 * CN_2026_JUN_YOY[city] / 100.0
    years.append(2026.5); P.append(p_jun26)
    x = np.array(years); y = np.array(P)
    k = int(np.argmax(y))
    OUT[city] = (x, y); PEAKS[city] = (float(x[k]), float(y[k]))
    print(f'{city}: 峰{x[k]:.1f}  现距峰 {y[-1]/y[k]*100-100:+.1f}%')

# ---- 首尔 KB 公寓指数 ----
kr = pd.read_csv('data/kr_kb_seoul_apt_index.csv', dtype={'date': str})
kr['x'] = kr['date'].map(lambda s: int(s[:4]) + (int(s[4:6]) - 0.5) / 12)
kr = kr[kr['x'] >= 2009]
x, y = kr['x'].values, kr['idx'].values.astype(float)
w = (x > 2020) & (x < 2023.5); k = int(np.argmax(y * w))
OUT['首尔'] = (x, y); PEAKS['首尔'] = (float(x[k]), float(y[k]))
print(f"首尔: 峰{x[k]:.1f}  现距峰 {y[-1]/y[k]*100-100:+.1f}%")

# ---- 新加坡 URA 私宅 ----
import json
ura = pd.DataFrame(json.load(open('data/sg_URA_PPI.json')))
ura = ura[ura['property_type'] == 'All Residential'].copy()
ura['index'] = ura['index'].astype(float)
ura['x'] = ura['quarter'].map(lambda q: int(q[:4]) + (int(q[-1]) - 0.5) / 4)
ura = ura[ura['x'] >= 2000]
x, y = ura['x'].values, ura['index'].values
w = (x > 2007) & (x < 2009); k = int(np.argmax(np.where(w, y, -1)))
OUT['新加坡私宅'] = (x, y); PEAKS['新加坡私宅'] = (float(x[k]), float(y[k]))
print(f"新加坡: 2008峰后现值 {y[-1]/y[k]*100:.0f}%(创新高)")

# ---- 美国 旧金山 Case-Shiller ----
cs = pd.read_csv('data/us_case_shiller.csv', parse_dates=['Date'])
d = cs[['Date', 'CA-San Francisco']].dropna()
d = d[d['Date'] >= '1998-01-01']
x = (d['Date'].dt.year + (d['Date'].dt.month - 0.5) / 12).values
y = d['CA-San Francisco'].values
w = (x > 2005) & (x < 2008); k = int(np.argmax(np.where(w, y, -1)))
OUT['旧金山'] = (x, y); PEAKS['旧金山'] = (float(x[k]), float(y[k]))
print(f"旧金山: 2006峰→谷 {y[(x>2008)&(x<2013)].min()/y[k]*100-100:.0f}% 现 {y[-1]/y[k]*100:.0f}%")

# ---- 东京圈 地价文献锚点(标估) ----
jp_pts = [(1985, 54), (1991, 100), (1995, 65), (2000, 48), (2005, 40), (2010, 36)]
jx = np.arange(1985.0, 2010.01, 0.5)
jy = np.interp(jx, [p[0] for p in jp_pts], [p[1] for p in jp_pts])
OUT['东京圈(地价,估)'] = (jx, jy); PEAKS['东京圈(地价,估)'] = (1991.0, 100.0)

# ---- 加拿大 Teranet锚点(标估) ----
ca = {
    '多伦多(估)': [(2016.1, 78), (2022.1, 100), (2023.1, 91.2), (2024.5, 89), (2025.5, 88), (2026.5, 81.6)],
    '温哥华(估)': [(2016.1, 80), (2022.1, 100), (2023.1, 96.1), (2024.5, 95), (2025.5, 94), (2026.5, 87.6)],
}
for name, pts in ca.items():
    x = np.array([p[0] for p in pts]); y = np.array([p[1] for p in pts])
    xq = np.arange(x[0], 2026.51, 0.25)
    OUT[name] = (xq, np.interp(xq, x, y)); PEAKS[name] = (2022.1, 100.0)

# ---- 出图 ----
COL = {'深圳': '#2a78d6', '北京': '#e34948', '上海': '#eda100', '广州': '#8a8a8a',
       '首尔': '#4a3aa7', '新加坡私宅': '#e87ba4', '旧金山': '#b0b0b0',
       '东京圈(地价,估)': '#555555', '多伦多(估)': '#7a4a9e', '温哥华(估)': '#b23a48'}
DASH = {'旧金山', '东京圈(地价,估)'}
DY = {'深圳': -2, '北京': 9, '上海': -8, '广州': -14, '首尔': 8, '新加坡私宅': 0,
      '旧金山': 0, '东京圈(地价,估)': 0, '多伦多(估)': -6, '温哥华(估)': 7}

fig, ax = plt.subplots(figsize=(13, 7.5), dpi=150)
fig.patch.set_facecolor('#fcfcfb'); ax.set_facecolor('#fcfcfb')
for name, (x, y) in OUT.items():
    px, pv = PEAKS[name]
    t = x - px; n = y / pv * 100
    m = (t >= -6) & (t <= 18)
    ax.plot(t[m], n[m], lw=1.6 if name in DASH else 2.2,
            ls='--' if name in DASH else '-', color=COL[name],
            zorder=1 if name in DASH else 3)
    ax.annotate(f'{name} {n[m][-1]:.0f}', (t[m][-1], n[m][-1]), textcoords='offset points',
                xytext=(6, DY[name]), fontsize=9, color=COL[name],
                va='center', fontweight='normal' if name in DASH else 'bold')
ax.axvline(0, color='#999', lw=0.8, ls=':')
ax.axhline(100, color='#999', lw=0.8, ls=':')
ax.set_xlim(-6.3, 21); ax.set_ylim(30, 180)
ax.set_xlabel('距各自名义价格峰值的年数(中国峰=2021, 加拿大=2022, 首尔=2022, 旧金山=2006, 东京=1991, 新加坡=2008)', fontsize=10.5)
ax.set_ylabel('名义房价指数(峰值=100)', fontsize=11)
ax.set_title('维度③ 名义房价绝对值:跌了多少,跌了多久(峰值=100,峰值对齐)', fontsize=15, fontweight='bold', pad=14)
ax.text(0, 1.005, '不除收入不除租金,看价格本身 | 虚线=已走完整周期的背景样本 | (估)=锚点插值',
        transform=ax.transAxes, fontsize=9, color='#777')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='y', color='#e8e8e4', lw=0.7)
ax.text(-6.1, 32, '数据:统计局70城链(中) · KB(韩) · URA(新) · Case-Shiller(美) · 不动产研究所地价/文献锚(日,估) · Teranet锚(加,估)',
        fontsize=7.5, color='#888')
plt.tight_layout()
plt.savefig('output/abs_price_aligned.png', facecolor='#fcfcfb')
plt.close()
print('saved output/abs_price_aligned.png')
