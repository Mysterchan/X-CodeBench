import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
fmri = sns.load_dataset("fmri")
fmri.sort_values('timepoint',inplace=True)
ax = sns.lineplot(x="timepoint", y="signal", data=fmri)
arr = np.ones(len(fmri))
arr[:300] = 0
arr[600:] = 2
fmri['background'] = arr

ax = sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)
