import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe from the input data
x = {
    'prediction': {5: 'c1', 4: 'c1', 3: 'c1', 2: 'c1', 0: 'c1', 1: 'c1', 7: 'c1', 6: 'c1'},
    'variable': {5: 'ft1', 4: 'ft2', 3: 'ft3', 2: 'ft4', 0: 'ft5', 1: 'ft6', 7: 'ft7', 6: 'ft8'},
    'value': {5: 0.020915912763961077, 4: 0.020388363414781133, 3: 0.007204373035913109, 2: 0.0035298765062560817,
              0: -0.002049702058734183, 1: -0.004283512505036808, 7: -0.01882610282871816, 6: -0.022324439779323434}
}
df = pd.DataFrame.from_dict(x)

# Create horizontal bar plot with red bars
sns.barplot(data=df, x='value', y='variable', hue='prediction', orient="h", palette=["red"])

# Remove the legend for hue since all bars are the same color
plt.legend(title='prediction', loc='upper right', handles=[plt.Line2D([0], [0], color='red', lw=4)])

import os
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images', '2.png'))
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
