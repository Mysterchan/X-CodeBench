import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1)
axes[1].set_ylim([0, 11])  # Set y-limits on the second axes, not globally
axes[1].axvline(15, ymin=0, ymax=1, color='red', lw=10)  # ymin and ymax are fractions of the y-axis height

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
