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
        
        # Find the size of the cycle
        cycle_size = 0
        x = i
        
        while not visited[x]:
            visited[x] = True
            # Move to the next index in the cycle
            x = indexed_P[x][1]
            cycle_size += 1
        
        # If there is a cycle of size k, the cost to sort it is (k-1) * (k)
        if cycle_size > 0:
            total_cost += (cycle_size - 1) * cycle_size
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
P = list(map(int, data[1:N+1]))

# Get the result and print it
result = min_cost_to_sort(N, P)
print(result)