import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

group = ['Simple', 'Simple', 'Complex', 'Complex', 'Cool']
alg = ['Alg 1', 'Alg 2', 'Alg 3', 'Alg 4', 'Alg 2']
results = [i+1 for i in range(len(group))]

# Create DataFrame
df = pd.DataFrame({'Group': group, 'Algorithm': alg, 'Result': results})

# Plot with dodge=True (default) to avoid spacing issues
sns.barplot(data=df, x='Group', y='Result', hue='Algorithm')

plt.show()