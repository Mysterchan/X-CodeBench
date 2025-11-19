import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS from 1 to get dist1 (distance from start)
dist1 = [-1] * (n + 1)
dist1[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for w in graph[u]:
        if dist1[w] == -1:
            dist1[w] = dist1[u] + 1
            q.append(w)

# BFS from n to get distn (distance from end)
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
    # no path from 1 to n
    print(-1)
    sys.exit()

d = dist1[n]

# Count edges on shortest paths
count = 0
for u in range(1, n + 1):
    for v in graph[u]:
        # To avoid double counting edges, only consider u < v
        if u < v:
            # Check if edge (u,v) lies on any shortest path from 1 to n
            # Condition: dist1[u] + 1 + distn[v] == d or dist1[v] + 1 + distn[u] == d
            if (dist1[u] != -1 and distn[v] != -1 and dist1[u] + 1 + distn[v] == d) or \
               (dist1[v] != -1 and distn[u] != -1 and dist1[v] + 1 + distn[u] == d):
                count += 1

if count == 0:
    # No edges on shortest path? Should not happen since graph connected and dist1[n] != -1
    print(-1)
else:
    # The minimal number of edges supporter must travel after police block one edge optimally
    # is original shortest path length + number of edges on shortest paths - 1
    # Explanation:
    # Police can block one edge on shortest path, forcing supporter to detour.
    # Supporter must travel at least d + (count - 1) edges.
    print(d + count - 1)