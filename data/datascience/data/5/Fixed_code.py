import matplotlib.pyplot as plt
import numpy as np


def mrt(midp):
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True)
    ax1.hist(np.random.normal(midp, 1, 100))
    ax2.set_axis_off()
    ax2.text(0.5, 0.5, f"TEST {midp}", transform=ax2.transAxes)  # missing parameter
    fig.savefig(f"test-{midp}.png")


mrt(10)