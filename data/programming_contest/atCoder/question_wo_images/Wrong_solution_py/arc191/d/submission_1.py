n,m,S,T=map(int,input().split())
S-=1
T-=1
e=[[] for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  e[a]+=[(b,i)]
  e[b]+=[(a,i)]
X=10**8
v=[X]*n
q=[S]
v[S]=0
for s in q:
  for t,i in e[s]:
    if v[t]==X:
      v[t]=v[s]+1
      q+=[t]
L=v[T]
p=T
o=[T]
u=[0]*m
while p!=S:
  for np,i in e[p]:
    if v[np]==v[p]-1:
      u[i]=1
      p=np
      o+=[p]
      break
o=o[1:len(o)-1]
ne=[[] for i in range(n*2)]
for s in range(n):
  for t,i in e[s]:
    if u[i]:
      ne[s]+=[t]
      ne[n+s]+=[n+t]
    else:
      ne[s]+=[n+t]
      ne[n+s]+=[n+t]
v=[X]*n*2
q=[S]
v[S]=0
for s in q:
  for t in ne[s]:
    if v[t]==X:
      v[t]=v[s]+1
      q+=[t]
if v[T]==L and v[n+T]<=L+1:
  print(v[T]+v[n+T])
  exit()
for p in o:
  if len(e[p])>=3:
    print(L*2+2)
    exit()
ne=[[] for i in range(n)]
for s in range(n):
  for t,i in e[s]:
    if u[i]==0:
      ne[s]+=[t]
e=ne
a=X
v=[X]*n
v[S]=0
q=[S]
for s in q:
  for t in e[s]:
    if v[t]==X:
      v[t]=v[s]+1
      q+=[t]
a=min(a,L+v[T])
v=[X]*n
v[S]=0
v[T]=0
q=[S,T]
for s in q:
  if len(e[s])>=3:
    a=min(a,L*2+(v[s]+1)*4)
  for t in e[s]:
    if v[t]==X:
      v[t]=v[s]+1
      q+=[t]
print(a if a<X else -1)