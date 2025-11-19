def count_cycles(N, M, edges):
    from collections import defaultdict
    from itertools import combinations

    MOD = 998244353

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for idx, (u, v) in enumerate(edges):
        graph[u].append((v, idx + 1))
        graph[v].append((u, idx + 1))

    cycle_count = 0

    # Check all combinations of edges
    for k in range(2, M + 1):
        for edge_combination in combinations(range(M), k):
            # Create a subgraph with the selected edges
            subgraph = defaultdict(list)
            vertices = set()
            for edge_index in edge_combination:
                u, v = edges[edge_index]
                subgraph[u].append(v)
                subgraph[v].append(u)
                vertices.add(u)
                vertices.add(v)

            # Check for cycles in the subgraph
            visited = set()
            def dfs(v, parent):
                visited.add(v)
                for neighbor in subgraph[v]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return True
                    if dfs(neighbor, v):
                        return True
                return False

            # Check if there's a cycle
            for vertex in vertices:
                if vertex not in visited:
                    if dfs(vertex, -1):
                        cycle_count += 1
                        break

    return cycle_count % MOD

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Output the result
print(count_cycles(N, M, edges))