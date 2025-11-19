import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = pd.DataFrame({'a': [1, 0, 1, 0]})
fig, (ax) = plt.subplots(ncols=1)
sns.heatmap(x, cmap="BuPu", annot=False, ax=ax, yticklabels=[], cbar=False, linewidths=.5)

for i, c in enumerate(x.columns):
    for j, v in enumerate(x[c]):
        if v == 1:
            ax.text(i + 0.5, j + 0.5, '★', color='gold', size=20, ha='center', va='center')

plt.show()