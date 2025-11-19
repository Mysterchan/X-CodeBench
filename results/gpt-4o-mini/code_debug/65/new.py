import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

test = pd.DataFrame({'month': ['2019-01','2019-02','2019-03','2019-04','2019-05'],
                     'freq':[3,5,22,6,3],
                     'word':['hello','world','seaborn','seaborn','python']})

# Create the bar plot
ax = sns.barplot(x='month', y='freq', data=test)

# Add labels on top of each bar
for index, row in test.iterrows():
    ax.text(row.name, row.freq, row.word, color='black', ha="center")

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
