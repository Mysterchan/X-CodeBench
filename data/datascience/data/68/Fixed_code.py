import matplotlib.pyplot as plt
import seaborn as sns

x = ['x1', 'x2', 'x3']
y = [4, 6, 3]
ax = sns.barplot(x=y, y=x, orient='h')

ax.invert_xaxis()
ax.yaxis.tick_right()

import os
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images','2.png'))