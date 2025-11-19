import threading
import sys
def main():
    import sys
    data = sys.stdin
    ril = lambda: map(int, data.readline().split())
    T = int(data.readline())
    out = []
    for _ in range(T):
        n, M = ril()
        A = list(ril())
        B = list(ril())
        A.sort()
        # sort B descending so intervals by increasing right-end
        B.sort(reverse=True)
        # edge-case: check if answer is 0
        # that requires for every b there is a = M-b in multiset A
        # we can do a quick counter check
        if n <= 2000:
            # small n: brute for zero-check
            cnt = {}
            for a in A:
                cnt[a] = cnt.get(a,0)+1
            ok0 = True
            for b in B:
                need = (-b) % M
                if cnt.get(need,0) == 0:
                    ok0 = False
                    break
                cnt[need] -= 1
            if ok0:
                out.append("0")
                continue
        else:
            # large n: use two-pointer
            # since A sorted, B reverse-sorted
            # build counter by linear scan
            i = 0
            ok0 = True
            from collections import Counter
            cnt = Counter(A)
            for b in B:
                need = (-b) % M
                if cnt[need] == 0:
                    ok0 = False
                    break
                cnt[need] -= 1
            if ok0:
                out.append("0")
                continue

        # compress A values
        comp = A[:]  # sorted
        # Fenwick on counts
        size = n
        # initial counts
        init_counts = [1]*n
        # Fenwick tree
        class Fenw:
            __slots__ = ('n','fenw')
            def __init__(self,n):
                self.n = n
                self.fenw = [0]*(n+1)
            def build(self,arr):
                fw = self.fenw
                n = self.n
                for i,v in enumerate(arr,1):
                    fw[i] += v
                for i in range(1,n+1):
                    j = i + (i & -i)
                    if j <= n:
                        fw[j] += fw[i]
            def sum(self,i):
                s = 0
                fw = self.fenw
                while i>0:
                    s += fw[i]
                    i &= i-1
                return s
            def add(self,i,v):
                fw = self.fenw
                n = self.n
                while i<=n:
                    fw[i] += v
                    i += i & -i
            # find smallest idx so that prefix sum >= k
            def kth(self,k):
                fw = self.fenw
                n = self.n
                idx = 0
                bit = 1 << (n.bit_length())
                while bit:
                    t = idx + bit
                    if t<=n and fw[t]<k:
                        idx = t
                        k -= fw[t]
                    bit >>= 1
                return idx+1

        # prepare fenw
        fenw = Fenw(n)
        # binary search
        lo,hi = 0, M-1
        from bisect import bisect_left, bisect_right
        while lo<hi:
            mid = (lo+hi)//2
            # rebuild fenw
            fenw.build(init_counts)
            total = n
            ok = True
            for b in B:
                if mid < b:
                    lb = M - b
                    ub = M + mid - b
                    # find first index i with comp[i]>=lb
                    i0 = bisect_left(comp, lb)
                    # find the (sum up to i0) count
                    cnt_before = fenw.sum(i0)
                    if cnt_before == fenw.sum(n):
                        ok = False
                        break
                    # we want the first element >= lb => it's the (cnt_before+1)-th overall
                    idx = fenw.kth(cnt_before+1)
                    # check that comp[idx-1] <= ub
                    if comp[idx-1] > ub:
                        ok = False
                        break
                    fenw.add(idx, -1)
                else:
                    # interval1: [0, mid-b]
                    ub1 = mid - b
                    # try smallest a overall
                    if total > 0:
                        # the smallest element is at kth(1)
                        idx1 = fenw.kth(1)
                        if comp[idx1-1] <= ub1:
                            fenw.add(idx1, -1)
                        else:
                            # try second interval [M-b, M-1]
                            lb2 = M - b
                            i0 = bisect_left(comp, lb2)
                            cnt_before = fenw.sum(i0)
                            if cnt_before == fenw.sum(n):
                                ok = False
                                break
                            idx2 = fenw.kth(cnt_before+1)
                            # comp[idx2-1] must be >= lb2
                            if comp[idx2-1] < lb2:
                                ok = False
                                break
                            fenw.add(idx2, -1)
                    else:
                        ok = False
                        break
                total -= 1
            if ok:
                hi = mid
            else:
                lo = mid+1
        out.append(str(lo))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()