import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    P = [int(next(it)) for _ in range(n)]

    # Function to compute for a given threshold T:
    #   C = total count of marginal costs <= T
    #   S = sum of those marginal costs
    def count_and_sum(T):
        # c_i = max t: P[i] * (2*t - 1) <= T  => 2*t - 1 <= T/P[i] => t <= (T/P[i] + 1)/2
        tot_c = 0
        tot_s = 0
        for pi in P:
            # if T < pi, then no unit from this product
            if T < pi:
                continue
            # compute c = floor((T//pi + 1)//2)
            # trick: (T//pi + 1) // 2
            c = (T // pi + 1) >> 1
            tot_c += c
            # cost contribution: pi * (1 + 3 + ... + (2c-1)) = pi * c^2
            tot_s += pi * (c * c)
            # small optimization: if tot_s > M we can early-stop counting sums
            # because we only need to know > M
            if tot_s > M:
                # but keep tot_c correct, so no break
                # we only break if too slow; here we continue to get tot_c
                # but tot_s large enough to indicate overflow
                pass
        return tot_c, tot_s

    # Binary search on T in [0, M], find max T with S(T) <= M
    lo, hi = 0, M + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        c, s = count_and_sum(mid)
        if s <= M:
            lo = mid
        else:
            hi = mid

    # lo is the largest threshold T where we can afford all marginal costs <= T
    ans, _ = count_and_sum(lo)
    print(ans)

if __name__ == "__main__":
    main()