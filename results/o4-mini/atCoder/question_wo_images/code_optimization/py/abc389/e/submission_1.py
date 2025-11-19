import sys
import threading

def main():
    import sys, math
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    P = [int(next(it)) for _ in range(n)]
    # Precompute binary-search upper bound for marginal cost C
    minP = min(P)
    # max k for product with minP: k^2 * minP <= M => k <= sqrt(M/minP)
    if minP > 0:
        k_max = int(math.isqrt(M // minP))
    else:
        k_max = 0
    C_max = (2 * k_max - 1) * minP
    if C_max < 0:
        C_max = 0

    # Binary search for largest C s.t. sum_{i} P_i * t_i(C)^2 <= M
    low, high = 0, C_max
    # We'll reuse local names for speed
    arr = P
    budget = M
    while low < high:
        mid = (low + high + 1) // 2
        total_cost = 0
        # compute sumcost(mid), break early if exceeds budget
        for p in arr:
            # number of taken marginal costs <= mid: t = floor((mid/p + 1)/2)
            x = mid // p
            t = (x + 1) >> 1
            if t:
                total_cost += p * t * t
                if total_cost > budget:
                    break
        if total_cost <= budget:
            low = mid
        else:
            high = mid - 1

    C = low
    # Now compute how many marginal costs <= C, their total cost, and next candidates
    tot = 0
    sumcost = 0
    nxt = [0] * n
    for i, p in enumerate(arr):
        x = C // p
        t = (x + 1) >> 1
        tot += t
        sumcost += p * t * t
        # next marginal cost for this product
        nxt[i] = p * (2 * t + 1)

    rem = budget - sumcost
    nxt.sort()
    extra = 0
    for cost in nxt:
        if cost <= rem:
            rem -= cost
            extra += 1
        else:
            break

    print(tot + extra)

if __name__ == "__main__":
    main()