import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.tick_params(which='major', length=10, width=2, color='r')
ax.tick_params(which='minor', length=5, width=2, color='b')
ax.set_xticks([0, 1])        # missing function call
ax.set_xticks(np.linspace(0, 1, 5), minor=True)

plt.show()