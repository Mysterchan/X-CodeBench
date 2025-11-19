n=int(input())
s=[]
t=[]
count=0
count90=1
count180=2
count270=3
for i in range(n):
    a=input().strip()
    s+=[list(a)]
for i in range(n):
    a=input().strip()
    t+=[list(a)]
for i in range(n):
    if s==t:
        break
    for j in range(n):
        if s[i][j]!=t[i][j]:
            count+=1
        if t[i][j]!=s[n-j-1][i]:
            count90+=1
        if t[i][j]!=s[n-i-1][n-j-1]:
            count180+=1
        if t[i][j]!=s[n-i-1][j]:
            count270+=1
print(min(count, count90,count180, count270))