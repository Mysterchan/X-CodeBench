n,m=map(int,input().split())
ans=m*(m-1)//2
s=set()
for i in range(m):
    a,b=map(int,input().split())
    if (a+b)%n in s:
        ans-=1
    s.add((a+b)%n)
print(ans)