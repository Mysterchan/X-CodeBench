#Python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]
z = [0, 1, 2, 3, 4, 5]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(x, y, z, c='g', s=20)
plt.xlabel("X data")
plt.ylabel("Y data")
#plt.zlabel("Z data") DOES NOT WORK
ax.view_init(60,35)
plt.show()