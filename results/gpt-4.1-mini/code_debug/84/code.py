import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Travel':  ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
        'Transporation': ['Airplaine', np.nan, 'Car', 'Train', 'Train', 'Car', np.nan]
       }
df = pd.DataFrame(data, columns=['Travel', 'Transporation'])

# Fix typo in 'Airplaine' to 'Airplane'
df['Transporation'] = df['Transporation'].replace('Airplaine', 'Airplane')

# Calculate counts for 'No'
no_count = df[df['Travel'] == 'No'].shape[0]

# Calculate counts for each transportation mode among 'Yes'
yes_transport_counts = df[df['Travel'] == 'Yes']['Transporation'].value_counts()

# Total respondents
total = df.shape[0]

# Prepare data for stacked bar
transport_modes = ['Airplane', 'Car', 'Train']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # blue, orange, green

# Get counts in order of transport_modes, fill missing with 0
yes_counts = [yes_transport_counts.get(mode, 0) for mode in transport_modes]

fig, ax = plt.subplots(figsize=(8, 3))

# Plot stacked bar for 'Yes'
left = 0
for count, color, mode in zip(yes_counts, colors, transport_modes):
    if count > 0:
        ax.barh('Yes', count, left=left, color=color, label=mode)
        # Annotate percentage inside the segment
        pct = 100 * count / total
        x_pos = left + count / 2
        ax.text(x_pos, 'Yes', f'{pct:.0f} %', va='center', ha='center', color='white', fontsize=12)
        left += count

# Plot bar for 'No'
ax.barh('No', no_count, color='red')
# Annotate percentage for 'No'
pct_no = 100 * no_count / total
ax.text(no_count + 0.1, 'No', f'{pct_no:.1f}%', va='center', ha='left', fontsize=12)

ax.set_title('Travel last year')
ax.set_ylabel('')
ax.set_xlim(0, total + 1)

# Add legend for transportation modes only
ax.legend(title='Transportation', loc='lower right')

plt.tight_layout()
plt.show()