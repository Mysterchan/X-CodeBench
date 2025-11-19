import sys
lambda input : sys.stdin.readline
n = int(input())
dp = [1]*(1<<20)
arr = map(int,input().split())
dd = []
for x in arr:
    p = x>>10
    q = x&1023
    ans = x
    for d in range(1024):
        if p&d==d:
            ans = ans*dp[d<<10|q]%998244353
    dd.append(ans)
    for d in range(1024):
        if d&q==q:
            dp[p<<10|d] = dp[p<<10|d]*x%998244353
print(*dd,sep='\n')