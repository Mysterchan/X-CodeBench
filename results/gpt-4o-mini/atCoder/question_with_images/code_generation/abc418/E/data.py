def count_trapezoids(points):
    from collections import defaultdict
    
    # Group points by their y-coordinates
    y_groups = defaultdict(list)
    for x, y in points:
        y_groups[y].append(x)
    
    # Count trapezoids
    trapezoid_count = 0
    
    # For each pair of y-coordinates, count the number of x-coordinates
    y_keys = list(y_groups.keys())
    for i in range(len(y_keys)):
        for j in range(i + 1, len(y_keys)):
            y1 = y_keys[i]
            y2 = y_keys[j]
            x1_list = y_groups[y1]
            x2_list = y_groups[y2]
            
            # Count pairs of x-coordinates
            count_x1 = len(x1_list)
            count_x2 = len(x2_list)
            
            # Each pair of x-coordinates from different y-coordinates can form a trapezoid
            trapezoid_count += count_x1 * count_x2
    
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