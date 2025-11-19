import matplotlib.pyplot as plt
import seaborn as sns

x = ['x1', 'x2', 'x3']
y = [4, 6, 3]

# Create a horizontal bar plot with right alignment
sns.barplot(x=[-val for val in y], y=x, orient='h')

# Set x-axis limits to start from maximum absolute value for proper alignment
plt.xlim(-max(y), 0)

# Adjusting the labels to be on the right side
plt.gca().invert_xaxis()

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
