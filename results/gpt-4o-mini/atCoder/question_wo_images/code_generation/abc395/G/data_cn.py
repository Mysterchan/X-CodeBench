import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

N, K = map(int, data[0].split())
C = [list(map(int, line.split())) for line in data[1:N+1]]
Q = int(data[N+1])
queries = [tuple(map(int, line.split())) for line in data[N+2:N+2+Q]]

# Precompute the minimum costs for all combinations of vertices
min_cost = {}

for s, t in combinations(range(K + 1, N + 1), 2):
    vertices = list(range(1, K + 1)) + [s, t]
    vertices_set = set(vertices)
    
    # Calculate the minimum spanning tree cost using Prim's algorithm
    total_cost = 0
    in_mst = [False] * (N + 1)
    min_edge = [float('inf')] * (N + 1)
    min_edge[1] = 0  # Start from vertex 1
    for _ in range(len(vertices)):
        # Find the vertex with the minimum edge cost
        u = -1
        for v in vertices:
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        total_cost += min_edge[u]
        in_mst[u] = True
        
        # Update the edge costs for the vertices not in the MST
        for v in vertices:
            if not in_mst[v]:
                min_edge[v] = min(min_edge[v], C[u-1][v-1])
    
    min_cost[(s, t)] = total_cost

# Answer the queries
output = []
for s, t in queries:
    output.append(str(min_cost[(s, t)]))

print("\n".join(output))