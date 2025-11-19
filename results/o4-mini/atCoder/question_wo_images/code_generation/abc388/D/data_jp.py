import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    maxA = max(A) if A else 0
    # Maximum possible T = A_i + i + K_i <= maxA + N + (i-1) <= maxA + 2N
    MAXT = maxA + 2 * N + 5

    # Fenwick Tree (BIT) for counts of T_j
    class BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (n + 1)
        def add(self, i, v):
            # add v at index i
            while i <= self.n:
                self.data[i] += v
                i += i & -i
        def sum(self, i):
            # sum of [1..i]
            s = 0
            while i > 0:
                s += self.data[i]
                i -= i & -i
            return s

    bit = BIT(MAXT)
    T = [0] * N
    # Compute T_i for i=1..N
    for idx in range(N):
        i = idx + 1
        # number of previous j<i with T_j >= i = (i-1) - sum of T_j <= i-1
        cnt_le = bit.sum(i - 1)
        K = (i - 1) - cnt_le
        Ti = A[idx] + i + K
        T[idx] = Ti
        # record in BIT
        bit.add(Ti, 1)

    # Final B_i = max(0, T_i - N)
    res = [str(max(0, T[i] - N)) for i in range(N)]
    print(" ".join(res))


if __name__ == "__main__":
    main()