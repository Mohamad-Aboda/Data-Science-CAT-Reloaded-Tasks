from matplotlib import pyplot as plt 
import numpy as np
plt.style.use('fivethirtyeight')

#plt.xkcd()
x = []
y = []
x2 = []
y2 = []
x3 = []
y3 = []

# just creating any data
for i in range(15):
	x.append(32 * i + 30)
	y.append(31 * i * i+ 90)
	x2.append(7 * i + 12)
	y2.append(120 * i * i * i - 12)
	x3.append(4 * i -3)
	y3.append(90 * i * i -8)

width = 2.5
plt.xlabel('x-axis')
plt.ylabel('y-lable')
plt.bar(x2, y2, width = width, color = 'g', label = 'bar graph 2')
plt.bar(x, y, width = width,color = 'red', label = 'bar graph 1')
plt.bar(x3, y3 ,width = width,color = 'blue', label = 'bar graph 3')
plt.legend()
plt.show()
