import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import math

# 为了matplotlib显示中文，必加
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.close()     #clf() # 清图    cla() # 清坐标轴    close() # 关窗口
fig=plt.figure().add_subplot(1,1,1)
#fig.figis("equal") #设置图像显示的时候XY轴比例
plt.grid(True)  #添加网格
#plt.ion()  #interactive mode on


#设置图标标题
plt.title("实时更新显示图", fontsize = 16)
#设置坐标轴标签
plt.xlabel("棋盘数", fontsize = 12)
plt.ylabel("重量/吨", fontsize = 12)
#设置每个坐标轴的取值范围（x轴取值，y轴取值）
plt.axis([0,50,0,10000])
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 9)

#画第1个曲线
print('开始仿真')
X = 0
N = 1
Y = 1
try:
    for t in range(64):
        #障碍物船只轨迹
        X = t
        N = N*2
        Y = N*2/100/1000/1000
#        fig.scatter(X,Y, c='red', marker='+')  #散点图
        plt.scatter(X,Y, c='red', s=10, marker='+')  #散点图
        #fig.lines.pop(1)  删除轨迹
        #下面的图,两船的距离
#        plt.pause(0.001)
except Exception as err:
    print(err)

#画第2个曲线
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=10)

#画第3个曲线

input_values = [5,10,30,40,50]  #图形输入值
squares = [1,400,9000,6000,1250]    #图形输出值
plt.plot(input_values,squares,linewidth=2)


plt.show()