import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

# Data
x = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
y = [1, 2, 3, 4, 5.8]
df = pd.DataFrame({'X': pd.to_datetime(x), 'Y': y})

# Plot
fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)

# Highlight maximum point
max_value = 5.7
ax.axhline(max_value, ls='dotted', color='blue')
ax.text(pd.to_datetime('2020-03-01'), max_value + 0.2, s=str(max_value), color='red', ha='center', va='bottom')

# Highlight minimum point
min_value = 1.7
ax.axhline(min_value, ls='dotted', color='blue')
ax.text(df['X'].iloc[0], min_value - 0.2, s=str(min_value), color='red', ha='center', va='top')

plt.show()