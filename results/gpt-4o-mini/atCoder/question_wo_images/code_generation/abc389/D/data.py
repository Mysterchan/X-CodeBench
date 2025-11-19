import sys

R = int(sys.stdin.read().strip())
count = 0

# Iterate through all possible integer coordinates (i, j)
# where i and j range from -R to R (inclusive)
for i in range(-R, R + 1):
    for j in range(-R, R + 1):
        # Calculate the distance from the origin to the center of the square
        distance = (i + 0.5)**2 + (j + 0.5)**2
        # If the distance is less than or equal to R^2, count this square
        if distance <= R**2:
            count += 1

print(count)