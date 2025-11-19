import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 1, 2, 3]
cat = ['N','Y','N','N','N']
test = pd.DataFrame(list(zip(x,cat)), 
                  columns =['x','cat']
                 )

colors = {'N': 'gray', 'Y': 'blue'}
sns.scatterplot(data=test, x='x', y='x', 
                hue='cat', hue_order=['Y', 'N', ],
                palette=colors,
               )

plt.show()