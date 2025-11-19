from collections import defaultdict
from bisect import bisect_left

n=int(input())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

INF=1<<62
def lis(A,n):
  DP=[INF]*(n+1)
  for i in range(n):
    DP[bisect_left(DP,A[i])]=A[i]
  for i in range(n+1):
    if DP[i]==INF: break
  return i

D=defaultdict(list)
for c,p in zip(C,P): D[c]+=[p]

s=0
for k,P in D.items():
  l=len(P)
  s+=k*(l-lis(P,l))

print(s)