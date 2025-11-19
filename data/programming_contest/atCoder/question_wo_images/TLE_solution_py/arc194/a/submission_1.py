#!/usr/bin/env python3
from collections import defaultdict,deque
n = int(input())
a_n = list(map(int,input().split()))
que = deque()
que.append(([(0,1)],1,0))
candidate = []
ans = float('-inf')
while que :
    stack,l,pos = que.popleft()
    if pos==n-1 :

        tmp = 0
        for i,_ in stack :
            tmp += a_n[i]
        ans = max(ans,tmp)
        continue
    que.append((stack+[(pos+1,1)],l+1,pos+1))
    if l>=1 :
        stack.pop()
        que.append((stack,l-1,pos+1))

print(ans)