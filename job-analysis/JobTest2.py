import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv("job.csv")

# 计算最低薪资和最高薪资的平均值作为估算的平均薪资
# 假设最低薪资和最高薪资字段分别为'最低薪资'和'最高薪资'
data['估算平均薪资'] = (data['最低薪资'] + data['最高薪资']) / 2

data_filtered = data[data['学历'] != '初中及以下']

# 按学历分组计算薪资的均值和中位数
salary_stats = data_filtered.groupby('学历')['估算平均薪资'].agg(['mean', 'median'])

# 设置中文字体为系统默认字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者您可以使用其他已安装的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 绘制图表
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制均值
salary_stats['mean'].plot(kind='bar', ax=ax, color='skyblue', position=0, label='均值', width=0.4)

# 绘制中位数
salary_stats['median'].plot(kind='bar', ax=ax, color='orange', position=1, label='中位数', width=0.4)

# 在柱子上方标注均值和中位数
for i, v in enumerate(salary_stats['mean']):
    plt.text(i, v, f"{v:.0f}", ha='center', va='bottom')

for i, v in enumerate(salary_stats['median']):
    plt.text(i + 0.4, v, f"{v:.0f}", ha='center', va='bottom')

# 设置图表标题和标签
ax.set_title('各学历薪资均值及中位数')
ax.set_xlabel('学历')
ax.set_ylabel('薪资（元）')

# 显示图例
ax.legend()

# 设置X轴标签的旋转角度
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()