N=int(input())
W=list(map(int,input().split()))
I=[tuple(map(int,input().split())) for _ in range(N)]

INF=10**18
L=[INF for _ in range(2*N+2)]
for i in range(N):L[I[i][1]]=min(L[I[i][1]],W[i])
for i in range(1,2*N+2):L[i]=min(L[i],L[i-1])

R=[INF for _ in range(2*N+2)]
for i in range(N):R[I[i][0]]=min(R[I[i][0]],W[i])
for i in range(2*N+1)[::-1]:R[i]=min(R[i],R[i+1])

Q=int(input())
for _ in range(Q):
  s,t=map(int,input().split())
  s-=1;t-=1
  base=W[s]+W[t]
  ls,rs=I[s]
  lt,rt=I[t]

  if ls>lt or (ls==lt and rs<rt):
    ls,rs,lt,rt=lt,rt,ls,rs

  if rs<lt:
    print(base)

  elif rt<=rs:
    add=INF

    add=min(add,L[ls-1])

    add=min(add,R[rs+1])
    print(-1 if add==INF else base+add)

  else:
    add=INF

    add=min(add,L[ls-1])

    add=min(add,R[rt+1])

    add=min(add,R[rs+1]+L[lt-1])
    print(-1 if add==INF else base+add)