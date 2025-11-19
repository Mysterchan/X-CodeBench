n = int(input())
a = list(map(int, input().split()))

# dp[i][j] = max sum after processing first i elements with j elements in S
# We need j <= i (can't have more elements than we've seen)
INF = float('-inf')
dp = [[INF] * (n + 1) for _ in range(n + 1)]

# Initially, S is empty
dp[0][0] = 0

for i in range(n):
    for j in range(i + 1):
        if dp[i][j] == INF:
            continue
        
        # Option 1: Append a[i] to S
        # After this operation, we have j+1 elements
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i])
        
        # Option 2: Delete last element (only if j > 0)
        if j > 0:
            # After deletion, we have j-1 elements
            # But we need to track what was deleted
            # Actually, if we delete, the sum doesn't change from the perspective
            # of what we're tracking - we just have fewer elements
            # Wait, this approach won't work because we don't track individual elements
            pass

# Let me reconsider: we need to track the actual sum, not just count