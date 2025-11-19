def count_distinct_bracket_sequences(n, s):
    MOD = 998244353
    
    # dp[i][j] will store the number of distinct valid sequences that can be formed
    # from the substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # A single pair of brackets is a valid sequence
    for i in range(n):
        if s[i] == '(' and i + 1 < n and s[i + 1] == ')':
            dp[i][i + 1] = 1
    
    # Fill the dp table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the current substring can be a valid sequence
            if s[i] == '(' and s[j] == ')':
                dp[i][j] = (dp[i + 1][j - 1] + 1) % MOD
            
            # Combine results from different partitions
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k] * dp[k + 1][j]) % MOD
    
    # The result is the number of distinct valid sequences for the whole string
    return dp[0][n - 1]

# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(count_distinct_bracket_sequences(n, s))