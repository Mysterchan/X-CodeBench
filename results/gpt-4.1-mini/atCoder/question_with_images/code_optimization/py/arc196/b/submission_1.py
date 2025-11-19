import sys
input = sys.stdin.readline

MOD = 998244353

# Precompute powers of 2 up to 10^6 (max HW)
MAX = 10**6
p2 = [1]*(MAX+1)
for i in range(MAX):
    p2[i+1] = (p2[i]<<1) % MOD

class UnionFind:
    __slots__ = ['parent', 'size', 'num_conn_comp']
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_conn_comp = n

    def leader(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        x, y = self.leader(x), self.leader(y)
        if x == y:
            return False
        self.num_conn_comp -= 1
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

    def issame(self, x, y):
        return self.leader(x) == self.leader(y)

class BipartiteChecker:
    __slots__ = ['n', 'uf', 'is_bipartite']
    def __init__(self, n):
        self.n = n
        self.uf = UnionFind(2*n)
        self.is_bipartite = True

    def add_edge(self, u, v):
        # u connected to v's opposite color
        if not self.uf.merge(u, v + self.n):
            pass
        if not self.uf.merge(u + self.n, v):
            pass
        if self.uf.issame(u, u + self.n):
            self.is_bipartite = False

    def add_same(self, u, v):
        # u and v same color
        if not self.uf.merge(u, v):
            pass
        if not self.uf.merge(u + self.n, v + self.n):
            pass
        if self.uf.issame(u, u + self.n):
            self.is_bipartite = False

def solve(H, W, grid):
    N = H * W * 4
    bc = BipartiteChecker(N)

    # Precompute indices for neighbors with wrap-around
    row_shift = 4 * W
    for i in range(H):
        i_down = (i + 1) % H
        for j in range(W):
            j_right = (j + 1) % W
            t = 4 * (i * W + j)

            c = grid[i][j]
            if c == 'A':
                # connect diagonals (0-2) and (1-3) with opposite colors
                bc.add_edge(t, t + 2)
                bc.add_edge(t + 1, t + 3)
            else:
                # B tile: vertical line (0-1) same color, and (0-2), (1-3) same color
                bc.add_edge(t, t + 1)
                bc.add_same(t, t + 2)
                bc.add_same(t + 1, t + 3)

            # vertical wrap-around edges (bottom-top)
            bc.add_same(t + 2, 4 * (i_down * W + j))
            # horizontal wrap-around edges (right-left)
            bc.add_same(t + 3, 4 * (i * W + j_right) + 1)

    if not bc.is_bipartite:
        return 0
    # Number of connected components in uf
    # Each component counted twice (due to bipartite doubling)
    return p2[bc.uf.num_conn_comp // 2]

T = int(input())
out = []
for _ in range(T):
    H, W = map(int, input().split())
    grid = [input().rstrip() for __ in range(H)]
    out.append(str(solve(H, W, grid)))
print('\n'.join(out))