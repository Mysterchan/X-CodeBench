import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 3))
ax.arrow(0, 1, 1, 1, head_width=0.1, head_length=0.1, length_includes_head=True)
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
