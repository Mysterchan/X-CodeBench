from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})   # different way to create graph
ax.plot3D(range(0, 60), range(0, 60), range(0,60))
plt.show()