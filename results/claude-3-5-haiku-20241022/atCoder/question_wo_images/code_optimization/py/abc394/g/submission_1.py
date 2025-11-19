import sys
from array import array

INF = 2147483647

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    H = int(next(it))
    W = int(next(it))
    N = H * W
    
    height = [0] * N
    for i in range(H):
        for j in range(W):
            height[i * W + j] = int(next(it))
    
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
        for j in range(W):
            u = i * W + j
            if i + 1 < H:
                v = (i + 1) * W + j
                w = min(height[u], height[v])
                edges.append((w, u, v))
            if j + 1 < W:
                v = i * W + (j + 1)
                w = min(height[u], height[v])
                edges.append((w, u, v))
    
    edges.sort(reverse=True)
    
    parent = list(range(N))
    rank = [0] * N
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> bool:
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        return True
    
    adj = [[] for _ in range(N)]
    for w, u, v in edges:
        if union(u, v):
            adj[u].append((v, w))
            adj[v].append((u, w))
    
    LOG = 20
    up = [[-1] * N for _ in range(LOG)]
    minW = [[INF] * N for _ in range(LOG)]
    
    root = 0
    visited = [False] * N
    stack = [(root, -1)]
    visited[root] = False
    depth = [0] * N
    
    while stack:
        v, p = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        up[0][v] = p if p != -1 else v
        
        for to, w in adj[v]:
            if not visited[to]:
                depth[to] = depth[v] + 1
                minW[0][to] = w
                stack.append((to, v))
    
    for k in range(1, LOG):
        for v in range(N):
            p = up[k - 1][v]
            if p != -1 and p != v:
                up[k][v] = up[k - 1][p]
                minW[k][v] = min(minW[k - 1][v], minW[k - 1][p])
            else:
                up[k][v] = p
                minW[k][v] = minW[k - 1][v]
    
    def min_on_path(u: int, v: int) -> int:
        if u == v:
            return INF
        if depth[u] < depth[v]:
            u, v = v, u
        
        ans = INF
        diff = depth[u] - depth[v]
        
        for bit in range(LOG):
            if diff & (1 << bit):
                ans = min(ans, minW[bit][u])
                u = up[bit][u]
        
        if u == v:
            return ans
        
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                ans = min(ans, minW[k][u], minW[k][v])
                u = up[k][u]
                v = up[k][v]
        
        return min(ans, minW[0][u], minW[0][v])
    
    result = []
    for u, v, y, z in queries:
        if u == v:
            result.append(abs(y - z))
        else:
            M = min_on_path(u, v)
            low = min(y, z)
            if M >= low:
                result.append(abs(y - z))
            else:
                result.append(y + z - 2 * M)
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == '__main__':
    solve()