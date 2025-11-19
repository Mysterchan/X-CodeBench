import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# We need to maintain dynamic connectivity for two graphs A and B.
# After each query, we want to find the minimum number of edges to add to A so that A includes B.
# Inclusion means: every connected component of B is fully contained in some connected component of A.
# Equivalently, for each connected component of B, it must be contained in a connected component of A.
# If a B-component spans multiple A-components, we need to add edges to A to connect those A-components.
# The minimal number of edges to add is sum over B-components of (number of A-components intersecting it - 1).

# We will maintain DSU (Disjoint Set Union) for both graphs A and B.
# We need to efficiently track, for each B-component, how many A-components it intersects.
# When edges are added or removed, components can merge or split.
# But splitting is hard in DSU, so we use a technique:
# We keep track of edges in each graph and maintain a DSU with rollback or persistent DSU.
# But since edges can be added or removed, we need a data structure supporting dynamic connectivity with edge insertions and deletions.
# This is a classic problem solved by "offline" approach using divide and conquer on the queries or using Euler Tour Tree or Link-Cut Tree.
# But constraints are large (up to 4*10^5), so we need an efficient approach.

# Observation:
# Each edge is toggled at most once per query (added if not present, removed if present).
# So each edge appears in a set of intervals (time intervals when it is present).
# We can process queries offline using a segment tree over time intervals.
# For each edge, we know the intervals it is active.
# We add the edge to the segment tree nodes covering its active intervals.
# Then we do a DFS on the segment tree, adding edges to DSU at each node, answering queries at leaves.
# We maintain DSU with rollback to undo merges after processing each segment.

# We need two DSUs: one for A and one for B.
# We also need to maintain the count of how many A-components each B-component intersects.
# For that, we maintain a map from B-component to a multiset of A-components it intersects.
# But sets are expensive, so we maintain counts:
# For each B-component root, we keep a count of how many A-components it intersects.
# For each vertex, we know its A-root and B-root.
# When A or B DSU merges, we update these counts accordingly.

# Implementation plan:
# 1. Parse queries, track edges for A and B separately.
# 2. For each edge, record intervals of presence.
# 3. Build segment tree over time [1..q].
# 4. Insert edges into segment tree nodes covering their active intervals.
# 5. Implement DSU with rollback for A and B.
# 6. Maintain for each B-component the count of distinct A-components it intersects.
# 7. When merging B-components, merge their A-component sets and update counts.
# 8. When merging A-components, update counts for all B-components intersecting these A-components.
# 9. At each query (leaf of segment tree), output sum over B-components of (count of A-components intersecting it - 1).
#    This sum = total number of B-components - number of B-components fully contained in one A-component.
#    But easier to maintain sum of (count - 1) over all B-components.

# To avoid iterating over all B-components, we maintain a global variable:
# total_needed = sum over B-components of (number of A-components intersecting it - 1)
# Initially, all vertices are isolated, so each B-component = vertex, each A-component = vertex,
# so total_needed = 0.

# When merging B-components:
# - The new B-component is union of two sets.
# - The number of A-components intersecting new B-component is union of two sets of A-components.
# - We update total_needed accordingly.

# When merging A-components:
# - For each B-component intersecting both A-components, the number of A-components intersecting it decreases by 1.
# - So total_needed decreases accordingly.

# We need to maintain for each B-component root:
# - a map from A-component root to count of vertices in intersection.
# - the number of distinct A-components intersecting it = size of this map.

# When merging B-components:
# - merge their maps, update total_needed.

# When merging A-components:
# - For each B-component that intersects both A-components, merge the two A-components in that B-component's map,
#   decreasing distinct A-components count by 1, update total_needed.

# To implement efficiently:
# - For each vertex, we know its A-root and B-root.
# - For each B-root, maintain a dict: A-root -> count.
# - For each A-root, maintain a set of B-roots intersecting it.

# When merging A-components:
# - We merge smaller A-root into bigger.
# - For each B-root in smaller A-root's set:
#   - In B-root's map, decrease count for smaller A-root, increase count for bigger A-root.
#   - If smaller A-root count > 0 and bigger A-root count == 0 before, distinct A-components count decreases by 1.
#   - Update total_needed accordingly.
# - Merge B-root sets.

# When merging B-components:
# - Merge smaller B-root into bigger.
# - Merge their maps of A-root counts.
# - For each A-root in smaller B-root's map:
#   - If A-root not in bigger B-root's map, distinct A-components count increases by 1.
# - Update total_needed accordingly.
# - Merge sets of A-roots.

# We need DSU with rollback for A and B.
# Also rollback for the maps and sets.

# This is complex but doable.

# Let's implement.

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.history = []
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1, -1))
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.history.append((y, self.parent[y], x, self.size[x]))
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True
    def rollback(self):
        y, py, x, sx = self.history.pop()
        if y == -1:
            return
        self.parent[y] = py
        self.size[x] = sx

# We will maintain:
# For each B-root:
#   - a dict: A-root -> count of vertices in intersection
#   - distinct_count = number of keys in dict
# For each A-root:
#   - a set of B-roots intersecting it

# We need rollback for these structures as well.

# To implement rollback for dicts and sets, we keep a stack of operations.

class RollbackDict:
    def __init__(self):
        self.d = dict()
        self.history = []
        self.size = 0
    def get(self, key):
        return self.d.get(key, 0)
    def inc(self, key, delta):
        old = self.d.get(key, 0)
        new = old + delta
        self.history.append((key, old))
        if new == 0:
            if key in self.d:
                del self.d[key]
                self.size -= 1
        else:
            if old == 0:
                self.size += 1
            self.d[key] = new
    def rollback(self):
        key, old = self.history.pop()
        cur = self.d.get(key, 0)
        if old == 0:
            if key in self.d:
                del self.d[key]
                self.size -= 1
        else:
            if cur == 0:
                self.size += 1
            self.d[key] = old

class RollbackSet:
    def __init__(self):
        self.s = set()
        self.history = []
    def add(self, x):
        if x not in self.s:
            self.s.add(x)
            self.history.append((x, True))
        else:
            self.history.append((x, False))
    def remove(self, x):
        if x in self.s:
            self.s.remove(x)
            self.history.append((x, True))
        else:
            self.history.append((x, False))
    def rollback(self):
        x, added = self.history.pop()
        if added:
            self.s.remove(x)
        else:
            self.s.add(x)
    def __contains__(self, x):
        return x in self.s
    def __iter__(self):
        return iter(self.s)
    def __len__(self):
        return len(self.s)

# Now we implement the main logic.

n, q = map(int, input().split())

# We will store edges for A and B separately.
# For each edge, we store the times it is toggled.
# Then we build intervals of presence.

# We need a mapping from edge to last toggle time.
# Edges are undirected, so store (min, max).

edge_map_A = dict()
edge_map_B = dict()

queries = []
for _ in range(q):
    c, x, y = input().split()
    x = int(x)-1
    y = int(y)-1
    if x > y:
        x, y = y, x
    queries.append((c, x, y))

# For each edge in A and B, store intervals of presence.
# We'll store intervals as (start, end) inclusive.

def build_intervals(queries, graph_char):
    last = dict()
    intervals = []
    for i, (c, x, y) in enumerate(queries, 1):
        if c != graph_char:
            continue
        e = (x, y)
        if e in last:
            intervals.append((last[e], i-1, e))
            del last[e]
        else:
            last[e] = i
    for e, start in last.items():
        intervals.append((start, q, e))
    return intervals

intervals_A = build_intervals(queries, 'A')
intervals_B = build_intervals(queries, 'B')

# Build segment tree over [1..q]
# Each node stores edges active in that interval.

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(4*n)]
    def add(self, l, r, edge, idx=1, tl=1, tr=None):
        if tr is None:
            tr = self.n
        if r < tl or tr < l:
            return
        if l <= tl and tr <= r:
            self.tree[idx].append(edge)
            return
        tm = (tl+tr)//2
        self.add(l, r, edge, idx*2, tl, tm)
        self.add(l, r, edge, idx*2+1, tm+1, tr)
    def get(self, idx=1, tl=1, tr=None):
        if tr is None:
            tr = self.n
        if tl == tr:
            yield idx, tl
        else:
            tm = (tl+tr)//2
            yield from self.get(idx*2, tl, tm)
            yield from self.get(idx*2+1, tm+1, tr)

# Insert edges into segment trees
segA = SegmentTree(q)
for l, r, e in intervals_A:
    segA.add(l, r, e)
segB = SegmentTree(q)
for l, r, e in intervals_B:
    segB.add(l, r, e)

# DSU for A and B
dsuA = DSU(n)
dsuB = DSU(n)

# For each B-root: map A-root -> count
# We'll store these in a dict: b_root -> RollbackDict
# For each A-root: set of B-roots intersecting it
# We'll store these in a dict: a_root -> RollbackSet

# Initially, each vertex is its own component in A and B.
# So for each vertex v:
#   B-root = v
#   A-root = v
#   b_map[v] = {v:1}
#   a_set[v] = {v}

b_map = [RollbackDict() for _ in range(n)]
a_set = [RollbackSet() for _ in range(n)]

for v in range(n):
    b_map[v].inc(v, 1)
    a_set[v].add(v)

# total_needed = sum over B-components of (number of A-components intersecting it - 1)
# Initially, each B-component has 1 A-component intersecting it, so total_needed = 0
total_needed = 0

# We need to implement union operations with updates to b_map, a_set and total_needed.

# Helper functions:

def b_root(v):
    return dsuB.find(v)
def a_root(v):
    return dsuA.find(v)

def merge_b(x, y):
    global total_needed
    x = dsuB.find(x)
    y = dsuB.find(y)
    if x == y:
        dsuB.history.append((-1, -1, -1, -1))
        return
    # Union by size
    if dsuB.size[x] < dsuB.size[y]:
        x, y = y, x
    # Save history for rollback
    dsuB.history.append((y, dsuB.parent[y], x, dsuB.size[x]))
    dsuB.parent[y] = x
    dsuB.size[x] += dsuB.size[y]

    # Merge b_map[y] into b_map[x]
    # For each A-root in b_map[y], update b_map[x]
    # Update total_needed accordingly

    # distinct counts before merge
    distinct_x = b_map[x].size
    distinct_y = b_map[y].size

    # For rollback, we need to record changes in b_map[x]
    # We'll just do inc operations and rollback them later

    for a_r, cnt in list(b_map[y].d.items()):
        old_cnt = b_map[x].get(a_r)
        b_map[x].inc(a_r, cnt)
        new_cnt = old_cnt + cnt
        # If old_cnt == 0 and new_cnt > 0, distinct count increases by 1
        # So total_needed increases by 1 for this B-component
        # But we are merging two B-components, so total_needed changes by:
        # (distinct_x - 1) + (distinct_y - 1) -> old total for these two components
        # After merge: (new distinct - 1)
        # So total_needed += (new distinct - 1) - (distinct_x - 1) - (distinct_y - 1)
        # We'll do this after merging all keys

    new_distinct = b_map[x].size
    # total_needed changes by:
    # new_distinct - 1 - (distinct_x - 1) - (distinct_y - 1) = new_distinct - distinct_x - distinct_y + 1
    total_needed += new_distinct - distinct_x - distinct_y + 1

    # Merge a_set[y] into a_set[x]
    # For rollback, record additions
    # Add all elements from a_set[y] to a_set[x]
    for b_r in list(a_set[y].s):
        a_set[x].add(b_r)

def rollback_b():
    global total_needed
    # Rollback a_set merge
    # We don't know how many elements were added, but rollback removes last added elements
    # Rollback b_map changes
    # Rollback dsuB union

    # Rollback a_set[x]
    # We must rollback all additions done in last merge_b call
    # But we don't know x here, so we must store x in dsuB.history

    y, py, x, sx = dsuB.history.pop()
    if y == -1:
        return
    # Rollback a_set[x]
    # We don't know how many elements were added, but we can rollback until a_set[x].history length is restored
    # We'll store history length before merge_b and restore it here
    # To do this, we need to store history length in dsuB.history

    # We'll store a_set[x] history length before merge in dsuB.history
    # So modify merge_b to store that

    # For now, just rollback b_map[x] changes and a_set[x] changes

    # Rollback b_map[x]
    # We don't know how many inc operations were done, but we can rollback until b_map[x].history length is restored
    # We'll store b_map[x] history length before merge in dsuB.history

    # So we need to change merge_b to store these lengths

    # We'll redo merge_b with these changes

# We need to rewrite merge_b and rollback_b to store history lengths for rollback.

# Similarly for merge_a and rollback_a.

# Let's implement a class to handle these merges with rollback.

class DSUWithMaps:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1]*n
        self.history = []

        # For B DSU: b_map: list of RollbackDict
        # For A DSU: a_set: list of RollbackSet

        self.b_map = [RollbackDict() for _ in range(n)]
        self.a_set = [RollbackSet() for _ in range(n)]

        for v in range(n):
            self.b_map[v].inc(v, 1)
            self.a_set[v].add(v)

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union_b(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1, -1, 0, 0))
            return 0
        if self.size[x] < self.size[y]:
            x, y = y, x
        # Save history lengths for rollback
        b_map_x_hist_len = len(self.b_map[x].history)
        a_set_x_hist_len = len(self.a_set[x].history)

        self.history.append((y, self.parent[y], x, self.size[x], b_map_x_hist_len, a_set_x_hist_len))

        self.parent[y] = x
        self.size[x] += self.size[y]

        distinct_x = self.b_map[x].size
        distinct_y = self.b_map[y].size

        # Merge b_map[y] into b_map[x]
        for a_r, cnt in list(self.b_map[y].d.items()):
            self.b_map[x].inc(a_r, cnt)

        new_distinct = self.b_map[x].size

        # Merge a_set[y] into a_set[x]
        for b_r in list(self.a_set[y].s):
            self.a_set[x].add(b_r)

        delta = new_distinct - distinct_x - distinct_y + 1
        return delta

    def rollback_b(self):
        y, py, x, sx, b_map_x_hist_len, a_set_x_hist_len = self.history.pop()
        if y == -1:
            return 0
        # Rollback a_set[x]
        while len(self.a_set[x].history) > a_set_x_hist_len:
            self.a_set[x].rollback()
        # Rollback b_map[x]
        while len(self.b_map[x].history) > b_map_x_hist_len:
            self.b_map[x].rollback()
        self.parent[y] = py
        self.size[x] = sx
        return 0

    def union_a(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1, -1, 0))
            return 0
        if self.size[x] < self.size[y]:
            x, y = y, x
        # Save history lengths for rollback
        a_set_x_hist_len = len(self.a_set[x].history)
        a_set_y_hist_len = len(self.a_set[y].history)

        self.history.append((y, self.parent[y], x, self.size[x], a_set_x_hist_len))

        self.parent[y] = x
        self.size[x] += self.size[y]

        # When merging A-components x and y:
        # For each B-root in a_set[y], update b_map of that B-root:
        # decrease count for y, increase count for x
        # If count for y > 0 and count for x == 0 before, distinct count decreases by 1
        # So total_needed decreases by number of such B-roots

        delta = 0
        for b_r in list(self.a_set[y].s):
            # b_r is B-root
            # b_map[b_r] is dict A-root -> count
            b_map_b = self.b_map[b_r]
            cnt_y = b_map_b.get(y)
            cnt_x = b_map_b.get(x)
            # Update counts
            b_map_b.inc(y, -cnt_y)
            b_map_b.inc(x, cnt_y)
            # If cnt_x == 0 before and cnt_y > 0, distinct count decreases by 1
            if cnt_x == 0 and cnt_y > 0:
                delta -= 1
        # Merge a_set[y] into a_set[x]
        for b_r in list(self.a_set[y].s):
            self.a_set[x].add(b_r)
        return delta

    def rollback_a(self):
        y, py, x, sx, a_set_x_hist_len = self.history.pop()
        if y == -1:
            return 0
        # Rollback a_set[x]
        while len(self.a_set[x].history) > a_set_x_hist_len:
            self.a_set[x].rollback()
        # Rollback b_map for all b_r in a_set[x]?
        # We must rollback b_map changes done in union_a
        # But we don't store b_map history length here, so we must store it

        # To fix this, we must store b_map history lengths for each b_r updated in union_a
        # This is complicated, so we will store all b_map history lengths before union_a and rollback all after

        # We'll change union_a to store b_map history lengths for all b_r updated

        # For now, we will store b_map history lengths for all b_r updated in union_a

        # So we need to rewrite union_a and rollback_a again

# We need to store b_map history lengths for each b_r updated in union_a

# Let's rewrite union_a and rollback_a:

class DSUWithMapsV2:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1]*n
        self.history = []

        self.b_map = [RollbackDict() for _ in range(n)]
        self.a_set = [RollbackSet() for _ in range(n)]

        for v in range(n):
            self.b_map[v].inc(v, 1)
            self.a_set[v].add(v)

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union_b(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1, -1, 0, 0))
            return 0
        if self.size[x] < self.size[y]:
            x, y = y, x
        b_map_x_hist_len = len(self.b_map[x].history)
        a_set_x_hist_len = len(self.a_set[x].history)

        self.history.append((y, self.parent[y], x, self.size[x], b_map_x_hist_len, a_set_x_hist_len))

        self.parent[y] = x
        self.size[x] += self.size[y]

        distinct_x = self.b_map[x].size
        distinct_y = self.b_map[y].size

        for a_r, cnt in list(self.b_map[y].d.items()):
            self.b_map[x].inc(a_r, cnt)

        new_distinct = self.b_map[x].size

        for b_r in list(self.a_set[y].s):
            self.a_set[x].add(b_r)

        delta = new_distinct - distinct_x - distinct_y + 1
        return delta

    def rollback_b(self):
        y, py, x, sx, b_map_x_hist_len, a_set_x_hist_len = self.history.pop()
        if y == -1:
            return 0
        while len(self.a_set[x].history) > a_set_x_hist_len:
            self.a_set[x].rollback()
        while len(self.b_map[x].history) > b_map_x_hist_len:
            self.b_map[x].rollback()
        self.parent[y] = py
        self.size[x] = sx
        return 0

    def union_a(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1, -1, [], []))
            return 0
        if self.size[x] < self.size[y]:
            x, y = y, x

        a_set_x_hist_len = len(self.a_set[x].history)
        a_set_y_hist_len = len(self.a_set[y].history)

        # For each b_r in a_set[y], store b_map history length before update
        b_map_hist_lens = []
        b_rs = list(self.a_set[y].s)
        for b_r in b_rs:
            b_map_hist_lens.append(len(self.b_map[b_r].history))

        self.history.append((y, self.parent[y], x, self.size[x], a_set_x_hist_len, b_rs, b_map_hist_lens))

        self.parent[y] = x
        self.size[x] += self.size[y]

        delta = 0
        for i, b_r in enumerate(b_rs):
            b_map_b = self.b_map[b_r]
            cnt_y = b_map_b.get(y)
            cnt_x = b_map_b.get(x)
            b_map_b.inc(y, -cnt_y)
            b_map_b.inc(x, cnt_y)
            if cnt_x == 0 and cnt_y > 0:
                delta -= 1

        for b_r in b_rs:
            self.a_set[x].add(b_r)

        return delta

    def rollback_a(self):
        y, py, x, sx, a_set_x_hist_len, b_rs, b_map_hist_lens = self.history.pop()
        if y == -1:
            return 0
        while len(self.a_set[x].history) > a_set_x_hist_len:
            self.a_set[x].rollback()
        for b_r, hist_len in zip(b_rs, b_map_hist_lens):
            while len(self.b_map[b_r].history) > hist_len:
                self.b_map[b_r].rollback()
        self.parent[y] = py
        self.size[x] = sx
        return 0

# Now we have DSUWithMapsV2 for both A and B.

dsuA = DSUWithMapsV2(n)
dsuB = DSUWithMapsV2(n)

total_needed = 0

# Now we implement the segment tree traversal.

# We will do a recursive DFS on segment tree nodes.
# At each node:
#   - add edges of A to dsuA
#   - add edges of B to dsuB
#   - update total_needed accordingly
#   - if leaf node (query), print total_needed
#   - rollback changes before returning

# For edges in A:
#   union_a in dsuA, update total_needed by delta returned
# For edges in B:
#   union_b in dsuB, update total_needed by delta returned

# For rollback:
#   rollback_b for B edges
#   rollback_a for A edges

# We must store the order of unions to rollback in reverse order.

# We'll implement a recursive function:

sys.setrecursionlimit(1 << 25)

def dfs(idx, tl, tr):
    global total_needed
    # Add edges in A
    a_deltas = []
    for x, y in segA.tree[idx]:
        delta = dsuA.union_a(x, y)
        total_needed += delta
        a_deltas.append(delta)
    # Add edges in B
    b_deltas = []
    for x, y in segB.tree[idx]:
        delta = dsuB.union_b(x, y)
        total_needed += delta
        b_deltas.append(delta)
    if tl == tr:
        # Output total_needed
        print(total_needed)
    else:
        tm = (tl+tr)//2
        dfs(idx*2, tl, tm)
        dfs(idx*2+1, tm+1, tr)
    # Rollback B edges
    for _ in segB.tree[idx]:
        dsuB.rollback_b()
    # Rollback A edges
    for _ in segA.tree[idx]:
        dsuA.rollback_a()
    # Rollback total_needed
    for delta in reversed(b_deltas):
        total_needed -= delta
    for delta in reversed(a_deltas):
        total_needed -= delta

dfs(1, 1, q)