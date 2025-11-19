import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    L, R = map(int, sys.stdin.readline().split())

    # Precompute powers: pw[d][k] = d^k for d in 0..9, k in 0..18
    pw = [[1] * 19 for _ in range(10)]
    for d in range(10):
        for k in range(1, 19):
            pw[d][k] = pw[d][k-1] * d

    # total_per_len[n] = count of snake numbers with exactly n digits
    # for n >= 2: sum_{d=1..9} d^(n-1)
    total_per_len = [0] * 20
    for n in range(2, 20):
        s = 0
        for d in range(1, 10):
            s += pw[d][n-1]
        total_per_len[n] = s

    def count_snakes(X):
        # Count snake numbers in [10..X]
        if X < 10:
            return 0
        s = str(X)
        digits = list(map(int, s))
        n = len(digits)
        ans = 0
        # Count all snake numbers with digit-length < n
        for length in range(2, n):
            ans += total_per_len[length]
        # Count n-digit snake numbers <= X
        first = digits[0]
        # Choose a smaller first digit
        for d in range(1, first):
            ans += pw[d][n-1]
        bound = first  # all other digits < bound
        # Now process remaining digits with tight constraint
        for i in range(1, n):
            cur = digits[i]
            # choose a digit < cur but also < bound
            maxd = min(bound-1, cur-1)
            if maxd >= 0:
                cnt_choices = maxd + 1  # 0..maxd
                ans += cnt_choices * pw[bound][n-1-i]
            # if cur is invalid (>= bound), we cannot continue the tight prefix
            if cur >= bound:
                return ans
            # else cur < bound: tight prefix continues
        # If we never broke, X itself is a valid snake
        ans += 1
        return ans

    result = count_snakes(R) - count_snakes(L-1)
    print(result)

if __name__ == "__main__":
    main()