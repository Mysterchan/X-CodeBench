n,m=map(int,input().split())
s=[*input()[::-1]]
t=[*input()]
r=[]
for i in sorted(t)[::-1]:
    while s and s[-1]>=i:r+=s.pop(),
    if s:s.pop();r+=i,
if t[-1]not in r:r[-1]=t[-1]
print(*r,sep="")