import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
exercise = sns.load_dataset("exercise")
f, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, sharey=True)
f = sns.catplot(x="time", y="pulse", hue="kind",data=exercise, kind="violin",ax=ax1)
f = sns.catplot(x="time", y="pulse", hue="kind",data=exercise, kind="violin",ax=ax2)
ax1.set_ylim(0, 6.5)   # those limits are fake
ax2.set_ylim(13.5, 20)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()