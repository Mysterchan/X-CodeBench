def count_cycles(N, M, edges):
    MOD = 998244353
    
    # Create an adjacency list for the graph
    from collections import defaultdict
    graph = defaultdict(list)
    
    for i in range(M):
        u, v = edges[i]
        graph[u].append(i)
        graph[v].append(i)
    
    # To count cycles, we will use a bitmask to represent subsets of edges
    total_cycles = 0
    
    # Iterate over all possible subsets of edges
    for mask in range(1, 1 << M):
        # Count the number of edges in the current subset
        edge_count = bin(mask).count('1')
        if edge_count < 2:
            continue
        
        # Create a graph for the current subset of edges
        subgraph = defaultdict(list)
        for i in range(M):
            if mask & (1 << i):
                u, v = edges[i]
                subgraph[u].append(v)
                subgraph[v].append(u)
        
        # Check for cycles using DFS
        visited = [False] * (N + 1)
        
        def dfs(node, parent):
            visited[node] = True
            for neighbor in subgraph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, node)
                elif neighbor != parent:
                    return True
            return False
        
        # Count cycles in the subgraph
        cycle_found = False
        for start in range(1, N + 1):
            if not visited[start]:
                if dfs(start, -1):
                    cycle_found = True
                    break
        
        if cycle_found:
            total_cycles = (total_cycles + 1) % MOD
    
    return total_cycles

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Get the result
result = count_cycles(N, M, edges)

# Print the result
print(result)