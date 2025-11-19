import seaborn as sns
from scipy.stats import gaussian_kde
from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset('planets')
data = df.mass.dropna()
kde = gaussian_kde(data)

x = np.linspace(data.min(), data.max(), 1000)
y = kde(x)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(x, y, c='k')

# Fill area for x < 0
x_neg = x[x < 0]
y_neg = y[x < 0]
ax.fill_between(x_neg, y_neg, color='red', alpha=0.5)

# Fill area for x >= 0
x_pos = x[x >= 0]
y_pos = y[x >= 0]
ax.fill_between(x_pos, y_pos, color='blue', alpha=0.5)

# Calculate proportions
total_area = simps(y, x)
area_neg = simps(y_neg, x_neg)
area_pos = simps(y_pos, x_pos)

# Add annotations
ax.annotate(f'{area_neg/total_area*100:.0f}%', xy=(x_neg[len(x_neg)//2], y_neg[len(y_neg)//2]),
            xytext=(x_neg[len(x_neg)//2]-5, y_neg[len(y_neg)//2]+0.05),
            arrowprops=dict(facecolor='red', alpha=0.3, shrink=0.05),
            color='red')

ax.annotate(f'{area_pos/total_area*100:.0f}%', xy=(x_pos[len(x_pos)//3], y_pos[len(y_pos)//3]),
            xytext=(x_pos[len(x_pos)//3]+5, y_pos[len(y_pos)//3]+0.05),
            arrowprops=dict(facecolor='blue', alpha=0.3, shrink=0.05),
            color='blue')

ax.set_xlabel('mass')
ax.set_ylabel('Density')

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
