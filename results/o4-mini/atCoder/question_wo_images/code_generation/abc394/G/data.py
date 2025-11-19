import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    H, W = map(int, input().split())
    N = H * W
    F = [0] * N
    maxF = 0
    for i in range(H):
        row = list(map(int, input().split()))
        for j in range(W):
            idx = i * W + j
            F[idx] = row[j]
            if row[j] > maxF:
                maxF = row[j]

    # Build edges: for each adjacent pair, weight = min(Fu, Fv)
    edges = []
    for i in range(H):
        for j in range(W):
            u = i * W + j
            if i + 1 < H:
                v = (i + 1) * W + j
                w = F[u] if F[u] < F[v] else F[v]
                edges.append((w, u, v))
            if j + 1 < W:
                v = i * W + (j + 1)
                w = F[u] if F[u] < F[v] else F[v]
                edges.append((w, u, v))

    # Sort edges descending by weight
    edges.sort(reverse=True, key=lambda x: x[0])
    E = len(edges)

    Q = int(input())
    s_node = [0] * Q
    t_node = [0] * Q
    Ys = [0] * Q
    Zs = [0] * Q

    for q in range(Q):
        A, B, Y, C, D, Z = map(int, input().split())
        A -= 1; B -= 1; C -= 1; D -= 1
        s_node[q] = A * W + B
        t_node[q] = C * W + D
        Ys[q] = Y
        Zs[q] = Z

    # Parallel binary search to find for each query the maximum M*:
    # We want the maximum w such that s and t are connected in subgraph of edges with weight >= w.
    lo = [0] * Q
    hi = [maxF + 1] * Q

    parent = [ -1 ] * N

    def dsu_find(x):
        # path compression
        while parent[x] >= 0:
            if parent[parent[x]] >= 0:
                parent[x] = parent[parent[x_parent[x]]]
            x = parent[x]
        return x

    def dsu_union(a, b):
        a = dsu_find(a)
        b = dsu_find(b)
        if a == b:
            return False
        # union by size
        if parent[a] > parent[b]:
            a, b = b, a
        parent[a] += parent[b]
        parent[b] = a
        return True

    # Continue until all queries have lo+1 == hi
    # We'll do at most log2(maxF+1) iterations ~20
    active = True
    while True:
        # Collect tasks: for each q with lo[q]+1 < hi[q], mid=(lo+hi)//2
        tasks = []
        for q in range(Q):
            if lo[q] + 1 < hi[q]:
                m = (lo[q] + hi[q]) // 2
                tasks.append((m, q))
        if not tasks:
            break
        # Sort tasks by mid descending
        tasks.sort(reverse=True, key=lambda x: x[0])

        # Reset DSU
        for i in range(N):
            parent[i] = -1
        ptr = 0  # pointer on edges

        # Process each task
        for m, qid in tasks:
            # add all edges with weight >= m
            while ptr < E and edges[ptr][0] >= m:
                _, u, v = edges[ptr]
                dsu_union(u, v)
                ptr += 1
            # check connectivity
            if dsu_find(s_node[qid]) == dsu_find(t_node[qid]):
                lo[qid] = m
            else:
                hi[qid] = m

    # Now lo[q] is the maximum bottleneck M*
    # Compute answer for each query:
    out = []
    for q in range(Q):
        M = lo[q]
        y = Ys[q]
        z = Zs[q]
        diff = y - z
        if diff < 0:
            diff = -diff
        mn = y if y < z else z
        extra = mn - M
        if extra < 0:
            extra = 0
        ans = diff + extra * 2
        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    main()