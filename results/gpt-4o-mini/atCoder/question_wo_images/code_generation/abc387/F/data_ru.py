def count_sequences(N, M, A):
    MOD = 998244353
    dp = [0] * (M + 1)
    dp[0] = 1  # Base case: 1 way to have an empty sequence

    # Generate x possibilities for each i in A
    for i in range(1, N + 1):
        new_dp = [0] * (M + 1)
        max_xi = dp[:]  # Copy the previous dp state for use in the current state

        # For every possible value of x_i from 1 to M
        for x_i in range(1, M + 1):
            # We want to sum up values from max_xi[1] to max_xi[x_i]
            # Find limit based on A[i-1] because those are the indices in A
            limit = A[i - 1]  # A is 0-indexed in Python
            for j in range(1, min(x_i, limit) + 1):
                new_dp[x_i] = (new_dp[x_i] + max_xi[j]) % MOD

        dp = new_dp

    # The total valid sequences are the total number of sequences of length N
    return sum(dp) % MOD

# Input reading and function calling
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(count_sequences(N, M, A))