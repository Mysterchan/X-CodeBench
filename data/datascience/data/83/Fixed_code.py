import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
ax = sns.violinplot(x="day", y="total_bill", hue="sex",
                    data=tips, palette="Set2", split=True,
                    scale="count", inner="stick",
                    scale_hue=False, bw=.2, width=2.5,
                    order=('Thur', 'Fri', '', 'Sat', '', 'Sun'))

# get rid of ticks for empty columns (levels)
ax.set_xticks([0,1,3,5])
ax.set_xticklabels(['Thur', 'Fri', 'Sat', 'Sun'])

plt.show()