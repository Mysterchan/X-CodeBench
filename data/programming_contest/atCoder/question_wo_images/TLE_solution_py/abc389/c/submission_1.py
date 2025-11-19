Q = int(input())
N = [0, 0]
S = 0
m = 0
for q in range(Q):
  L = list(map(int, input().split()))
  if L[0] == 1:
    S += L[1]
    N += [S]
  elif L[0] == 2:
    N.pop(1)
    m = N[1]
  else:
    print(N[L[1]]-m)