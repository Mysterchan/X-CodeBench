import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
fmri = sns.load_dataset("fmri")
fmri.sort_values('timepoint',inplace=True)
arr = np.ones(len(fmri))
arr[:300] = 0
arr[600:] = 2
fmri['background'] = arr
fmri['background'] = fmri['background'].astype(int).astype(str).map(lambda x: 'C'+x)

ax = sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)
ranges = fmri.groupby('background')['timepoint'].agg(['min', 'max'])
for i, row in ranges.iterrows():
    ax.axvspan(xmin=row['min'], xmax=row['max'], facecolor=i, alpha=0.3)

plt.show()