import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

np.random.seed(42)
n = 5000
df = pd.DataFrame({
    'PERSON': np.random.randint(100000, 999999, n),
    'Fruit': np.random.choice(['Banana', 'Strawberry'], n),
    'Age': np.random.randint(9, 18, n)
})

# Create a count plot instead of a displot for better control
fig = sns.countplot(
    data=df,
    x='Age',
    hue='Fruit',
    dodge=True)

# Improve tick placement on x-axis
plt.xticks(ticks=np.arange(9, 18, 1), labels=np.arange(10, 17, 2), rotation=0)
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Fruit')
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
