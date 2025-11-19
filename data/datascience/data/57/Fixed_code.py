import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 1, 2, 3]
cat = ['N','Y','N','N','N']
test = pd.DataFrame(list(zip(x,cat)), 
                  columns =['x','cat']
                 )

hue_order = ["N", "Y"]
colors = {'N': 'gray', 'Y': 'blue'}
sns.scatterplot(
    data=test.sort_values('cat', key=np.vectorize(hue_order.index)),
    x='x', y='x',
    hue='cat', hue_order=hue_order,
    palette=colors, s=100,
)

plt.show()