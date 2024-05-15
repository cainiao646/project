import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv("job.csv")

# 确保数据类型正确
data['招聘人数'] = data['招聘人数'].astype(int)

# 统计每个省份的招聘人数
province_recruitment = data.groupby('省市')['招聘人数'].sum()

# 设置中文字体为系统默认字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者您可以使用其他已安装的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 绘制柱状图
plt.figure(figsize=(10, 8))
plt.bar(province_recruitment.index, province_recruitment.values, color='skyblue')

# 设置X轴和Y轴标签
plt.xlabel('省市')
plt.ylabel('招聘人数')

# 设置图表标题
plt.title('各省份招聘人数分布')

# 设置X轴标签的旋转角度
plt.xticks(rotation=45)

# 在柱子上方标注招聘人数
for i, v in enumerate(province_recruitment.values):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()