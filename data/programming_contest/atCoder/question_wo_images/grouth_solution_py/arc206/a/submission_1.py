from collections import defaultdict
N=int(input())
A=list(map(int,input().split()))
idx=[]
size=0
now=-1
for i in range(N):
    if A[i]!=now:
        idx.append([i-1,A[i-1],size])
        size=0
        now=A[i]
    size+=1
idx.append([N-1,A[-1],size])

idx.sort(reverse=True)
idx.pop(-1)
d=defaultdict(int)
renketu=defaultdict(int)

ans=1
for loop in idx:
    i,num,size=loop
    ans+=N-1-i-d[num]+renketu[num]
    d[num]+=size
    renketu[num]+1

print(ans)