import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label', labelpad=15)  # Add padding to make label fully visible
ax.set_title('3D Surface Plot')
ax.view_init(elev=30, azim=90)  # Adjust azim to 90 for upright Z-axis

plt.tight_layout()
plt.show()