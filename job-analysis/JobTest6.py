import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv("job.csv")

# 计算各工作经验的招聘人数占比
experience_recruitment = data['工作经验'].value_counts(normalize=True)

# 设置中文字体为系统默认字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者您可以使用其他已安装的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 绘制各工作经验的招聘人数占比图
plt.figure(figsize=(10, 8))
experience_recruitment.plot(kind='pie', autopct='%1.1f%%')
plt.title('各工作经验的招聘人数占比')
plt.ylabel('')  # 隐藏y轴标签

# 显示图表
plt.show()