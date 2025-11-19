import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # dp[i][j]: max score triangulating polygon vertices from i to j (inclusive, modulo n)
    # We use 0-based indexing internally
    dp = [[0]*(n) for __ in range(n)]

    # length from 2 to n-1 (since polygon with less than 3 vertices can't form triangle)
    for length in range(2, n):
        for i in range(n):
            j = (i + length) % n
            # We want to find max dp[i][j]
            # Try all k between i and j (mod n)
            # Because polygon is convex and vertices are in order, k must be strictly between i and j
            # To handle modulo indexing, we iterate k from i+1 to j-1 modulo n
            # We'll iterate linearly and use modulo to get k
            max_val = 0
            k = (i + 1) % n
            while k != j:
                left = dp[i][k]
                right = dp[k][j]
                # triangle formed by vertices i, k, j
                val = left + right + a[i]*a[k]*a[j]
                if val > max_val:
                    max_val = val
                k = (k + 1) % n
            dp[i][j] = max_val

    # The polygon is circular, so the answer is max over dp[i][(i+n-1)%n]
    # i.e. triangulating the polygon starting at i and ending at i-1 mod n
    ans = 0
    for i in range(n):
        j = (i + n - 1) % n
        if dp[i][j] > ans:
            ans = dp[i][j]
    print(ans)