def max_points(N, K, P):
    NK = N * K
    sorted_P = sorted(P)
    index_map = {value: idx for idx, value in enumerate(P)}
    visited = [False] * NK
    points = 0

    for i in range(NK):
        if visited[i] or P[i] == sorted_P[i]:
            continue
        
        cycle_length = 0
        cycle_points = 0
        current = i
        
        while not visited[current]:
            visited[current] = True
            cycle_length += 1
            next_value = sorted_P[current]
            next_index = index_map[next_value]
            if abs(current - next_index) % N == 0:
                cycle_points += 1
            current = next_index
        
        if cycle_length > 0:
            points += cycle_points - 1

    return points

# Input reading
N, K = map(int, input().split())
P = list(map(int, input().split()))

# Output the result
print(max_points(N, K, P))