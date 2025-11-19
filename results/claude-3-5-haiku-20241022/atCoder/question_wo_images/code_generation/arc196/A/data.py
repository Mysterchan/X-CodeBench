def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        return
    
    # dp[i][j] = max score for removing elements from index i to j
    # considering the parity constraint
    dp = {}
    
    def rec(i, j):
        if i > j:
            return 0
        if i == j:
            return 0  # Single element, can't remove
        
        if (i, j) in dp:
            return dp[(i, j)]
        
        length = j - i + 1
        result = 0
        
        if length % 2 == 0:
            # Even length - must remove all
            # Try pairing i with each element, leaving the rest
            for k in range(i + 1, j + 1):
                # Pair a[i] with a[k]
                score = abs(a[i] - a[k])
                # Solve for [i+1, k-1] and [k+1, j]
                score += rec(i + 1, k - 1) + rec(k + 1, j)
                result = max(result, score)
        else:
            # Odd length - one element remains
            # Try leaving each element unpaired
            for k in range(i, j + 1):
                # Leave a[k] unpaired
                score = rec(i, k - 1) + rec(k + 1, j)
                result = max(result, score)
        
        dp[(i, j)] = result
        return result
    
    print(rec(0, n - 1))

solve()