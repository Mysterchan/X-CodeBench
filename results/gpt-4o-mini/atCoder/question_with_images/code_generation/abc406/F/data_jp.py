import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:N]]
Q = int(data[N])
queries = [line.split() for line in data[N+1:]]

# Initialize the tree and weights
tree = defaultdict(list)
weights = [1] * (N + 1)

# Build the tree
for i, (u, v) in enumerate(edges):
    tree[u].append((v, i + 1))
    tree[v].append((u, i + 1))

# To store the results of type 2 queries
results = []

def dfs(node, parent):
    subtree_weight = weights[node]
    for neighbor, edge_id in tree[node]:
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
        y = int(query[1])
        u, v = edges[y - 1]
        
        # Reset subtree weights
        subtree_weights = [0] * (N + 1)
        
        # Calculate the total weight of the tree
        total_weight = sum(weights)
        
        # Perform DFS from u to find the weight of the subtree rooted at v
        subtree_weight_v = dfs(v, u)
        
        # The weight of the other subtree is total_weight - subtree_weight_v
        weight_diff = abs(subtree_weight_v - (total_weight - subtree_weight_v))
        results.append(weight_diff)

# Output results for type 2 queries
sys.stdout.write('\n'.join(map(str, results)) + '\n')