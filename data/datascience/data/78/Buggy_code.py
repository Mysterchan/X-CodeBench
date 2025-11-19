import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f, axes = plt.subplots(1, 1)

np.random.seed(1)
a = np.arange(0, 10, 0.1)

np.random.rand()

def myFunc(x):
    myReturn = x + 1*np.random.random(x.shape[0])
    return myReturn

b = myFunc(a)
c = a * np.sin(a)

df = pd.DataFrame({'a': a, 'b': b, 'c': c})

sns.pairplot(df, corner=True)
plt.show()

