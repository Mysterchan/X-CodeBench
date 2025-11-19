import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    adj=[[]for _ in range(n)]
    [adj[u-1].append(v-1) or adj[v-1].append(u-1) for _ in range(n-1) for u,v in [map(int,input().split())]]
    r=[0]*n
    s=[(0,-1,0,0)]
    while s:
        u,p,pp,pn=s.pop()
        r[u]=a[u]+pn
        cp=max(0,a[u]+pn)
        cn=max(0,-a[u]+pp)
        s+=[(v,u,cp,cn) for v in adj[u] if v!=p]
    print(*r)
