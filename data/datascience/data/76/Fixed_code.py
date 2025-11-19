import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_dict={'court':[1,1,2,2,3,3,4,4],
         'player':['Bob','Ian','Bob','Ian','Bob','Ian','Ian','Bob'],
         'score':[6,8,12,15,8,16,11,13],
         'win':['no','yes','no','yes','no','yes','no','yes']}

df=pd.DataFrame.from_dict(df_dict)

ax = sns.boxplot(x='score',y='player',data=df)
sns.lineplot(
    data=df, x="score", y="player", units="court",
    color=".7", estimator=None
)
ax = sns.swarmplot(x='score',y='player',hue='win',data=df,s=10,palette=['red','green'])
# plt.show()
