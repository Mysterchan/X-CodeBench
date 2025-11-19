import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame([['2017-01-01', 'Orange', 'FP'], ['2017-04-01', 'Orange', 'CP'], ['2017-07-01', 'Orange', 'CP'], ['2017-10-08', 'Orange', 'CP'], ['2017-01-01', 'Apple', 'NP'], ['2017-04-01', 'Apple', 'CP'], ['2017-07-01', 'Banana', 'NP'], ['2017-10-08', 'Orange', 'CP']], columns=['Date', 'Fruit', 'type'])
df['quarter'] = pd.PeriodIndex(df['Date'], freq='Q')

df = df.sort_values('quarter')
df['xticks'] = df.groupby('quarter').ngroup()
ends = df.groupby('Fruit')['xticks'].agg(['min', 'max'])

g = sns.catplot(x='quarter', y='Fruit', hue='type', kind='swarm', s=8, data=df)
g.axes[0, 0].hlines(ends.index, ends['min'], ends['max'])

import os
import matplotlib.pyplot as plt
cur_dir = os.path.dirname(__file__)
plt.savefig(os.path.join(cur_dir, 'images','2.png'))