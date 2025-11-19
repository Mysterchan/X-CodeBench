import pandas as pd
import matplotlib.pyplot as plt

values = pd.Series([False, False, True, True])
v_counts = values.value_counts()
fig = plt.figure()
plt.pie(v_counts, labels=v_counts.index, autopct='%.4f', shadow=True)

plt.show()