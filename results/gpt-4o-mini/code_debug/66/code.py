import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# Load and prepare the data
fmri = sns.load_dataset("fmri")
fmri.sort_values('timepoint', inplace=True)

# Create the background column
arr = np.ones(len(fmri))
arr[:300] = 0   # First region
arr[300:600] = 1  # Second region
arr[600:] = 2   # Third region
fmri['background'] = arr

# Create the plot
plt.figure(figsize=(10, 6))

# Create background shading
colors = ['lightblue', 'lightcoral', 'lightgreen']  # Colors for the background regions
for i in range(3):
    plt.fill_between(fmri['timepoint'], -0.1, 0.3, where=(fmri['background'] == i), color=colors[i], alpha=0.5)

# Plot the line plot with the signal data
ax = sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri)

# Display the plot
plt.show()