W,H,L,R,D,U=map(int,input().split())
result=0
u=[1]*(3*10**6)
u2=[1]*(3*10**6)
mod=998244353
for i in range(1,3*10**6):
  u[i]=u[i-1]*i
  u[i]%=mod
u2[-1]=pow(u[-1],-1,mod)
for i in range(3*10**6-2,0,-1):
  u2[i]=u2[i+1]*(i+1)
  u2[i]%=mod
def ncm(x,y):
  if x<0 or y<0 or y>x:
    return 0
  ans=u[x]*u2[y]
  ans%=mod
  ans*=u2[x-y]
  ans%=mod
  return ans
def g(a,b):
  if a<0 or b<0:
    return 0
  ans=ncm(a+b+4,a+2)-a-b-4-(a+1)*(b+1)
  return ans
def f(a,b):
  if a<0 or b<0:
    return 0
  ans=ncm(a+b+2,a+1)-1
  return ans
result=0
a,b=D-1,W
result+=g(a,b)
result%=mod
a,b=H-D,W-(R+1)
result+=g(a,b)
result%=mod
for pos in range(R+1,W+1):
  a,b=D-1,pos
  ans0=f(a,b)
  ans1=f(H-D,W-pos)
  result+=ans0*ans1
  result%=mod
a,b=H,L-1
result+=g(a,b)
result%=mod
a,b=H-(U+1),W-L
result+=g(a,b)
result%=mod
for pos in range(U+1,H+1):
  a,b=pos,L-1
  ans0=f(a,b)
  ans1=f(H-pos,W-L)
  result+=ans0*ans1
  result%=mod
a,b=D-1,L-1
result-=g(a,b)
a,b=H-(U+1),W-(R+1)
result-=g(a,b)
result%=mod
print(result)