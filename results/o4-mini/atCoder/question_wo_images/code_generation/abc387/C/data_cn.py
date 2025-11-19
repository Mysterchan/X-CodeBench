import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    L = int(data[0])
    R = int(data[1])

    # Precompute powers powD[d][k] = d**k for d=0..9, k=0..19
    max_len = 19  # up to 10^18 has at most 19 digits
    powD = [[1] * (max_len + 1) for _ in range(10)]
    for d in range(10):
        for k in range(1, max_len + 1):
            powD[d][k] = powD[d][k-1] * d

    # S[m] = number of snake numbers of exact length m (m>=2)
    # S[m] = sum_{D=1..9} D^(m-1)
    S = [0] * (max_len + 1)
    for m in range(2, max_len + 1):
        s = 0
        exp = m - 1
        for D in range(1, 10):
            s += powD[D][exp]
        S[m] = s

    # lenSum[n] = sum_{m=2..n} S[m]
    lenSum = [0] * (max_len + 1)
    acc = 0
    for m in range(2, max_len + 1):
        acc += S[m]
        lenSum[m] = acc

    def count_snakes_upto(X):
        # Count snake numbers <= X
        if X < 10:
            return 0
        ds = list(map(int, str(X)))
        n = len(ds)
        # Count all with length < n
        res = lenSum[n-1]
        D0 = ds[0]
        # Count length==n, leading digit < D0
        for D in range(1, D0):
            res += powD[D][n-1]
        # Count length==n, leading digit == D0 and rest <= X
        # Other digits must be < D0
        for i in range(1, n):
            a = ds[i]
            rem = n - 1 - i
            if a < D0:
                # choices d = 0..a-1 => a choices, each gives D0^rem sequences
                res += a * powD[D0][rem]
                # continue matching
            else:
                # a >= D0: all allowed digits (0..D0-1) are < a
                res += D0 * powD[D0][rem]
                break
        else:
            # matched all digits with ds[i] < D0 => X itself is a snake
            res += 1
        return res

    ans = count_snakes_upto(R) - count_snakes_upto(L-1)
    print(ans)

if __name__ == "__main__":
    main()