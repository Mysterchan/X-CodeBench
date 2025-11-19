import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
so.Plot(tips, x="day", color="sex").add(so.Bar(), so.Count(), so.Dodge(gap=0.2))
