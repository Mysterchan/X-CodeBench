n=int(input())
for i in range(n):
    m=int(input())
    px,py,qx,qy=map(int,input().split())
    r=(px-qx)**2+(py-qy)**2
    l=list(map(int,input().split()))
    ma=sum(l)
    p=max(l)
    if (2*p-ma)**2<=r<=ma**2:
        print('YES')
    else:
        print('NO')
