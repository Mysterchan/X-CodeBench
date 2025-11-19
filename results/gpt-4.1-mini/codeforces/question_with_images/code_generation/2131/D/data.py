import sys
import collections
input = sys.stdin.readline

def bfs(start, n, graph):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = collections.deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    farthest_node = dist.index(max(dist))
    max_dist = dist[farthest_node]
    return farthest_node, max_dist, dist

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = [[] for __ in range(n+1)]
        for __ in range(n-1):
            u,v = map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)

        # Find diameter endpoints
        u, _, _ = bfs(1, n, graph)
        v, diameter, dist_u = bfs(u, n, graph)
        _, _, dist_v = bfs(v, n, graph)

        # Find the diameter path
        path = []
        cur = v
        # To reconstruct path, we use dist_u and dist_v:
        # On diameter path, dist_u[x] + dist_v[x] == diameter
        # We can reconstruct path from v to u by moving to neighbors with dist_u[x] == dist_u[cur]-1
        # and dist_u[x] + dist_v[x] == diameter
        # This is a standard approach to find diameter path.
        path = [v]
        while cur != u:
            for nxt in graph[cur]:
                if dist_u[nxt] == dist_u[cur] - 1 and dist_u[nxt] + dist_v[nxt] == diameter:
                    path.append(nxt)
                    cur = nxt
                    break
        path.reverse()

        # The minimal diameter after operations is:
        # - If diameter is 1 or 2, minimal diameter is diameter (0 operations)
        # - If diameter >= 3, minimal diameter is 2
        # Number of operations needed = max(0, diameter - 2)

        # Explanation:
        # Each operation can reduce the diameter by at most 1.
        # The minimal diameter achievable is 2 (star or near-star shape).
        # So operations = max(0, diameter - 2)

        print(max(0, diameter - 2))

if __name__ == "__main__":
    solve()