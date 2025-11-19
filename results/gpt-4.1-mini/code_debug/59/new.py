import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

group = np.repeat(['G1', 'G2'], 4)
value = np.array(['1', '2', '3', '4', '1', '2', '3', '4'])
percentage = np.array([20, 10, 40, 30, 50, 25, 20, 5])
stacked = pd.DataFrame({'Group': group, 'Value': value, 'Percentage': percentage})

# Define the order of the hue categories to reverse stacking order
hue_order = ['1', '2', '3', '4']

sns.histplot(
    stacked,
    x='Group',
    hue='Value',
    weights='Percentage',
    multiple='stack',
    palette='colorblind',
    shrink=0.75,
    hue_order=hue_order
)

# Use the same order reversed for legend labels to match stacking order
plt.legend(labels=hue_order[::-1], bbox_to_anchor=(1, 1), fontsize=8)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
