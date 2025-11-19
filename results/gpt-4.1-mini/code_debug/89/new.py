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
sns.heatmap(df, cbar=False, ax=ax)
ax.invert_yaxis()
ax.plot([x[0], x[-1]], [y[0], y[-1]], color='tab:blue')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
