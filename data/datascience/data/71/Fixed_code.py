from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)

kdeplot = sns.jointplot(x=np.random.normal(0.25, 0.5, 10), y=np.random.normal(0.25, 0.5, 10),
                          kind='kde', xlim=(-.75, 1.25), ylim=(-.75, 1.25), height=4)
# draw a vertical line on the joint plot, optionally also on the x margin plot
for ax in (kdeplot.ax_joint, kdeplot.ax_marg_x):
    ax.axvline(0, color='crimson', ls='--', lw=3)

import os
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images','2.png'))