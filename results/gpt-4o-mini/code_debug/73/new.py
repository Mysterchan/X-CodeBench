import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

years = range(2016, 2019)
months = range(1, 6)
df = pd.DataFrame(index=pd.MultiIndex.from_product([years, months]))
df['vals'] = np.random.random(size=len(df))

# Create a heatmap with y-axis labels showing only years
heatmap = sns.heatmap(df, yticklabels=["{}".format(year) for year, month in df.index.tolist()])

import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
