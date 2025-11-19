import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    P = [int(next(it)) for _ in range(n)]
    # Binary search on threshold T of marginal cost
    lo, hi = 0, 2 * 10**14  # upper bound for marginal cost
    while lo < hi:
        mid = (lo + hi + 1) // 2
        cost = 0
        # Check total cost if we take all increments with marginal <= mid
        for p in P:
            t = mid // p
            # number of increments for this product
            k = (t + 1) // 2
            if k > 0:
                cost += p * k * k
                if cost > M:
                    break
        if cost <= M:
            lo = mid
        else:
            hi = mid - 1

    # lo is the maximum threshold T* with total cost <= M
    T = lo
    total_units = 0
    for p in P:
        t = T // p
        k = (t + 1) // 2
        total_units += k

    print(total_units)

if __name__ == "__main__":
    main()