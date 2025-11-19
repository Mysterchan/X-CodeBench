import pandas as pd
import numpy as np
from datetime import date

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator
from matplotlib.dates import ConciseDateFormatter

xs = [pd.date_range(f'{y}-07-01', '2021-12-31', freq='M') for y in range(2016, 2019)]
ys = [np.random.rand(len(x)) for x in xs]

fig, axs = plt.subplots(3, 1, figsize=(10, 8))

for ax, x, y in zip(axs, xs, ys):
    ax.plot(x, y)

    locator = MonthLocator((1, 4, 7, 10))
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(ConciseDateFormatter(locator))

    # Set a uniform font size for all x-axis tick labels
    for text in ax.get_xticklabels():
        text.set_fontsize(10)  # Set font size for all labels

    ax.set_xlim(date(2016, 7, 1), date(2022, 1, 1))  # Adjust x-axis limits

plt.tight_layout()
plt.show()