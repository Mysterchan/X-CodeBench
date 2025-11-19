def has_euler_trail(n, m, k, edges):
    # Count the degree of each vertex in the original graph G
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    # Count the number of vertices with odd degree in G
    odd_count = sum(1 for deg in degree if deg % 2 == 1)

    # Check the necessary conditions for Euler trails in L^k(G)
    if odd_count == 0:
        # L^1(G) will have all vertices with even degree
        return True if k >= 1 else False
    elif odd_count == 2:
        # L^1(G) will have 2 vertices with odd degree
        return True if k >= 1 else False
    else:
        return False

def process_cases(tc):
    results = []
    for _ in range(tc):
        n, m, k = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        if has_euler_trail(n, m, k, edges):
            results.append("YES")
        else:
            results.append("NO")
    return results

if __name__ == "__main__":
    t = int(input())
    results = process_cases(t)
    print("\n".join(results))