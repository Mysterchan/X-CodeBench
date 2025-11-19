def count_valid_sequences(N, M, A):
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        max_value = max(A[i - 1], 1)
        for j in range(max_value, N + 1):
            dp[j] = (dp[j] + dp[j - max_value]) % MOD

    result = 0
    for j in range(1, N + 1):
        result = (result + dp[j] * M) % MOD
    
    return result

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(count_valid_sequences(N, M, A))