import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
plt.plot(X, Ya)
plt.fill_between(X, Ya, 0,
                 where = (X >=3.00) & (Ya<= 0),
                 color = 'b',alpha=.1)

plt.show()