from heapq import heappush,heappop

N,M,X = map(int,input().split())

G = [[] for _ in range(600000)]

for i in range(M):
    u,v = map(int,input().split())
    G[u].append([v,1])
    G[u].append([u+300000,X])
    G[u+300000].append([u,X])

    G[v+300000].append([u+300000,1])
    G[v+300000].append([v,X])
    G[v].append([v+300000,X])

dist = [-1]*(600000+10)
visited = [False]*(600000+10)

Q = []
heappush(Q,(0,1))
dist[1] = 0

while len(Q)>0:
    a,b = heappop(Q)

    if visited[b]:
        continue

    visited[b] = True

    for c,d in G[b]:
        if dist[c] == -1 or dist[c] > dist[b]+d:
            dist[c] = dist[b]+d
            heappush(Q,(dist[c],c))

print(min(dist[N],dist[N+300000]))