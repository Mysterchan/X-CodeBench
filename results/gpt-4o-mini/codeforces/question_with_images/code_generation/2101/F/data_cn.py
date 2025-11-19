def dfs(node, parent):
    size = 1
    max_depth = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            child_size, child_depth = dfs(neighbor, node)
            size += child_size
            max_depth = max(max_depth, child_depth + 1)
    return size, max_depth

def calculate_coolness(n):
    total_coolness = 0
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v:
                distance = depth[u] + depth[v] - 2 * depth[lca(u, v)]
                total_coolness += distance
    return total_coolness

def lca(u, v):
    # Implement LCA finding logic here
    pass

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Initialize depth array
    depth = [0] * (n + 1)
    
    # Perform DFS to calculate sizes and depths
    dfs(1, -1)

    # Calculate total coolness
    result = calculate_coolness(n) % MOD
    print(result)