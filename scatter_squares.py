import matplotlib.pyplot as plt


'''
使用matplotlib 绘制散点图
'''
# 绘制一个点，s实参指定点的大小，
# plt.scatter(2, 4, s=200)
# 绘制多个点
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

# 绘制多个点，
# s 实参指定点的大小，
# c="red" 指定数据点的颜色为红色
# edgecolor='none' 删除数据点的轮廓
# plt.scatter(x_values, y_values, c="red", edgecolor='none', s=100)

# 绘制多个点，
# s 实参指定点的大小，
# 令c等于一系列值 cmap指定颜色映射，下面代码y值小的点会显示浅蓝色，y值大的点会显示深蓝色。
# edgecolor='none' 删除数据点的轮廓
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)


# 设置每个坐标轴的取值范围
# plt.axis([0, 6, 0, 30])
# plt.show()
# 将绘制的散点图保存到文件，第二个实参指定将图表多余的空白区域裁剪掉，该方法与show()方法互斥
plt.savefig('squares_plot.png', bbox_inches='tight')
