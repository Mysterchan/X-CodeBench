import sys
from collections import deque

input = sys.stdin.readline
n, m, s, t = map(int, input().split())
s, t = s - 1, t - 1
g = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    g[u].append((v, i))
    g[v].append((u, i))
inf = 10**9
dist = [inf] * n
dist[s] = 0
q = deque()
q.append(s)
while q:
    x = q.popleft()
    for i, idx in g[x]:
        if dist[i] != inf:
            continue
        dist[i] = dist[x] + 1
        q.append(i)
visited = [False] * n
visited[t] = True
cnt = [0] * n
cnt[t] = 1
q.append(t)
ciritical_vertex = []
ciritical_path = [False] * m
while q:
    x = q.popleft()
    for i, idx in g[x]:
        if dist[i] + 1 != dist[x]:
            continue
        ciritical_path[idx] = True
        if i != s:
            ciritical_vertex.append(i)
        if not visited[i]:
            visited[i] = True
            q.append(i)
        cnt[i] = min(2, cnt[i] + cnt[x])
if cnt[s] == 2:
    print(2 * dist[t])
    exit()
d = [inf] * (2 * n)
d[s] = 0
q.append(s)
while q:
    xx = q.popleft()
    x = xx
    c = x >= n
    if c:
        x -= n
    for i, idx in g[x]:
        to = i
        if c or not ciritical_path[idx]:
            to += n
        if d[to] != inf:
            continue
        d[to] = d[xx] + 1
        q.append(to)
if d[t + n] == dist[t] + 1:
    print(2 * dist[t] + 1)
    exit()
for x in ciritical_vertex:
    if len(g[x]) >= 3:
        print(2 * dist[t] + 2)
        exit()
d2 = [inf] * n
for i in range(n):
    if len(g[i]) >= 3:
        d2[i] = 0
        q.append(i)
while q:
    x = q.popleft()
    for i, idx in g[x]:
        if d2[i] != inf:
            continue
        d2[i] = d2[x] + 1
        q.append(i)
ans = 2 * dist[t] + 4 * min(d2[s], d2[t]) + 4
gg = [[] for _ in range(n)]
for i in range(n):
    for x, idx in g[i]:
        if not ciritical_path[idx]:
            gg[i].append(x)
d3 = [inf] * n
d3[s] = 0
q.append(s)
while q:
    x = q.popleft()
    for i in gg[x]:
        if d3[i] != inf:
            continue
        d3[i] = d3[x] + 1
        q.append(i)
ans = min(ans, dist[t] + d3[t])
print(-1 if ans >= inf else ans)