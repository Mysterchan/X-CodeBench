N, X = map(int, input().split())

F = [list(map(int, input().split())) for _ in range(N)]

v1 = [f[1:] for f in F if f[0] == 1]
v2 = [f[1:] for f in F if f[0] == 2]
v3 = [f[1:] for f in F if f[0] == 3]

ub = 0
for f in F:
    ub += f[2]

inf = float("inf")
def dpv(V):
    dp = [-inf] * (ub+1)
    dp[0] = 0
    for a, c in V:
        ndp = [-inf] * (ub+1)

        for cal in range(ub+1):
            ndp[cal] = max(ndp[cal], dp[cal])
            if cal + c <= ub:
                ndp[cal+c] = max(ndp[cal+c], dp[cal] + a)
        dp = ndp

    for i in range(1, len(dp)):
        dp[i] = max(dp[i], dp[i-1])
    return dp

dp1 = dpv(v1)
dp2 = dpv(v2)
dp3 = dpv(v3)

from bisect import bisect_left

def judge(k):
    cal_1 = bisect_left(dp1, k)
    cal_2 = bisect_left(dp2, k)
    cal_3 = bisect_left(dp3, k)

    if cal_1 == ub + 1 or cal_2 == ub + 1 or cal_3 == ub + 1:
        return False

    return cal_1 + cal_2 + cal_3 <= X

ok = 0
ng = 10**9
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2

    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)