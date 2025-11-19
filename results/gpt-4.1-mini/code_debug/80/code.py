import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Calculate mean and confidence intervals manually
import numpy as np
import pandas as pd
from scipy import stats

# Group data by 'day'
grouped = tips.groupby('day')['total_bill']

# Calculate mean, count, std, sem, and confidence intervals
summary = grouped.agg(['mean', 'count', 'std'])
summary['sem'] = summary['std'] / np.sqrt(summary['count'])
confidence = 0.95
h = summary['sem'] * stats.t.ppf((1 + confidence) / 2., summary['count'] - 1)
summary['lower'] = summary['mean'] - h
summary['upper'] = summary['mean'] + h

# Plot only the confidence interval as a filled area
plt.fill_between(summary.index, summary['lower'], summary['upper'], alpha=0.3)

plt.xlabel('day')
plt.ylabel('total_bill')
plt.show()