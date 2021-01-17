import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

f, (ax1, ax2) = plt.subplots(figsize=(6, 4), nrows=2)
dict1 = {'weight': [65, 100, 32, 150, 700, 950, 463, 1000], 'age': [700, 560, 430, 139, 421, 392, 462, 182],
         'height': [65, 100, 32, 150, 700, 950, 463, 1000]}
df = pd.DataFrame(data=dict1, index=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"])

# cmap用cubehelix map颜色
cmap = sns.cubehelix_palette(start=1.5, rot=3, gamma=0.8, as_cmap=True)
# pt = df.corr()  # pt为数据框或者是协方差矩阵
sns.heatmap(df, linewidths=0.05, ax=ax1, vmax=900, vmin=0, cmap=cmap)
ax1.set_title('cubehelix map')
ax1.set_xlabel('')
ax1.set_xticklabels([])  # 设置x轴图例为空值
ax1.set_ylabel('kind')

# cmap用matplotlib colormap
sns.heatmap(df, linewidths=0.05, ax=ax2, vmax=900, vmin=0, cmap='rainbow')
# rainbow为 matplotlib 的colormap名称
ax2.set_title('matplotlib colormap')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
# plt.show()

# 色块带数字
np.random.seed(20180316)
x = np.random.randn(4, 4)
f, (ax1, ax2) = plt.subplots(figsize=(6, 6), nrows=2)
# ax控制子图坐标
sns.heatmap(x, annot=True, ax=ax1)
# sns.heatmap(x, annot=True, fmt='.5f', ax=ax2, annot_kws={'size': 9, 'weight': 'bold', 'color': 'blue'})
# plt.show()

# 色块之间带间隔线
sns.heatmap(x, annot=True, fmt='.5f', linewidths=1.1, linecolor='white',
            annot_kws={'size': 9, 'weight': 'bold', 'color': 'blue'}, robust=True)

f, (ax1, ax2) = plt.subplots(figsize=(6, 6), nrows=2)
# mask掩盖值
p1 = sns.heatmap(df, ax=ax1, cmap=cmap, xticklabels=False, mask=None)
ax1.set_title('mask=None')
ax1.set_ylabel('kind')

p2 = sns.heatmap(df, ax=ax2, cmap=cmap, xticklabels=True, mask=(df < 60))
# mask对pt进行布尔型转化,结果为True的位置用白色覆盖
ax2.set_title('mask: boolean DataFrame')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')

plt.show()
