from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

data = {'species': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Z', 'Z'],
        'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
        'mass (g)': [4000, 3500, 3800, 3200, 5500, 4900, 2500, 2100, 2400, 2000, 4200, 3800],
        'age': ['adult', 'adult', 'adult', 'adult', 'adult', 'adult', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile']}
df = pd.DataFrame(data)
df['sex'] = pd.Categorical(df['sex'])  # make hue column categorical, forcing a fixed order

sns.set_theme(style='whitegrid')
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5), sharey=True, gridspec_kw={'wspace': 0})


# draw adult subplot at the right
sns.barplot(data=df[df['age'] == 'adult'], x='mass (g)', y='species', hue='sex',
            ci=False, orient='horizontal', dodge=True, ax=ax2)
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='y', labelright=True, right=True)
ax2.set_title('  '+'adult', loc='left')
ax2.legend_.remove()  # remove the legend; the legend will be in ax1

# draw juvenile subplot at the left
sns.barplot(data=df[df['age'] == 'juvenile'], x='mass (g)', y='species', hue='sex',
            ci=False, orient='horizontal', dodge=True, ax=ax1)

# optionally use the same scale left and right
xmax = max(ax1.get_xlim()[1], ax2.get_xlim()[1])
ax1.set_xlim(xmax=xmax)
ax2.set_xlim(xmax=xmax)

ax1.invert_xaxis()  # reverse the direction
ax1.tick_params(labelleft=False, left=False)
ax1.set_ylabel('')
ax1.set_title('juvenile'+'  ', loc='right')

plt.tight_layout()