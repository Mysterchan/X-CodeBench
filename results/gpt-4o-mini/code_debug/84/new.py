import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Corrected spelling and replaced np.nan with None
data = {'Travel':  ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
        'Transporation': ['Airplane', None, 'Car', 'Train', 'Train', 'Car', None]
       }
df = pd.DataFrame(data, columns=['Travel', 'Transporation'])

# Filter out rows with None in Transportation
df = df.dropna(subset=['Transporation'])

# Create a count of travel by type
travel_counts = df.groupby(['Travel', 'Transporation']).size().unstack(fill_value=0)

# Plotting
ax = travel_counts.plot(kind='barh', stacked=True, color=['blue', 'orange', 'green'], legend=True)
ax.set_title('Travel last year')
ax.set_ylabel('')

# Annotation of the percentages
for i in ax.patches:
    width = i.get_width()
    ax.annotate(f'{width * 100 / travel_counts.sum().sum():.1f} %', 
                (width, i.get_y() + i.get_height() / 2), 
                ha='center', va='center', color='white', fontsize=10)

# We need to also calculate and display the percentage for the 'No' category
no_count = df[df['Travel'] == 'No'].shape[0]
total_count = df.shape[0]
ax.annotate(f'{no_count * 100 / total_count:.1f} %', 
            (0, 1), 
            ha='center', va='center', color='white', fontsize=10)

plt.legend(title='Transportation')
plt.tight_layout()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
