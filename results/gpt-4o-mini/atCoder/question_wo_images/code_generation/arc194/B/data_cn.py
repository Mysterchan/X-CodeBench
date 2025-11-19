def min_cost_to_sort(N, P):
    # Create a list of tuples (value, original_index)
    indexed_P = [(P[i], i) for i in range(N)]
    # Sort based on the values to get the target positions
    indexed_P.sort()
    
    visited = [False] * N
    total_cost = 0
    
    for i in range(N):
        if visited[i] or indexed_P[i][1] == i:
            continue
        
        cycle_size = 0
        x = i
        
        while not visited[x]:
            visited[x] = True
            x = indexed_P[x][1]
            cycle_size += 1
        
        if cycle_size > 0:
            total_cost += (cycle_size - 1) * (cycle_size) // 2
    
    return total_cost

# Read input
N = int(input())
P = list(map(int, input().split()))

# Calculate and print the minimum cost
print(min_cost_to_sort(N, P))