import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:N]]
Q = int(data[N])
queries = [line.split() for line in data[N + 1:]]

# Initialize weights and graph
weights = [1] * (N + 1)
graph = defaultdict(list)

for i, (u, v) in enumerate(edges):
    graph[u].append((v, i + 1))
    graph[v].append((u, i + 1))

# To store the results of type 2 queries
results = []

def dfs(node, parent):
    subtree_weight = weights[node]
    for neighbor, edge_id in graph[node]:
        if neighbor != parent:
            child_weight = dfs(neighbor, node)
            subtree_weight += child_weight
    subtree_weights[node] = subtree_weight
    return subtree_weight

subtree_weights = [0] * (N + 1)

for query in queries:
    if query[0] == '1':
        x, w = int(query[1]), int(query[2])
        weights[x] += w
    elif query[0] == '2':
        y = int(query[1]) - 1
        u, v = edges[y]
        
        # Reset subtree weights and calculate
        subtree_weights = [0] * (N + 1)
        total_weight = sum(weights)
        
        # Perform DFS from u
        dfs(u, v)
        
        # Weight of the subtree rooted at u
        weight_u = subtree_weights[u]
        weight_v = total_weight - weight_u
        
        results.append(abs(weight_u - weight_v))

# Print results for all type 2 queries
sys.stdout.write('\n'.join(map(str, results)) + '\n')