import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]
z = [0, 1, 2, 3, 4, 5]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='g', s=20)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
ax.view_init(60, 35)
plt.show()