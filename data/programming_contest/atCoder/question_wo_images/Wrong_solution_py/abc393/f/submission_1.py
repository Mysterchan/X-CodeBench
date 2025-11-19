n,q = map(int,input().split())
a = list(map(int,input().split()))
dp =  [10**10] * n
qu = [list(map(int,input().split())) for _ in range(q)]
import bisect
kai = 0
d = {}
for A,B in qu:
    d[(A,B)] = kai
    kai += 1
qu.sort()
ans = [0] * q
kai = 0
for i,A in enumerate(a):
    k = bisect.bisect_left(dp,A)
    dp[k] = A
    while qu[kai][0] == i+1:
        ans[d[(qu[kai][0],qu[kai][1])]] = bisect.bisect(dp,qu[kai][1])
        kai += 1
        if kai == q: break
    if kai == q: break
for A in ans:
    print(A)