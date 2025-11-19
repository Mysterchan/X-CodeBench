import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

stepsize = 0.5
num_steps = 20
num_trials = 5

final_position = []

for _ in range(num_trials):
    pos = np.array([0, 0])
    path = []
    for i in range(num_steps):
        pos = pos + np.random.normal(0, stepsize, 2)
        path.append(pos)
    final_position.append(np.array(path))
    
x = [final_position[i][:,0] for i in range(len(final_position))]
y = [final_position[j][:,1] for j in range(len(final_position))]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

cmap = plt.get_cmap('tab10')

# Store line objects for each trial to update them instead of plotting new lines every frame
lines = [ax.plot([], [], ls='-', linewidth=0.5, marker='o', ms=8, mec='k', zorder=i)[0] for i in range(num_trials)]

def animate(frame):
    step_num = frame % num_steps
    trial_num = frame // num_steps
    
    # Clear legend each frame to avoid duplicates
    ax.legend_.remove() if ax.legend_ else None
    
    # Update the current trial line data
    lines[trial_num].set_data(x[trial_num][:step_num+1], y[trial_num][:step_num+1])
    lines[trial_num].set_color(cmap(trial_num % 10))
    lines[trial_num].set_markerfacecolor(cmap(trial_num % 10))
    lines[trial_num].set_label(f"Trial = {trial_num+1}")
    
    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f"Number of trials = {trial_num+1} \nNumber of steps = {step_num+1}")  
    ax.grid(True)
    
    # Show legend only when a trial finishes
    if step_num == num_steps - 1:
        # Only include lines for completed trials in the legend
        completed_lines = lines[:trial_num+1]
        ax.legend(handles=completed_lines, fontsize=10, bbox_to_anchor=(1, 1))
    
    return lines

fig.suptitle(f"2D random walk simulation for {num_steps} steps over {num_trials} trials.")
ani = FuncAnimation(fig, animate, frames=np.arange(0, num_steps * num_trials), interval=50, repeat=False)
plt.show()