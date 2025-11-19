import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10000)
    from functools import lru_cache

    def solve(N):
        # Count snake numbers between 10 and N inclusive.
        if N < 10:
            return 0
        s = list(map(int, str(N)))
        n = len(s)

        @lru_cache(maxsize=None)
        def dfs(pos, tight, started, top):
            # pos: current position [0..n)
            # tight: 1 if prefix == N's prefix
            # started: 1 if we've placed a non-zero digit
            # top: the first non-zero digit placed (d0), valid when started==1
            if pos == n:
                # count only if we have placed at least one non-zero digit
                return 1 if started else 0

            res = 0
            lim = s[pos] if tight else 9

            for d in range(lim+1):
                nt = tight and (d == lim)
                if not started:
                    # still skipping leading zeros
                    if d == 0:
                        # stay not started
                        res += dfs(pos+1, nt, False, 0)
                    else:
                        # start number with top digit d
                        res += dfs(pos+1, nt, True, d)
                else:
                    # already have top digit
                    # current digit must be strictly less than top
                    if d < top:
                        res += dfs(pos+1, nt, True, top)
                    # else skip
            return res

        total = dfs(0, True, False, 0)
        # subtract single-digit numbers counted (1..9)
        single_digits = min(N, 9)
        return total - single_digits

    data = sys.stdin.read().strip().split()
    L = int(data[0])
    R = int(data[1])
    ans = solve(R) - solve(L-1)
    print(ans)

if __name__ == "__main__":
    main()