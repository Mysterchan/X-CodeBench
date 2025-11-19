import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline
    H, W = map(int, input().split())
    N = H * W
    F = [0] * N
    for i in range(H):
        row = list(map(int, input().split()))
        base = i * W
        for j in range(W):
            F[base + j] = row[j]
    # Build all edges with weight = min(F[u], F[v])
    edges = []
    # Right edges
    for i in range(H):
        bi = i * W
        for j in range(W - 1):
            u = bi + j
            v = u + 1
            w = F[u] if F[u] < F[v] else F[v]
            edges.append((w, u, v))
    # Down edges
    for i in range(H - 1):
        bi = i * W
        bi2 = (i + 1) * W
        for j in range(W):
            u = bi + j
            v = bi2 + j
            w = F[u] if F[u] < F[v] else F[v]
            edges.append((w, u, v))
    # Kruskal maximum spanning tree
    edges.sort(reverse=True, key=lambda x: x[0])
    parent = list(range(N))
    rank = [0] * N
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        x = find(x); y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    # MST adjacency
    adj = [[] for _ in range(N)]
    ecount = 0
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))
            ecount += 1
            if ecount == N - 1:
                break
    # Prepare LCA on MST, tracking min edge on path
    LOG = (N - 1).bit_length()
    parent_up = [[-1] * N for _ in range(LOG)]
    min_up = [[10**9+7] * N for _ in range(LOG)]
    depth = [0] * N
    # DFS/BFS to set parent_up[0], min_up[0], depth
    from collections import deque
    INF = 10**9+7
    root = 0
    depth[root] = 0
    parent_up[0][root] = root
    min_up[0][root] = INF
    dq = deque([root])
    visited = [False] * N
    visited[root] = True
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent_up[0][v] = u
                min_up[0][v] = w
                dq.append(v)
    # Binary lifting
    for k in range(1, LOG):
        pu = parent_up[k - 1]
        mu = min_up[k - 1]
        pu2 = parent_up[k]
        mu2 = min_up[k]
        for v in range(N):
            mid = pu[v]
            pu2[v] = pu[mid]
            mv = mu[v]
            mv2 = mu[mid]
            # minimal edge on 2^k jump = min(min_up[k-1][v], min_up[k-1][mid])
            mu2[v] = mv if mv < mv2 else mv2
    # Function to query minimum edge weight on path u-v
    def query_min(u, v):
        if u == v:
            return INF
        mn = INF
        du = depth[u]; dv = depth[v]
        if du < dv:
            u, v = v, u
            du, dv = dv, du
        # Lift u up
        diff = du - dv
        k = 0
        while diff:
            if diff & 1:
                w = min_up[k][u]
                if w < mn: mn = w
                u = parent_up[k][u]
            diff >>= 1
            k += 1
        if u == v:
            return mn
        # Lift both up
        for k in range(LOG - 1, -1, -1):
            pu = parent_up[k][u]
            pv = parent_up[k][v]
            if pu != pv:
                w1 = min_up[k][u]
                if w1 < mn: mn = w1
                w2 = min_up[k][v]
                if w2 < mn: mn = w2
                u, v = pu, pv
        # Final one-step to LCA
        w1 = min_up[0][u]
        if w1 < mn: mn = w1
        w2 = min_up[0][v]
        if w2 < mn: mn = w2
        return mn
    # Process queries
    Q = int(input())
    out = []
    for _ in range(Q):
        a, b, y, c, d, z = map(int, input().split())
        u = (a - 1) * W + (b - 1)
        v = (c - 1) * W + (d - 1)
        T = query_min(u, v)
        # Compute answer
        if y <= T or z <= T:
            # they can meet at level between y and z
            ans = abs(y - z)
        else:
            ans = y + z - 2 * T
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()