import sys
import bisect
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # Coordinate compression of A
    sorted_unique = sorted(set(a))
    comp = {v: i+1 for i, v in enumerate(sorted_unique)}  # 1-based indexing for Fenwicks

    # Fenwick Tree (BIT) for max queries
    class Fenwicks:
        def __init__(self, size):
            self.n = size
            self.fw = [0]*(self.n+1)
        def update(self, i, val):
            while i <= self.n:
                if self.fw[i] < val:
                    self.fw[i] = val
                i += i & (-i)
        def query(self, i):
            res = 0
            while i > 0:
                if self.fw[i] > res:
                    res = self.fw[i]
                i -= i & (-i)
            return res

    fenw = Fenwicks(len(sorted_unique))
    dp = [0]*n

    # Compute dp[i] = length of LIS ending at i
    for i in range(n):
        c = comp[a[i]]
        best = fenw.query(c-1)
        dp[i] = best + 1
        fenw.update(c, dp[i])

    # Build segment tree over dp for range max queries
    size = 1
    while size < n:
        size <<= 1
    seg = [0]*(2*size)

    for i in range(n):
        seg[size+i] = dp[i]
    for i in range(size-1, 0, -1):
        seg[i] = max(seg[i<<1], seg[i<<1|1])

    def seg_query(l, r):
        # max in [l, r)
        res = 0
        l += size
        r += size
        while l < r:
            if l & 1:
                if seg[l] > res:
                    res = seg[l]
                l += 1
            if r & 1:
                r -= 1
                if seg[r] > res:
                    res = seg[r]
            l >>= 1
            r >>= 1
        return res

    # For each query:
    # We want max dp[i] for i in [0, R_i-1] with A[i] <= X_i
    # Preprocessing done, now answer queries efficiently.

    # To answer queries efficiently, we need to find indices i <= R_i with A[i] <= X_i
    # We can pre-sort indices by A[i] to binary search by X_i

    # Create array of (A[i], i)
    arr = [(val, idx) for idx, val in enumerate(a)]
    arr.sort(key=lambda x: x[0])  # sort by value

    # For each query, we want to find all indices i with A[i] <= X_i and i < R_i
    # Among those, find max dp[i]

    # To do this efficiently, we can:
    # For each unique value in sorted_unique, maintain a segment tree or BIT over indices to get max dp[i] for i < R_i

    # But indices are up to 2e5, so we can build a segment tree over indices for each prefix of sorted_unique values.

    # Instead, we can build a segment tree over indices (0..n-1) for dp[i], and for each query:
    # We want max dp[i] where i < R_i and A[i] <= X_i

    # So we can:
    # - For each query, find the largest value <= X_i in sorted_unique (using bisect)
    # - For all indices i with A[i] <= X_i, we want max dp[i] with i < R_i

    # We can build a segment tree over indices 0..n-1 with dp[i], and for each query:
    # - We want to consider only those i with A[i] <= X_i
    # So we need a data structure to filter indices by A[i] <= X_i.

    # Approach:
    # For each unique value val in sorted_unique, store the list of indices where A[i] = val, sorted.
    # For each val, build a Fenwicks over indices to get max dp[i] for i < R_i.

    # But this is complicated.

    # Alternative approach:
    # Offline queries:
    # Sort queries by X_i ascending.
    # Process array elements in ascending order of A[i].
    # Maintain a Fenwicks over indices 1..n to store max dp[i] for processed elements.
    # For each query with X_i, process all elements with A[i] <= X_i, update Fenwicks at position i+1 with dp[i].
    # Then query Fenwicks for max dp[i] with i+1 <= R_i.

    # This works because we process queries in order of increasing X_i.

    queries = []
    for i in range(q):
        r, x = map(int, input().split())
        queries.append((x, r, i))
    queries.sort()

    # Sort elements by A[i]
    elems = sorted([(val, idx) for idx, val in enumerate(a)], key=lambda x: x[0])

    fenw_idx = Fenwicks(n)
    res = [0]*q
    pos = 0  # pointer for elems

    for x, r, qi in queries:
        # Process all elements with val <= x
        while pos < n and elems[pos][0] <= x:
            _, idx = elems[pos]
            fenw_idx.update(idx+1, dp[idx])
            pos += 1
        # Query fenwicks for max dp[i] with i+1 <= r
        res[qi] = fenw_idx.query(r)

    print('\n'.join(map(str, res)))

solve()