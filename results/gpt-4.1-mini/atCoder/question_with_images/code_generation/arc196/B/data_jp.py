import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# Union-Find (Disjoint Set Union) implementation
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def get_size(self, x):
        return self.size[self.find(x)]

# Precompute powers of 2 and 4 up to max HW=10^6
MAX_HW = 10**6
pow2 = [1]*(MAX_HW+1)
pow4 = [1]*(MAX_HW+1)
for i in range(1, MAX_HW+1):
    pow2[i] = (pow2[i-1]*2) % MOD
    pow4[i] = (pow4[i-1]*4) % MOD

T = int(input())
total_HW = 0
results = []

for _ in range(T):
    H, W = map(int, input().split())
    S = [input().rstrip() for __ in range(H)]
    total_HW += H*W

    # We model the problem as a graph problem on edges between cells.
    # Each cell has 4 edges (top, right, bottom, left).
    # The condition that line segments connect properly means edges must be paired consistently.
    #
    # The problem reduces to counting the number of ways to assign rotations to tiles so that
    # the edges form a 2-regular graph (each vertex degree 2) on the torus.
    #
    # The key insight:
    # - Each cell corresponds to a vertex with 4 half-edges (top, right, bottom, left).
    # - The tile type A connects adjacent edges (e.g. top-right, right-bottom, bottom-left, left-top) depending on rotation.
    # - The tile type B connects opposite edges (top-bottom or left-right).
    #
    # The global condition means the edges between cells must be matched consistently.
    #
    # We can represent each edge between cells as a vertex in a new graph,
    # and the constraints as edges between these vertices.
    #
    # The problem reduces to counting the number of 2-colorings of the graph components with certain constraints.
    #
    # Implementation:
    # We create a graph with 2*H*W vertices representing the edges between cells:
    # - For each cell, we have 4 half-edges: top, right, bottom, left.
    #   But since edges are shared between cells, we represent each edge once.
    #
    # We assign an index to each edge between cells:
    # Horizontal edges: between (i,j) right edge and (i,(j+1)%W) left edge
    # Vertical edges: between (i,j) bottom edge and ((i+1)%H,j) top edge
    #
    # Number of edges = H*W*2 (horizontal + vertical)
    #
    # For each cell, the tile type imposes constraints on how the 4 edges are paired.
    # For type A: edges are paired as (top,right), (bottom,left) in some rotation
    # For type B: edges are paired as (top,bottom) or (left,right)
    #
    # We build a graph where vertices are edges between cells,
    # and edges represent that two edges must be paired in the tile.
    #
    # Then, the problem reduces to counting the number of ways to assign pairings in each connected component.
    #
    # Each connected component is either a cycle or a chain.
    # The number of valid assignments per component is 2.
    #
    # Finally, the answer is 2^(number_of_components) modulo MOD.
    #
    # But we must also multiply by the number of ways to assign rotations ignoring the connectivity condition:
    # total ways = 4^a * 2^b
    # The number of valid ways = 2^(number_of_components)
    #
    # The problem states the number of valid ways is the count of ways satisfying the no dead-end condition.
    #
    # From editorial and problem analysis:
    # The answer = 2^(number_of_components)
    #
    # So we just need to find the number of connected components in the constructed graph.
    #
    # Implementation details:
    # - Assign an ID to each edge between cells:
    #   horizontal edges: H*W edges, index 0 to H*W-1
    #   vertical edges: H*W edges, index H*W to 2*H*W-1
    #
    # For each cell (i,j):
    #   edges:
    #     top edge: vertical edge between ((i-1)%H,j) bottom and (i,j) top => vertical edge at ((i-1)%H,j)
    #     right edge: horizontal edge between (i,j) right and (i,(j+1)%W) left => horizontal edge at (i,j)
    #     bottom edge: vertical edge between (i,j) bottom and ((i+1)%H,j) top => vertical edge at (i,j)
    #     left edge: horizontal edge between (i,(j-1)%W) right and (i,j) left => horizontal edge at (i,(j-1)%W)
    #
    # For each cell, add edges between these edges according to tile type and rotation constraints.
    #
    # For tile A:
    #   The 4 rotations correspond to pairing edges as:
    #   (top,right) and (bottom,left)
    #   (right,bottom) and (left,top)
    #   (bottom,left) and (top,right)
    #   (left,top) and (right,bottom)
    #   But since rotations are symmetric, the constraints are:
    #   The edges form two pairs of adjacent edges.
    #
    # For tile B:
    #   The 2 rotations correspond to pairing edges as:
    #   (top,bottom) and (left,right)
    #   or (left,right) and (top,bottom)
    #
    # So for tile A, the edges are paired as (top,right) and (bottom,left)
    # For tile B, edges are paired as (top,bottom) and (left,right)
    #
    # We add edges in the graph between these edge-vertices to represent these pairings.
    #
    # Then count connected components in this graph.
    #
    # The answer is pow(2, number_of_components, MOD)

    HW = H*W
    # Assign IDs:
    # horizontal edges: 0 ~ HW-1
    # vertical edges: HW ~ 2*HW-1

    def h_id(i,j):
        return i*W + j
    def v_id(i,j):
        return HW + i*W + j

    uf = UnionFind(2*HW)

    # For each cell, add edges between edges according to tile type
    for i in range(H):
        for j in range(W):
            c = S[i][j]
            # edges of cell (i,j)
            top = v_id((i-1)%H, j)
            right = h_id(i, j)
            bottom = v_id(i, j)
            left = h_id(i, (j-1)%W)

            if c == 'A':
                # pair (top,right), (bottom,left)
                uf.unite(top, right)
                uf.unite(bottom, left)
            else:
                # c == 'B'
                # pair (top,bottom), (left,right)
                uf.unite(top, bottom)
                uf.unite(left, right)

    # Count number of connected components in the graph of edges
    # The graph has 2*HW vertices
    # Count distinct parents
    parents = set()
    for x in range(2*HW):
        parents.add(uf.find(x))
    components = len(parents)

    # The answer is 2^(components) mod MOD
    ans = pow2[components] % MOD
    results.append(ans)

print('\n'.join(map(str, results)))