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
        while i>0:
            if ((m+1)//i)*(i-1)<=c<=((m+1)//(i+1))*i:
                print(i)
                break
            i+=1
