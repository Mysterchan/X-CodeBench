import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
edges = []
graph = defaultdict(list)

for i in range(1, N):
    u, v = map(int, data[i].split())
    edges.append((u, v))
    graph[u].append(v)
    graph[v].append(u)

Q = int(data[N])
queries = data[N + 1:]

weights = [1] * (N + 1)
results = []

def dfs(node, parent):
    subtree_weight = weights[node]
    for neighbor in graph[node]:
        if neighbor != parent:
            child_weight = dfs(neighbor, node)
            subtree_weight += child_weight
    subtree_weights[node] = subtree_weight
    return subtree_weight

subtree_weights = [0] * (N + 1)

for query in queries:
    parts = list(map(int, query.split()))
    if parts[0] == 1:
        x, w = parts[1], parts[2]
        weights[x] += w
    elif parts[0] == 2:
        y = parts[1] - 1
        u, v = edges[y]
        
        # Reset subtree weights
        subtree_weights = [0] * (N + 1)
        
        # Calculate the total weight of the tree
        total_weight = dfs(u, -1)
        
        # Calculate the weight of the subtree rooted at v
        subtree_weight_v = subtree_weights[v]
        
        # The weight of the other subtree is total_weight - subtree_weight_v
        weight_difference = abs(subtree_weight_v - (total_weight - subtree_weight_v))
        results.append(weight_difference)

print("\n".join(map(str, results)))