n=int(input())
a=list(map(int, input().split()))
ans=True
for i in range(1,n-1):
    if a[i]*a[i]!=a[i-1]*a[i+1]:
        ans=False
        break
if ans:
    print("Yes")
else:
    print("No")