from collections import deque
n=int(input())
A=list(map(int,input().strip()))
votes=[deque() for _ in range(n+1)]
tmp=[]
for i in A:
    tmp.append(i)
    if len(tmp)==3:
        count=0
        for k in tmp:
            if k==0:
                count+=1
        votes[n-1].append(max(2-count,0))
        tmp=[]

idx=n-1
while idx!=0:
    while votes[idx]:
        tmp=[]
        for i in range(3):
            c=votes[idx].popleft()
            tmp.append(c)
        tmp.sort()
        votes[idx-1].append(tmp[1])
    idx-=1

zeroans=(votes[0].popleft())

votes=[deque() for _ in range(n+1)]
tmp=[]
for i in A:
    tmp.append(i)
    if len(tmp)==3:
        count=0
        for k in tmp:
            if k==1:
                count+=1
        votes[n-1].append(max(2-count,0))
        tmp=[]

idx=n-1
while idx!=0:
    while votes[idx]:
        tmp=[]
        for i in range(3):
            c=votes[idx].popleft()
            tmp.append(c)
        tmp.sort()
        votes[idx-1].append(tmp[1])
    idx-=1

oneans=(votes[0].popleft())
print(max(oneans,zeroans))