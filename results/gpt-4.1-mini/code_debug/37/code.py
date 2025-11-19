import matplotlib.pyplot as plt
W, H = 2, 3
offsetX = 0.1*W

arrow_style = {"head_width":0.1, "head_length":0.2, "color":"k"}
plt.arrow(x=0, y=0, dx=W, dy=H, **arrow_style)

# Add text label "U" near the middle of the arrow
plt.text(W/2 + offsetX, H/2, "U", fontsize=12)

plt.show()