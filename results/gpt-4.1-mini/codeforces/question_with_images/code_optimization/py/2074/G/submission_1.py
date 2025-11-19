import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i][j] = max score for polygon vertices from i to j (inclusive, modulo n)
    # We will use 0-based indexing internally
    dp = [[0]*n for _ in range(n)]
    
    # We consider polygons of length >= 3
    for length in range(3, n+1):
        for i in range(n):
            j = (i + length - 1) % n
            # Because polygon is circular, we handle indices carefully
            # We try all possible k between i and j (mod n)
            # To handle circular indexing, we map indices to linear order
            # We'll consider vertices in order i, i+1, ..., j (mod n)
            # So k runs from i+1 to j-1 (mod n)
            
            # To avoid complexity, we will "unwrap" the polygon by duplicating array
            # and use linear indices for dp calculation
            
    # To simplify circular indexing, we duplicate array and solve linear polygon of length n
    # Then answer is dp[0][n-1]
    
    a = a * 2
    dp = [[0]*(2*n) for _ in range(2*n)]
    
    for length in range(3, n+1):
        for i in range(0, 2*n - length + 1):
            j = i + length - 1
            best = 0
            for k in range(i+1, j):
                val = dp[i][k] + dp[k][j] + a[i]*a[k]*a[j]
                if val > best:
                    best = val
            dp[i][j] = best
    
    # The polygon is circular, so the answer is max over dp[i][i+n-1] for i in [0, n-1]
    ans = 0
    for i in range(n):
        if dp[i][i+n-1] > ans:
            ans = dp[i][i+n-1]
    print(ans)