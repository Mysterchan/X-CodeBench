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
sns.lineplot(x=x*num, y=y*num)

plt.show()