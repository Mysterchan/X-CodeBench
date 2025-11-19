n,m=map(int,input().split())
from collections import defaultdict
edge=defaultdict(set)

uv=[]
parents=[i for i in range(n)]

members=defaultdict(set)
for i in range(n):
    members[i].add(i)
for j in range(m):
    u,v=map(lambda x:int(x)-1,input().split())
    edge[u].add(v)
    edge[v].add(u)
    uv.append((u,v))
q=int(input())
x=list(map(lambda x:int(x)-1,input().split()))
ans=m
for i in range(q):
    u,v=uv[x[i]]
    u_root=parents[u]
    while u_root!=parents[u_root]:
        u_root=parents[u_root]
    v_root=parents[v]
    while v_root!=parents[v_root]:
        v_root=parents[v_root]
    if u_root==v_root:
        print(ans)
        continue
    if len(members[u_root])<len(members[v_root]):
        u_root,v_root=v_root,u_root
    parents[u]=u_root
    parents[v]=u_root
    ans-=len(edge[u_root])+len(edge[v_root])

    for ele in edge[v_root]:
        if ele in members[u_root]:
            ans+=1
    for ele in members[v_root]:
        members[u_root].add(ele)
        edge[u_root].discard(ele)

    for ele in edge[v_root]:
        if not ele in members[u_root]:
            edge[u_root].add(ele)
    ans+=len(edge[u_root])
    print(ans)