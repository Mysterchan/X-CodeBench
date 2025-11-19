import sys
import threading

sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())

    # We need to maintain dynamic connectivity for two graphs A and B.
    # After each update (add/remove edge), we must find minimal edges to add to A
    # so that A includes B.
    #
    # Inclusion means: each connected component of B is contained in some connected component of A.
    #
    # Let:
    #   - compA(v) = component id of vertex v in A
    #   - compB(v) = component id of vertex v in B
    #
    # For each component C_B in B, it must be fully inside some component C_A in A.
    # If a B-component is split across multiple A-components, we need to add edges in A to connect those A-components.
    #
    # The minimal number of edges to add is:
    #   sum over all B-components of (number of distinct A-components intersecting it - 1)
    #
    # We want to maintain this value dynamically.
    #
    # Approach:
    # - Maintain DSU for A and DSU for B.
    # - For each B-component, track how many distinct A-components it intersects.
    # - For each A-component, track how many vertices it has in each B-component.
    #
    # When A or B changes (edge added or removed), update DSUs and these counts.
    #
    # The problem is dynamic connectivity with edge insertions and deletions.
    # We can use offline approach with "divide and conquer" on time or use Euler Tour Tree or Link-Cut Tree.
    #
    # Here, we will use the standard offline approach with "edge insertion/deletion" intervals:
    # - For each edge, track intervals when it exists.
    # - Build segment tree over time.
    # - On each segment tree node, add edges active in that interval.
    # - Use DSU with rollback to maintain connectivity.
    #
    # We will maintain two DSUs: one for A and one for B.
    # For each DSU, we maintain:
    #   - parent, size
    #   - For each component, a map from the other graph's component id to count of vertices in intersection.
    #
    # We also maintain for each B-component:
    #   - how many distinct A-components it intersects
    #
    # The answer is sum over B-components of (count of distinct A-components - 1).
    #
    # We maintain a global variable "answer" = sum of (distinct A-components per B-component - 1).
    #
    # When merges happen in A or B, we update these counts accordingly.
    #
    # Implementation details:
    # - We assign each edge an id and track its add/remove intervals.
    # - Build segment tree over [1..q].
    # - For each query, we toggle edge presence.
    # - After processing each query, output current answer.
    #
    # Complexity: O(q log q) with efficient DSU rollback.

    # DSU with rollback and extra data
    class DSU:
        __slots__ = ['parent', 'size', 'history', 'comp_count']

        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1]*n
            self.history = []
            self.comp_count = n  # number of components

        def find(self, x):
            while self.parent[x] != x:
                x = self.parent[x]
            return x

        def union(self, a, b):
            a = self.find(a)
            b = self.find(b)
            if a == b:
                self.history.append((-1, -1, -1, -1))
                return False
            if self.size[a] < self.size[b]:
                a, b = b, a
            # a is bigger
            self.history.append((b, self.parent[b], a, self.size[a]))
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.comp_count -= 1
            return True

        def snapshot(self):
            return len(self.history)

        def rollback(self, snap):
            while len(self.history) > snap:
                b, pb, a, sa = self.history.pop()
                if b == -1:
                    continue
                self.parent[b] = pb
                self.size[a] = sa
                self.comp_count += 1

    # We need to maintain the intersection counts between A and B components.
    # For that, we maintain:
    # For each vertex v:
    #   - compA[v] = DSU_A.find(v)
    #   - compB[v] = DSU_B.find(v)
    #
    # For each B-component root b_root:
    #   - map from A-component root to count of vertices in intersection
    #
    # For each A-component root a_root:
    #   - map from B-component root to count of vertices in intersection
    #
    # We maintain these maps in a global structure with rollback.
    #
    # Also maintain for each B-component root:
    #   - how many distinct A-components it intersects
    #
    # answer = sum over B-components of (distinct A-components - 1)
    #
    # When merges happen in A or B, we update these maps and answer accordingly.
    #
    # To do this efficiently, we store for each vertex its current compA and compB roots.
    # When DSU merges happen, we merge these maps accordingly.
    #
    # We implement a structure IntersectionTracker with rollback.

    from collections import defaultdict

    class IntersectionTracker:
        def __init__(self, n):
            # For each B-component root: dict A_root -> count
            self.b_to_a = [defaultdict(int) for _ in range(n)]
            # For each A-component root: dict B_root -> count
            self.a_to_b = [defaultdict(int) for _ in range(n)]

            # For each vertex: current compA and compB
            self.compA = list(range(n))
            self.compB = list(range(n))

            # For each B-component root: number of distinct A-components intersecting it
            self.b_distinct_a = [1]*n  # initially each vertex alone, so 1
            # For each A-component root: number of distinct B-components intersecting it
            # (not needed for answer, but useful for merges)
            # self.a_distinct_b = [1]*n

            # answer = sum over B-components of (distinct A-components - 1)
            # Initially all singletons: distinct A-components = 1 for each B-component
            # So answer = sum (1-1) = 0
            self.answer = 0

            # We keep track of which B-components are alive (roots)
            # Initially all vertices are separate B-components
            self.b_alive = [True]*n
            self.a_alive = [True]*n

            # History stack for rollback:
            # Each entry: (type, data)
            # type:
            # 0 - update b_to_a: (b_root, a_root, old_count)
            # 1 - update a_to_b: (a_root, b_root, old_count)
            # 2 - update b_distinct_a: (b_root, old_value)
            # 3 - update a_distinct_b: (a_root, old_value) - not used
            # 4 - update compA[v]: (v, old_compA)
            # 5 - update compB[v]: (v, old_compB)
            # 6 - update answer: old_answer
            # 7 - mark b_alive[b_root] = False or True
            # 8 - mark a_alive[a_root] = False or True

            self.history = []

        def _update_b_to_a(self, b_root, a_root, delta):
            d = self.b_to_a[b_root]
            old_count = d.get(a_root, 0)
            new_count = old_count + delta
            self.history.append((0, b_root, a_root, old_count))
            if new_count == 0:
                del d[a_root]
                # distinct count decreases by 1
                old_distinct = self.b_distinct_a[b_root]
                self.history.append((2, b_root, old_distinct))
                self.b_distinct_a[b_root] = old_distinct - 1
                self._update_answer(-1)
            else:
                d[a_root] = new_count
                if old_count == 0:
                    # distinct count increases by 1
                    old_distinct = self.b_distinct_a[b_root]
                    self.history.append((2, b_root, old_distinct))
                    self.b_distinct_a[b_root] = old_distinct + 1
                    self._update_answer(1)

        def _update_a_to_b(self, a_root, b_root, delta):
            d = self.a_to_b[a_root]
            old_count = d.get(b_root, 0)
            new_count = old_count + delta
            self.history.append((1, a_root, b_root, old_count))
            if new_count == 0:
                del d[b_root]
                # We don't track distinct B-components count for answer, so no answer update here
            else:
                d[b_root] = new_count
                # no answer update here

        def _update_answer(self, delta):
            old_answer = self.answer
            self.history.append((6, old_answer))
            self.answer += delta

        def set_compA(self, v, new_comp):
            old_comp = self.compA[v]
            if old_comp == new_comp:
                self.history.append((4, v, old_comp))
                return
            self.history.append((4, v, old_comp))
            self.compA[v] = new_comp

        def set_compB(self, v, new_comp):
            old_comp = self.compB[v]
            if old_comp == new_comp:
                self.history.append((5, v, old_comp))
                return
            self.history.append((5, v, old_comp))
            self.compB[v] = new_comp

        def add_vertex(self, v):
            # Called when vertex v is initially alone in A and B
            # Add intersection count 1 for (b_root, a_root)
            b_root = self.compB[v]
            a_root = self.compA[v]
            self._update_b_to_a(b_root, a_root, 1)
            self._update_a_to_b(a_root, b_root, 1)

        def remove_vertex(self, v):
            # Remove intersection count 1 for (b_root, a_root)
            b_root = self.compB[v]
            a_root = self.compA[v]
            self._update_b_to_a(b_root, a_root, -1)
            self._update_a_to_b(a_root, b_root, -1)

        def merge_A(self, a_root, b_root):
            # Merge two A-components: a_root absorbs b_root
            # Merge a_to_b maps: move all b_root's B-components counts to a_root
            # For each B-component in a_to_b[b_root], update b_to_a accordingly
            d_from = self.a_to_b[b_root]
            d_to = self.a_to_b[a_root]

            # For each B-component in d_from:
            for b_comp, cnt in list(d_from.items()):
                # Remove old counts
                self._update_b_to_a(b_comp, b_root, -cnt)
                self._update_b_to_a(b_comp, a_root, cnt)
                self._update_a_to_b(a_root, b_comp, cnt)
                self._update_a_to_b(b_root, b_comp, -cnt)
            # Merge dicts
            for k, v in d_from.items():
                d_to[k] = d_to.get(k, 0) + v
            d_from.clear()

            # Mark b_root as dead
            self.history.append((8, b_root, True))
            self.a_alive[b_root] = False

        def merge_B(self, a_root, b_root):
            # Merge two B-components: a_root absorbs b_root
            # Merge b_to_a maps: move all b_root's A-components counts to a_root
            d_from = self.b_to_a[b_root]
            d_to = self.b_to_a[a_root]

            for a_comp, cnt in list(d_from.items()):
                # Remove old counts
                self._update_a_to_b(a_comp, b_root, -cnt)
                self._update_a_to_b(a_comp, a_root, cnt)
                self._update_b_to_a(a_root, a_comp, cnt)
                self._update_b_to_a(b_root, a_comp, -cnt)
            # Merge dicts
            for k, v in d_from.items():
                d_to[k] = d_to.get(k, 0) + v
            d_from.clear()

            # Update answer: distinct A-components for new B-component = sum distinct A-components of merged
            old_distinct_a_a = self.b_distinct_a[a_root]
            old_distinct_a_b = self.b_distinct_a[b_root]
            self.history.append((2, a_root, old_distinct_a_a))
            self.history.append((2, b_root, old_distinct_a_b))
            self.b_distinct_a[a_root] = len(self.b_to_a[a_root])
            self.b_distinct_a[b_root] = 0
            self._update_answer(- (old_distinct_a_a - 1) - (old_distinct_a_b - 1))
            self._update_answer(self.b_distinct_a[a_root] - 1)

            # Mark b_root as dead
            self.history.append((7, b_root, True))
            self.b_alive[b_root] = False

        def rollback(self, snap):
            while len(self.history) > snap:
                t = self.history.pop()
                tp = t[0]
                if tp == 0:
                    # b_to_a update
                    _, b_root, a_root, old_count = t
                    d = self.b_to_a[b_root]
                    if old_count == 0:
                        # was removed
                        d.pop(a_root, None)
                    else:
                        d[a_root] = old_count
                elif tp == 1:
                    # a_to_b update
                    _, a_root, b_root, old_count = t
                    d = self.a_to_b[a_root]
                    if old_count == 0:
                        d.pop(b_root, None)
                    else:
                        d[b_root] = old_count
                elif tp == 2:
                    # b_distinct_a update
                    _, b_root, old_val = t
                    self.b_distinct_a[b_root] = old_val
                elif tp == 3:
                    # a_distinct_b update (not used)
                    pass
                elif tp == 4:
                    # compA update
                    _, v, old_comp = t
                    self.compA[v] = old_comp
                elif tp == 5:
                    # compB update
                    _, v, old_comp = t
                    self.compB[v] = old_comp
                elif tp == 6:
                    # answer update
                    _, old_answer = t
                    self.answer = old_answer
                elif tp == 7:
                    # b_alive update
                    _, b_root, old_val = t
                    self.b_alive[b_root] = old_val
                elif tp == 8:
                    # a_alive update
                    _, a_root, old_val = t
                    self.a_alive[a_root] = old_val

    # We will implement DSU with rollback and intersection tracker combined.

    # We need to handle merges in DSU_A and DSU_B and update intersection tracker accordingly.

    # For DSU_A:
    # When merging two components a and b:
    #   - merge a_to_b maps in intersection tracker
    #   - update compA[v] for all vertices in smaller component to new root
    # For efficiency, we do not update compA[v] for all vertices explicitly,
    # but we can store compA[v] = DSU_A.find(v) on demand.
    # But intersection tracker needs compA[v] for each vertex.
    #
    # To avoid O(n) updates, we store compA[v] explicitly and update on merges.
    # We keep track of vertices in each component to update compA[v].
    #
    # Similarly for DSU_B.

    # To avoid complexity, we store for each vertex its compA and compB explicitly,
    # and when merging DSU, we update compA or compB for vertices in smaller component.

    # To do this efficiently, we maintain for each DSU component a list of vertices.

    class DSUWithVertices:
        __slots__ = ['parent', 'size', 'history', 'comp_count', 'verts']

        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1]*n
            self.history = []
            self.comp_count = n
            self.verts = [[i] for i in range(n)]

        def find(self, x):
            while self.parent[x] != x:
                x = self.parent[x]
            return x

        def union(self, a, b, is_A):
            a = self.find(a)
            b = self.find(b)
            if a == b:
                self.history.append((-1, -1, -1, -1, []))
                return False
            if self.size[a] < self.size[b]:
                a, b = b, a
            # a is bigger
            self.history.append((b, self.parent[b], a, self.size[a], self.verts[b][:]))
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.comp_count -= 1

            # Update compA or compB for vertices in b's component
            if is_A:
                for v in self.verts[b]:
                    tracker.set_compA(v, a)
            else:
                for v in self.verts[b]:
                    tracker.set_compB(v, a)

            # Merge vertex lists
            self.verts[a].extend(self.verts[b])
            self.verts[b].clear()

            # Update intersection tracker merges
            if is_A:
                tracker.merge_A(a, b)
            else:
                tracker.merge_B(a, b)

            return True

        def snapshot(self):
            return len(self.history)

        def rollback(self, snap, is_A):
            while len(self.history) > snap:
                b, pb, a, sa, verts_b = self.history.pop()
                if b == -1:
                    continue
                # Rollback intersection tracker merges
                # We do not rollback merges explicitly here,
                # intersection tracker rollback will handle it.

                self.parent[b] = pb
                self.size[a] = sa
                self.comp_count += 1

                # Rollback compA or compB for vertices in b's component
                # We must revert compA/compB[v] to b for vertices in verts_b
                if is_A:
                    for v in verts_b:
                        tracker.set_compA(v, b)
                else:
                    for v in verts_b:
                        tracker.set_compB(v, b)

                # Rollback vertex lists
                # Remove verts_b from a's list and restore to b
                for v in verts_b:
                    self.verts[a].pop()
                self.verts[b] = verts_b

    # Now we implement offline processing of queries with segment tree.

    # We need to track edges in A and B separately.
    # For each edge, track intervals when it exists.

    # We'll map edges to ids and store their intervals.

    # Since edges can be added and removed multiple times, we track toggle times.

    # We'll store for each graph a dict: edge -> list of toggle times

    edges_A = dict()
    edges_B = dict()

    queries = []
    for i in range(q):
        c, x, y = input().split()
        x = int(x)-1
        y = int(y)-1
        if x > y:
            x, y = y, x
        queries.append((c, x, y))

    # For each graph, for each edge, store toggle times
    def add_toggle(d, e, t):
        if e not in d:
            d[e] = []
        d[e].append(t)

    for i, (c, x, y) in enumerate(queries):
        if c == 'A':
            add_toggle(edges_A, (x,y), i)
        else:
            add_toggle(edges_B, (x,y), i)

    # For each edge, build intervals of existence
    # If odd number of toggles, last interval goes to q

    def build_intervals(d):
        intervals = []
        for e, times in d.items():
            times.sort()
            for i in range(0, len(times), 2):
                start = times[i]
                end = times[i+1] if i+1 < len(times) else q
                intervals.append((start, end, e))
        return intervals

    intervals_A = build_intervals(edges_A)
    intervals_B = build_intervals(edges_B)

    # Build segment tree over [0..q-1]
    # Each node stores edges active in that interval

    size = 1
    while size < q:
        size <<= 1

    segtree_A = [[] for _ in range(size*2)]
    segtree_B = [[] for _ in range(size*2)]

    def add_edge(seg, l, r, e, idx=1, left=0, right=size):
        if r <= left or right <= l:
            return
        if l <= left and right <= r:
            seg[idx].append(e)
            return
        mid = (left+right)//2
        add_edge(seg, l, r, e, idx*2, left, mid)
        add_edge(seg, l, r, e, idx*2+1, mid, right)

    for l, r, e in intervals_A:
        add_edge(segtree_A, l, r, e)
    for l, r, e in intervals_B:
        add_edge(segtree_B, l, r, e)

    # Initialize DSUs and tracker
    tracker = IntersectionTracker(n)
    dsuA = DSUWithVertices(n)
    dsuB = DSUWithVertices(n)

    # Initially, each vertex is alone in A and B
    # So intersection tracker must be initialized with each vertex intersection count
    for v in range(n):
        tracker.set_compA(v, v)
        tracker.set_compB(v, v)
        tracker.add_vertex(v)

    res = [0]*q

    def dfs(idx, left, right):
        snapA = dsuA.snapshot()
        snapB = dsuB.snapshot()
        snapT = len(tracker.history)

        # Add edges active in this segment
        for (x,y) in segtree_A[idx]:
            dsuA.union(x,y, True)
        for (x,y) in segtree_B[idx]:
            dsuB.union(x,y, False)

        if right - left == 1:
            # leaf node, output answer
            res[left] = tracker.answer
        else:
            mid = (left+right)//2
            dfs(idx*2, left, mid)
            dfs(idx*2+1, mid, right)

        # rollback
        tracker.rollback(snapT)
        dsuA.rollback(snapA, True)
        dsuB.rollback(snapB, False)

    dfs(1, 0, size)

    print('\n'.join(map(str, res[:q])))

threading.Thread(target=main).start()