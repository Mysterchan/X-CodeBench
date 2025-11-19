import sys
input = sys.stdin.readline

MOD = 998244353
MAX_BIT = 20
MAX_MASK = 1 << MAX_BIT

N = int(input())
A = list(map(int, input().split()))

# dp[mask] = product of all A_i with value == mask (mod MOD)
dp = [1] * MAX_MASK
count = [0] * MAX_MASK  # count of elements with exact mask

for x in A:
    dp[x] = (dp[x] * x) % MOD
    count[x] += 1

# SOS DP for OR convolution:
# After this, dp[mask] = product of all A_i with value subset of mask (i.e. A_i | mask == mask)
# Because for OR, subset means A_i is subset of mask in bits (A_i | mask == mask)
for bit in range(MAX_BIT):
    for mask in range(MAX_MASK):
        if (mask & (1 << bit)) != 0:
            dp[mask] = (dp[mask] * dp[mask ^ (1 << bit)]) % MOD

# For each k, answer is dp[A_k]
for x in A:
    print(dp[x])