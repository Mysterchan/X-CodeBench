import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
y = [1, 2, 3, 4, 5.8]
df = pd.DataFrame({'X': pd.to_datetime(x), 'Y': y})

fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)

show_point = 5.7
ax.axhline(show_point, ls='dotted')
# Place the max label slightly right and above the line to avoid overlap with y-axis ticks
ax.text(df['X'].iloc[1], show_point, f"{show_point}", color="red", ha="left", va="bottom")

show_point2 = 1.7
ax.axhline(show_point2, ls='dotted')
# Place the min label slightly right and above the line, aligned with the second x value for clarity
ax.text(df['X'].iloc[1], show_point2, f"{show_point2}", color="red", ha="left", va="bottom")

plt.show()