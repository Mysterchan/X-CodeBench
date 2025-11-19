H,W=map(int,input().split())
if H%2==0:
  print(0)
  exit()
mod=998244353
u=[1]*10**6
u2=[1]*10**6
for i in range(1,10**6):
  u[i]=u[i-1]*i
  u[i]%=mod
  u2[i]=pow(u[i],-1,mod)
def ncm(x,y):
  if y<0 or y>x:
    return 0
  ans=u[x]*u2[y]
  ans%=mod
  ans*=u2[x-y]
  ans%=mod
  return ans
result=0
from math import gcd
for a in range(1,H):
  d=a-(H-a)
  d=abs(d)
  if d==0:
    continue
  p=gcd(W,d)
  if p==1:
    result+=ncm(H,a)
    result%=mod
if W%2==0:
  result=0
  for a in range(1,2*H):
    d=a-(2*H-a)
    d=abs(d)
    if d==0:
      continue
    p=gcd(W,d)
    if p==2:
      result+=ncm(2*H,a)
      result%=mod
print(result)