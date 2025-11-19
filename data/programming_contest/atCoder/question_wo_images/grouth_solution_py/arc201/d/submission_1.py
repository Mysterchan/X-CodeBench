t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    A=[-int(x)%m for x in input().split()]
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    C=B[:]
    for b in B:
        C.append(b+m)
    bl=0
    br=m
    while bl<br:
        bm=(bl+br)//2
        j=0
        k=0
        l=-1e20
        r=1e20
        for i in range(n):
            while C[j]<A[i]:
                j+=1
            while k<2*n and C[k]<A[i]+bm:
                k+=1
            l=max(l,j-i)
            r=min(r,k-i)
        if l<r:
            br=bm
        else:
            bl=bm+1
    print(bl-1)