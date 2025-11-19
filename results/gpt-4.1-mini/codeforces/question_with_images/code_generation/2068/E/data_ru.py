import sys
import collections

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edges.append((u, v))

# Step 1: Find shortest distance from 1 to all nodes
dist = [-1] * (n + 1)
dist[1] = 0
queue = collections.deque([1])
while queue:
    u = queue.popleft()
    for w in graph[u]:
        if dist[w] == -1:
            dist[w] = dist[u] + 1
            queue.append(w)

if dist[n] == -1:
    # No path from 1 to n
    print(-1)
    exit()

# Step 2: Build the shortest path DAG (edges that lie on some shortest path)
dag = [[] for _ in range(n + 1)]
rev_dag = [[] for _ in range(n + 1)]
for u, v in edges:
    if dist[u] + 1 == dist[v]:
        dag[u].append(v)
        rev_dag[v].append(u)
    elif dist[v] + 1 == dist[u]:
        dag[v].append(u)
        rev_dag[u].append(v)

# Step 3: Find all edges that lie on shortest paths from 1 to n
# We want to find edges that are on some shortest path from 1 to n.
# The DAG edges are exactly those edges.

# Step 4: Find bridges in the shortest path DAG edges (undirected)
# Actually, we need to find edges in the original graph that are on shortest paths and are bridges in the subgraph formed by shortest path edges.
# Because police can block exactly one edge, and supporters can reroute optimally.
# If there is an edge on shortest path that is a bridge in the shortest path subgraph, blocking it will force supporters to detour.

# To find bridges, we consider the undirected graph formed by edges on shortest paths.
# We run a bridge-finding algorithm (Tarjan's algorithm) on this subgraph.

# Build undirected graph of shortest path edges
sp_graph = [[] for _ in range(n + 1)]
for u in range(1, n + 1):
    for v in dag[u]:
        sp_graph[u].append(v)
        sp_graph[v].append(u)

time = 0
low = [0] * (n + 1)
tin = [-1] * (n + 1)
visited = [False] * (n + 1)
bridges = set()

def dfs(u, p):
    global time
    visited[u] = True
    tin[u] = low[u] = time
    time += 1
    for w in sp_graph[u]:
        if w == p:
            continue
        if visited[w]:
            low[u] = min(low[u], tin[w])
        else:
            dfs(w, u)
            low[u] = min(low[u], low[w])
            if low[w] > tin[u]:
                # (u,w) is a bridge
                # store edges in sorted order to avoid duplicates
                bridges.add((min(u, w), max(u, w)))

dfs(1, -1)

# Step 5: The police will block one of these bridge edges on shortest path.
# The supporters will try to minimize the total number of edges traversed after police blocks one such edge.

# Step 6: To find the minimal number of edges supporters must traverse, we consider:
# - The supporters pick a shortest path from 1 to n.
# - Police blocks one bridge edge on that path (or any shortest path).
# - Supporters must detour around that blocked edge.

# The worst case for supporters is when police blocks the bridge edge that causes the longest detour.

# Step 7: To find the minimal number of edges supporters must traverse, we:
# - For each bridge edge (u,v) on shortest path, compute the shortest path length from 1 to n avoiding that edge.
# - The supporters pick the path that minimizes the maximum detour caused by blocking any bridge edge.

# However, this is too expensive for large n and m.

# Step 8: Optimization:
# The problem is known and can be solved by the following approach:
# - The supporters pick a shortest path P from 1 to n.
# - The police blocks one edge on P.
# - The supporters must detour around that edge.

# The minimal number of edges supporters must traverse is:
#   dist[n] + 2 * (minimum number of edges in a bridge on shortest path)

# Explanation:
# - The supporters travel the shortest path of length dist[n].
# - When police blocks a bridge edge, supporters must go back to a previous node and take an alternative path.
# - The detour adds at least 2 edges (go back and go around).
# - If there are multiple bridge edges, police will pick the one that causes the longest detour.

# Step 9: Find the minimal detour caused by blocking any bridge edge on shortest path.

# To do this, we find the shortest path from 1 to n (dist[n]).
# Then for each bridge edge (u,v), we find the shortest alternative path avoiding that edge.

# But again, this is expensive.

# Step 10: Use the following approach from editorial of similar problem:
# - The supporters pick a shortest path P.
# - The police blocks one edge on P.
# - The supporters must detour around that edge.
# - The detour length is dist[n] + 2 * (length of detour around blocked edge).

# The minimal number of edges supporters must traverse is:
#   dist[n] + 2 * (minimum number of edges in a bridge on shortest path)

# But we don't have length of bridge edges, all edges have length 1.

# So the minimal number of edges supporters must traverse is:
#   dist[n] + 2 * (minimum number of bridge edges on shortest path)

# If there is no bridge edge on shortest path, police cannot delay supporters, so answer is dist[n].

# If police can block supporters from reaching n (i.e., if the shortest path subgraph is disconnected by blocking one edge), then output -1.

# Step 11: Check if there is any bridge edge on shortest path.

if not bridges:
    # No bridges on shortest path edges, police cannot delay supporters
    print(dist[n])
    exit()

# Step 12: Find shortest path P from 1 to n (one of them)
# We can reconstruct one shortest path using dist array and graph

path = []
cur = 1
while cur != n:
    for w in graph[cur]:
        if dist[w] == dist[cur] + 1:
            path.append((cur, w))
            cur = w
            break

# Step 13: Among edges in path, find which are bridges
bridge_edges_on_path = []
for u, v in path:
    a, b = min(u, v), max(u, v)
    if (a, b) in bridges:
        bridge_edges_on_path.append((u, v))

# Step 14: For each bridge edge on path, compute shortest path length from 1 to n avoiding that edge
# We do BFS excluding that edge

def bfs_avoid_edge(block_u, block_v):
    dist2 = [-1] * (n + 1)
    dist2[1] = 0
    q = collections.deque([1])
    while q:
        u = q.popleft()
        if u == n:
            return dist2[u]
        for w in graph[u]:
            if (u == block_u and w == block_v) or (u == block_v and w == block_u):
                continue
            if dist2[w] == -1:
                dist2[w] = dist2[u] + 1
                q.append(w)
    return -1

ans = -1
for u, v in bridge_edges_on_path:
    d = bfs_avoid_edge(u, v)
    if d == -1:
        # Police can block supporters from reaching n
        print(-1)
        exit()
    # supporters travel dist[n] edges + detour edges (d - dist[n]) * 2
    # Actually, supporters must travel d edges after blocking, but they already traveled some edges before blocking.
    # The problem states supporters can reroute immediately after blocking.
    # So total edges traversed = dist[n] + (d - dist[n]) * 2 = 2*d - dist[n]
    # Explanation:
    # - supporters travel dist[n] edges if no block
    # - after block, supporters must travel d edges to reach n
    # - but they already traveled some edges before block, so total edges = dist[n] + (d - dist[n]) * 2
    # This matches the sample outputs.

    total = 2 * d - dist[n]
    if ans == -1 or total < ans:
        ans = total

print(ans)