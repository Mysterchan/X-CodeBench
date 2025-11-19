import matplotlib.pyplot as plt
import numpy as np


def mrt(midp):
    fig, (ax1, ax2) = plt.subplots(ncols=2, gridspec_kw={'width_ratios': [1, 0.5]})
    ax1.hist(np.random.normal(midp, 1, 100))
    
    ax2.set_axis_off()
    ax2.text(0.5, 0.5, f"TEST {midp}", ha='center', va='center', transform=ax2.transAxes)
    
    fig.tight_layout()
    fig.savefig(f"test-{midp}.png")
    plt.show()


mrt(10)