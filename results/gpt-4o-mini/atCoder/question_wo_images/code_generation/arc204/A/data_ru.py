def count_ways(N, L, R, A, B):
    MOD = 998244353
    max_C = sum(B) + 1
    dp = [[0] * max_C for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for c in range(max_C):
            dp[i][c] = dp[i - 1][c]  # Action 1: do not take A[i-1]
            if c >= A[i - 1]:
                dp[i][c] = (dp[i][c] + dp[i - 1][c - A[i - 1]]) % MOD

        for c in range(max_C):
            if c + B[i - 1] < max_C:
                dp[i][c + B[i - 1]] = (dp[i][c + B[i - 1]] + dp[i][c]) % MOD

    result = 0
    for c in range(L, R + 1):
        result = (result + dp[N][c]) % MOD

    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
L = int(data[1])
R = int(data[2])
A = list(map(int, data[3:3 + N]))
B = list(map(int, data[3 + N:3 + 2 * N]))

# Calculate and print the result
print(count_ways(N, L, R, A, B))