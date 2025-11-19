import sys
input = sys.stdin.readline

mod = 998244353
n = int(input())
p = list(map(lambda x: int(x) - 1, input().split()))

two = [1] * (n + 1)
for i in range(n):
    two[i + 1] = two[i] * 2 % mod

# Precompute prefix sums of powers of two for quick range sum queries
# Not strictly necessary here but kept for clarity

def calc(p):
    res = 0
    # We will count contribution of vertical spans
    # Using a Fenwick tree (BIT) to maintain counts efficiently
    # But since the original code uses a LazySegTree with doubling,
    # we can optimize by using prefix sums and a stack approach.

    # The original code applies doubling on suffixes repeatedly,
    # which is equivalent to counting subsets with certain constraints.

    # We'll implement a more direct O(n) approach using a stack to count
    # the number of subsets where a particular segment is the max/min.

    # However, since the original code is complex and uses a segment tree,
    # we can optimize by using a monotonic stack approach to count contributions.

    # But since the problem is symmetric and the original code uses a segment tree
    # to apply doubling on suffixes, we can replicate the logic with prefix sums.

    # Here, we implement the same logic as the original LazySegTree approach,
    # but with a Fenwick tree (BIT) for faster updates and queries.

    class BIT:
        def __init__(self, n):
            self.n = n
            self.bit = [0] * (n + 1)
        def add(self, i, x):
            i += 1
            while i <= self.n:
                self.bit[i] = (self.bit[i] + x) % mod
                i += i & -i
        def sum(self, i):
            s = 0
            i += 1
            while i > 0:
                s = (s + self.bit[i]) % mod
                i -= i & -i
            return s
        def range_sum(self, l, r):
            return (self.sum(r) - self.sum(l - 1)) % mod

    bit = BIT(n)
    # Initially, all positions have count 1 (empty subset count)
    for i in range(n):
        bit.add(i, 1)

    for i in range(n - 1):
        # For position p[i], double all counts from p[i] to end
        # Doubling means adding current counts again
        # So we add bit.range_sum(p[i], n-1) to each position p[i]..n-1
        # But this is O(n) if done naively, so we do a range add with BIT
        # BIT supports point add and prefix sum, not range add
        # So we use a difference array approach with two BITs or a segment tree
        # To keep it simple and efficient, we revert to the original segment tree approach

        # Since the above is complicated, we revert to the original segment tree approach,
        # but implement it more efficiently without lazy propagation.

        # So we break here and implement the original segment tree approach below.

        break

    # Since the above approach is complicated, we implement the original segment tree approach
    # but optimized with iterative segment tree without lazy propagation.

    # We'll implement a segment tree that supports range multiplication by 2 and sum query.

def op(x, y):
    return (x + y) % mod

class SegTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.data = [0] * (2 * self.n)
        self.lazy = [1] * (2 * self.n)  # lazy multiplication
    def _apply(self, k, v):
        self.data[k] = self.data[k] * v % mod
        self.lazy[k] = self.lazy[k] * v % mod
    def _push(self, k):
        self._apply(k*2, self.lazy[k])
        self._apply(k*2+1, self.lazy[k])
        self.lazy[k] = 1
    def _update(self, k):
        self.data[k] = (self.data[k*2] + self.data[k*2+1]) % mod
    def build(self, arr):
        for i in range(len(arr)):
            self.data[self.n + i] = arr[i] % mod
        for i in range(self.n - 1, 0, -1):
            self._update(i)
    def _range_mul(self, l, r, v, k, left, right):
        if r <= left or right <= l:
            return
        if l <= left and right <= r:
            self._apply(k, v)
            return
        self._push(k)
        mid = (left + right) // 2
        self._range_mul(l, r, v, k*2, left, mid)
        self._range_mul(l, r, v, k*2+1, mid, right)
        self._update(k)
    def range_mul(self, l, r, v):
        self._range_mul(l, r, v, 1, 0, self.n)
    def query(self):
        return self.data[1]

def calc(p):
    st = SegTree(n - 1)
    st.build([1] * (n - 1))
    res = 0
    for i in range(n - 1):
        st.range_mul(p[i], n - 1, 2)
        res += st.query()
    return res % mod

ans = (two[n] - 1) * (n - 1) * (n - 1) % mod
for i in range(1, n):
    ans -= 4 * two[i] * (n - 1) % mod
ans %= mod

ans += calc(p)
ans += calc(p[::-1])
p_rev = [n - 1 - x for x in p]
ans += calc(p_rev)
ans += calc(p_rev[::-1])
ans %= mod

print(ans)