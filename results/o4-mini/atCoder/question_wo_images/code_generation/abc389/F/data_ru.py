import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.readline
    N = int(data())
    intervals = []
    maxR = 0
    for _ in range(N):
        l, r = map(int, data().split())
        intervals.append((l, r))
        if r > maxR: maxR = r
    Q = int(data())
    queries = [0] * Q
    maxX = 0
    for i in range(Q):
        x = int(data().strip())
        queries[i] = x
        if x > maxX: maxX = x
    M = max(maxR, maxX)
    # Segment tree arrays
    size = 1
    while size < M:
        size <<= 1
    # We will use a 1-based recursive tree on [1..M]
    tree = [0] * (4 * M + 4)
    lazy = [0] * (4 * M + 4)

    # Build initial tree: f_old[x] = x
    def build(node, l, r):
        if l == r:
            tree[node] = l
            return
        mid = (l + r) >> 1
        lc = node << 1
        rc = lc | 1
        build(lc, l, mid)
        build(rc, mid + 1, r)
        # max of children
        a = tree[lc]; b = tree[rc]
        tree[node] = a if a > b else b

    # Push down lazy value
    def pushdown(node):
        v = lazy[node]
        if v:
            lc = node << 1
            rc = lc | 1
            tree[lc] += v
            lazy[lc] += v
            tree[rc] += v
            lazy[rc] += v
            lazy[node] = 0

    # Range add +1 on [ql..qr]
    def add(node, l, r, ql, qr):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            tree[node] += 1
            lazy[node] += 1
            return
        pushdown(node)
        mid = (l + r) >> 1
        lc = node << 1
        rc = lc | 1
        if ql <= mid:
            add(lc, l, mid, ql, qr)
        if qr > mid:
            add(rc, mid + 1, r, ql, qr)
        # pull up
        a = tree[lc]; b = tree[rc]
        tree[node] = a if a > b else b

    # Find first index x in [1..M] with f_old[x] >= T, or return None
    def find_first_ge(T):
        if tree[1] < T:
            return None
        node = 1
        l = 1
        r = M
        while l != r:
            if lazy[node]:
                v = lazy[node]
                lc = node << 1
                rc = lc | 1
                tree[lc] += v; lazy[lc] += v
                tree[rc] += v; lazy[rc] += v
                lazy[node] = 0
            mid = (l + r) >> 1
            lc = node << 1
            # go left or right
            if tree[lc] >= T:
                node = lc
                r = mid
            else:
                node = lc | 1
                l = mid + 1
        return l

    # Query point x
    def query_point(idx):
        node = 1
        l = 1
        r = M
        while l != r:
            if lazy[node]:
                v = lazy[node]
                lc = node << 1
                rc = lc | 1
                tree[lc] += v; lazy[lc] += v
                tree[rc] += v; lazy[rc] += v
                lazy[node] = 0
            mid = (l + r) >> 1
            if idx <= mid:
                node = node << 1
                r = mid
            else:
                node = (node << 1) | 1
                l = mid + 1
        return tree[node]

    # Build initial
    build(1, 1, M)
    # Process intervals
    for l, r in intervals:
        # find p1 = first x with f_old[x] >= l
        p1 = find_first_ge(l)
        if p1 is None:
            continue
        # find p2 = first x with f_old[x] > r
        p2 = find_first_ge(r + 1)
        if p2 is None:
            p2 = M + 1
        # add on [p1..p2-1]
        if p1 <= p2 - 1:
            add(1, 1, M, p1, p2 - 1)

    # Answer queries
    out = []
    w = out.append
    for x in queries:
        res = query_point(x)
        w(str(res))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()