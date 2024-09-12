import matplotlib.pyplot as plt
import numpy as np

xaxis = [2,4,6,8]
yaxis = [3,1,7,5]

# line graph
# plt.plot(xaxis,yaxis,marker='.',linewidth='10')
# plt.xlabel('x val')
# plt.ylabel('y val')
# plt.title('x and y plot')
# plt.grid(axis='x')
# plt.show()

#scatter
# plt.scatter(xaxis,yaxis,marker='x')
# plt.xlabel('x val')
# plt.ylabel('y val')
# plt.title('x and y plot')
# plt.grid(axis='x')
# plt.show()

# #bar
# plt.bar(xaxis,yaxis)
# plt.xlabel('x val')
# plt.ylabel('y val')
# plt.title('x and y plot')
# plt.grid(axis='y')
# plt.show()

# #pie
# y = np.array([35, 25, 25, 15])
# pielabels = ["Apples", "Bananas", "Cherries", "Dates"]
# pieexplode = [0.05,.05,.05,.050]
# plt.pie(y,labels=pielabels,shadow=True,explode=pieexplode)
# plt.show()


# histograms
y = np.array([20,40,30,20])
plt.hist(y)
plt.show()


