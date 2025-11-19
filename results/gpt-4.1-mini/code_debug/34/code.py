import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

date = ["Jan", "Feb", "Mar", "Apr", "May"]
value = [4, 12, 15, 7, 25]

# Convert categorical dates to numeric values for interpolation
x = np.arange(len(date))
y = np.array(value)

# Create smooth spline interpolation
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)  # Cubic spline
y_smooth = spl(x_smooth)

plt.plot(x_smooth, y_smooth)
plt.xticks(x, date)  # Set original month labels on x-axis

plt.show()