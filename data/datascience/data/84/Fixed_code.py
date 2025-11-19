import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Travel': ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
        'Transporation': ['Airplaine', np.nan, 'Car', 'Train', 'Train', 'Car', 'np.nan']}
df = pd.DataFrame (data, columns = ['Travel','Transporation'])

df_plot = df.fillna('_Hidden').replace('np.nan', '_Hidden').groupby(['Travel', 'Transporation']).size().reset_index().pivot(columns = 'Transporation', index = 'Travel', values = 0)
ax = df_plot.plot(kind = 'barh', stacked = True)
ax.legend(['Airplaine', 'Car', 'Train'])
ax.set_yticklabels(ax.get_yticklabels(), rotation = 45)
ax.set_title('Travel last year')
ax.set_ylabel('')

total = df.shape[0]
yes = len(df[df['Travel'] == 'Yes'])/total
no = len(df[df['Travel'] == 'No'])/total
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    x = x + width
    y = y + height / 2 - 0.05

    if x/total == yes:
        ax.annotate(f'{round(100*yes, 1)}%', (x, y), size = 12)
    if x/total == no:
        ax.annotate(f'{round(100*no, 1)}%', (x, y), size = 12)

    if width != 0:
        x, y = p.get_xy()
        if y > 0:
            ax.text(x + width/2,
                    y + height/2,
                    '{:.0f} %'.format(100*width/(yes*total)),
                    horizontalalignment = 'center',
                    verticalalignment = 'center')

plt.show()