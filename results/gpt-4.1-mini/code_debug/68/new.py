import matplotlib.pyplot as plt
import seaborn as sns

x = ['x1', 'x2', 'x3']
y = [4, 6, 3]

ax = sns.barplot(x=y, y=x, orient='h')
ax.invert_xaxis()
ax.yaxis.tick_right()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
