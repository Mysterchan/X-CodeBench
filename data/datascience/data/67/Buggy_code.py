import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'species': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Z', 'Z'],
        'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'], 
        'mass (g)': [4000, 3500, 3800, 3200, 5500, 4900, 2500, 2100, 2400, 2000, 4200, 3800],
        'age': ['adult', 'adult', 'adult', 'adult', 'adult', 'adult', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile']}
df = pd.DataFrame(data)

df.loc[df.age.eq('juvenile'), 'mass (g)'] = df['mass (g)'].mul(-1)

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=df, x='mass (g)', y='species', hue='sex', ci=False, orient='horizontal', dodge=True)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
