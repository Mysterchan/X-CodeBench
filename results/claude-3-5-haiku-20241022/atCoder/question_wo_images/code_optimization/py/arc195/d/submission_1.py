t = int(input())

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    # Count initial segments (groups of consecutive equal elements)
    segments = 1
    for i in range(1, n):
        if A[i] != A[i-1]:
            segments += 1
    
    # DP approach: dp[i] = minimum operations to clear first i elements
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    i = 0
    while i < n:
        if dp[i] == float('inf'):
            i += 1
            continue
            
        # Find the longest prefix of equal elements starting at i
        j = i
        while j < n and A[j] == A[i]:
            j += 1
        
        # Option 1: Delete this group directly
        dp[j] = min(dp[j], dp[i] + 1)
        
        # Option 2: Try to extend by swapping
        # Look for next occurrence of A[i]
        for k in range(j, n):
            if A[k] == A[i]:
                # Calculate swaps needed to bring A[k] next to position j-1
                swaps = k - j
                # New position would be at k+1 (after moving A[k] forward)
                # We can delete from i to k
                ops = dp[i] + swaps + 1
                dp[k+1] = min(dp[k+1], ops)
        
        i += 1
    
    return dp[n]

for _ in range(t):
    print(solve())