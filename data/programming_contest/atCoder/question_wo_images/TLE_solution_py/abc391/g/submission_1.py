N,M=map(int, input().split())
SS=input()
S=[]
for s in SS:
  S.append(ord(s)-ord('a'))
mod=998244353

from collections import deque,defaultdict
D=defaultdict(int)
A=[0]*(N+1)
D[tuple(A)]=1

for i in range(M):
  DD=defaultdict(int)
  for d,c in D.items():

    for j in range(26):
      C=[0]*(N+1)
      for k in range(N):
        C[k+1]=max(C[k],d[k+1])
        if S[k]==j:
          C[k+1]=max(C[k+1],d[k]+1)
      CC=tuple(C)
      DD[CC]=(DD[CC]+c)%mod
  D=DD

ans=[0]*(N+1)
for d,c in D.items():
  ans[d[-1]]+=c
  ans[d[-1]]%=mod

print(*ans)