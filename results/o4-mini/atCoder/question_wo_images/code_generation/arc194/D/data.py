def count_distinct_parenthesis_sequences(N, S):
    MOD = 998244353
    
    # dp[i][j] will store the number of distinct valid parenthesis sequences
    # that can be formed from the substring S[i:j+1]
    dp = [[0] * N for _ in range(N)]
    
    # Base case: single pairs of parentheses
    for i in range(N):
        if S[i] == '(' and i + 1 < N and S[i + 1] == ')':
            dp[i][i + 1] = 1
    
    # Fill the dp table
    for length in range(2, N + 1):  # length of the substring
        for i in range(N - length + 1):
            j = i + length - 1
            
            # Check if the current substring can be a valid sequence
            if S[i] == '(' and S[j] == ')':
                dp[i][j] = (dp[i + 1][j - 1] + 1) % MOD
            
            # Combine results from different partitions
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k] * dp[k + 1][j]) % MOD
    
    # The result is the number of distinct sequences for the whole string
    return dp[0][N - 1]

# Read input
N = int(input().strip())
S = input().strip()

# Output the result
print(count_distinct_parenthesis_sequences(N, S))