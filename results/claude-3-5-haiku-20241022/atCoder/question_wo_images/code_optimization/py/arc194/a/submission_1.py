#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

# dp[j] represents the maximum sum with stack size j after processing current elements
# We only need current and previous state
INF = float('-inf')
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(n):
    new_dp = [INF] * (n + 1)
    
    # For each possible current stack size
    for j in range(n + 1):
        if dp[j] == INF:
            continue
        
        # Option 1: Add current element (if we have space)
        if j < n:
            new_dp[j + 1] = max(new_dp[j + 1], dp[j] + a[i])
        
        # Option 2: Remove last element (if stack is not empty)
        if j > 0:
            new_dp[j - 1] = max(new_dp[j - 1], dp[j])
    
    dp = new_dp

# Find maximum sum across all valid stack sizes
# Note: stack cannot be empty at the end if we must process all elements and start empty
ans = max(dp)
print(ans)