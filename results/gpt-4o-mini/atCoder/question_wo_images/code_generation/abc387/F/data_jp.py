def count_valid_sequences(N, M, A):
    MOD = 998244353
    # DP array to count the number of valid sequences ending with a certain value
    dp = [0] * (M + 1)
    dp[0] = 1  # base case: 1 way to have an empty sequence
    
    for i in range(1, N + 1):
        next_dp = [0] * (M + 1)
        for j in range(1, M + 1):
            for k in range(1, M + 1):
                if k <= j:
                    next_dp[j] = (next_dp[j] + dp[k]) % MOD
        dp = next_dp
    
    result = 0
    for i in range(1, M + 1):
        result = (result + dp[i]) % MOD
        
    return result

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))

# Output the result
print(count_valid_sequences(N, M, A))