import matplotlib.pyplot as plt
import numpy as np

date = ["Jan", "Feb", "Mar", "Apr", "May"]
value = [4, 12, 15, 7, 25]

# Create a smoother line by using cubic spline interpolation
x = np.linspace(0, len(date)-1, 100)
y = np.interp(x, np.arange(len(date)), value)

plt.plot(date, value, marker='o')  # original points
plt.plot(np.linspace(0, len(date)-1, 100), y)  # smooth line

plt.show()