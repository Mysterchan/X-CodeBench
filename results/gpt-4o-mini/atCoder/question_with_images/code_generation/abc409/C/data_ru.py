def count_equilateral_triangles(N, L, distances):
    # Calculate the positions of the points on the circle
    positions = [0] * N
    for i in range(1, N):
        positions[i] = (positions[i - 1] + distances[i - 1]) % L

    # Count the number of equilateral triangles
    count = 0
    position_map = {}
    
    # Store the positions and their indices
    for i in range(N):
        pos = positions[i]
        if pos not in position_map:
            position_map[pos] = []
        position_map[pos].append(i + 1)  # Store 1-based index

    # Check for each unique position
    unique_positions = list(position_map.keys())
    for i in range(len(unique_positions)):
        for j in range(i + 1, len(unique_positions)):
            pos_a = unique_positions[i]
            pos_b = unique_positions[j]
            # Calculate the third position for an equilateral triangle
            pos_c = (pos_a + (pos_b - pos_a) * 2) % L
            
            if pos_c in position_map:
                # Count valid combinations
                count += len(position_map[pos_a]) * len(position_map[pos_b]) * len(position_map[pos_c])

    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
L = int(data[1])
distances = list(map(int, data[2:]))

# Get the result and print it
result = count_equilateral_triangles(N, L, distances)
print(result)