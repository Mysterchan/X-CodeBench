def find_connected_components(N, weights, intervals):
    parent = list(range(N))
    component_weights = [0] * N

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            component_weights[rootX] += component_weights[rootY]

    # Initialize component weights
    for i in range(N):
        component_weights[i] = weights[i]

    # Check for intersections and union components
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]:
                union(i, j)

    # Aggregate weights for each component
    component_map = {}
    for i in range(N):
        root = find(i)
        if root not in component_map:
            component_map[root] = 0
        component_map[root] += weights[i]

    return parent, component_map

def process_queries(N, weights, intervals, queries):
    parent, component_map = find_connected_components(N, weights, intervals)
    
    results = []
    for s, t in queries:
        root_s = find(parent[s - 1])
        root_t = find(parent[t - 1])
        
        if root_s == root_t:
            # They are in the same component, return the weight of the component
            results.append(component_map[root_s])
        else:
            results.append(-1)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
weights = list(map(int, data[1].split()))
intervals = [tuple(map(int, line.split())) for line in data[2:N + 2]]
Q = int(data[N + 2])
queries = [tuple(map(int, line.split())) for line in data[N + 3:N + 3 + Q]]

results = process_queries(N, weights, intervals, queries)
print("\n".join(map(str, results)))