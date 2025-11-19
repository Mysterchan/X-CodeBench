import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'species': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Z', 'Z'],
        'sex': ['female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male'], 
        'mass (g)': [3500, 4000, 3200, 3800, 4900, 5500, 2100, 2500, 2000, 2400, 3800, 4200],
        'age': ['adult', 'adult', 'adult', 'adult', 'adult', 'adult', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile', 'juvenile']}
df = pd.DataFrame(data)

# Calculate widths for juveniles and adults
juvenile_mass = df[df['age'] == 'juvenile'].copy()
adult_mass = df[df['age'] == 'adult'].copy()

# Create a new DataFrame for plotting
juvenile_mass['mass (g)'] = juvenile_mass['mass (g)'] * -1
df_combined = pd.concat([juvenile_mass, adult_mass])

sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 5))

# Use barplot to show juvenile and adult with sex as hue
sns.barplot(data=df_combined, x='mass (g)', y='species', hue='sex', ci=False, orient='horizontal', dodge=True)

# Customizing axes to have correct labels
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.set_xticks(ax.get_xticks())
ax.set_xticklabels([abs(int(x)) for x in ax.get_xticks()])
ax.set_xlabel("mass (g)")
ax.set_title("Mass of Individuals by Species, Age, and Sex")

# Set x-axis limits to see separation clearly
ax.set_xlim(-6000, 6000)
ax.legend(title='sex', loc='upper right', bbox_to_anchor=(1.1, 1))

# Add vertical lines to separate juvenile and adult mass
ax.axvline(x=0, color='black', linewidth=1)

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
