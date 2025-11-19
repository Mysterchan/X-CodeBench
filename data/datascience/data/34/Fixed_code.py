import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

date = ["Jan", "Feb", "Mar", "Apr", "May"]
value = [4,12,15,7,25]

idx = range(len(date))
xnew = np.linspace(min(idx), max(idx), 300)

spl = make_interp_spline(idx, value, k=3)
smooth = spl(xnew)

plt.plot(xnew, smooth)
plt.xticks(idx, date)

plt.show()