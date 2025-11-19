import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import pandas as pd
import numpy as np

def myFunc(x):
    myReturn = x + 1 * np.random.random(x.shape[0])
    return myReturn

np.random.seed(1)
a = np.arange(0, 10, 0.1)
np.random.rand()

b = myFunc(a)
c = a * np.sin(a)
df = pd.DataFrame({'a': a, 'b': b, 'c': c})

cmap = LinearSegmentedColormap.from_list('blue-yellow', ['gold', 'lightblue', 'darkblue'])  # plt.get_cmap('viridis_r')
g = sns.pairplot(df, corner=True)
for ax in g.axes.flat:
    if ax is not None and not ax in g.diag_axes:
        for collection in ax.collections:
            collection.set_cmap(cmap)
            collection.set_array(df['a'])

import os
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images','2.png'))