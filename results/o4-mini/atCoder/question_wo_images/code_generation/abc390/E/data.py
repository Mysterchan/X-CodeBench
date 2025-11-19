import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    X = int(next(it))
    # Group items by vitamin type
    items1 = []
    items2 = []
    items3 = []
    for _ in range(N):
        v = int(next(it))
        a = int(next(it))
        c = int(next(it))
        if v == 1:
            items1.append((c, a))
        elif v == 2:
            items2.append((c, a))
        else:
            items3.append((c, a))

    # Build dp_k[c] = max vitamin amount using <=c calories, for each type
    # We'll do 0/1 knapsack, then make dp non-decreasing
    def build_dp(items):
        dp = [0] * (X + 1)
        for cal, vit in items:
            # For 0/1 knapsack, iterate calories from X down to cal
            for cur in range(X, cal - 1, -1):
                val = dp[cur - cal] + vit
                if val > dp[cur]:
                    dp[cur] = val
        # Make dp[c] non-decreasing
        for i in range(1, X + 1):
            if dp[i] < dp[i-1]:
                dp[i] = dp[i-1]
        return dp

    dp1 = build_dp(items1)
    dp2 = build_dp(items2)
    dp3 = build_dp(items3)

    # Maximum possible M is limited by the smallest of dp_k[X]
    hi = min(dp1[X], dp2[X], dp3[X])

    # Function to find minimal calories needed to reach at least M vitamins
    def min_cal(dp, M):
        # binary search on dp[] which is non-decreasing
        lo, hi_ = 0, X
        while lo < hi_:
            mid = (lo + hi_) // 2
            if dp[mid] >= M:
                hi_ = mid
            else:
                lo = mid + 1
        return lo  # could be X+1 if not found, but our dp[X]>=M check avoids that

    # Check if it's possible to get M vitamins of each type within X calories
    def can(M):
        # If any type can't reach M even at X calories, fail early
        if dp1[X] < M or dp2[X] < M or dp3[X] < M:
            return False
        c1 = min_cal(dp1, M)
        c2 = min_cal(dp2, M)
        c3 = min_cal(dp3, M)
        return (c1 + c2 + c3) <= X

    # Binary search for the answer
    lo = 0
    hi = hi
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)

if __name__ == "__main__":
    main()