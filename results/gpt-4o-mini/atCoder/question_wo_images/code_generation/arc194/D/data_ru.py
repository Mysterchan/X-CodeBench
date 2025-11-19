def count_distinct_bracket_sequences(n, s):
    MOD = 998244353

    # dp[i][j] will store the number of distinct valid sequences that can be formed
    # from the substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single pairs of brackets
    for i in range(n):
        if s[i] == '(' and i + 1 < n and s[i + 1] == ')':
            dp[i][i + 1] = 1

    # Fill the dp table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == '(' and s[j] == ')':
                # If the outer brackets are valid, we can consider the inner part
                dp[i][j] = (dp[i + 1][j - 1] + 1) % MOD  # +1 for the current valid pair
            # Now consider splitting the sequence into two parts
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k] * dp[k + 1][j]) % MOD

    return dp[0][n - 1]

# Read input
n = int(input().strip())
s = input().strip()

# Get the result and print it
result = count_distinct_bracket_sequences(n, s)
print(result)