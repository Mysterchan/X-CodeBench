import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_dict={'court':[1,1,2,2,3,3,4,4],
         'player':['Bob','Ian','Bob','Ian','Bob','Ian','Ian','Bob'],
         'score':[6,8,12,15,8,16,11,13],
         'win':['no','yes','no','yes','no','yes','no','yes']}

df=pd.DataFrame.from_dict(df_dict)

plt.figure(figsize=(8,5))
ax = sns.boxplot(x='score', y='player', data=df)
ax = sns.swarmplot(x='score', y='player', hue='win', data=df, s=10, palette=['red','green'])

# Create a mapping from player to y-axis position
yticks = ax.get_yticks()
yticklabels = [t.get_text() for t in ax.get_yticklabels()]
player_to_y = dict(zip(yticklabels, yticks))

# For each player, plot lines connecting their points across courts
for player in df['player'].unique():
    player_data = df[df['player'] == player].sort_values('court')
    x = player_data['score'].values
    y = np.array([player_to_y[player]] * len(player_data))
    ax.plot(x, y, color='gray', linewidth=1, zorder=0)

plt.legend(title='win', loc='best')
plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
