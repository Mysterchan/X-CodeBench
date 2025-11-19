import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {'x': [3,2,5,1,1,0],
     'y': [1,1,2,3,0,2],
     'cat': ['a','a','a','b','b','b']}
)

sns.scatterplot(data=df, x='x', y='y', hue='cat', facecolors='none', s=100, edgecolor='auto')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
