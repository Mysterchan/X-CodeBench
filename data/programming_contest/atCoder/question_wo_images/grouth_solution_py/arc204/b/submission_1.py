N, K = map(int,input().split())
P = list(map(int,input().split()))
P = [p - 1 for p in P]

def derive(A, C):
  N = len(A)

  clr = [[] for _ in range(C)]
  for i, a in enumerate(A):
    clr[a].append(i)

  DP = [[0 for _ in range(N)] for _ in range(N)]
  for l in range(N - 2, -1, -1):
    DP_l = DP[l]
    DP_l1 = DP[l+1]
    for r in range(l + 1, N):

      tmp = max(DP_l[r-1], DP_l1[r])

      c = A[l]
      for v in clr[c]:
        if l < v <= r:

          tmp = max(tmp, DP_l1[v-1] + 1 + DP[v][r])

      DP_l[r] = tmp

  return DP[0][-1]

vis = [False] * (N * K)
ans = 0
for i in range(N * K):
  if vis[i]: continue
  V = [i % N]
  j = i
  vis[i] = True
  while not vis[P[j]]:
    j = P[j]
    V.append(j % N)
    vis[j] = True

  ans += derive(V, N)
print(ans)