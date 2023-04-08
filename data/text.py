import pandas as pd
import pandas as pd

# 10%   0.2909
# 15%   0.2913
# 20%   0.1883
# 25%   0.1924
# 30%   0.19
# 35%   0.1881
# 40%   0.1856
# 45%   0.3318
# 50%   0.3107

数据 = pd.read_csv('../15%填充效果表.csv')
# 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# 解决坐标轴负号问题
plt.rcParams['axes.unicode_minus'] = False
# Pandas笔记7.1：数据排序,按分数这列，直接修改数据，降序
# 数据.sort_values(by="分数",inplace=True,ascending=False)
plt.plot(数据.index, 数据.ori_data_x, label='蔬菜', color='r', marker='*', ms=2, linewidth=0.3)
plt.plot(数据.index, 数据.imputed_data, label='水果', color='k', marker='o', ms=2, linewidth=0.3)

# 显示图例
# lable的位置，左上解
plt.legend(loc="upper left")
# 设置X与Y轴的标题
plt.xlabel("姓名")
plt.ylabel("分数")

# 刻度标签及文字旋转
# plt.xticks(数据.index,rotation=45)

# y轴的刻度范围
plt.ylim([0, 1200])
plt.xlim([0, 100])

# 紧凑型的布局
plt.tight_layout()

# 设置图表的标题、字号、粗体
plt.title("三年二班学生成绩", fontsize=16, fontweight='bold')

# plt.savefig(r"d:\柱状图.jpg")

plt.show()
