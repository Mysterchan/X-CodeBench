import sys
from collections import defaultdict

def solve_one(n, m, k, edges):
    # Create an adjacency list
    graph = defaultdict(list)
    for idx, (u, v, l, r) in enumerate(edges):
        graph[u].append((v, l, r, idx))
        graph[v].append((u, l, r, idx))

    # Minimum and maximum weight from 1 to k
    dist_from_start = {i: float('inf') for i in range(1, n + 1)}
    dist_from_k = {i: float('inf') for i in range(1, n + 1)}
    dist_from_start[1] = 0
    dist_from_k[k] = 0

    # Bellman-Ford like propagation to find all reachable distances
    def relax(node, dist):
        for neighbor, l, r, idx in graph[node]:
            if dist[node] + l < dist[neighbor]:
                dist[neighbor] = dist[node] + l
            elif dist[node] + r < dist[neighbor]:
                dist[neighbor] = dist[node] + r

    for _ in range(n - 1):
        for u in range(1, n + 1):
            relax(u, dist_from_start)
            relax(u, dist_from_k)

    # The lower bounds of distances
    d1k = dist_from_start[k]
    dkn = dist_from_k[n]
    lower_bound = dist_from_start[k] + dist_from_k[n]

    # Check if there is a valid assignment
    for _, _, r, idx in edges:
        # Check if the weights can create divergence
        if dist_from_start[1] < lower_bound and lower_bound < dist_from_start[k] + r:
            return True

    return False

def solve():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        edges = []
        for __ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            l = int(data[index + 2])
            r = int(data[index + 3])
            edges.append((u, v, l, r))
            index += 4
        
        if solve_one(n, m, k, edges):
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()