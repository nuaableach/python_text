import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("square numbers",fontsize=20)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square value",fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0, 1000, 0, 1100000])

plt.savefig('squares_plot.png',bbox_inches='tight')