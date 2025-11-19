import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Data
np.random.seed(42)
n = 5000
df = pd.DataFrame({
    'PERSON': np.random.randint(100000, 999999, n),
    'Fruit': np.random.choice(['Banana', 'Strawberry'], n),
    'Age': np.random.randint(9, 18, n)
})

sns.displot(
    data=df,
    x='Age',
    hue='Fruit',
    multiple='dodge',
    discrete=True,
    shrink=0.8)
