import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
edges = []
graph = defaultdict(list)

# Read edges and build the graph
for i in range(1, N):
    u, v = map(int, data[i].split())
    edges.append((u, v))
    graph[u].append(v)
    graph[v].append(u)

Q = int(data[N])
queries = data[N + 1:]

# Initialize weights
weights = [1] * (N + 1)

# To store the results of type 2 queries
results = []

def dfs(node, parent):
    subtree_weight = weights[node]
    for neighbor in graph[node]:
        if neighbor != parent:
            child_weight = dfs(neighbor, node)
            subtree_weight += child_weight
    subtree_weights[node] = subtree_weight
    return subtree_weight

# Process each query
for query in queries:
    parts = list(map(int, query.split()))
    if parts[0] == 1:
        # Update weight of vertex x
        x, w = parts[1], parts[2]
        weights[x] += w
    elif parts[0] == 2:
        # Query the difference in weights if edge y is removed
        y = parts[1] - 1
        u, v = edges[y]
        
        # Reset subtree weights for DFS
        subtree_weights = [0] * (N + 1)
        
        # Calculate the total weight of the tree
        total_weight = dfs(u, v)
        
        # The weight of the subtree rooted at u
        weight_u = subtree_weights[u]
        weight_v = total_weight - weight_u
        
        # Calculate the difference
        results.append(abs(weight_u - weight_v))

# Print all results for type 2 queries
sys.stdout.write('\n'.join(map(str, results)) + '\n')