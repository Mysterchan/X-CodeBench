import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.tick_params(which='major', length=10, width=2, color='r')
ax.tick_params(which='minor', length=5, width=2, color='b')
ax.set_xticks(np.linspace(0, 1, 5), minor=False)  # Set major ticks
ax.set_xticks(np.linspace(0, 1, 5), minor=True)   # Set minor ticks
ax.xaxis.set_minor_locator(plt.FixedLocator(np.linspace(0, 1, 5)))  # Define minor tick locations

plt.show()