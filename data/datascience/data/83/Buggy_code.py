import seaborn as sns

tips = sns.load_dataset("tips")
ax = sns.violinplot(x="day", y="total_bill", hue="sex",
                    data=tips, palette="Set2", split=True,
                    scale="count", inner="stick",
                    scale_hue=False, bw=.2)