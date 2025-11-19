def max_points(N, K, P):
    NK = N * K
    sorted_P = sorted(P)
    index_map = {value: idx for idx, value in enumerate(P)}
    visited = [False] * NK
    points = 0

    for i in range(NK):
        if visited[i] or P[i] == sorted_P[i]:
            continue
        
        cycle_size = 0
        current = i
        
        while not visited[current]:
            visited[current] = True
            current_value = P[current]
            current = index_map[sorted_P[current_value - 1]]
            cycle_size += 1
        
        if cycle_size > 0:
            points += (cycle_size - 1) // N

    return points

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
P = list(map(int, data[2:]))

# Output the result
print(max_points(N, K, P))