import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import numpy as np


np.random.seed(0)
t = pd.DataFrame(
    {
    'Value': np.random.uniform(low=100000, high=500000, size=(50,)), 
    'Type': ['B' if x < 6 else 'R' for x in np.random.uniform(low=1, high=10, size=(50,))] 
    }
)

ax = sns.histplot(data=t, x='Value', bins=5, hue='Type', palette="dark")
ax.set(title="R against B")
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}\n',
                (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='center', color='crimson')        
plt.show()
