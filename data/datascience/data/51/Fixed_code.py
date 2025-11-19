import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {'X': [13, 13, 13, 12, 11], 'Y':[14, 11, 13, 15, 20], 'NumberOfPlanets':[2, 5, 2, 1, 2]}
cts = pd.DataFrame(data=data)
cts = cts.sort_values('Y')

plt.figure(figsize=(10,10))
plt.scatter(cts['X'], cts['Y'], zorder=1)
plt.plot(cts['X'], cts['Y'], zorder=2)
plt.show()
