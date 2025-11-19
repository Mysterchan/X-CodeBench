def has_eulerian_path_in_line_graph(n, m, k, edges):
    # 1. Create degree array
    degree = [0] * (n + 1)

    # 2. Calculate degrees
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # 3. Calculate the number of vertices with odd degrees
    odd_count = sum(1 for deg in degree if deg % 2 == 1)

    if k == 0:
        # L^0(G) = G itself
        return odd_count == 0 or odd_count == 2

    # 4. When k >= 1, check the odd degree count for L^k(G)
    if k >= 1:
        if odd_count == 0 or odd_count == 2:
            return True
        elif odd_count > 2 and odd_count % 2 == 0:
            return True
    
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        n, m, k = map(int, data[index].split())
        edges = [tuple(map(int, data[index + i + 1].split())) for i in range(m)]
        index += m + 1

        if has_eulerian_path_in_line_graph(n, m, k, edges):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()