from matplotlib import pyplot as plt

data = [1, 5, 2, 1, 1, 4, 3, 1, 7, 8, 9, 6, 1]
plt.plot(data)

# Set y-axis limits
plt.ylim(bottom=min(data), top=max(data))

# Hide all ticks on x and y axis
plt.xticks([])
plt.yticks([])

# Add minimum and maximum y-axis labels
plt.yticks([min(data), max(data)])

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
