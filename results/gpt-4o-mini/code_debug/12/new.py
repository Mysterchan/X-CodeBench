import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=-45, azim=45)

# Correctly setting the point that should be clearly visible
ax.scatter(1, 1, -1, c='g', marker='^', s=100)  # Increased size of the point for visibility

# Generating the meshgrid and plotting it
point_2d_x = np.arange(0, 11, 1)
point_2d_y = np.arange(0, 11, 1)

point_2d_x, point_2d_y = np.meshgrid(point_2d_x, point_2d_y)
point_2d_z = - point_2d_x

point_2d_x = point_2d_x[np.eye(11) == 1]
point_2d_y = point_2d_y[np.eye(11) == 1]
point_2d_z = point_2d_z[np.eye(11) == 1]

ax.scatter(point_2d_x, point_2d_y, point_2d_z, c='g', marker='^')

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
