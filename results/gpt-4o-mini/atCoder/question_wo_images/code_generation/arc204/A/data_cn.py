def count_ways(N, L, R, A, B):
    MOD = 998244353
    max_sum_B = sum(B)
    
    # dp[i][j] means the number of ways to perform operations with first i elements of A and j as the current C value
    dp = [[0] * (max_sum_B + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Starting with 0 elements and C = 0
    
    for i in range(N):
        for j in range(max_sum_B + 1):
            if dp[i][j] == 0:
                continue
            
            # Action 1: Add i+1 to Q
            new_C = max(0, j - A[i])
            dp[i + 1][new_C] = (dp[i + 1][new_C] + dp[i][j]) % MOD
            
            # Action 2: Remove from Q (if we have added something before)
            if i > 0:  # We can only perform action 2 if we have at least one element in Q
                new_C = j + B[i - 1]
                if new_C <= max_sum_B:
                    dp[i + 1][new_C] = (dp[i + 1][new_C] + dp[i][j]) % MOD
    
    # Count the number of ways where C is between L and R
    result = 0
    for c in range(L, R + 1):
        result = (result + dp[N][c]) % MOD
    
    return result

# Read input
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Get the result and print it
print(count_ways(N, L, R, A, B))