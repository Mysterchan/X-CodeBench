def count_equilateral_triangles(N, L, d):
    # Calculate the positions of the points on the circle
    positions = [0] * N
    for i in range(1, N):
        positions[i] = (positions[i - 1] + d[i - 1]) % L

    # Sort the positions
    positions.sort()

    # Count equilateral triangles
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Calculate the distance between points i and j
            dist = (positions[j] - positions[i]) % L
            # The third point must be at this distance from both i and j
            third_point1 = (positions[j] + dist) % L
            third_point2 = (positions[i] + dist) % L
            
            # Check if the third point exists in the positions
            if third_point1 in positions:
                count += 1
            if third_point2 in positions and third_point2 != third_point1:
                count += 1

    # Each triangle is counted 3 times (once for each vertex), so divide by 3
    return count // 3

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
L = int(data[1])
d = list(map(int, data[2:]))

# Output the result
print(count_equilateral_triangles(N, L, d))