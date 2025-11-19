N,M = map(int, input().split())
W = list(map(int, input().split()))
edges = []
for i in range(M):
    a,b = map(int, input().split())
    a-=1;b-=1
    edges.append((a,b))
    edges.append((b,a))
inf = 10 ** 18
dp = [inf]*N
dp[0] = 0
for i in reversed(range(1,N)):
    ndp = [inf]*N
    ndp[0] = 0
    for u,v in edges:
        ndp[v] = min(ndp[v],dp[u]+W[u]*i)
    dp = ndp
for i in dp:
    print(i)