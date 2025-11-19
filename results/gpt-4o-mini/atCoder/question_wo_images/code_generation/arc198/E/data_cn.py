def count_ways(N, M, S):
    MOD = 998244353
    target = 1 << N  # 2^N
    dp = [0] * (target + 1)
    dp[0] = 1  # There's one way to reach 0 (doing nothing)

    for s in S:
        for x in range(target, -1, -1):
            if dp[x] > 0:
                new_x = (x | s) + 1
                if new_x <= target:
                    dp[new_x] = (dp[new_x] + dp[x]) % MOD

    return dp[target]

# Read input
N, M = map(int, input().split())
S = list(map(int, input().split()))

# Calculate and print the result
result = count_ways(N, M, S)
print(result)