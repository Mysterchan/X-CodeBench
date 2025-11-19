import sys
import threading

def main():
    import sys

    data = sys.stdin.readline().split()
    L = int(data[0])
    R = int(data[1])

    # Precompute powers f^e for f=0..9, e=0..18
    MAXP = 18
    pow_f = [[0] * (MAXP+1) for _ in range(10)]
    for f in range(10):
        pow_f[f][0] = 1
        for e in range(1, MAXP+1):
            pow_f[f][e] = pow_f[f][e-1] * f

    # total_by_len[k] = number of snake numbers of length k
    # only lengths >=2 matter
    total_by_len = [0] * (MAXP+1)
    for k in range(2, MAXP+1):
        # sum_{f=1..9} f^{k-1}
        s = 0
        for f in range(1, 10):
            s += pow_f[f][k-1]
        total_by_len[k] = s

    # prefix_total_len[k] = sum total_by_len[0..k]
    prefix_total_len = [0] * (MAXP+1)
    for k in range(1, MAXP+1):
        prefix_total_len[k] = prefix_total_len[k-1] + total_by_len[k]

    def count_snake(x: int) -> int:
        # count snake numbers <= x
        if x < 10:
            return 0
        ds = list(map(int, str(x)))
        n = len(ds)
        # sum of all snake numbers of length < n
        res = prefix_total_len[n-1]
        first = ds[0]
        # count those of length n with leading digit f < first
        for f in range(1, first):
            res += pow_f[f][n-1]
        # now f == first
        f = first
        # only if length >=2
        tight = True
        # suffix DP over positions 1..n-1
        for i in range(1, n):
            if not tight:
                break
            di = ds[i]
            # other digits must be in [0..f-1]
            # count choices < di
            lower = min(f-1, di-1)
            if lower >= 0:
                res += (lower + 1) * pow_f[f][n-1-i]
            # can we match di exactly?
            if di > f-1:
                tight = False
                break
            # else di <= f-1: continue tight
        if tight:
            # x itself is a snake if all ds[i] <= f-1
            # that is ensured by tight
            res += 1
        return res

    ans = count_snake(R) - count_snake(L-1)
    print(ans)

if __name__ == "__main__":
    main()