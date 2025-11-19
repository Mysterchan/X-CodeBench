import matplotlib.pyplot as plt

x = ["A", "B", "C", "D", "E", "F", "G", "H"]
y = [-25, -10, 5, 10, 30, 40, 50, 60]
colors = ["yellow", "limegreen", "green", "blue", "red", "brown", "grey", "black"]

# Create uniform width for bars
bar_width = 0.8  # Set a fixed width for uniformity

# Create bar chart
plt.bar(x, height=y, width=bar_width, color=colors, alpha=0.8)

# Add a legend
plt.legend(x, title="Categories", loc="upper left", bbox_to_anchor=(1, 1))

# Set limits for x-axis
plt.xlim((-0.5, len(x) - 0.5))

# Display plot
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
