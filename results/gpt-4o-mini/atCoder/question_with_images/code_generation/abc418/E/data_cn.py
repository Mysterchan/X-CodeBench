def count_trapezoids(points):
    from collections import defaultdict

    n = len(points)
    y_map = defaultdict(list)

    # Group points by their y-coordinates
    for i in range(n):
        y_map[points[i][1]].append(points[i][0])

    trapezoid_count = 0

    # For each unique y-coordinate, count pairs of x-coordinates
    for y, x_list in y_map.items():
        m = len(x_list)
        if m < 2:
            continue
        # Count pairs of x-coordinates
        trapezoid_count += (m * (m - 1)) // 2

    # Each pair of y-coordinates can form a trapezoid with the counted pairs
    return trapezoid_count

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
points = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# Calculate and print the result
result = count_trapezoids(points)
print(result)