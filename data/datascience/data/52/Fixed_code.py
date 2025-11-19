import seaborn as sns
import matplotlib.pyplot as plt     
cm = [[1102,   88],
   [  85,  725]]
sns.heatmap(cm, annot=True,fmt="d",cmap='Blues')
plt.show()