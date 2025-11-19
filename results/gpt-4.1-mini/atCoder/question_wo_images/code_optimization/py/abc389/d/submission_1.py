import sys
input = sys.stdin.readline

R = int(input())

R_sq = R * R
ans = 0

# We iterate over i from 1 to R-1 (positive quadrant excluding axes)
for i in range(1, R):
    # For each i, find the maximum j such that all four corners of the square are inside the circle
    # The corners are at (i±0.5, j±0.5)
    # The farthest corner from origin is (i+0.5, j+0.5)
    # So we require (i+0.5)^2 + (j+0.5)^2 <= R^2
    # Solve for j:
    max_j_sq = R_sq - (i + 0.5) * (i + 0.5)
    if max_j_sq < 0:
        continue
    max_j = int((max_j_sq ** 0.5) - 0.5)
    if max_j < 1:
        continue
    ans += max_j

# Multiply by 4 for all four quadrants
ans *= 4

# Add squares on axes (i=0 or j=0)
# For i=0, the square center is at (0, j)
# The corners are at (±0.5, j±0.5)
# The farthest corner is at (0.5, j+0.5)
# Condition: (0.5)^2 + (j+0.5)^2 <= R^2
# Solve for j:
max_j_axis_sq = R_sq - 0.25
if max_j_axis_sq < 0:
    max_j_axis = 0
else:
    max_j_axis = int((max_j_axis_sq ** 0.5) - 0.5)
# Count squares on positive axis excluding origin
axis_count = max_j_axis

# Total squares on axes (both x and y axes), excluding origin counted twice
# origin square counted once
ans += 4 * axis_count + 1

print(ans)