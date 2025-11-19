M=998244353
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    ans=0
    e=[]
    o=[]
    se=0
    so=0
    ed=0
    od=0
    ans=0
    neo=0
    for ai in a:
        for (a,d) in ((e,ed),(o,od)):
            if len(a)>0 and a[-1][0]==-d:
                a[-1]=(-d,a[-1][1]+1)
            else:
                a.append((-d,1))
        se-=ed
        so-=od
        od+=ai
        ed-=ai
        neo+=1
        nz=0
        while len(e)>0 and e[-1][0]+ed<0:
            se-=(e[-1][0]+ed)*e[-1][1]
            nz+=e[-1][1]
            e.pop()
        if nz>0:
            e.append((-ed,nz))
        ans+=se+so+(ed+od)*neo
        (e,se,ed),(o,so,od)=(o,so,od),(e,se,ed)
    print(ans%M)

