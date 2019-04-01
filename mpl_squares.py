import matplotlib.pyplot as plt

'''
使用matplotlib 绘制折线图
'''

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value, squares, linewidth=5)  #传递一个列表，并指定线条粗细
#分别设置图标，x，y的标题，并指定字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
