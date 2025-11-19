import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = [1, 2, 1.5]
y = [2, 1, 1.5]
ax.scatter(x, y)

# Draw a circle around the point (1.5, 1.5) with radius 0.1
circle = plt.Circle((1.5, 1.5), 0.1, color='red', fill=False)
ax.add_patch(circle)

# Adjust limits to make sure the circle is fully visible
ax.set_xlim(0.8, 2.2)
ax.set_ylim(0.8, 2.2)

plt.show()