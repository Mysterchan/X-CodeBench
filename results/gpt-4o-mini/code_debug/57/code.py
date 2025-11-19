import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 1, 2, 3]
cat = ['N','Y','N','N','N']
test = pd.DataFrame(list(zip(x, cat)), 
                    columns=['x', 'cat'])

colors = {'N': 'gray', 'Y': 'blue'}

# First, plot the 'N' category in gray
sns.scatterplot(data=test[test['cat'] == 'N'], x='x', y='x', 
                color='gray', label='N')

# Then, plot the 'Y' category in blue on top
sns.scatterplot(data=test[test['cat'] == 'Y'], x='x', y='x', 
                color='blue', label='Y')

plt.legend(title='cat')
plt.show()