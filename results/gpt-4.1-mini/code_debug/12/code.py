import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=-45, azim=45)

# Coordinates of the single point
point_x = np.array([1])
point_y = np.array([1])
point_z = np.array([-1])

ax.scatter(point_x, point_y, point_z, c='g', marker='^')

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

plt.show()