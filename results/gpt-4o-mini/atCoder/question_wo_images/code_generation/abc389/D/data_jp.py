import sys
import math

R = int(sys.stdin.read().strip())

count = 0
R_squared = R * R

# (i, j) is the center of the square
for i in range(-R, R + 1):
    for j in range(-R, R + 1):
        if (i + 0.5) ** 2 + (j + 0.5) ** 2 <= R_squared and \
           (i - 0.5) ** 2 + (j + 0.5) ** 2 <= R_squared and \
           (i + 0.5) ** 2 + (j - 0.5) ** 2 <= R_squared and \
           (i - 0.5) ** 2 + (j - 0.5) ** 2 <= R_squared:
            count += 1

print(count)