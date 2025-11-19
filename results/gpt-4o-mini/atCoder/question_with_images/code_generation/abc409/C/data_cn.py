def count_equilateral_triangles(N, L, d):
    # Calculate the positions of the points on the circle
    positions = [0] * N
    for i in range(1, N):
        positions[i] = (positions[i - 1] + d[i - 1]) % L

    # Sort the positions
    positions.sort()

    # Count the number of equilateral triangles
    count = 0
    position_map = {}
    
    for i in range(N):
        pos = positions[i]
        if pos not in position_map:
            position_map[pos] = []
        position_map[pos].append(i + 1)  # Store 1-based index

    # Check for each unique position
    unique_positions = sorted(position_map.keys())
    for i in range(len(unique_positions)):
        for j in range(i + 1, len(unique_positions)):
            for k in range(j + 1, len(unique_positions)):
                a = unique_positions[i]
                b = unique_positions[j]
                c = unique_positions[k]
                
                # Check if they can form an equilateral triangle
                if (b - a) % L == (c - b) % L == (c - a) % L:
                    count += len(position_map[a]) * len(position_map[b]) * len(position_map[c])

    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
L = int(data[1])
d = list(map(int, data[2:]))

# Get the result
result = count_equilateral_triangles(N, L, d)

# Print the result
print(result)