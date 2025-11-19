import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(10**7)
    L, R = map(int, sys.stdin.readline().split())

    # Precompute powers: pow_d[d][k] = d**k for d in 0..9, k in 0..19
    MAX_N = 20
    pow_d = [[1] * (MAX_N+1) for _ in range(10)]
    for d in range(10):
        for k in range(1, MAX_N+1):
            pow_d[d][k] = pow_d[d][k-1] * d

    # sum_len[l] = number of heavy numbers of exact length l (for l >= 2), unconstrained
    # sum_len[l] = sum_{d=1..9} d^(l-1)
    sum_len = [0] * (MAX_N+1)
    for l in range(2, MAX_N+1):
        s = 0
        for d in range(1, 10):
            s += pow_d[d][l-1]
        sum_len[l] = s

    def count_heavy_upto(X: int) -> int:
        # Count heavy numbers in [10..X]
        if X < 10:
            return 0
        s = str(X)
        n = len(s)
        digits = list(map(int, s))

        # Count all heavy numbers of length < n
        res = 0
        for l in range(2, n):
            res += sum_len[l]

        # Count heavy numbers of length == n and <= X
        # First digit d0 runs from 1 to digits[0]
        first = digits[0]
        # Those with first digit < first => free choices on rest
        for d0 in range(1, first):
            # each of the remaining n-1 digits can be 0..d0-1
            res += pow_d[d0][n-1]

        # Case d0 == first: need digit DP on the rest
        d0 = first
        # if length >= 2
        if n >= 2:
            dp_tight = 1  # number of ways matching prefix so far
            dp_not = 0    # number of ways already below prefix
            # process positions 1..n-1
            for i in range(1, n):
                di = digits[i]
                new_tight = 0
                new_not = 0
                # from tight state
                if dp_tight:
                    # allowed digits 0..min(di, d0-1)
                    up = di if di < d0 else (d0-1)
                    if up >= 0:
                        if di < d0:
                            # all up+1 choices go to "not tight"
                            new_not += dp_tight * (up + 1)
                        else:
                            # di == d0-1 < di => never equality case here
                            # but if di <= d0-1, we can have one choice di==original digit
                            # which stays tight, and up choices go to not-tight
                            # however di <= d0-1 iff up == di
                            # so:
                            #   equal-case (di) stays tight: +dp_tight
                            #   lesser-case (0..di-1): di choices to not-tight
                            new_tight += dp_tight
                            new_not += dp_tight * di
                # from already-not-tight state
                if dp_not:
                    # each of the remaining positions can be 0..d0-1 freely
                    new_not += dp_not * d0
                dp_tight, dp_not = new_tight, new_not
            res += dp_tight + dp_not

        return res

    ans = count_heavy_upto(R) - count_heavy_upto(L-1)
    print(ans)

if __name__ == "__main__":
    main()