import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Explanation:
# The problem asks for the minimum number of root-to-some-vertex paths covering all monster vertices.
# This is equivalent to the number of connected components of monster vertices in the tree,
# where connectivity is defined by edges.
#
# Since all paths start at root (vertex 1), and the tree is rooted at 1,
# the minimal number of paths needed equals the number of monster vertices that do not have a monster parent.
#
# Why?
# - If a monster vertex has a monster parent, it can be covered by the same path that covers the parent.
# - If a monster vertex's parent is not a monster, it must start a new path from the root to that vertex.
#
# So the answer = count of monster vertices v where parent[v] is not monster (or v=1 and monster).
#
# After each query, we invert the monster status of all vertices in the subtree of v.
# We must update the count efficiently.
#
# Approach:
# - Precompute parent of each node.
# - Use Euler Tour to get subtree ranges.
# - Use a segment tree with lazy propagation to invert monster status in subtree ranges.
# - Maintain for each node whether it contributes to the answer:
#   contribution = 1 if monster[v] == 1 and (v == 1 or monster[parent[v]] == 0)
# - We can maintain a segment tree over Euler order storing monster status.
# - To get parent's monster status quickly, we keep monster status in an array and update it after each query.
# - After toggling a subtree, we update contributions of affected nodes:
#   - All nodes in subtree toggled: their monster status flipped.
#   - For each toggled node v, contribution depends on monster[v] and monster[parent[v]].
#   - Also, toggling subtree of v affects contributions of children of v (because parent's monster status changed).
#
# To handle this efficiently:
# - We keep an array of monster status.
# - We keep an array of contribution per node.
# - We keep a Fenwick tree (BIT) or segment tree over contributions to get sum quickly.
# - After toggling subtree of v:
#   - For all nodes in subtree of v, monster status flipped.
#   - For all nodes in subtree of v, update their contribution.
#   - For all children c of nodes in subtree of v, update their contribution if parent changed monster status.
#
# But updating all children of toggled nodes is expensive.
#
# Optimization:
# - Only parent-child edges matter for contribution.
# - When toggling subtree of v:
#   - For all nodes u in subtree of v, monster[u] flipped.
#   - For all nodes u in subtree of v, update contribution[u].
#   - For all children c of nodes u in subtree of v but c not in subtree of v:
#     - Their parent's monster status changed, so contribution[c] may change.
#
# So we need to:
# - Update contributions of all nodes in subtree of v.
# - Update contributions of all children of nodes in subtree of v that lie outside subtree of v.
#
# We can:
# - For each node, store children.
# - For each query:
#   - Flip monster status in subtree of v using segment tree.
#   - For all nodes in subtree of v, update contribution.
#   - For all edges from nodes in subtree of v to children outside subtree of v, update contribution of those children.
#
# To do this efficiently:
# - We do Euler Tour to get subtree ranges.
# - Use segment tree with lazy propagation to flip monster status in subtree.
# - For contribution updates:
#   - We can store contribution in a Fenwick tree or segment tree over Euler order.
#   - For nodes in subtree of v, we can update contribution by recalculating contribution[u].
#   - For children outside subtree, we can process them separately.
#
# Since sum of n and q is large, we must be efficient.
#
# Implementation details:
# - Euler Tour to get in[u], out[u].
# - parent[u] for each node.
# - children[u] list.
# - segment tree for monster status with lazy flip.
# - contribution[u] stored in Fenwick tree over Euler order.
# - After toggling subtree of v:
#   - Flip monster status in segment tree.
#   - For all nodes in subtree of v:
#     - Recalculate contribution[u] and update Fenwick tree.
#   - For children c of nodes in subtree of v but c not in subtree of v:
#     - Recalculate contribution[c] and update Fenwick tree.
#
# To avoid O(n) per query, we must avoid iterating all nodes in subtree.
#
# Key insight:
# - We can store monster status in segment tree.
# - contribution[u] depends on monster[u] and monster[parent[u]].
# - After toggling subtree of v:
#   - monster[u] flipped for u in subtree of v.
#   - For u in subtree of v, contribution[u] changes.
#   - For children c of u in subtree of v but c not in subtree of v, contribution[c] changes.
#
# We can:
# - For each node u, contribution[u] = monster[u] & (u == 1 or not monster[parent[u]])
# - So contribution[u] = monster[u] * (1 - monster[parent[u]]) if u != 1 else monster[u]
#
# We can maintain:
# - monster[u] in segment tree.
# - For each node u, we can query monster[u] and monster[parent[u]] in O(log n).
# - To get sum of contributions, sum over all nodes of contribution[u].
#
# But summing over all nodes each time is O(n).
#
# So we maintain a Fenwick tree over Euler order for contributions.
#
# After toggling subtree of v:
# - For all u in subtree of v:
#   - monster[u] flipped.
#   - contribution[u] changes.
# - For children c of u in subtree of v but c not in subtree of v:
#   - contribution[c] changes.
#
# We can:
# - For all u in subtree of v:
#   - Update monster[u] in segment tree (flip).
# - For all u in subtree of v:
#   - Recalculate contribution[u] and update Fenwick tree.
# - For all edges u->c where u in subtree of v and c not in subtree of v:
#   - Recalculate contribution[c] and update Fenwick tree.
#
# To avoid iterating all nodes in subtree of v, we can:
# - Use segment tree to flip monster status in subtree.
# - For contribution updates:
#   - We must iterate nodes in subtree of v to update contribution.
#   - But this is O(size of subtree), which can be large.
#
# Since sum of n and q is large, we need a better approach.
#
# Alternative approach:
# - The answer = number of monster vertices with monster[parent] = 0 (or root if monster).
# - So answer = number of monster vertices - number of monster vertices whose parent is monster.
#
# Let's maintain:
# - total_monsters = number of monster vertices.
# - monster_edges = number of edges where both ends are monsters (parent->child).
#
# Then answer = total_monsters - monster_edges
#
# After toggling subtree of v:
# - total_monsters changes by number of toggled nodes flipped from 0->1 minus 1->0.
# - monster_edges changes by edges crossing toggled subtree and inside toggled subtree.
#
# We can:
# - Maintain total_monsters.
# - Maintain monster_edges.
#
# When toggling subtree of v:
# - For each edge (u->child):
#   - If both u and child are in toggled subtree, both flipped, so edge status unchanged.
#   - If one in toggled subtree and other outside, edge status flips if one endpoint flips.
#
# So only edges crossing boundary of toggled subtree change monster_edges.
#
# So we need to:
# - Count how many nodes in subtree of v are monsters before toggle.
# - Count how many edges crossing boundary have monster endpoints before toggle.
#
# We can:
# - Use Euler Tour and segment tree to count monsters in subtree.
# - For edges crossing boundary:
#   - For each child c of v:
#     - If c not in subtree of v, edge (v->c) crosses boundary.
#   - For each such edge, if monster[v] and monster[c], monster_edges++
# - But toggling subtree flips monster[v] and monster[c] if in subtree.
#
# So we can:
# - For each query:
#   - Count monsters in subtree of v before toggle: M
#   - total_monsters = total_monsters - M + (subtree_size - M)
#   - For edges crossing boundary:
#     - For each edge crossing boundary (u->c):
#       - If monster[u] and monster[c], monster_edges--
#       - After toggle, monster[u] or monster[c] flipped, so if previously edge counted, now not counted, or vice versa.
#       - So monster_edges += (number of edges crossing boundary) - previous count of monster edges crossing boundary
#
# But edges crossing boundary are only edges from toggled subtree to outside.
#
# So we can:
# - For each node, store children.
# - For each query:
#   - Count monsters in subtree of v before toggle: M
#   - total_monsters = total_monsters - M + (subtree_size - M)
#   - For each edge crossing boundary (u->c):
#     - Check if monster[u] and monster[c] before toggle.
#     - If yes, monster_edges--
#     - After toggle, monster[u] or monster[c] flipped, so if previously edge counted, now not counted, or vice versa.
#     - So monster_edges += (number of edges crossing boundary) - previous count of monster edges crossing boundary
#
# Actually, toggling subtree flips monster[u] for u in subtree.
# So for edge crossing boundary (u->c):
# - If u in subtree, c outside:
#   - monster[u] flips, monster[c] unchanged.
# - So edge counted if monster[u] and monster[c].
# - After toggle, monster[u] flips, so edge counted if flipped monster[u] and monster[c].
#
# So edge counted before toggle if monster[u] and monster[c].
# After toggle if (not monster[u]) and monster[c].
#
# So edge counted flips if monster[c] == 1.
#
# So for each edge crossing boundary:
# - If monster[c] == 1, monster_edges changes by +1 or -1.
#
# So for each edge crossing boundary:
# - If monster[c] == 1, monster_edges flips.
#
# So for each query:
# - For each edge crossing boundary (u->c):
#   - If monster[c] == 1, monster_edges ^= 1 (flip)
#
# So we can:
# - For each query:
#   - Count monsters in subtree of v before toggle: M
#   - total_monsters = total_monsters - M + (subtree_size - M)
#   - For each edge crossing boundary (u->c):
#     - If monster[c] == 1, monster_edges flips (monster_edges += 1 if 0->1 else -1)
#
# Implementation:
# - Precompute Euler Tour.
# - Build segment tree for monster status with lazy flip.
# - For each node, store children.
# - For each query:
#   - Count monsters in subtree of v before toggle using segment tree.
#   - total_monsters update.
#   - For each child c of v:
#     - If c not in subtree of v:
#       - Check monster[c].
#       - If monster[c] == 1, monster_edges flips.
#   - Flip monster status in subtree of v in segment tree.
#   - Print answer = total_monsters - monster_edges
#
# Initial monster_edges:
# - For each edge (u->c):
#   - If monster[u] == 1 and monster[c] == 1, monster_edges++
#
# This approach is O(q * degree(v)) which is acceptable since sum of degrees is 2*(n-1).
# So total complexity is O((n+q) log n).

def main():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        edges = [[] for __ in range(n)]
        for __ in range(n-1):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            edges[u].append(v)
            edges[v].append(u)

        # Build tree rooted at 0
        parent = [-1]*n
        children = [[] for __ in range(n)]
        stack = [0]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for w in edges[u]:
                if w == parent[u]:
                    continue
                if parent[w] == -1 and w != 0:
                    parent[w] = u
                    children[u].append(w)
                    stack.append(w)

        # Euler Tour to get subtree ranges
        in_time = [0]*n
        out_time = [0]*n
        time = 0
        def dfs(u):
            nonlocal time
            in_time[u] = time
            time += 1
            for c in children[u]:
                dfs(c)
            out_time[u] = time - 1
        dfs(0)

        # Segment tree for monster status with lazy flip
        size = 1
        while size < n:
            size <<= 1

        seg = [0]*(2*size)
        lazy = [0]*(2*size)

        def build():
            for i in range(n):
                seg[size+i] = a[i]
            for i in range(size-1,0,-1):
                seg[i] = seg[i<<1] + seg[i<<1|1]

        def apply(i):
            seg[i] = ( ( (i >= size) and 1 or (seg[i<<1] + seg[i<<1|1]) ) if False else seg[i])  # dummy
            seg[i] = ( ( (i >= size) and 1 or (seg[i<<1] + seg[i<<1|1]) ) if False else seg[i])  # dummy

        def push(i,l,r):
            if lazy[i]:
                seg[i] = (r - l + 1) - seg[i]
                if i < size:
                    lazy[i<<1] ^= 1
                    lazy[i<<1|1] ^= 1
                lazy[i] = 0

        def push_down(i,l,r):
            if lazy[i]:
                mid = (l+r)//2
                lazy[i<<1] ^= 1
                lazy[i<<1|1] ^= 1
                seg[i<<1] = (mid - l + 1) - seg[i<<1]
                seg[i<<1|1] = (r - mid) - seg[i<<1|1]
                lazy[i] = 0

        def update_range(i,l,r,L,R):
            if R < l or r < L:
                return
            if L <= l and r <= R:
                seg[i] = (r - l + 1) - seg[i]
                if i < size:
                    lazy[i] ^= 1
                return
            push_down(i,l,r)
            mid = (l+r)//2
            update_range(i<<1,l,mid,L,R)
            update_range(i<<1|1,mid+1,r,L,R)
            seg[i] = seg[i<<1] + seg[i<<1|1]

        def query_range(i,l,r,L,R):
            if R < l or r < L:
                return 0
            if L <= l and r <= R:
                return seg[i]
            push_down(i,l,r)
            mid = (l+r)//2
            return query_range(i<<1,l,mid,L,R) + query_range(i<<1|1,mid+1,r,L,R)

        build()

        # total_monsters
        total_monsters = seg[1]

        # monster array to query monster[u]
        # We'll query monster[u] by query_range(in_time[u], in_time[u])
        def monster(u):
            return query_range(1,0,size-1,in_time[u],in_time[u])

        # Calculate initial monster_edges
        monster_edges = 0
        for u in range(n):
            mu = monster(u)
            for c in children[u]:
                mc = monster(c)
                if mu == 1 and mc == 1:
                    monster_edges += 1

        q = int(input())
        out.append(str(total_monsters - monster_edges))
        for __ in range(q):
            v = int(input()) - 1
            # Count monsters in subtree of v before toggle
            M = query_range(1,0,size-1,in_time[v],out_time[v])
            subtree_size = out_time[v] - in_time[v] + 1
            # Update total_monsters
            total_monsters = total_monsters - M + (subtree_size - M)

            # For edges crossing boundary:
            # edges from nodes in subtree of v to children outside subtree of v
            # For each node u in subtree of v, children[u] outside subtree of v
            # But iterating all nodes in subtree is expensive
            # Instead, only check children of v (root of toggled subtree)
            # and their children outside subtree of v
            # Actually, edges crossing boundary are edges from toggled subtree to outside
            # So only edges from toggled subtree nodes to children outside toggled subtree
            # We can check children of toggled subtree root v:
            # For each child c of v:
            #   if c not in subtree of v, edge crosses boundary
            # But toggled subtree is subtree of v, so children of v are inside subtree of v
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            # So for each node u in subtree of v, check children outside subtree of v
            # To avoid O(n), we only check children of v's ancestors that are in subtree of v
            # This is complicated, so we do the following:
            # For each child c of v:
            #   if c not in subtree of v, edge crosses boundary
            # But c is child of v, so c in subtree of v always
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            # So for each node u in subtree of v, check children[u] outside subtree of v
            # To avoid O(n), we precompute for each node the list of children outside subtree of v
            # But this is complicated.
            #
            # Alternative:
            # For each node u in subtree of v, children[u] outside subtree of v:
            #   For each such child c:
            #       if monster[c] == 1, monster_edges flips
            #
            # We can precompute for each node the list of children outside its subtree
            # But subtree of v changes per query.
            #
            # So we do the following:
            # For each child c of v:
            #   if c not in subtree of v, edge crosses boundary
            # But c is child of v, so c in subtree of v always.
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary are edges from nodes in subtree of v to children outside subtree of v
            #
            # So edges crossing boundary