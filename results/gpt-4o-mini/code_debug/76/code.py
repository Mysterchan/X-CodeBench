import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_dict = {'court': [1, 1, 2, 2, 3, 3, 4, 4],
           'player': ['Bob', 'Ian', 'Bob', 'Ian', 'Bob', 'Ian', 'Ian', 'Bob'],
           'score': [6, 8, 12, 15, 8, 16, 11, 13],
           'win': ['no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes']}

df = pd.DataFrame.from_dict(df_dict)

ax = sns.boxplot(x='score', y='player', data=df)
ax = sns.swarmplot(x='score', y='player', hue='win', data=df, s=10, palette=['red', 'green'])

# Adding connecting lines between points representing the same player across different courts
for player in df['player'].unique():
    player_data = df[df['player'] == player]
    plt.plot(player_data['score'], [player] * len(player_data), color='gray', alpha=0.5)

plt.legend(title='win')
plt.show()