from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**13

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def addEdge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def minCostFlow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N

        d0 = [INF]*N
        dist = [INF]*N

        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return -1

            for i in range(N):
                H[i] += dist[i]

            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res

H,W=map(int, input().split())
C=MinCostFlow(H*W+2)
A=[];su=0;c=0
for i in range(H):
  B=list(map(int, input().split()))
  su+=sum(B)
  c=min(c,min(B))
  A.append(B)

if c==0:
  print(su)
  exit()

big=10**12
for i in range(H):
  for j in range(W):
    c=i*W+j
    if (i+j)%2==0:
      C.addEdge(H*W,c,1,0)
    else:
      C.addEdge(c,H*W+1,1,0)
    if i!=H-1:
      if (i+j)%2==0:
        C.addEdge(c,c+W,1,big+A[i][j]+A[i+1][j])
      else:
        C.addEdge(c+W,c,1,big+A[i][j]+A[i+1][j])
    if j!=W-1:
      if (i+j)%2==0:
        C.addEdge(c,c+1,1,big+A[i][j]+A[i][j+1])
      else:
        C.addEdge(c+1,c,1,big+A[i][j]+A[i][j+1])

for i in range(H*W//2+1):
  c=C.minCostFlow(H*W,H*W+1,1)
  if c==-1:
    break
  p=c-big
  if p>0:
    break
  su-=p
print(su)