N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Find positions that need to be flipped
diff = []
for i in range(N):
    if A[i] != B[i]:
        diff.append(i)

if not diff:
    print(0)
else:
    m = len(diff)
    INF = float('inf')
    
    # dp[mask] = minimum cost to flip the positions indicated by mask
    dp = [INF] * (1 << m)
    dp[0] = 0
    
    for mask in range(1 << m):
        if dp[mask] == INF:
            continue
        
        # Current state of A after flips indicated by mask
        curr_A = A[:]
        for j in range(m):
            if mask & (1 << j):
                curr_A[diff[j]] = 1 - curr_A[diff[j]]
        
        # Try flipping each remaining position
        for j in range(m):
            if not (mask & (1 << j)):
                # Flip position diff[j]
                new_mask = mask | (1 << j)
                curr_A[diff[j]] = 1 - curr_A[diff[j]]
                
                # Calculate cost
                cost = sum(curr_A[k] * C[k] for k in range(N))
                
                dp[new_mask] = min(dp[new_mask], dp[mask] + cost)
                
                # Restore
                curr_A[diff[j]] = 1 - curr_A[diff[j]]
    
    print(dp[(1 << m) - 1])