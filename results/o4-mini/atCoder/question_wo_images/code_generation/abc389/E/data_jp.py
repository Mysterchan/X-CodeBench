import sys
import threading

def main():
    import sys
    from math import isqrt

    input = sys.stdin.readline
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()

    # Upper bound for threshold T: 2 * sqrt(max_P * M) + a little margin
    maxP = P[-1]
    hi = 2 * isqrt(maxP * M) + 2
    lo = 0

    def feasible(T):
        # Check if picking all items with marginal cost <= T stays within budget M
        total = 0
        for pi in P:
            k = (T // pi + 1) // 2
            if k <= 0:
                # further pi are larger, k will be 0 as well
                break
            # cost for this type
            c = pi * k * k
            total += c
            if total > M:
                return False
        return True

    # Binary search the largest T such that feasible(T) is True
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1

    # Compute the total number of items for threshold lo
    ans = 0
    T = lo
    for pi in P:
        k = (T // pi + 1) // 2
        if k <= 0:
            break
        ans += k

    print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()