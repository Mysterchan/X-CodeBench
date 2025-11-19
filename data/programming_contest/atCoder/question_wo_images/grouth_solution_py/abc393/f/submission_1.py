from bisect import bisect_left, bisect_right
N,Q = map(int,input().split())
A = list(map(int,input().split()))

q = []
for i in range(N):
    q.append((i+1,A[i],-1))

for i in range(Q):
    R,X = map(int,input().split())
    q.append((R,X,i))

q.sort()
INF = 10**18
LIS = [INF]*N

ans = [None] * Q
for i in range(N+Q):
    r,x,t = q[i]
    if t < 0:
        idx = bisect_left(LIS, x)
        LIS[idx] = x

    else:
        idx = bisect_right(LIS, x)
        ans[t] = idx

print(*ans,sep="\n")