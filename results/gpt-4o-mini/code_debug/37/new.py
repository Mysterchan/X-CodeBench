import matplotlib.pyplot as plt

W, H = 2, 3
arrow_style = {"head_width": 0.1, "head_length": 0.2, "color": "k"}
plt.arrow(x=0, y=0, dx=W, dy=H, **arrow_style)

# Adding the text label next to the arrow
plt.text(x=W/2, y=H/2, s='U', fontsize=12, ha='left')

plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 3.5)
import os
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, '1.png')
plt.savefig(output_path)
