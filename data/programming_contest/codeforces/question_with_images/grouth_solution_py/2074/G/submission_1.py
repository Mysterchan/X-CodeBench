def f(l, r):
    if l+2 > r: return 0
    if dp[l][r] != -1: return dp[l][r]
    ret = 0
    for m in range(l+1, r):
        ret = max(ret, a[l]*a[m]*a[r] + f(l+1, m-1) + f(m+1, r-1))
    for m in range(l, r):
        ret = max(ret, f(l, m) + f(m+1, r))
    dp[l][r] = ret
    return ret

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[-1]*n for _ in range(n)]
    print(f(0, n-1))
