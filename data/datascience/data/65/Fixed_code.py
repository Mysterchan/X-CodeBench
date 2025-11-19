import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

test = pd.DataFrame({'month': ['2019-01','2019-02','2019-03','2019-04','2019-05'],
             'freq':[3,5,22,6,3],
             'word':['hello','world','seaborn','seaborn','python']})

for i in test.index:
    word = test.loc[i, "word"]
    y = test.loc[i, "freq"]
    plt.annotate(word, (i, y), ha="center", va="bottom")

sns.barplot(x = 'month', y = 'freq', data = test)