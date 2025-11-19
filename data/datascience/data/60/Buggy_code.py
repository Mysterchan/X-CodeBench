import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random((10,10,)))

fig,axn = plt.subplots(2, 2, sharex=True, sharey=True)

for ax in axn.flat:
    sns.heatmap(df, ax=ax)