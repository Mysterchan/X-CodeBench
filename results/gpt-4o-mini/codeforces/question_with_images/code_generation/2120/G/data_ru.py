def eulerian_path_exists(n, m, k, edges):
    from collections import defaultdict

    # Step 1: Count the degree of each edge (which is a vertex in the line graph L(G))
    degree = defaultdict(int)
    
    # Each edge connects two vertices, increase the count for both vertices
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    # Count the number of odd degree vertices in G
    odd_count = sum(1 for deg in degree.values() if deg % 2 == 1)

    # Step 2: Determine if Eulerian path exists in L^k(G)
    # An Eulerian path exists in L^k(G) under two cases depending on k:
    # - If k is 1:
    #     -> Eulerian path exists in L(G) if and only if exactly 0 or 2 vertices have odd degree in G.
    # - If k > 1:
    #     -> Eulerian path exists in L^k(G) if and only if the number of vertices with odd degree in G is even.

    if k == 1:
        # For L(G), we need 0 or 2 odd degree in G
        return "YES" if odd_count in (0, 2) else "NO"
    else:
        # For L^k(G) with k > 1, we need the number of odd degree vertices to be even
        return "YES" if odd_count % 2 == 0 else "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    index = 1
    for _ in range(t):
        n, m, k = map(int, data[index].split())
        edges = []
        for i in range(m):
            u, v = map(int, data[index + 1 + i].split())
            edges.append((u, v))
        index += m + 1
        
        result = eulerian_path_exists(n, m, k, edges)
        results.append(result)

    print("\n".join(results))

if __name__ == "__main__":
    main()