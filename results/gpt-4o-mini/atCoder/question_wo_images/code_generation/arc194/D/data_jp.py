def count_valid_parentheses(n, s):
    MOD = 998244353

    # dp[i][j] will store the number of valid parentheses sequences
    # that can be formed from s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single pairs of parentheses
    for i in range(n):
        if s[i] == '(' and i + 1 < n and s[i + 1] == ')':
            dp[i][i + 1] = 1

    # Fill the dp table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            # Check if the current substring can be a valid parentheses sequence
            if s[i] == '(' and s[j] == ')':
                dp[i][j] = (dp[i + 1][j - 1] + 1) % MOD  # Count the valid sequence formed by enclosing
            # Add the counts of valid sequences formed by splitting the substring
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k] * dp[k + 1][j]) % MOD

    return dp[0][n - 1]

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_valid_parentheses(n, s))