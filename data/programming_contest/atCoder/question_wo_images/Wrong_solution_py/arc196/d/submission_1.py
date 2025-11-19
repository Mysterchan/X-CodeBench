import bisect
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
MOD = 998244353

def dprint(*args, **kwargs) -> None:
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    sys.stderr.write(sep.join(map(str, args)) + end)

class BitVector:

    def __init__(self, num: int = 0) -> None:
        self.n: int = 0
        self.zeros: int = 0
        self.block: list[int] = []
        self.count: list[int] = []
        if num:
            self.resize(num)

    def resize(self, num: int) -> None:
        self.n = num

        num_blocks = (num + 63) // 64 + 1
        self.block = [0] * num_blocks
        self.count = [0] * num_blocks

    def set(self, i: int, val: int = 1) -> None:

        self.block[i >> 6] |= (int(val) & 1) << (i & 63)

    def get(self, i: int) -> int:
        return (self.block[i >> 6] >> (i & 63)) & 1

    def build(self) -> None:

        for i in range(1, len(self.block)):
            self.count[i] = self.count[i - 1] + self.block[i - 1].bit_count()
        self.zeros = self.rank0(self.n)

    def rank1(self, i: int, j: int | None = None) -> int:
        if j is not None:
            return self.rank1(j) - self.rank1(i)

        blk = i >> 6
        offset = i & 63

        return self.count[blk] + (self.block[blk] & ((1 << offset) - 1)).bit_count()

    def rank0(self, i: int, j: int | None = None) -> int:
        if j is not None:
            return self.rank0(j) - self.rank0(i)
        return i - self.rank1(i)

    def rank0_all(self) -> int:
        return self.zeros

class FenwickTree:

    def __init__(self, n: int, unity_sum: int = 0) -> None:
        self.UNITY_SUM = unity_sum
        self.N = n
        self.dat = [unity_sum] * n

    def init(self, n: int) -> None:
        self.N = n
        self.dat = [self.UNITY_SUM] * n

    def add(self, a: int, x: int) -> None:
        i = a
        size = len(self.dat)
        while i < size:
            self.dat[i] += x
            i |= i + 1

    def sum(self, a: int, b: int | None = None) -> int:
        if b is not None:
            return self.sum(b) - self.sum(a)

        res = self.UNITY_SUM
        i = a - 1
        while i >= 0:
            res += self.dat[i]
            i = (i & (i + 1)) - 1
        return res

class BITonWaveletMatrix:

    def __init__(self, points: list[tuple[int, int]] | None = None) -> None:
        self.n: int = 0
        self.height: int = 0
        self.bv: list[BitVector] = []
        self.ps: list[tuple[int, int]] = []
        self.ys: list[int] = []
        self.bit: list[FenwickTree] = []
        if points:
            for x, y in points:
                self.add_point(x, y)
            self.build()

    def add_point(self, x: int, y: int) -> None:
        self.ps.append((x, y))
        self.ys.append(y)

    def xid(self, x: int) -> int:

        return bisect.bisect_left(self.ps, (x, 0))

    def yid(self, y: int) -> int:
        return bisect.bisect_left(self.ys, y)

    def build(self) -> None:

        self.ps = sorted(set(self.ps))
        self.n = len(self.ps)
        self.ys = sorted(set(self.ys))

        if self.n == 0:
            self.height = 0
            self.bv = []
            self.bit = []
            return

        v = [0] * self.n
        left = [0] * self.n
        right = [0] * self.n
        ord_idx = list(range(self.n))

        mv = 1
        for i in range(self.n):
            _, y = self.ps[i]
            vy = self.yid(y)
            v[i] = vy
            if vy > mv:
                mv = vy

        self.height = 1
        tmp = mv
        while tmp != 0:
            self.height += 1
            tmp >>= 1

        self.bv = [BitVector(self.n) for _ in range(self.height)]
        self.bit = [FenwickTree(self.n) for _ in range(self.height + 1)]

        for h in range(self.height - 1, -1, -1):
            left_size = 0
            right_size = 0
            for i in range(self.n):
                idx = ord_idx[i]
                if (v[idx] >> h) & 1:
                    self.bv[h].set(i)
                    right[right_size] = idx
                    right_size += 1
                else:
                    left[left_size] = idx
                    left_size += 1
            self.bv[h].build()

            ord_idx[:left_size] = left[:left_size]
            ord_idx[left_size : left_size + right_size] = right[:right_size]

    def add(self, x: int, y: int, val: int) -> None:

        i = bisect.bisect_left(self.ps, (x, y))
        j = self.yid(y)
        for h in range(self.height - 1, -1, -1):
            i0 = self.bv[h].rank0(i)
            if (j >> h) & 1:
                i += self.bv[h].rank0_all() - i0
            else:
                i = i0
            self.bit[h].add(i, val)

    def _inner_sum(self, left_index: int, right_index: int, upper: int) -> int:

        if not (0 <= left_index <= right_index <= self.n):
            raise ValueError(
                "index out of range in _inner_sum",
                left_index,
                right_index,
                upper,
                self.n,
            )
        res = 0
        for h in range(self.height - 1, -1, -1):
            left_rank0 = self.bv[h].rank0(left_index)
            right_rank0 = self.bv[h].rank0(right_index)
            if (upper >> h) & 1:
                left_index += self.bv[h].rank0_all() - left_rank0
                right_index += self.bv[h].rank0_all() - right_rank0
                res += self.bit[h].sum(left_rank0, right_rank0)
            else:
                left_index = left_rank0
                right_index = right_rank0
        return res

    def sum(self, lx: int, rx: int, ly: int, ry: int) -> int:

        x_left_index = self.xid(lx)
        x_right_index = self.xid(rx)
        return self._inner_sum(x_left_index, x_right_index, self.yid(ry)) - self._inner_sum(
            x_left_index, x_right_index, self.yid(ly)
        )

def check_overlap(w: BITonWaveletMatrix, l: int, r: int) -> bool:

    return w.sum(0, l + 1, l + 1, r) + w.sum(l, r, r + 1, N) > 0

N, M, Q = map(int, input().split())
A = [[int(x) - 1 for x in input().split()] for _ in range(M)]
B = [[int(x) - 1 for x in input().split()] for _ in range(Q)]
plus_points = []
minus_points = []
for i in range(M):
    l, r = A[i]
    if l < r:
        plus_points.append((l, r))
    else:
        minus_points.append((r, l))

wp = BITonWaveletMatrix(plus_points)
wn = BITonWaveletMatrix(minus_points)
nl = defaultdict(int)
nr = defaultdict(int)

ans = [0] * (M + 1)

j = 0
for i in range(M + 1):
    while j < M:
        l, r = A[j]
        if l < r:
            if check_overlap(wp, l, r) or nl[l] > 0 or nr[r] > 0:
                break
            wp.add(l, r, 1)
            nl[l] += 1
            nr[r] += 1
            j += 1
        else:
            l, r = r, l
            if check_overlap(wn, l, r) or nl[l] > 0 or nr[r] > 0:
                break
            wn.add(l, r, 1)
            nl[l] += 1
            nr[r] += 1
            j += 1
    ans[i] = j
    if i < M:
        if A[i][0] < A[i][1]:
            wp.add(A[i][0], A[i][1], -1)
            nl[A[i][0]] -= 1
            nr[A[i][1]] -= 1
        else:
            wn.add(A[i][1], A[i][0], -1)
            nl[A[i][0]] -= 1
            nr[A[i][1]] -= 1

for i in range(Q):
    if B[i][1] < ans[B[i][0]]:
        print("Yes")
    else:
        print("No")