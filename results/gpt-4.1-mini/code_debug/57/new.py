import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 1, 2, 3]
cat = ['N','Y','N','N','N','N']
test = pd.DataFrame(list(zip(x,cat)), 
                  columns =['x','cat']
                 )

colors = {'N': 'gray', 'Y': 'blue'}

# Plot 'N' category first (gray points)
sns.scatterplot(data=test[test['cat'] == 'N'], x='x', y='x', 
                color=colors['N'], label='N')

# Plot 'Y' category on top (blue points)
sns.scatterplot(data=test[test['cat'] == 'Y'], x='x', y='x', 
                color=colors['Y'], label='Y')

plt.legend(title='cat')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
