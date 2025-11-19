import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS from start (1)
dist_start = [-1] * (n + 1)
dist_start[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for w in graph[u]:
        if dist_start[w] == -1:
            dist_start[w] = dist_start[u] + 1
            q.append(w)

# BFS from end (n)
dist_end = [-1] * (n + 1)
dist_end[n] = 0
q = deque([n])
while q:
    u = q.popleft()
    for w in graph[u]:
        if dist_end[w] == -1:
            dist_end[w] = dist_end[u] + 1
            q.append(w)

# The shortest distance from 1 to n
shortest = dist_start[n]
if shortest == -1:
    # No path from 1 to n (should not happen as graph is connected)
    print(-1)
    exit()

# We want to find the minimal length of the supporters' club path after police blocks one edge optimally.
# The police can block exactly one edge that is not currently being traversed.
# The supporters know the police will block optimally and can re-route accordingly.

# Key insight:
# The supporters want to minimize the number of roads traversed.
# The police want to maximize it or block the path entirely.
# The police can block one edge at any time, except the edge currently being traversed.
# The supporters know this and plan accordingly.

# The problem reduces to:
# Find the minimal length of a path from 1 to n after removing one edge on some shortest path from 1 to n.
# Because police will block an edge on a shortest path to delay supporters.
# The supporters will then find the shortest path avoiding that blocked edge.

# So, for each edge on any shortest path from 1 to n, consider blocking it.
# Then find the shortest path length from 1 to n avoiding that edge.
# The police will pick the edge that maximizes the supporters' shortest path length.
# If supporters cannot reach n after blocking that edge, output -1.

# However, enumerating all shortest path edges is expensive.
# Instead, we use the following approach:

# For each edge (u,v), check if it lies on any shortest path from 1 to n:
# That is, if dist_start[u] + 1 + dist_end[v] == shortest or dist_start[v] + 1 + dist_end[u] == shortest
# Because the graph is undirected.

# For each such edge, we consider blocking it and find the shortest path length avoiding it.

# To do this efficiently, we can:
# - For each edge on shortest paths, temporarily remove it and run BFS to find shortest path length.
# - Keep track of the maximum shortest path length found.
# - If no path exists after blocking that edge, answer is -1.

# Since m can be up to 200,000, running BFS for each edge is too expensive.

# Optimization:
# We can use a modified BFS that considers the possibility of blocking one edge.
# We model states as (node, blocked) where blocked is 0 or 1 indicating whether police has blocked an edge yet.
# The supporters can choose any path, but the police will block one edge on the supporters' shortest path.
# The supporters know this and can plan accordingly.

# We want to find the minimal number of edges supporters must traverse assuming police blocks optimally.

# Approach:
# We do a 0-1 BFS or Dijkstra-like BFS on states:
# State: (node, blocked)
# blocked = 0 means police has not blocked any edge yet.
# blocked = 1 means police has blocked one edge.

# Transitions:
# From (u, 0), supporters move to (v, 0) if edge (u,v) is not blocked yet.
# Police can block any edge not currently being traversed.
# The police will block exactly one edge at some point.
# The supporters know this and can plan accordingly.

# The problem is complex, but the editorial approach is:
# The minimal number of edges supporters must traverse is:
# min over all edges e on shortest paths of:
#   shortest + 2 * (length of detour around e)
# Because supporters must detour around the blocked edge.

# The detour length can be computed by:
# For each edge e=(u,v) on shortest paths:
#   detour = dist_start[u] + 1 + dist_end[v]
#   or dist_start[v] + 1 + dist_end[u]
# But this equals shortest, so detour is shortest path length.

# So supporters must go back and take another path, which adds extra edges.

# The problem is known as "minimize the length of the path after blocking one edge on shortest path".

# The solution is to find the minimal length of the shortest path after removing one edge on any shortest path.

# We can do the following:

# 1. Find all edges on shortest paths.
# 2. For each such edge, remove it and run BFS to find shortest path length.
# 3. Keep track of minimal such length.
# 4. If no path exists for some edge removal, answer is -1.

# But this is too slow.

# Alternative approach:

# Since the supporters can backtrack, the minimal number of edges traversed is:
# shortest + minimal extra cost to detour around the blocked edge.

# The minimal extra cost is 2 * (distance from the node before the blocked edge to the node after the blocked edge) - 1
# Because supporters must go back and take another path.

# The editorial solution is to find the minimal length of the shortest path after blocking one edge on shortest path.

# We can do the following:

# For each edge on shortest path, we consider the supporters must detour around it.
# The detour length is dist_start[u] + 1 + dist_end[v] or dist_start[v] + 1 + dist_end[u] (equals shortest)
# The supporters must go back to some node and take another path.

# The minimal number of edges supporters must traverse is:
# shortest + minimal length of the shortest alternative path avoiding the blocked edge.

# To find the minimal length of the shortest alternative path avoiding the blocked edge, we can:

# For each edge on shortest path:
#   Run BFS ignoring that edge.
#   Find shortest path length.
#   Keep track of minimal such length.

# Since this is expensive, we can do the following:

# Use a modified BFS that keeps track of the number of edges blocked.

# We can do a BFS with states (node, blocked_edge_used)
# blocked_edge_used = 0 or 1

# The supporters start at (1, 0)
# The police can block one edge at any time, so supporters must be prepared for any edge on shortest path to be blocked.

# The supporters want to minimize the number of edges traversed in worst case.

# The problem reduces to finding the shortest path from 1 to n in a graph where one edge on shortest path can be removed.

# We can model this as a shortest path in a graph with two layers:
# - Layer 0: no edge blocked yet
# - Layer 1: one edge blocked

# From layer 0, when traversing an edge on shortest path, police can block that edge, so supporters must detour in layer 1.

# So we do a BFS on states (node, blocked_used)
# blocked_used = 0 or 1

# Transitions:
# From (u, 0):
#   For each edge (u,v):
#     - If edge is on shortest path, police can block it now:
#       supporters must go to (v, 1) avoiding that edge (i.e., edge blocked)
#       So supporters cannot use that edge in layer 1.
#     - Or supporters can use that edge without police blocking it:
#       go to (v, 0)
# From (u, 1):
#   supporters cannot use the blocked edge
#   so only edges not blocked can be used.

# To implement this, we need to know which edges are on shortest paths.

# Let's implement this approach.

# First, mark edges on shortest paths.

on_shortest_path = set()
for u in range(1, n + 1):
    for v in graph[u]:
        if dist_start[u] + 1 + dist_end[v] == shortest or dist_start[v] + 1 + dist_end[u] == shortest:
            # Store edges as (min, max) to avoid duplicates
            on_shortest_path.add((min(u, v), max(u, v)))

# BFS with states (node, blocked_used)
# blocked_used = 0 or 1
# dist[node][blocked_used] = minimal edges traversed to reach node with blocked_used state

dist = [[-1, -1] for _ in range(n + 1)]
dist[1][0] = 0
q = deque()
q.append((1, 0))

while q:
    u, blocked_used = q.popleft()
    for v in graph[u]:
        edge = (min(u, v), max(u, v))
        if blocked_used == 0:
            # Police can block this edge now, so supporters can choose:
            # 1) Police blocks this edge now -> supporters must avoid it from now on (blocked_used=1)
            # supporters cannot traverse this edge in blocked_used=1 state, so here supporters must skip this edge
            # but police blocks it exactly once, so supporters must detour.

            # So supporters can:
            # a) Traverse edge without police blocking it now (blocked_used=0)
            if dist[v][0] == -1:
                dist[v][0] = dist[u][0] + 1
                q.append((v, 0))

            # b) Police blocks this edge now, supporters must detour (blocked_used=1)
            # supporters cannot traverse this edge in blocked_used=1 state, so supporters must skip this edge
            # So supporters do not traverse this edge now, but police blocks it.
            # So supporters remain at u but now blocked_used=1
            # We can model this by adding state (u,1) if not visited
            if dist[u][1] == -1:
                dist[u][1] = dist[u][0]
                q.append((u, 1))

        else:
            # blocked_used == 1, police already blocked one edge
            # supporters cannot traverse the blocked edge
            # So if edge is blocked edge, supporters cannot use it
            # But we don't know which edge is blocked, so we must assume supporters cannot use any edge on shortest path that police could have blocked.

            # Actually, police blocks exactly one edge on shortest path.
            # So supporters cannot use that edge in blocked_used=1 state.

            # So supporters can traverse edge only if edge is NOT on shortest path.

            if edge not in on_shortest_path:
                if dist[v][1] == -1:
                    dist[v][1] = dist[u][1] + 1
                    q.append((v, 1))

# The answer is minimal dist[n][0] or dist[n][1]
# dist[n][0] means supporters reach n without police blocking any edge (police can block only once, so if supporters reach n without police blocking, police wasted the block)
# dist[n][1] means supporters reach n after police blocked one edge.

ans = -1
if dist[n][0] != -1 and dist[n][1] != -1:
    ans = max(dist[n][0], dist[n][1])
elif dist[n][0] != -1:
    ans = dist[n][0]
elif dist[n][1] != -1:
    ans = dist[n][1]

print(ans)