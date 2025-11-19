import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    from collections import deque

    input = sys.stdin.readline

    H, W = map(int, input().split())
    N = H * W
    F = [list(map(int, input().split())) for _ in range(H)]

    # Build all edges with capacity = min(F[u], F[v])
    edges = []
    # directions: right and down to avoid duplicates
    for i in range(H):
        for j in range(W):
            u = i * W + j
            if j + 1 < W:
                v = i * W + (j + 1)
                w = min(F[i][j], F[i][j+1])
                edges.append((w, u, v))
            if i + 1 < H:
                v = (i + 1) * W + j
                w = min(F[i][j], F[i+1][j])
                edges.append((w, u, v))

    # DSU for Kruskal
    parent_dsu = list(range(N))
    rank_dsu = [0] * N
    def find(x):
        while parent_dsu[x] != x:
            parent_dsu[x] = parent_dsu[parent_dsu[x]]
            x = parent_dsu[x]
        return x
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank_dsu[x] < rank_dsu[y]:
            parent_dsu[x] = y
        else:
            parent_dsu[y] = x
            if rank_dsu[x] == rank_dsu[y]:
                rank_dsu[x] += 1
        return True

    # Kruskal maximum spanning tree
    edges.sort(reverse=True, key=lambda e: e[0])
    adj = [[] for _ in range(N)]
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))

    # Prepare LCA with binary lifting, storing min edge on path to ancestor
    LOG = (N-1).bit_length()
    up = [[0] * N for _ in range(LOG)]
    minW = [[10**9] * N for _ in range(LOG)]
    depth = [0] * N

    # BFS to set parent[0] and minW[0]
    INF = 10**9
    root = 0
    depth[root] = 0
    up[0][root] = root
    minW[0][root] = INF
    q = deque([root])
    visited = [False] * N
    visited[root] = True
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                minW[0][v] = w
                q.append(v)

    # Build binary lifting tables
    for k in range(1, LOG):
        for v in range(N):
            mid = up[k-1][v]
            up[k][v] = up[k-1][mid]
            minW[k][v] = min(minW[k-1][v], minW[k-1][mid])

    def getMinEdge(u, v):
        # returns minimum edge weight on path u-v in MST
        if u == v:
            return INF
        res = INF
        if depth[u] < depth[v]:
            u, v = v, u
        # lift u to depth v
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if diff & (1 << k):
                res = min(res, minW[k][u])
                u = up[k][u]
        if u == v:
            return res
        # lift both
        for k in reversed(range(LOG)):
            if up[k][u] != up[k][v]:
                res = min(res, minW[k][u], minW[k][v])
                u = up[k][u]
                v = up[k][v]
        # last step to LCA
        res = min(res, minW[0][u], minW[0][v])
        return res

    # Process queries
    Q = int(input())
    out = []
    for _ in range(Q):
        Ai, Bi, Yi, Ci, Di, Zi = map(int, input().split())
        Ai -= 1; Bi -= 1; Ci -= 1; Di -= 1
        u = Ai * W + Bi
        v = Ci * W + Di
        T = getMinEdge(u, v)
        L = Yi if Yi < Zi else Zi
        D = Yi - Zi if Yi > Zi else Zi - Yi
        if T >= L:
            ans = D
        else:
            ans = D + 2 * (L - T)
        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()