import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS from start (1) to get dist1
dist1 = [-1] * (n + 1)
dist1[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for w in graph[u]:
        if dist1[w] == -1:
            dist1[w] = dist1[u] + 1
            q.append(w)

# BFS from end (n) to get distn
distn = [-1] * (n + 1)
distn[n] = 0
q = deque([n])
while q:
    u = q.popleft()
    for w in graph[u]:
        if distn[w] == -1:
            distn[w] = distn[u] + 1
            q.append(w)

if dist1[n] == -1:
    # No path from 1 to n
    print(-1)
    exit()

d = dist1[n]

# Count how many edges on shortest paths go through each node
# For each edge (u,v), if dist1[u] + 1 + distn[v] == d or dist1[v] + 1 + distn[u] == d,
# then this edge is on some shortest path.

# For each node, count how many shortest path edges are incident
count_on_sp = [0] * (n + 1)
for u in range(1, n + 1):
    for v in graph[u]:
        if dist1[u] + 1 + distn[v] == d:
            count_on_sp[u] += 1

# Find nodes on shortest path with only one shortest path edge incident
# These nodes are bottlenecks where police can block the only edge forward on shortest path
bottlenecks = [u for u in range(1, n + 1) if dist1[u] != -1 and distn[u] != -1 and count_on_sp[u] == 1]

if not bottlenecks:
    # Police cannot block any edge on shortest path to increase length
    print(d)
    exit()

# The police will block the edge leaving the bottleneck node on shortest path
# The supporters club will have to detour around that edge

# To find the minimal detour, we try blocking each such edge and find shortest path length with that edge blocked

# We only need to consider edges that are on shortest paths and are the unique shortest path edge from bottleneck nodes

# Collect edges to block
edges_to_block = set()
for u in bottlenecks:
    for v in graph[u]:
        if dist1[u] + 1 + distn[v] == d:
            edges_to_block.add((u, v))
            edges_to_block.add((v, u))  # undirected

# BFS function with one blocked edge
def bfs_blocked(blocked_edge):
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        if u == n:
            return dist[u]
        for w in graph[u]:
            if (u, w) == blocked_edge:
                continue
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                q.append(w)
    return -1

ans = -1
for edge in edges_to_block:
    length = bfs_blocked(edge)
    if length == -1:
        # Police can block supporters from reaching Porto
        print(-1)
        exit()
    if ans == -1 or length > ans:
        ans = length

print(ans)