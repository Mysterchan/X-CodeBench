def min_cost_to_sort(N, P):
    # Create a list of tuples (value, original_index)
    indexed_P = [(P[i], i) for i in range(N)]
    # Sort based on the values
    indexed_P.sort()
    
    visited = [False] * N
    total_cost = 0
    
    for i in range(N):
        # If already visited or already in the correct position
        if visited[i] or indexed_P[i][1] == i:
            continue
        
        cycle_size = 0
        x = i
        
        # Count the size of the cycle
        while not visited[x]:
            visited[x] = True
            x = indexed_P[x][1]
            cycle_size += 1
        
        # If there is a cycle of size k, the cost to sort it is (k-1) * (k)
        if cycle_size > 0:
            total_cost += (cycle_size - 1) * cycle_size // 2
    
    return total_cost

# Read input
N = int(input())
P = list(map(int, input().split()))

# Get the result and print it
result = min_cost_to_sort(N, P)
print(result)