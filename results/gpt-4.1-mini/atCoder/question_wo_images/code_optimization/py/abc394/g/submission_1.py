import sys
from array import array

def solve() -> None:
    input = sys.stdin.buffer.read().split()
    it = iter(input)
    H = int(next(it))
    W = int(next(it))
    N = H * W
    height = [0] * N
    for i in range(N):
        height[i] = int(next(it))
    Q = int(next(it))
    queries = []
    for _ in range(Q):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        y = int(next(it))
        c = int(next(it)) - 1
        d = int(next(it)) - 1
        z = int(next(it))
        u = a * W + b
        v = c * W + d
        queries.append((u, v, y, z))

    edges = []
    for i in range(H):
        base = i * W
        for j in range(W):
            u = base + j
            if i + 1 < H:
                v = (i + 1) * W + j
                w = height[u] if height[u] < height[v] else height[v]
                edges.append((w, u, v))
            if j + 1 < W:
                v = base + j + 1
                w = height[u] if height[u] < height[v] else height[v]
                edges.append((w, u, v))

    edges.sort(reverse=True, key=lambda x: x[0])

    parent = array('i', range(N))
    size = array('i', [1] * N)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        return True

    adj = [[] for _ in range(N)]
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))

    LOG = (N.bit_length())
    up = [array('i', [-1] * N) for _ in range(LOG)]
    minW = [array('I', [0xFFFFFFFF] * N) for _ in range(LOG)]
    depth = array('i', [0] * N)

    # Find a root for DFS (any node, e.g., 0)
    root = 0
    stack = [root]
    visited = array('b', [0] * N)
    visited[root] = 1
    up[0][root] = root
    minW[0][root] = 0xFFFFFFFF

    while stack:
        v = stack.pop()
        for to, w in adj[v]:
            if visited[to]:
                continue
            visited[to] = 1
            depth[to] = depth[v] + 1
            up[0][to] = v
            minW[0][to] = w
            stack.append(to)

    for k in range(1, LOG):
        upk = up[k]
        upk_1 = up[k - 1]
        minWk = minW[k]
        minWk_1 = minW[k - 1]
        for v in range(N):
            p = upk_1[v]
            if p != -1:
                upk[v] = upk_1[p]
                a = minWk_1[v]
                b = minWk_1[p]
                minWk[v] = a if a < b else b
            else:
                upk[v] = -1
                minWk[v] = minWk_1[v]

    def min_on_path(u: int, v: int) -> int:
        if u == v:
            return 0xFFFFFFFF
        ans = 0xFFFFFFFF
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        bit = 0
        while diff:
            if diff & 1:
                w = minW[bit][u]
                if w < ans:
                    ans = w
                u = up[bit][u]
            diff >>= 1
            bit += 1
        if u == v:
            return ans
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != -1 and up[k][u] != up[k][v]:
                w1 = minW[k][u]
                if w1 < ans:
                    ans = w1
                w2 = minW[k][v]
                if w2 < ans:
                    ans = w2
                u = up[k][u]
                v = up[k][v]
        w1 = minW[0][u]
        if w1 < ans:
            ans = w1
        w2 = minW[0][v]
        if w2 < ans:
            ans = w2
        return ans

    out = []
    append = out.append
    for u, v, y, z in queries:
        if u == v:
            append(str(abs(y - z)))
            continue
        M = min_on_path(u, v)
        low = y if y < z else z
        if M >= low:
            append(str(abs(y - z)))
        else:
            append(str(y + z - 2 * M))
    print('\n'.join(out))


if __name__ == '__main__':
    solve()