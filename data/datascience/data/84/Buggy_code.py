import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Travel':  ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
    'Transporation': ['Airplaine', np.nan, 'Car', 'Train', 'Train', 'Car', 'np.nan']
    }
df = pd.DataFrame (data, columns = ['Travel','Transporation'])

ax = sns.countplot(y='Travel', data=df, palette=['green',"red"])
ax.set_yticklabels(ax.get_yticklabels(), rotation=45)
ax.set_title('Travel last year')
ax.set_ylabel('')
total = df.shape[0]
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_width()/total)
    x = p.get_x() + p.get_width()# / 2 - 0.05
    y = p.get_y() + p.get_height() / 2 - 0.05
    ax.annotate(percentage, (x, y), size = 12)
plt.show()