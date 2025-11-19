def max_min_vitamins(N, X, products):
    # Create a DP table for the vitamins
    # dp[c] will store the maximum amounts of vitamins we can achieve with c calories
    dp = [[0] * 4 for _ in range(X + 1)]  # dp[c][v] for calories c and vitamin v (1-based index)
    
    for (v, a, c) in products:
        # We go backwards to avoid overwriting the results of the previous iteration
        for cal in range(X, c - 1, -1):
            dp[cal][v] = max(dp[cal][v], dp[cal - c][v] + a)

    # Now we need to determine the largest minimum vitamin amount we can get
    # Iterate over the possible minimum vitamin amount
    left, right = 0, 2 * 10**5  # The maximum possible value for any vitamin amount
    best_min = 0
    
    while left <= right:
        mid = (left + right) // 2
        # Check if we can achieve at least 'mid' of each vitamin
        possible = False
        
        for cal in range(X + 1):
            # Check if we can achieve at least 'mid' of all three vitamins
            if dp[cal][1] >= mid and dp[cal][2] >= mid and dp[cal][3] >= mid:
                possible = True
                break
        
        if possible:
            best_min = mid  # If we can achieve 'mid', try for better
            left = mid + 1
        else:
            right = mid - 1

    return best_min

import sys
input = sys.stdin.read

data = input().strip().split('\n')
N, X = map(int, data[0].split())
products = [tuple(map(int, line.split())) for line in data[1:]]

result = max_min_vitamins(N, X, products)
print(result)