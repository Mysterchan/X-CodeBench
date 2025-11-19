import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import numpy as np


np.random.seed(0)
t = pd.DataFrame(
    {
    'Value': np.random.uniform(low=100000, high=500000, size=(50,)), 
    'Type': ['B' if x < 6 else 'R' for x in np.random.uniform(low=1, high=10, size=(50,))] 
    }
)

palette = sns.color_palette("dark", 2)
color_map = {'R': palette[0], 'B': palette[1]}

ax = sns.histplot(data=t, x='Value', bins=5, hue='Type', palette="dark")
ax.set(title="R against B")
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))

for p in ax.patches:
    # Get the color of the patch
    patch_color = p.get_facecolor()
    # Find the closest matching color in the palette to determine the type
    # Since we know the order of hues in the legend, we can map colors by comparing
    # But simpler is to use the patch's label or the hue order from the legend
    # Instead, we can get the color from the patch and match it to the palette keys
    # We'll compare the patch color to the palette colors to find the closest match
    # Convert to RGB ignoring alpha
    patch_rgb = patch_color[:3]
    # Find closest color in color_map
    def color_dist(c1, c2):
        return sum((a - b) ** 2 for a, b in zip(c1, c2))
    closest_type = min(color_map.keys(), key=lambda k: color_dist(patch_rgb, color_map[k]))
    ax.annotate(f'{p.get_height():.0f}\n',
                (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center', color=color_map[closest_type])        
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
