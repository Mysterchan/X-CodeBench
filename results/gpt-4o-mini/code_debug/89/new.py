import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

num = 11
a = np.eye(num)
x = np.round(np.linspace(0, 1, num=num), 1)
y = np.round(np.linspace(0, 1, num=num), 1)

df = pd.DataFrame(a, columns=x, index=y)

f, ax = plt.subplots()
ax = sns.heatmap(df, cbar=False)
ax.axes.invert_yaxis()

# Update the lineplot to use the correct limits for the diagonal line
sns.lineplot(x=[0, 1], y=[0, 1], ax=ax, color='blue')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
