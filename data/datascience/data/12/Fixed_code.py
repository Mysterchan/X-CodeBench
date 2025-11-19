import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=-35.2, azim=45)

ax.scatter(np.arange(0, 11), np.arange(0, 11), -np.arange(0, 11), c='g', marker='^')

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
ax.set_aspect('equal')
ax.set_proj_type('ortho')
plt.show()
