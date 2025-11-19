def count_ways(N, L, R, A, B):
    MOD = 998244353
    max_C = sum(B)
    
    # dp[i][j] will store the number of ways to perform i operations with C = j
    dp = [[0] * (max_C + 1) for _ in range(2 * N + 1)]
    dp[0][0] = 1  # 1 way to perform 0 operations with C = 0
    
    for i in range(1, 2 * N + 1):
        for j in range(max_C + 1):
            if i % 2 == 1:  # Action 1
                if (i // 2) < N:  # We can only perform action 1 if we have not exhausted A
                    dp[i][j] = dp[i - 1][j]  # Not using action 1
                    if j >= A[i // 2]:  # If we can afford to reduce C
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - A[i // 2]]) % MOD
            else:  # Action 2
                if (i // 2) > 0:  # We can only perform action 2 if Q is not empty
                    for k in range(max_C + 1):
                        if j >= B[k]:  # If we can afford to add B[k] to C
                            dp[i][j] = (dp[i][j] + dp[i - 1][j - B[k]]) % MOD

    # Count the number of ways to have C in the range [L, R]
    result = 0
    for j in range(L, R + 1):
        result = (result + dp[2 * N][j]) % MOD

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

# Get the result and print it
result = count_ways(N, L, R, A, B)
print(result)