import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# sample data
data = {'fruity': -0.380938, 'hard': -0.310382, 'pluribus': -0.247448,
        'nougat': 0.199375, 'caramel': 0.213416, 'crispedricewafer': 0.32468,
        'peanutyalmondy': 0.406192, 'bar': 0.429929, 'chocolate': 0.636517}
win_corr = pd.Series(data)

color = ['black','red','green','orange','blue','limegreen','darkgreen','royalblue','navy']

fig, ax = plt.subplots(figsize=(8,6))
ax = sns.barplot(x=win_corr.values, y=win_corr.index, hue=win_corr.index, orient='h', palette=color, dodge=False)
ax.set_ylabel('')    
ax.set_xlabel('Value')
plt.title('Correlation Coefficients for winpercent')
ax.bar_label(ax.containers[0], fmt= '%0.1f', label_type='center' )

plt.show()