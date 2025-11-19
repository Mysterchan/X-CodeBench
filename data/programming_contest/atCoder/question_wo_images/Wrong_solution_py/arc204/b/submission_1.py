N, K = map(int,input().split())
P = list(map(int,input().split()))
P = [p - 1 for p in P]

def derive(A, C):
  N = len(A)
  if N == 1:
    return 0

  clr = [[] for _ in range(C)]
  for i, a in enumerate(A):
    clr[a].append(i)

  DP = [[0 for _ in range(N)] for _ in range(N)]
  for l in range(N - 2, -1, -1):
    for r in range(l + 1, N):
      tmp = max(DP[l][r-1], DP[l+1][r])
      if A[l] == A[r]:
        c = A[l]
        for v in clr[c]:
          if l < v <= r:
            tmp = max(tmp, DP[l+1][v-1] + 1 + DP[v][r])

      DP[l][r] = tmp

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