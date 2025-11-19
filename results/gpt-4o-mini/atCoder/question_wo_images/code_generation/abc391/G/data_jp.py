def count_lcs(S, M, N):
    MOD = 998244353
    # dp[k][j] will store the number of strings of length j with LCS of length k with S
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: 1 way to have LCS of length 0 with any string of length j (using empty subsequence)
    for j in range(M + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for k in range(1, N + 1):
        for j in range(1, M + 1):
            # If we take the k-th character of S
            dp[k][j] = dp[k][j - 1] * 25 % MOD  # 25 choices (not matching S[k-1])
            if j > 0:
                dp[k][j] = (dp[k][j] + dp[k - 1][j - 1]) % MOD  # 1 choice (matching S[k-1])
    
    # Calculate the results for each k
    results = []
    for k in range(N + 1):
        results.append(dp[k][M])
    
    return results

# Read input
N, M = map(int, input().split())
S = input().strip()

# Get the results
results = count_lcs(S, M, N)

# Print the results
print(" ".join(map(str, results)))