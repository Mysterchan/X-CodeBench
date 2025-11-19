import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Scatter plot points
ax.scatter([1, 2, 1.5], [2, 1, 1.5])

# Define the center of the circle and the radius
circle_center = (1.5, 1.5)  # (x, y) coordinates of the center
radius = 0.2  # Radius of the circle

# Create a circle
circle = plt.Circle(circle_center, radius, color='red', fill=False)

# Add the circle to the axes
ax.add_artist(circle)

# Set limits to better visualize the circle
ax.set_xlim(0.8, 2.2)
ax.set_ylim(0.8, 2.2)

# Show the plot
plt.show()