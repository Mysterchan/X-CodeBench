import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

a4_dims = (12, 4)
fig, ax = plt.subplots(figsize=a4_dims)
ax.set_xlim(-.75, 1.25)
ax.set_ylim(-.75,1.25)
plt.axvline(0)
sns.jointplot(x=np.random.normal(0.25, 0.5, 10), y=np.random.normal(0.25, 0.5, 10),
                          kind='kde', xlim=(-.75, 1.25), ylim=(-.75, 1.25), height=4)