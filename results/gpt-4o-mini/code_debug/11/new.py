import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1)

# Correctly draw vertical line in the second axes
axes[1].axvline(15, ymin=0, ymax=1, color='red', lw=10)

# Setting y-limits for the second axes
axes[1].set_ylim(-1, 11)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
