t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    if k%n==0:
        c=k//n
    else:
        c=k//n+1
    i=1
    if m==c:
        print(c)
    elif m==c+1:
        print(m//2)
    else:
        k=m-c
        if c%(k+1)==0:
            print(c//(k+1))
        else:
            print(c//(k+1)+1)
