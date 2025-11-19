import sys

MOD = 998244353

def solve(n, m, a):
    # Adjust for zero-based indexing
    a = [x - 1 for x in a]
    
    # Create a list to count the number of inputs pointing to each index
    count = [0] * n
    for x in a:
        count[x] += 1

    dp = [0] * (m + 1)
    dp[0] = 1  # Base case: There's one way to create a valid sequence of length 0

    for i in range(n):
        new_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            new_dp[j] = dp[j]  # Start by inheriting the current dp state
            # Each position i can take values from 1 to j
            for k in range(1, j + 1):
                new_dp[j] = (new_dp[j] + dp[k] * count[i]) % MOD
        dp = new_dp

    # The answer is the total number of ways to fill all positions with values from 1 to M
    return dp[m]

# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))