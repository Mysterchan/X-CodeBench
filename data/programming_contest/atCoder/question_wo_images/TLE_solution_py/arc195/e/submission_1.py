N,Q=map(int,input().split())
A=list(map(int,input().split()))
u=[1]*(N+1)
mod=998244353
u2=[1]*(N+1)
for i in range(1,N+1):
  u[i]=u[i-1]*i
  u[i]%=mod
  u2[i]=pow(u[i],-1,mod)
v=[0]*(N+1)
for x in range(2,N):
  w=x*(x+1)
  w%=mod
  p=pow(w,-1,mod)
  p*=2*(x-1)
  p%=mod
  v[x]=p*A[x-2]
  v[x]%=mod
  v[x]+=v[x-1]
  v[x]%=mod
for _ in range(Q):
  a,b=map(int,input().split())
  result=0
  z=max(a,b)
  for x in range(a,z+1):
    if x==b:
      result+=A[x-2]
      result%=mod
    elif x>a:
      result+=pow(x,-1,mod)*A[x-2]
      result%=mod
    elif x==a:
      p=(x-1)*pow(x,-1,mod)
      p%=mod
      result+=p*A[x-2]
      result%=mod
  result+=v[a-1]
  result%=mod
  result*=u[N-1]
  result%=mod
  print(result)