N = int(input()) * 2
P = [i for i in range(N)]
for _ in range(N // 2):
  a, b = map(int,input().split())
  a -= 1
  b -= 1
  P[a] = b
  P[b] = a

inf = N + 2
from bisect import bisect_left
T = [inf] * N
ansr = [0] * N
for i in range(N-1, -1, -1):
  p = P[i]
  if i < p:
    j = bisect_left(T, p)
    T[j] = p
  ansr[i] = bisect_left(T, inf)

T = [inf] * N
ansl = [0] * N
for i in range(N):
  p = P[i]
  if i > p:
    j = bisect_left(T, -p)
    T[j] = -p
  ansl[i] = bisect_left(T, inf)

print(max(ansr[0], max(ansl[i] + ansr[i+1] for i in range(N-1))))