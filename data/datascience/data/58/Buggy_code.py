import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = pd.DataFrame({'a':[1,0,1,0]})
fig, (ax) = plt.subplots(ncols=1)
sns.heatmap(x, cmap="BuPu",annot=True,fmt='g',annot_kws={'size':10},ax=ax, yticklabels=[], cbar=False, linewidths=.5,robust=True, vmin=0, vmax=1)

plt.show()