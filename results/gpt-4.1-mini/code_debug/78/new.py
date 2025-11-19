import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors

np.random.seed(1)
a = np.arange(0, 10, 0.1)

def myFunc(x):
    return x + 1*np.random.random(x.shape[0])

b = myFunc(a)
c = a * np.sin(a)

df = pd.DataFrame({'a': a, 'b': b, 'c': c})

# Normalize 'b' for color mapping
norm = mcolors.Normalize(vmin=df['b'].min(), vmax=df['b'].max())
cmap = plt.cm.get_cmap('YlGnBu')

# Create the pairplot without default scatterplots
g = sns.pairplot(df, corner=True, diag_kind='hist', plot_kws={'s': 40, 'alpha': 0.8})

# Apply color gradient to all off-diagonal scatter plots
for i, j in zip(*np.tril_indices_from(g.axes, -1)):
    ax = g.axes[i, j]
    x_var = df.columns[j]
    y_var = df.columns[i]
    colors = cmap(norm(df['b']))
    ax.clear()
    ax.scatter(df[x_var], df[y_var], c=colors, s=40, alpha=0.8)
    ax.set_xlabel(x_var)
    ax.set_ylabel(y_var)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
