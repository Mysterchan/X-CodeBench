from collections import deque

N = int(input())
C = [input() for _ in range(N)]

# dist[i][j]: shortest palindrome path length from i to j
# We'll use 0-based indexing internally
# The problem: find shortest path from i to j such that the concatenation of edge labels along the path is a palindrome.

# Key idea:
# We consider pairs of nodes (u,v) representing the "front" and "back" positions in the palindrome.
# We do a BFS on states (u,v) where the path from u to v can be extended to a palindrome.
# The length of the palindrome path corresponding to (u,v) is stored in dist[u][v].
# 
# Initialization:
# - dist[i][i] = 0 (empty path, empty string is palindrome)
# - For each edge u->v with label c, dist[u][v] = 1 (single edge path is palindrome)
#
# Transition:
# From (u,v), try to extend palindrome by adding edges:
# For all edges u->u2 with label c and v2->v with label c (same label),
# if dist[u2][v2] not set, set dist[u2][v2] = dist[u][v] + 2
#
# After BFS, dist[i][j] is the shortest palindrome path length from i to j, or -1 if none.

dist = [[-1]*N for _ in range(N)]
queue = deque()

# Initialize dist[i][i] = 0 (empty path)
for i in range(N):
    dist[i][i] = 0
    queue.append((i,i))

# Initialize dist[u][v] = 1 if edge u->v exists
for u in range(N):
    for v in range(N):
        if C[u][v] != '-':
            if dist[u][v] == -1 or dist[u][v] > 1:
                dist[u][v] = 1
                queue.append((u,v))

# Precompute edges by label for quick lookup
# out_edges[u][c] = list of nodes reachable from u by edge labeled c
# in_edges[v][c] = list of nodes from which v is reachable by edge labeled c
out_edges = [{} for _ in range(N)]
in_edges = [{} for _ in range(N)]
for u in range(N):
    for v in range(N):
        c = C[u][v]
        if c != '-':
            if c not in out_edges[u]:
                out_edges[u][c] = []
            out_edges[u][c].append(v)
            if c not in in_edges[v]:
                in_edges[v][c] = []
            in_edges[v][c].append(u)

while queue:
    u,v = queue.popleft()
    d = dist[u][v]
    # Try to extend palindrome by adding edges with same label c:
    # from u to u2 and from v2 to v with label c
    for c in out_edges[u]:
        if c in in_edges[v]:
            for u2 in out_edges[u][c]:
                for v2 in in_edges[v][c]:
                    if dist[u2][v2] == -1:
                        dist[u2][v2] = d + 2
                        queue.append((u2,v2))

# Output dist matrix
for i in range(N):
    print(' '.join(str(dist[i][j]) for j in range(N)))