from collections import deque
N = int(input())
A = list(map(int,input().split()))
ans = 0
q = deque()
for i,v in enumerate(A[::-1]):
    if len(q) == 0:
        q.append(v)
        continue
    if q[0] >= 2* v:
        ans += 1
        q.popleft()
    else:
        q.append(v)
print(ans)