import bisect
N,Q = map(int,input().split())
Hato = [[i,-1] for i in range(N+1)]
V = []
for k in range(Q):
  Qu = list(map(int,input().split()))
  V.append(Qu)
  if Qu[0] == 1:
    Hato[Qu[1]] = [Qu[2],k]
  elif Qu[0] == 2:
    continue
  else:
    nw = Hato[Qu[1]][0]
    t = Hato[Qu[1]][1]
    for i in range(t+1,k):
      if V[i][0] == 2:
        if nw == V[i][1]:
          nw = V[i][2]
        elif nw == V[i][2]:
          nw = V[i][1]
    Hato[Qu[1]] = [nw,k]
    print(Hato[Qu[1]][0])