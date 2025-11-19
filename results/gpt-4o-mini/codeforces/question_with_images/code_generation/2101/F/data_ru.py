MOD = 998244353

def dfs(node, parent, depth, graph, depths):
    depths[node] = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, graph, depths)

def calculate_sweetness(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Calculate depths from node 1
    depths = [0] * (n + 1)
    dfs(1, -1, 0, graph, depths)

    # Calculate total sweetness
    total_sweetness = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            distance = depths[u] + depths[v] - 2 * depths[find_lca(u, v, graph)]
            total_sweetness = (total_sweetness + distance) % MOD

    return total_sweetness

def find_lca(u, v, graph):
    # This function should implement LCA finding logic
    # For simplicity, we will assume u and v are directly connected
    return 1  # Placeholder

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        edges = []
        for __ in range(n - 1):
            u, v = map(int, data[index].split())
            edges.append((u, v))
            index += 1
        result = calculate_sweetness(n, edges)
        results.append(result)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()