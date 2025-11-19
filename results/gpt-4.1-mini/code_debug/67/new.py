import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'species': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Z', 'Z'],
        'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'], 
        'mass (g)': [4000, 3500, 3800, 3200, 5500, 4900, 2500, 2100, 2400, 2000, 4200, 3800],
        'age': ['adult', 'adult', 'adult', 'adult', 'adult', 'adult', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile']}
df = pd.DataFrame(data)

# Negate juvenile masses to plot them on the left side
df.loc[df.age.eq('juvenile'), 'mass (g)'] = df.loc[df.age.eq('juvenile'), 'mass (g)'] * -1

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10,5))

# Create a combined categorical variable for species and age to separate juvenile and adult groups
df['species_age'] = df['species'] + ' ' + df['age']

# Plot horizontal barplot with hue=sex, dodge=False to stack male/female bars
sns.barplot(data=df, x='mass (g)', y='species_age', hue='sex', ci=False, orient='h', dodge=False, ax=ax)

# Draw vertical line at zero to separate juvenile and adult bars
ax.axvline(0, color='black')

# Adjust y-axis labels to show only species (remove age from labels)
yticks = ax.get_yticks()
ylabels = [label.get_text().split()[0] for label in ax.get_yticklabels()]
ax.set_yticklabels(ylabels)

# Add top x-axis labels for juvenile and adult groups
ax_top = ax.twiny()
ax_top.set_xlim(ax.get_xlim())
midpoint = 0
juvenile_pos = (ax.get_xlim()[0] + midpoint) / 2
adult_pos = (midpoint + ax.get_xlim()[1]) / 2
ax_top.set_xticks([juvenile_pos, adult_pos])
ax_top.set_xticklabels(['juvenile', 'adult'])
ax_top.xaxis.set_ticks_position('top')
ax_top.xaxis.set_label_position('top')
ax_top.set_xlabel('')

# Move y-axis ticks and label to the right
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_ylabel('species')

# Reverse legend order to match expected output (female first)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='sex')

plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
