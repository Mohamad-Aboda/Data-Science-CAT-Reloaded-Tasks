from matplotlib import pyplot as plt 
x = [3, 5, 99, -43, 43, 90, 10]
y = [11, 22, 33, 55, 55, 5, 123]
y2 = [12, 3, 42, 45, 55, 65, 63]
# for creating funny graph 
plt.xkcd()
# this style makes things better
plt.style.use('fivethirtyeight')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("My plot")
# specify both vars to plot and color , linespace , label in order (color, linespace, label)
plt.plot(x, y, color = '#a123cb', linestyle = '--',label = 'ONe')
plt.plot(x, y2, color = '#255234', linestyle = '--',label = 'TWo')
# if we pass label in plot we don't need to pass it in legend 
# leged when we have more than graph and we want to identify all the graphs
plt.legend()
plt.show()
