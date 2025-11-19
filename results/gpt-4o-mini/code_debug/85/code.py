import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Group': ['Simple', 'Simple', 'Complex', 'Complex', 'Cool'],
    'Algorithm': ['Alg 1', 'Alg 2', 'Alg 3', 'Alg 4', 'Alg 2'],
    'Results': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Create a filter to keep only necessary algorithms
filtered_df = df[(df['Group'] != 'Cool') | (df['Algorithm'].isin(['Alg 2', 'Alg 3', 'Alg 4']))]
filtered_df = df[(df['Group'] == 'Simple') & (df['Algorithm'] == 'Alg 1') | (df['Group'] == 'Complex') & (df['Algorithm'].isin(['Alg 3', 'Alg 4'])) | (df['Group'] == 'Cool') & (df['Algorithm'] == 'Alg 2')]

# Plot the data
sns.barplot(x='Group', y='Results', hue='Algorithm', data=filtered_df)
plt.show()