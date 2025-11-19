from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig=fig)
ax.plot3D(range(0, 60), range(0, 60), range(0,60))
plt.show()