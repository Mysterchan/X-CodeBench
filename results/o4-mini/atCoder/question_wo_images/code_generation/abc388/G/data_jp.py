import sys
import threading

def main():
    import sys
    import bisect

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    # Precompute B[i]: smallest index j such that A[j] >= 2*A[i], or N if none
    B = [0] * N
    for i in range(N):
        # bisect_left on A for 2*A[i]
        j = bisect.bisect_left(A, 2 * A[i])
        B[i] = j  # j may be N

    # C[i] = B[i] - i
    C = [B[i] - i for i in range(N)]

    # Build log table
    log2 = [0] * (N + 1)
    for i in range(2, N + 1):
        log2[i] = log2[i // 2] + 1

    # Build sparse table for range maximum on C
    K = log2[N] + 1
    st = [ [0] * N for _ in range(K) ]
    # level 0
    for i in range(N):
        st[0][i] = C[i]
    # higher levels
    j = 1
    while (1 << j) <= N:
        length = 1 << j
        half = length >> 1
        prev = st[j - 1]
        curr = st[j]
        for i in range(N - length + 1):
            # max on [i, i+length-1]
            a = prev[i]
            b = prev[i + half]
            curr[i] = a if a >= b else b
        j += 1

    def range_max(l, r):
        """Return max of C[l..r], 0-based inclusive."""
        length = r - l + 1
        k = log2[length]
        a = st[k][l]
        b = st[k][r - (1 << k) + 1]
        return a if a >= b else b

    Q = int(input())
    out = []
    for _ in range(Q):
        L, R = map(int, input().split())
        # convert to 0-based
        l = L - 1
        r = R - 1
        length = r - l + 1
        # max possible pairs
        high = length // 2
        low = 0
        # binary search for max K in [0..high]
        while low < high:
            mid = (low + high + 1) // 2
            # check if mid pairs can be formed
            # need max C on [l..l+mid-1] + mid <= length
            if mid == 0:
                ok = True
            else:
                if l + mid - 1 <= r:
                    f = range_max(l, l + mid - 1)
                    ok = (f + mid <= length)
                else:
                    ok = False
            if ok:
                low = mid
            else:
                high = mid - 1
        out.append(str(low))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()