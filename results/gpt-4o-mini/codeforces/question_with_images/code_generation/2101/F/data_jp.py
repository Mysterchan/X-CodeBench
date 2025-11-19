def dfs(node, parent, graph, depth, depths):
    depths[node] = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, depth + 1, depths)

def calculate_coolness(n, edges):
    MOD = 998244353
    graph = [[] for _ in range(n + 1)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    total_coolness = 0
    
    for root in range(1, n + 1):
        depths = [0] * (n + 1)
        dfs(root, -1, graph, 0, depths)
        
        max_depth = max(depths)
        count_red = pow(3, n - 1, MOD)  # All nodes can be colored in 3 ways except the root
        count_blue = pow(3, n - 1, MOD)  # Same for blue
        
        for d in range(max_depth + 1):
            count = (count_red * count_blue) % MOD
            total_coolness = (total_coolness + count * d) % MOD
    
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