import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MOD = 998244353

# Precompute prefix sums
A_sum = [0] * (N + 1)
B_sum = [0] * (N + 1)
for i in range(N):
    A_sum[i + 1] = A_sum[i] + A[i]
    B_sum[i + 1] = B_sum[i] + B[i]

# Adjust L and R according to problem statement
L += A_sum[N] - B_sum[N]
R += A_sum[N] - B_sum[N]

# dp[j]: number of ways with j elements currently in Q
# We only need to track if any valid sequence has been found (flag)
# We'll keep two arrays: dp0 and dp1
# dp0[j]: number of ways with j elements in Q and no valid C found yet
# dp1[j]: number of ways with j elements in Q and at least one valid C found
dp0 = [0] * (N + 1)
dp1 = [0] * (N + 1)

# Initial state: no elements pushed, Q empty, C=0
# Check if 0 in [L,R]
if L <= 0 <= R:
    dp1[0] = 1
else:
    dp0[0] = 1

for i in range(N + 1):
    ndp0 = [0] * (N + 1)
    ndp1 = [0] * (N + 1)
    for j in range(i + 1):
        if dp0[j] == 0 and dp1[j] == 0:
            continue
        # Action 1: push i+1 if i < N
        if i < N:
            c = A_sum[i + 1] - B_sum[j]
            valid = L <= c <= R
            # From dp0[j]
            if dp0[j]:
                if valid:
                    ndp1[j] = (ndp1[j] + dp0[j]) % MOD
                else:
                    ndp0[j] = (ndp0[j] + dp0[j]) % MOD
            # From dp1[j]
            if dp1[j]:
                ndp1[j] = (ndp1[j] + dp1[j]) % MOD
        # Action 2: pop from Q if j < i
        if j < i:
            c = A_sum[i] - B_sum[j + 1]
            valid = L <= c <= R
            # From dp0[j]
            if dp0[j]:
                if valid:
                    ndp1[j + 1] = (ndp1[j + 1] + dp0[j]) % MOD
                else:
                    ndp0[j + 1] = (ndp0[j + 1] + dp0[j]) % MOD
            # From dp1[j]
            if dp1[j]:
                ndp1[j + 1] = (ndp1[j + 1] + dp1[j]) % MOD
    dp0, dp1 = ndp0, ndp1

print(dp1[N] % MOD)