import pandas as pd
import matplotlib.pyplot as plt

def my_fmt(x):
    print(x)
    return '{:.4f}%\n({:.0f})'.format(x, total*x/100)


values = pd.Series([False, False, True, True])
v_counts = values.value_counts()
total = len(values)
fig = plt.figure()
plt.pie(v_counts, labels=v_counts.index, autopct=my_fmt, shadow=True)

plt.show()