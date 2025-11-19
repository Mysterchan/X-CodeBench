def min_cost_to_good_sequence(N, P, C):
    # Create a list of tuples (size, color) and sort by size
    slimes = sorted(zip(P, C))
    
    # Create a mapping from size to its original index
    index_map = {size: i for i, size in enumerate(P)}
    
    # Create a visited array to track which slimes have been processed
    visited = [False] * N
    total_cost = 0
    
    for i in range(N):
        if visited[i] or slimes[i][0] == P[i]:
            continue
        
        # Start a cycle
        cycle_cost = 0
        cycle_length = 0
        min_color = float('inf')
        
        j = i
        while not visited[j]:
            visited[j] = True
            cycle_length += 1
            cycle_cost += slimes[j][1]  # Add the color cost
            min_color = min(min_color, slimes[j][1])  # Find the minimum color in the cycle
            j = index_map[slimes[j][0]]  # Move to the next index in the original array
        
        if cycle_length > 1:
            # Cost to fix the cycle
            total_cost += cycle_cost - min_color + (cycle_length - 1) * min_color
    
    return total_cost

# Read input
N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

# Get the result and print it
result = min_cost_to_good_sequence(N, P, C)
print(result)