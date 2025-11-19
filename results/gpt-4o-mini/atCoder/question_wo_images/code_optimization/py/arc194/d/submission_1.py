MOD = 998244353

def count_distinct_sequences(N, S):
    # To keep track of the counts of valid configurations
    dp = [0] * (N // 2 + 1)
    dp[0] = 1  # There's one valid way to create an empty configuration

    for i in range(1, N // 2 + 1):
        for j in range(i):
            dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD

    # The result corresponds to how many different configurations can be created
    return dp[N // 2]

N = int(input().strip())
S = input().strip()

print(count_distinct_sequences(N, S))