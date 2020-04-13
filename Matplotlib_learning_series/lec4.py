from matplotlib import pyplot as plt 
plt.style.use('fivethirtyeight')

slices = [20, 80, 89, 90]
labels = ['twinty', 'eighty', 'eighty_nine', 'eighty']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
plt.pie(slices, labels = labels, colors = colors,wedgeprops = {'edgecolor': 'g'})
plt.title('My Awesome pie Chart')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red  = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
