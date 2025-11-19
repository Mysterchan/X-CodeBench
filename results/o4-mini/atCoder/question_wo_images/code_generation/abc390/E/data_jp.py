import sys
import threading

def main():
    import sys
    from bisect import bisect_left

    input = sys.stdin.readline
    N, X = map(int, input().split())
    items = {1: [], 2: [], 3: []}
    for _ in range(N):
        v, a, c = map(int, input().split())
        items[v].append((a, c))

    # For each vitamin type v, dp_v[c] = max total A we can get with cost exactly c
    # Then we do prefix-max so dp_v is non-decreasing in c.
    dp = {}
    for v in (1, 2, 3):
        dpv = [0] * (X+1)
        for a, cost in items[v]:
            # 0/1 knapsack step
            for c in range(X, cost-1, -1):
                val = dpv[c-cost] + a
                if val > dpv[c]:
                    dpv[c] = val
        # make it prefix-max so dpv is non-decreasing
        for c in range(1, X+1):
            if dpv[c-1] > dpv[c]:
                dpv[c] = dpv[c-1]
        dp[v] = dpv

    # The maximum possible t is bounded by the minimal total we can get among the 3 types
    max_t = min(dp[1][X], dp[2][X], dp[3][X])

    # Check if we can achieve at least t of each vitamin within calorie X
    def can(t):
        total_cost = 0
        for v in (1, 2, 3):
            # find minimal c such that dp[v][c] >= t
            c = bisect_left(dp[v], t)
            if c > X:
                return False
            total_cost += c
            if total_cost > X:
                return False
        return total_cost <= X

    # binary search on t in [0, max_t]
    lo, hi = 0, max_t
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    main()