def f(a,b):
    if b==0:
        return 1
    if b%2==1:
        return a*f(a,b//2)*f(a,b//2)
    return f(a,b//2)*f(a,b//2)

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=min(n,m)-1
    print(f(2,a))