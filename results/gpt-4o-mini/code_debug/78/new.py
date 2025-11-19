import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(1)
a = np.arange(0, 10, 0.1)

def myFunc(x):
    myReturn = x + 1*np.random.random(x.shape[0])
    return myReturn

b = myFunc(a)
c = a * np.sin(a)

df = pd.DataFrame({'a': a, 'b': b, 'c': c})

# Create a new column for color mapping based on 'b'
df['color'] = pd.cut(df['b'], bins=10, labels=range(10))

# Create a pairplot with a custom palette using the 'color' column
pal = sns.color_palette("YlGnBu", as_cmap=True)

g = sns.pairplot(df, corner=True, plot_kws={'scatter_kws': {'c': df['color'], 'cmap': pal}})
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
