def count_trapezoids(points):
    n = len(points)
    count = 0

    # Sort points by x-coordinate
    points.sort()

    # Create a dictionary to store y-coordinates by x-coordinate
    from collections import defaultdict
    y_by_x = defaultdict(list)

    for x, y in points:
        y_by_x[x].append(y)

    # Iterate over all pairs of x-coordinates
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Check if y1 and y2 can form a trapezoid
            if y1 != y2:
                # Count how many y-coordinates are between y1 and y2
                y_lower = min(y1, y2)
                y_upper = max(y1, y2)

                # Count valid y-coordinates for the trapezoid
                for x in y_by_x:
                    if x > x1 and x < x2:
                        count += sum(y_lower < y < y_upper for y in y_by_x[x])

    return count

import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
points = [tuple(map(int, line.split())) for line in data[1:N + 1]]

result = count_trapezoids(points)
print(result)