import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    A = [0] * (n + 1)
    for i in range(1, n + 1):
        A[i] = int(next(it))
    # Precompute nothing except A sorted
    from bisect import bisect_left, bisect_right

    q = int(next(it))
    out = []
    for _ in range(q):
        l = int(next(it)); r = int(next(it))
        length = r - l + 1
        # Quick bound on k
        # cnt_smalls = number of A[i] in [l..r] with A[i] <= A[r]//2
        halfR = A[r] >> 1
        if A[l] > halfR:
            out.append("0")
            continue
        # find rightmost index <= halfR in [l..r]
        hi = bisect_right(A, halfR, l, r+1) - 1
        cnt_smalls = hi - l + 1
        # cnt_bigs = number of A[j] in [l..r] with A[j] >= 2*A[l]
        twoL = A[l] << 1
        lo = bisect_left(A, twoL, l, r+1)
        cnt_bigs = r - lo + 1
        ub = cnt_smalls
        if cnt_bigs < ub: ub = cnt_bigs
        half = length >> 1
        if half < ub: ub = half
        if ub <= 0:
            out.append("0")
            continue
        # binary search k in [1..ub]
        low, high = 1, ub
        res = 0
        while low <= high:
            mid = (low + high) >> 1
            # check mid
            # we need for all i in 0..mid-1: A[l+i]*2 <= A[r-mid+1+i]
            ok = True
            # pointers
            a_idx = l
            b_idx = r - mid + 1
            # unroll small loops might help
            for _ in range(mid):
                if A[a_idx] * 2 > A[b_idx]:
                    ok = False
                    break
                a_idx += 1; b_idx += 1
            if ok:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(res))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    threading.Thread(target=main).start()