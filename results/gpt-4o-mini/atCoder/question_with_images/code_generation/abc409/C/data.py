def count_equilateral_triangles(N, L, d):
    # Calculate the positions of the points on the circle
    positions = [0] * N
    for i in range(1, N):
        positions[i] = (positions[i - 1] + d[i - 1]) % L

    # Sort the positions
    positions.sort()

    # Count the number of equilateral triangles
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Calculate the distance between points i and j
            dist = (positions[j] - positions[i]) % L
            # The third point must be at a distance of dist from both i and j
            third_pos1 = (positions[j] + dist) % L
            third_pos2 = (positions[i] + dist) % L
            
            # Check if the third point exists in the positions
            if third_pos1 in positions[j + 1:]:
                count += 1
            if third_pos2 in positions[i + 1:j]:
                count += 1

    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
L = int(data[1])
d = list(map(int, data[2:]))

# Get the result and print it
result = count_equilateral_triangles(N, L, d)
print(result)