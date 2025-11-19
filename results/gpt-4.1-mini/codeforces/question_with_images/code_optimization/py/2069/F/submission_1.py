import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class UndoableDSU:
    __slots__ = ['parent', 'size', 'history', 'components']
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.history = []
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.history.append((-1, -1, -1))
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.history.append((b, self.parent[b], self.size[a]))
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.components -= 1

    def snapshot(self):
        return len(self.history)

    def rollback(self, snap):
        while len(self.history) > snap:
            b, pb, sa = self.history.pop()
            if b == -1:
                continue
            a = self.parent[b]
            self.size[a] = sa
            self.parent[b] = pb
            self.components += 1

def process(n, q, queries, res):
    # We will use segment tree like approach to handle add/remove edges over time
    # For each edge, we store intervals [l, r) where it is active
    # Then we do a divide and conquer over time, adding edges active in the current segment,
    # recursing on children, and undoing changes after recursion.

    # Map edges to their add/remove times
    edge_map = {}
    intervals = []

    for i, (c, u, v) in enumerate(queries):
        if u > v:
            u, v = v, u
        key = (c, u, v)
        if key not in edge_map:
            edge_map[key] = []
        edge_map[key].append(i)

    # For each edge, create intervals of activity
    for key, times in edge_map.items():
        # times are sorted by insertion order
        # edges toggle presence on each query
        for i in range(0, len(times), 2):
            l = times[i]
            r = times[i+1] if i+1 < len(times) else q
            intervals.append((l, r, key[1], key[2]))

    # Build segment tree structure for intervals
    # seg[i] will hold edges active in segment i
    # We'll implement a recursive divide and conquer over [0, q)
    seg = [[] for _ in range(q*4)]

    def add_interval(idx, left, right, l, r, u, v):
        if r <= left or right <= l:
            return
        if l <= left and right <= r:
            seg[idx].append((u, v))
            return
        mid = (left + right) >> 1
        add_interval(idx*2, left, mid, l, r, u, v)
        add_interval(idx*2+1, mid, right, l, r, u, v)

    for l, r, u, v in intervals:
        add_interval(1, 0, q, l, r, u, v)

    dsu = UndoableDSU(n)
    ans = [0]*q

    def dfs(idx, left, right):
        snap = dsu.snapshot()
        for u, v in seg[idx]:
            dsu.union(u, v)
        if right - left == 1:
            ans[left] = dsu.components
        else:
            mid = (left + right) >> 1
            dfs(idx*2, left, mid)
            dfs(idx*2+1, mid, right)
        dsu.rollback(snap)

    dfs(1, 0, q)
    for i in range(q):
        res[i] = ans[i]

def main():
    n, q = map(int, input().split())
    queries = []
    for _ in range(q):
        c, u, v = input().split()
        u = int(u)-1
        v = int(v)-1
        queries.append((c, u, v))

    # We need to compute for each query:
    # minimal edges to add to A so that A includes B
    # This equals: number_of_components_in_B - number_of_components_in_A
    # after applying the query.

    # So we process graph A and graph B separately to get components count after each query.

    resA = [0]*q
    resB = [0]*q

    # Extract queries for A and B separately
    queriesA = [('A', u, v) for (c, u, v) in queries if c == 'A']
    queriesB = [('B', u, v) for (c, u, v) in queries if c == 'B']

    # But we need to process all queries in order, so we keep all queries but mark which graph
    # We'll process both graphs independently using the same approach.

    # For graph A:
    process(n, q, queries, resA)
    # For graph B:
    process(n, q, queries, resB)

    # Output difference
    output = []
    for i in range(q):
        output.append(str(resB[i] - resA[i]))
    print('\n'.join(output))

if __name__ == "__main__":
    main()