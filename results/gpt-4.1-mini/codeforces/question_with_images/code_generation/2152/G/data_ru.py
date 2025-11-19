import sys
import threading
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    t = int(input())
    
    # We will process all test cases one by one.
    # The main challenge is to efficiently:
    # - maintain the minimal number of root-to-leaf paths covering all monster nodes
    # - after toggling monsters in a subtree
    
    # Key observations:
    # 1) The minimal number of root-to-leaf paths covering all monster nodes
    #    equals the number of monster nodes that do NOT have a monster ancestor.
    #    Why? Because each such node requires a separate path starting from root,
    #    and if a monster node has a monster ancestor, it is covered by the same path.
    #
    # 2) So the answer = count of monster nodes u such that no ancestor of u is monster.
    #
    # 3) When toggling monsters in a subtree, the status of all nodes in that subtree flips.
    #
    # 4) We need to quickly update and query the count of "monster nodes without monster ancestors".
    #
    # Approach:
    # - Root the tree at 1.
    # - Compute Euler tour of the tree to get subtree intervals.
    # - Maintain for each node:
    #   - a_i: monster status (0 or 1)
    #   - parent
    # - We want to maintain the count of "monster nodes without monster ancestors".
    #
    # Let's define:
    # - For each node u, define "covered" = True if it has a monster ancestor.
    #   Then "monster nodes without monster ancestors" are monster nodes with covered=False.
    #
    # How to maintain covered efficiently?
    #
    # Observation:
    # - covered[u] = True if parent[u] is monster or covered[parent[u]] = True
    # - covered[1] = False always (root has no ancestors)
    #
    # So covered[u] = monster[parent[u]] or covered[parent[u]]
    #
    # This means covered[u] depends only on parent's monster status and parent's covered.
    #
    # So if we know monster status of all nodes, we can compute covered[u] by:
    # covered[1] = False
    # covered[u] = monster[parent[u]] or covered[parent[u]]
    #
    # But we need to update covered after toggling monsters in a subtree.
    #
    # When toggling monsters in a subtree, monster[u] flips for all u in subtree.
    # This may change covered[u] for u in subtree and also for descendants.
    #
    # But covered[u] depends on parent's monster and parent's covered.
    #
    # So toggling monsters in a subtree affects covered of nodes in that subtree and their descendants.
    #
    # But covered[u] depends on parent's monster and parent's covered, so if parent's monster or covered changes,
    # covered[u] may change.
    #
    # So toggling monsters in a subtree can affect covered of nodes in that subtree and their descendants.
    #
    # But subtree of v is a contiguous segment in Euler order.
    #
    # We can do the following:
    #
    # - We will store monster status in a segment tree with lazy propagation for toggling.
    # - We will store covered status in a segment tree or array.
    #
    # But covered depends on parent's monster and parent's covered.
    #
    # So we can do a BFS or DFS from root to recompute covered after each toggle.
    # But that is too slow.
    #
    # Alternative approach:
    #
    # Let's consider the problem from another angle:
    #
    # The minimal number of paths = number of monster nodes with no monster ancestor.
    #
    # Equivalently, the minimal number of paths = number of monster nodes u such that
    # monster[parent[u]] = 0 (or u=1).
    #
    # Because if parent[u] is monster, then u is covered by parent's path.
    #
    # So minimal paths = count of monster nodes u where parent[u] is not monster.
    #
    # So if we maintain:
    # - monster[u] for all u
    # - For each node u != 1, check if monster[u] == 1 and monster[parent[u]] == 0
    # - For root (u=1), if monster[1] == 1, it always counts as a path.
    #
    # So answer = sum over u:
    #   (monster[u] == 1) and (u == 1 or monster[parent[u]] == 0)
    #
    # This is easy to maintain if we can quickly:
    # - toggle monster status in subtree
    # - update counts of nodes where monster[u] == 1 and monster[parent[u]] == 0
    #
    # We can do this with a segment tree over Euler order:
    #
    # For each node u, we store:
    # - monster[u]
    # - monster[parent[u]] (we can store parent[u] separately)
    #
    # We want to maintain:
    # - For each node u, a boolean "contrib[u]" = monster[u] == 1 and (u == 1 or monster[parent[u]] == 0)
    #
    # When toggling monsters in subtree of v:
    # - monster[u] flips for all u in subtree
    # - For each u in subtree, contrib[u] may change because monster[u] changed
    # - For each child c of nodes in subtree, if c not in subtree, their contrib depends on monster[parent[c]]
    #   which may have changed if parent[c] in subtree and toggled.
    #
    # So toggling monsters in subtree affects:
    # - contrib[u] for u in subtree (because monster[u] flips)
    # - contrib[c] for children c of nodes in subtree but c not in subtree (because monster[parent[c]] flips)
    #
    # So we must update contrib for:
    # - all nodes in subtree (monster[u] flips)
    # - all children of nodes in subtree but outside subtree (monster[parent[c]] flips)
    #
    # Implementation plan:
    #
    # 1) Euler tour to get subtree intervals.
    # 2) Store monster[u] in an array.
    # 3) For each node u, store children[u].
    # 4) Maintain contrib[u] = monster[u] == 1 and (u == 1 or monster[parent[u]] == 0)
    # 5) Maintain sum of contrib[u] over all nodes.
    #
    # 6) For toggling subtree of v:
    #    - Flip monster[u] for all u in subtree[v]
    #    - For all u in subtree[v], update contrib[u]
    #    - For all children c of nodes in subtree[v] but c not in subtree[v], update contrib[c]
    #
    # 7) To efficiently flip monster[u] in subtree[v], use segment tree with lazy propagation.
    #    But we also need to update contrib[u].
    #
    # 8) For children c outside subtree[v], we can process them separately.
    #
    # Details:
    #
    # - We will build Euler tour arrays: in[u], out[u]
    # - Build segment tree over monster array in Euler order.
    # - For each node u, we know its position in Euler order.
    #
    # - To flip monster in subtree[v], we flip segment [in[v], out[v]] in segment tree.
    #
    # - To update contrib[u], we need monster[u] and monster[parent[u]].
    #
    # - monster[u] can be obtained from segment tree.
    # - monster[parent[u]] can be obtained similarly.
    #
    # - For each node u, contrib[u] = monster[u] == 1 and (u == 1 or monster[parent[u]] == 0)
    #
    # - We maintain contrib[u] in a Fenwick tree or segment tree to get sum quickly.
    #
    # - After toggling subtree[v], we must update contrib[u] for all u in subtree[v].
    #
    # - For children c of nodes in subtree[v] but c not in subtree[v], we must update contrib[c].
    #
    # To do this efficiently:
    #
    # - We can store for each node u:
    #   - list of children
    #   - parent[u]
    #
    # - After toggling subtree[v], we:
    #   - flip monster in subtree[v] in segment tree
    #   - for all u in subtree[v], update contrib[u]
    #   - for all u in subtree[v], for each child c of u:
    #       if c not in subtree[v], update contrib[c]
    #
    # But iterating all children of all nodes in subtree[v] can be large.
    #
    # Optimization:
    #
    # - For each node u, we know in[u], out[u].
    # - For each child c of u, check if c in subtree[v] by comparing in[c] and in[v], out[v].
    #
    # - We can process only children of v (and their children) outside subtree[v].
    #
    # But this can be large.
    #
    # Alternative approach:
    #
    # - We can maintain contrib[u] in a segment tree over Euler order.
    # - After toggling subtree[v], we update contrib[u] for u in subtree[v].
    # - For children c outside subtree[v], we update contrib[c] individually.
    #
    # Since sum of q and n is 250000, and each node has only one parent,
    # total number of children outside toggled subtree over all queries is manageable.
    #
    # So we implement as described.
    
    # Let's implement the solution now.
    
    # Segment tree for monster status with lazy flip
    class SegmentTree:
        def __init__(self, data):
            n = len(data)
            self.N = 1
            while self.N < n:
                self.N <<= 1
            self.data = [0]*(2*self.N)
            self.lazy = [0]*(2*self.N)
            for i in range(n):
                self.data[self.N+i] = data[i]
            for i in range(self.N-1, 0, -1):
                self.data[i] = self.data[i<<1] + self.data[i<<1|1]
        
        def push(self, v, l, r):
            if self.lazy[v]:
                self.data[v] = (r - l + 1) - self.data[v]
                if v < self.N:
                    self.lazy[v<<1] ^= 1
                    self.lazy[v<<1|1] ^= 1
                self.lazy[v] = 0
        
        def update(self, ql, qr, v=1, l=0, r=None):
            if r is None:
                r = self.N - 1
            self.push(v, l, r)
            if qr < l or ql > r:
                return
            if ql <= l and r <= qr:
                self.lazy[v] ^= 1
                self.push(v, l, r)
                return
            m = (l + r) >> 1
            self.update(ql, qr, v<<1, l, m)
            self.update(ql, qr, v<<1|1, m+1, r)
            self.data[v] = self.data[v<<1] + self.data[v<<1|1]
        
        def get(self, pos, v=1, l=0, r=None):
            if r is None:
                r = self.N - 1
            self.push(v, l, r)
            if l == r:
                return self.data[v]
            m = (l + r) >> 1
            if pos <= m:
                return self.get(pos, v<<1, l, m)
            else:
                return self.get(pos, v<<1|1, m+1, r)
    
    # Fenwick tree for contrib sums
    class Fenw:
        def __init__(self, n):
            self.n = n
            self.fw = [0]*(n+1)
        def update(self, i, delta):
            i += 1
            while i <= self.n:
                self.fw[i] += delta
                i += i & (-i)
        def query(self, i):
            i += 1
            s = 0
            while i > 0:
                s += self.fw[i]
                i -= i & (-i)
            return s
        def range_query(self, l, r):
            return self.query(r) - self.query(l-1)
    
    # Euler tour to get subtree intervals
    def dfs(u, p):
        nonlocal time
        in_order[u] = time
        euler[time] = u
        time += 1
        parent[u] = p
        for w in g[u]:
            if w != p:
                dfs(w, u)
        out_order[u] = time - 1
    
    # Update contrib[u] in Fenw
    def update_contrib(u):
        pos = in_order[u]
        old = contrib_arr[pos]
        mu = monster_seg.get(pos)
        if u == 1:
            new = mu
        else:
            mp = parent[u]
            mp_monster = monster_seg.get(in_order[mp])
            new = mu & (mp_monster ^ 1)
        if old != new:
            contrib_arr[pos] = new
            fenw.update(pos, new - old)
    
    # After toggling subtree[v], update contrib for:
    # - all nodes in subtree[v]
    # - all children c of nodes in subtree[v] but c not in subtree[v]
    def update_subtree_and_children(v):
        # update contrib for all nodes in subtree[v]
        stack = [v]
        while stack:
            u = stack.pop()
            update_contrib(u)
            for c in g[u]:
                if c != parent[u]:
                    if in_order[c] >= in_order[v] and in_order[c] <= out_order[v]:
                        stack.append(c)
        # update contrib for children outside subtree[v]
        # For all u in subtree[v], check children outside subtree[v]
        # To avoid repeated work, we do a BFS over subtree[v] and for each node check children outside
        from collections import deque
        q = deque([v])
        while q:
            u = q.popleft()
            for c in g[u]:
                if c != parent[u]:
                    if not (in_order[c] >= in_order[v] and in_order[c] <= out_order[v]):
                        update_contrib(c)
                    else:
                        q.append(c)
    
    # Read input and process test cases
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        g = [[] for __ in range(n)]
        for __ in range(n-1):
            u,vv = map(int, input().split())
            u -= 1
            vv -= 1
            g[u].append(vv)
            g[vv].append(u)
        
        q = int(input())
        queries = [int(input())-1 for __ in range(q)]
        
        # Euler tour
        in_order = [0]*n
        out_order = [0]*n
        euler = [0]*n
        parent = [-1]*n
        time = 0
        dfs(0, -1)
        
        # Build monster array in Euler order
        monster_init = [0]*n
        for i in range(n):
            monster_init[in_order[i]] = a[i]
        
        monster_seg = SegmentTree(monster_init)
        
        # contrib array: contrib[u] = monster[u] == 1 and (u == 1 or monster[parent[u]] == 0)
        contrib_arr = [0]*n
        fenw = Fenw(n)
        
        # Initialize contrib_arr and fenw
        for i in range(n):
            u = euler[i]
            mu = monster_init[i]
            if u == 0:
                c = mu
            else:
                mp = parent[u]
                mp_monster = monster_init[in_order[mp]]
                c = mu & (mp_monster ^ 1)
            contrib_arr[i] = c
            if c:
                fenw.update(i, 1)
        
        # Output initial answer
        print(fenw.query(n-1))
        
        # Process queries
        for v in queries:
            # toggle monster in subtree[v]
            l = in_order[v]
            r = out_order[v]
            monster_seg.update(l, r)
            # update contrib for subtree[v] and children outside subtree[v]
            update_subtree_and_children(v)
            print(fenw.query(n-1))
    

threading.Thread(target=main).start()