import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
y = [1,2,3,4,5.8]
df = pd.DataFrame({'X': x, 'Y': y})

fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)
show_point = 5.7
ax.axhline(show_point, ls='dotted')
ax.annotate(show_point, [ax.get_xticks()[0], show_point], va='bottom', 
            ha='right', color='red')

show_point2 = 1.7
ax.axhline(show_point2, ls='dotted')
ax.annotate(show_point2, [ax.get_xticks()[0], show_point2], va='bottom', 
            ha='right', color='red')

plt.show()