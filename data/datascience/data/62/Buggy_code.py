import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x="day", y="total_bill", data=tips)