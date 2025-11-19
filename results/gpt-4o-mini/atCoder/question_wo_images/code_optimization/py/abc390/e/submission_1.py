N, X = map(int, input().split())

F = [list(map(int, input().split())) for _ in range(N)]

# Separate foods by vitamin type
v1 = [(a, c) for v, a, c in F if v == 1]
v2 = [(a, c) for v, a, c in F if v == 2]
v3 = [(a, c) for v, a, c in F if v == 3]

# Function to compute the maximum vitamin intake for a given vitamin type
def dpv(V):
    dp = [0] + [-float('inf')] * X
    for a, c in V:
        for cal in range(X, c - 1, -1):
            dp[cal] = max(dp[cal], dp[cal - c] + a)
    return dp

dp1 = dpv(v1)
dp2 = dpv(v2)
dp3 = dpv(v3)

# Binary search to find the maximum minimum intake
def canAchieve(k):
    for cal1 in range(X + 1):
        if dp1[cal1] >= k:
            for cal2 in range(X + 1 - cal1):
                if dp2[cal2] >= k:
                    cal3_needed = k
                    cal3_max = X - cal1 - cal2
                    if cal3_max >= 0 and dp3[cal3_max] >= cal3_needed:
                        return True
    return False

low, high = 0, 10**9
while low < high:
    mid = (low + high + 1) // 2
    if canAchieve(mid):
        low = mid
    else:
        high = mid - 1

print(low)