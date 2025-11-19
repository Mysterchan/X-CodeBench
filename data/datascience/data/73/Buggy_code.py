import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

years = range(2016,2019)
months = range(1,6)
df = pd.DataFrame(index=pd.MultiIndex.from_product([years,months]))
df['vals'] = np.random.random(size=len(df))
sns.heatmap(df)