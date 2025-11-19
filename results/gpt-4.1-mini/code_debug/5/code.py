import matplotlib.pyplot as plt
import numpy as np


def mrt(midp):
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True)
    ax1.hist(np.random.normal(midp, 1, 100))
    ax2.set_axis_off()
    # Use figure coordinates to center text regardless of axis limits
    ax2.text(0.5, 0.5, f"TEST {midp}", transform=fig.transFigure, ha='center', va='center')
    fig.savefig(f"test-{midp}.png")


mrt(10)