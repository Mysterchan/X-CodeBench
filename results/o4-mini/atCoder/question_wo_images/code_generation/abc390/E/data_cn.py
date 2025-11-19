import sys
import threading
def main():
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline
    N, X = map(int, input().split())
    # Separate items by vitamin category
    items = {1: [], 2: [], 3: []}
    for _ in range(N):
        v, a, c = map(int, input().split())
        items[v].append((c, a))

    # Knapsack DP for each category: dp_k[c] = max vitamin sum with <= c calories
    dp = {}
    for k in (1, 2, 3):
        dp_k = [0] * (X + 1)
        for cost, val in items[k]:
            # 0/1 knapsack transition
            for cal in range(X, cost - 1, -1):
                new = dp_k[cal - cost] + val
                if new > dp_k[cal]:
                    dp_k[cal] = new
        # Prefix-max to make dp_k non-decreasing
        for cal in range(1, X + 1):
            if dp_k[cal - 1] > dp_k[cal]:
                dp_k[cal] = dp_k[cal - 1]
        dp[k] = dp_k

    # Upper bound for answer is min obtainable with full budget in each category
    hi = min(dp[1][X], dp[2][X], dp[3][X])
    lo = 0

    # Binary search on K = minimal vitamin among three
    # Check if we can achieve at least K in each category within total calories <= X
    while lo < hi:
        mid = (lo + hi + 1) // 2
        # For each category, find minimal calories to reach at least mid vitamins
        # dp[k] is non-decreasing, so we can bisect
        c1 = bisect_left(dp[1], mid, 0, X + 1)
        c2 = bisect_left(dp[2], mid, 0, X + 1)
        c3 = bisect_left(dp[3], mid, 0, X + 1)
        # If any category cannot reach mid, bisect gives X+1
        if c1 + c2 + c3 <= X:
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    main()