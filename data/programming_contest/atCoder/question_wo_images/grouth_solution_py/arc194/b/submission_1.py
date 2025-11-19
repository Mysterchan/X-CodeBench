n=int(input())
P=list(map(int,input().split()))

_D=[0]*(n+1)
def add(i,x):
  while i<=n: _D[i]+=x; i+=i&-i
def sum(i):
  s=0
  while i>0: s+=_D[i]; i-=i&-i
  return s

s=0; c=0
for i in range(n):
  t=(sum(n)-sum(P[i]))
  s+=(2*i-t+1)*t//2
  add(P[i],1)
print(s)