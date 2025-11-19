import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = pd.DataFrame({'a':[1,0,1,0]})

# Create annotation DataFrame with '*' for 1 and '' for 0
annot = x.replace({1: '★', 0: ''})

fig, ax = plt.subplots(ncols=1)
sns.heatmap(x, cmap="BuPu", annot=annot, fmt='', annot_kws={'size':20, 'color':'gold'}, ax=ax, yticklabels=[], cbar=False, linewidths=.5, robust=True, vmin=0, vmax=1)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
