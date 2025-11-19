import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i][j]: maximum score for polygon vertices from i to j (inclusive, modulo n)
    # We consider vertices in circular order, so indices wrap around modulo n.
    # We'll use a linearization trick by doubling the array to handle wrap-around easily.
    
    # Double the array to handle circular indexing
    a = a * 2
    dp = [[0]*(2*n) for _ in range(2*n)]
    
    # length is the length of the polygon segment considered
    for length in range(3, n+1):
        for i in range(0, 2*n - length + 1):
            j = i + length - 1
            # Try all possible k between i+1 and j-1 to form triangle (i,k,j)
            for k in range(i+1, j):
                val = dp[i][k] + dp[k][j] + a[i]*a[j]*a[k]
                if val > dp[i][j]:
                    dp[i][j] = val
    
    # The polygon is circular, so the answer is max over dp[i][i+n-1] for i in [0,n-1]
    ans = 0
    for i in range(n):
        if dp[i][i+n-1] > ans:
            ans = dp[i][i+n-1]
    print(ans)