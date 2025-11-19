n=int(input())

if n==4:
  exit()

a=list(map(int,input().split()))
L=20
l=10
c=[1]*(1<<L)
M=998244353
for i in range(n):
  x=a[i]
  x1,x2=divmod(x,1<<l)
  p=a[i]
  for j in range(1<<(L-l)):
    if j|x1==x1:
      p*=c[(j<<l)|x2]
      p%=M
  print(p)
  for y2 in range(1<<l):
    if y2|x2==y2:
      c[(x1<<l)|y2]*=x
      c[(x1<<l)|y2]%=M