import sys
import math

R = int(sys.stdin.readline())

R_sq = R * R
count = 0

# For each integer i, find the range of j such that all four corners are inside the circle.
# The farthest corner from origin for square centered at (i,j) is the corner with max distance:
# max distance corner = (i ± 0.5, j ± 0.5)
# The condition is that all four corners are inside circle:
# max distance corner distance <= R
# So check the corner with largest distance:
# distance^2 = (i ± 0.5)^2 + (j ± 0.5)^2 <= R^2
# To ensure all corners inside, the corner with max distance must be inside.
# The max distance corner is the one with signs chosen to maximize distance:
# So for fixed i,j, max distance corner is (i + 0.5 * sign_i, j + 0.5 * sign_j)
# where sign_i = 1 if i >= 0 else -1, similarly for j.
# But to simplify, we can just check the corner with max distance:
# max_dist_corner = (i + 0.5, j + 0.5) or (i + 0.5, j - 0.5) or (i - 0.5, j + 0.5) or (i - 0.5, j - 0.5)
# The max distance corner is the one with max |i ± 0.5| and |j ± 0.5|.

# Actually, the max distance corner is the one with (i + 0.5 * sign(i), j + 0.5 * sign(j))
# where sign(i) = 1 if i >= 0 else -1, same for j.

# So for each i, we find the range of j such that:
# (i + 0.5 * sign(i))^2 + (j + 0.5 * sign(j))^2 <= R^2

# But sign(j) depends on j, so to be safe, we check all four corners for each (i,j).
# However, this is expensive for large R.

# Alternative approach:
# For each i, find the max j such that all four corners are inside.
# The max distance corner is the one with max |i ± 0.5| and |j ± 0.5|.

# Since the square is 1x1, the corners are at (i ± 0.5, j ± 0.5).
# The farthest corner from origin is the one with max absolute coordinate in both x and y.

# So for fixed i, the max distance corner is at (i + 0.5 * sign(i), j + 0.5 * sign(j))
# where sign(i) = 1 if i >= 0 else -1, sign(j) = 1 if j >= 0 else -1.

# To simplify, we can consider i >= 0 and i < 0 separately.

# But better approach:
# For each i in range [-R, R], find the max j >= 0 such that all corners inside circle.
# Because of symmetry, count j >= 0 and multiply accordingly.

# Let's do the following:

# For i in [-R, R]:
#   For j >= 0:
#     Check if all four corners inside circle:
#       max distance corner = (i + 0.5 * sign(i), j + 0.5)
#       min distance corner = (i - 0.5 * sign(i), j - 0.5)
#     But to be safe, check all four corners:
#       corners = [(i+0.5, j+0.5), (i+0.5, j-0.5), (i-0.5, j+0.5), (i-0.5, j-0.5)]
#     If all corners inside circle, count += 1

# But this is O(R^2), too slow for R=10^6.

# Optimization:
# The condition that all four corners inside circle means:
# max distance corner <= R
# The max distance corner is the one with max |x| and max |y| among corners.

# For fixed i, the max |x| among corners is |i| + 0.5
# For j, max |y| among corners is |j| + 0.5

# So the condition reduces to:
# (|i| + 0.5)^2 + (|j| + 0.5)^2 <= R^2

# For each i in [-R, R], find all j such that:
# (|i| + 0.5)^2 + (|j| + 0.5)^2 <= R^2
# => (|j| + 0.5)^2 <= R^2 - (|i| + 0.5)^2

# Let x = |i| + 0.5
# Then max y = sqrt(R^2 - x^2) - 0.5

# The number of integer j with |j| <= max_y is floor(max_y)

# So for each i in [-R, R]:
#   x = abs(i) + 0.5
#   if x > R: no squares
#   else:
#     max_y = sqrt(R^2 - x^2) - 0.5
#     if max_y < 0: no squares
#     else:
#       count += 2 * floor(max_y) + 1  # j from -floor(max_y) to floor(max_y)

# Finally sum over i.

count = 0
for i in range(-R, R + 1):
    x = abs(i) + 0.5
    if x > R:
        continue
    max_y = math.sqrt(R_sq - x * x) - 0.5
    if max_y < 0:
        continue
    max_j = int(math.floor(max_y))
    count += 2 * max_j + 1

print(count)