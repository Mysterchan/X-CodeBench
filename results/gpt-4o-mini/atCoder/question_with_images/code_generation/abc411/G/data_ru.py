def count_cycles(N, M, edges):
    MOD = 998244353
    
    from collections import defaultdict
    from itertools import combinations
    
    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for i in range(M):
        u, v = edges[i]
        graph[u].append(i)
        graph[v].append(i)
    
    # Function to find all cycles using backtracking
    def find_cycles(start, path, visited, edge_indices):
        if len(path) > 1 and path[0] == path[-1]:
            # Found a cycle
            cycle_set = set(edge_indices)
            if len(cycle_set) >= 2:
                cycle_count[0] += 1
            return
        
        for edge_index in graph[path[-1]]:
            u, v = edges[edge_index]
            next_node = v if u == path[-1] else u
            
            if next_node not in visited:
                visited.add(next_node)
                path.append(next_node)
                find_cycles(start, path, visited, edge_indices + [edge_index])
                path.pop()
                visited.remove(next_node)
    
    cycle_count = [0]
    
    for start in range(1, N + 1):
        visited = {start}
        find_cycles(start, [start], visited, [])
    
    return cycle_count[0] // 2  # Each cycle is counted twice

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Calculate and print the result
result = count_cycles(N, M, edges) % 998244353
print(result)