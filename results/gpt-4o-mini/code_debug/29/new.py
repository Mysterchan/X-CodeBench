import matplotlib.pyplot as plt

x = [0, 2, 4, 6]
y = [(1, 5), (1, 3), (2, 4), (2, 7)]

# Plot lines connecting the pairs of y-values
for xi, (yi, yj) in zip(x, y):
    plt.plot([xi, xi], [yi, yj], 'k-', linewidth=0.5)  # Draw thin lines connecting pairs

# Plot the markers for each series
plt.plot(x, [i for (i,j) in y], 'rs', markersize=4, label='Series 1')
plt.plot(x, [j for (i,j) in y], 'bo', markersize=4, label='Series 2')

plt.xlim(xmin=-3, xmax=10)
plt.ylim(ymin=-1, ymax=10)

plt.xlabel('ID')
plt.ylabel('Class')
plt.legend()
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
