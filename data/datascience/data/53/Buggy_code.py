import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms

x = ['2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04', '2020-03-05']
y = [1,2,3,4,5.8]
df = pd.DataFrame({'X': x, 'Y': y})

fig, ax = plt.subplots()
sns.lineplot(x='X', y='Y', data=df)
show_point = 5.7
ax.axhline(show_point, ls='dotted')
trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transData)
ax.text('2020-03-01', show_point, color="red", s=show_point, transform=trans, ha="right", va="bottom")

show_point2 = 1.7
ax.axhline(show_point2, ls='dotted')
trans = transforms.blended_transform_factory(ax.get_yticklabels()[0].get_transform(), ax.transAxes)
ax.text(0.05, 0.15, color="red", s=show_point2, transform=trans, ha="center", va="bottom")

plt.show()