import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

fig, ax = plt.subplots()
ax.tick_params(which='major', length=10, width=2, color='r')
ax.tick_params(which='minor', length=5, width=2, color='b')

# Set major ticks automatically (default)
# Set minor ticks explicitly using FixedLocator
minor_locs = np.linspace(0, 1, 5)
ax.xaxis.set_minor_locator(FixedLocator(minor_locs))

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
