def lcs_count(S, M):
    MOD = 998244353
    N = len(S)
    
    # dp[i][j] will store the number of strings of length M with LCS length j with S[0:i]
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    dp[0][0] = 1  # Base case: 1 way to have LCS of length 0 with empty string
    
    for i in range(1, M + 1):
        for j in range(N + 1):
            # If we don't use the current character
            dp[i][j] = dp[i - 1][j] * 26 % MOD
            
            if j > 0:
                # If we use the current character and it matches S[j-1]
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    # Now we need to count the number of strings with LCS length exactly k
    ans = [0] * (N + 1)
    
    for k in range(N + 1):
        ans[k] = (dp[M][k] * pow(26, M - k, MOD)) % MOD

    return ans

# Read input
N, M = map(int, input().split())
S = input().strip()

# Get the result
result = lcs_count(S, M)

# Print the result
print(' '.join(map(str, result)))