import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    X = int(next(it))
    groups = [[], [], [], []]  # 1-based indexing: groups[1], groups[2], groups[3]
    tot = [0, 0, 0, 0]
    for _ in range(n):
        v = int(next(it))
        a = int(next(it))
        c = int(next(it))
        if c <= X:
            groups[v].append((a, c))
            tot[v] += a

    # For each group 1..3, build dp_k[c] = max vitamin amount with exactly c calories
    dp = [[-10**18] * (X + 1) for _ in range(4)]
    for k in (1, 2, 3):
        dpk = dp[k]
        dpk[0] = 0
        for a, cost in groups[k]:
            # 0/1 knapsack on cost, maximize vitamin sum
            # iterate backwards to avoid reuse
            for c in range(X, cost - 1, -1):
                val = dpk[c - cost] + a
                if val > dpk[c]:
                    dpk[c] = val

    # Search t in [0 .. min(tot[1],tot[2],tot[3])]
    hi = min(tot[1], tot[2], tot[3])
    lo = 0
    ans = 0

    # feasibility check for given t: find minimal cost in each group to reach >= t
    def feasible(t):
        # if t == 0 always true
        total_c = 0
        for k in (1, 2, 3):
            dpk = dp[k]
            # find minimal c in [0..X] with dpk[c] >= t
            # linear scan
            mc = X + 1
            # small optimization: break early if sum already > X
            for c in range(0, X + 1):
                if dpk[c] >= t:
                    mc = c
                    break
            total_c += mc
            if total_c > X:
                return False
        return total_c <= X

    # binary search
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    main()