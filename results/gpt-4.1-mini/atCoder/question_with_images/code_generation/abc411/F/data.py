import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(int, input().split()))

# DSU (Disjoint Set Union) with edge count and adjacency sets for each component
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n
        # adjacency sets store neighbors of each component (by root)
        self.adj = [set() for _ in range(n)]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        # union by size
        if self.size[a] < self.size[b]:
            a, b = b, a
        # merge b into a
        self.parent[b] = a
        self.size[a] += self.size[b]

        # Calculate number of edges between a and b components
        # The edges between a and b are counted twice in adj sets (once in a, once in b)
        # So count how many neighbors in a.adj are b and vice versa
        # Actually, edges between a and b are the intersection of a.adj and b.adj
        # But adj sets store neighbors by root, so edges between a and b are those edges connecting a and b
        # Actually, edges between a and b are those edges connecting vertices in a and vertices in b.
        # But we don't have direct info about edges between components except adjacency sets.
        # The edges between a and b are those edges that appear in both a.adj and b.adj as neighbors.
        # Actually, edges between a and b are those edges that connect a and b, so neighbors of a include b if there's an edge.
        # But adjacency sets store neighbors by root, so if b in a.adj, that means there is at least one edge between a and b.
        # But we need the count of edges between a and b, not just existence.
        # So we need to count how many edges connect a and b.
        # We can count edges between a and b as the number of neighbors in a.adj equal to b, but adj sets only store unique neighbors.
        # So we need to store counts of edges between components, not just sets.
        # To handle this, we will store adjacency as dict {neighbor_root: count_of_edges} instead of set.

        # So we need to change adj from set to dict to store counts.

        return a, b

# We need to rewrite DSU with adjacency dict to store counts of edges between components.

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n
        # adjacency dict: for each root, map neighbor root -> count of edges
        self.adj = [{} for _ in range(n)]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

        # Merge adjacency dicts and update edge counts
        # Edges inside a and b remain, edges between a and b become self loops and removed
        # So total edges after merge:
        # edge_count[a] + edge_count[b] - 2 * edges_between_a_b

        # Count edges between a and b
        edges_between = self.adj[a].get(b, 0)

        # Update edge count
        self.edge_count[a] += self.edge_count[b] - 2 * edges_between

        # Merge adjacency dicts
        # Remove b from a.adj and b.adj (edges between a and b)
        if b in self.adj[a]:
            del self.adj[a][b]
        if a in self.adj[b]:
            del self.adj[b][a]

        # Merge neighbors of b into a
        for nb, cnt in self.adj[b].items():
            if nb == a:
                # This edge is now a self-loop, ignore
                continue
            # Add edges from b's neighbors to a's adjacency
            self.adj[a][nb] = self.adj[a].get(nb, 0) + cnt
            # Update neighbor's adjacency to point to a instead of b
            self.adj[nb][a] = self.adj[nb].get(a, 0) + cnt
            # Remove b from neighbor's adjacency
            del self.adj[nb][b]

        self.adj[b].clear()
        return True

dsu = DSU(N)

# Initialize adjacency dict and edge counts
for i, (u, v) in enumerate(edges):
    u -= 1
    v -= 1
    dsu.edge_count[u] += 0  # initially zero, will count edges per component after union
    dsu.edge_count[v] += 0
    # add edge to adjacency dict
    dsu.adj[u][v] = dsu.adj[u].get(v, 0) + 1
    dsu.adj[v][u] = dsu.adj[v].get(u, 0) + 1

# Initially, each vertex is its own component with zero edges
# But edges exist between vertices, so edge_count per component is zero initially
# We need to count edges per component correctly:
# Actually, initially each vertex is a component with zero edges, edges connect different components
# So edge_count per component is zero initially

# The total number of edges is M initially
total_edges = M

# We need to track pieces positions:
# piece i is on vertex i initially
# After union, pieces on merged vertices are on the merged vertex (component)
# So piece i is on component find(i)

# For each operation:
# Given edge index X_i, check if pieces U_{X_i} and V_{X_i} are on different components and connected by an edge
# If yes, contract the edge (union the two components)
# Output the number of edges after each operation

# To check if pieces are on different vertices and connected by an edge:
# find the components of pieces U_x and V_x
# check if they are different
# check if adjacency dict of one contains the other

# pieces are numbered 1..N, vertices 1..N, so piece i is on vertex i initially

# Let's implement the logic:

# For each operation:
# 1) find components of U_x and V_x
# 2) if same, do nothing
# 3) else if adjacency dict of one contains the other, union them and update total_edges
# 4) else do nothing
# 5) print total_edges

for x in X:
    u, v = edges[x-1]
    u -= 1
    v -= 1
    ru = dsu.find(u)
    rv = dsu.find(v)
    if ru != rv and rv in dsu.adj[ru]:
        # edges between ru and rv
        edges_between = dsu.adj[ru][rv]
        # union components
        dsu.union(ru, rv)
        total_edges -= edges_between
    print(total_edges)