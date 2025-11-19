import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
data = [['Alex',25],['Bob',34],['Sofia',26],["Claire",35]]
df = pd.DataFrame(data,columns=['Name','Age'])
df["sex"]=["male","male","female","female"]


age_plot=sns.barplot(data=df,x="Name",y="Age", hue="sex",dodge=False)
age_plot.get_legend().remove()
plt.setp(age_plot.get_xticklabels(), rotation=90)
plt.ylim(0,40)
age_plot.tick_params(labelsize=14)
age_plot.set_ylabel("Age",fontsize=15)
age_plot.set_xlabel("",fontsize=1)
plt.tight_layout()
plt.show()