import matplotlib.pyplot as plt

x = [0, 2, 4, 6]
y = [(1, 5), (1, 3), (2, 4), (2, 7)]


plt.plot(x, [i for (i,j) in y], 'rs', markersize = 4)
plt.plot(x, [j for (i,j) in y], 'bo', markersize = 4)

plt.xlim(xmin=-3, xmax=10)
plt.ylim(ymin=-1, ymax=10)

plt.xlabel('ID')
plt.ylabel('Class')
plt.show()