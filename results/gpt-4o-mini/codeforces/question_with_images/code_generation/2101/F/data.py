MOD = 998244353

def dfs(node, parent, graph, depth, depths):
    depths[node] = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, depth + 1, depths)

def calculate_coolness(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Calculate depths from node 1
    depths = [0] * (n + 1)
    dfs(1, -1, graph, 0, depths)

    # Calculate the total coolness
    total_coolness = 0
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v:
                total_coolness += depths[u] + depths[v] - 2 * depths[1]  # distance from u to v
                total_coolness %= MOD

    # Each coloring contributes to the coolness
    total_colorings = pow(3, n, MOD)
    total_coolness = (total_coolness * total_colorings) % MOD

    return total_coolness

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
        result = calculate_coolness(n, edges)
        results.append(result)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()