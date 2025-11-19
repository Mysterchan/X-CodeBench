import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 6, num=100)  # More points for a smoother line
r = [0, 1, 0.5, 1, 0.5, 1, 0]  # Given radial values

plt.title("stuff")
ax = plt.subplot(111, projection='polar')  # Specify polar projection
ax.plot(theta, r)  # Plot using the polar axes
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
