def count_ways(N, M, S):
    MOD = 998244353
    target = 1 << N  # 2^N
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to start with x = 0

    for s in S:
        for x in range(target, -1, -1):
            if dp[x] > 0:
                new_x = (x | s) + 1
                if new_x <= target:
                    dp[new_x] = (dp[new_x] + dp[x]) % MOD

    return dp[target]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
S = list(map(int, data[2:]))

# Calculate and print the result
result = count_ways(N, M, S)
print(result)