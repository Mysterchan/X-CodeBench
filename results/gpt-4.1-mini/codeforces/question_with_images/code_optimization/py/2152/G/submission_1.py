import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    t = int(input())
    # We will process all test cases
    # Constraints:
    # sum of n <= 250000
    # sum of q <= 250000

    # Approach:
    # The minimal number of paths k is the number of "monster groups" that cannot be covered by a single path from root.
    # The problem reduces to counting how many children of a node have monsters in their subtree when the node itself is a monster or not.
    #
    # Key insight:
    # For each node u:
    #   cnt[u] = 1 if u has monster and none of its children have monsters in their subtree
    #   else 0
    #
    # global_k = sum of cnt[u] over all u
    #
    # After flipping monsters in a subtree, we need to update the values efficiently.
    #
    # We will:
    # - Build tree and parent/children arrays
    # - Euler tour to get subtree ranges
    # - Maintain current_a[u] = current monster status of u
    # - Maintain x[u] = number of monsters in subtree of u
    # - Maintain cnt[u] as above
    #
    # Updates:
    # - Flip monsters in subtree of v: toggle all current_a[u] in subtree of v
    # - We will use a segment tree with lazy propagation to flip monsters in subtree ranges
    # - But we also need to update x[u], cnt[u], and global_k
    #
    # To avoid heavy recomputation, we will:
    # - Store x[u] and cnt[u]
    # - After flipping subtree, update x[u] and cnt[u] bottom-up from v to root
    #
    # To do this efficiently:
    # - We will store children and parent arrays
    # - After flipping subtree, we update x[u] and cnt[u] for all ancestors of v up to root
    #
    # Since sum of q and n is large, we must do updates in O(log n) or amortized O(1)
    #
    # We will:
    # - Use Euler tour to map subtree to segment
    # - Use BIT or segment tree to store monster counts and flips
    # - For each node, store number of monsters in subtree (x[u]) and cnt[u]
    # - After flipping subtree, update x[u] for all ancestors of v
    #
    # To update x[u] for ancestors efficiently, we can:
    # - For each node, store the sum of monsters in children subtrees
    # - When a child's subtree monster count changes, update parent's sum accordingly
    #
    # So we need a data structure to maintain:
    # - For each node u, sum of x[v] for v in children[u]
    # - x[u] = current_a[u] + sum of x[children]
    #
    # When flipping subtree of v:
    # - Flip current_a[u] for all u in subtree of v (using segment tree)
    # - For each node u in path from v to root:
    #     - Recompute x[u] = current_a[u] + sum of x[children[u]]
    #     - Update cnt[u] accordingly
    #     - Update global_k
    #
    # To do this efficiently, we will:
    # - Use Euler tour + segment tree for current_a[u]
    # - For each node, maintain sum of x[children] in a variable
    # - When child's x changes, update parent's sum of children
    #
    # Implementation details:
    # - Euler tour to get in[u], out[u]
    # - Segment tree with lazy propagation to flip current_a[u] in subtree
    # - For each node, maintain:
    #     - current_a[u] (from segment tree)
    #     - x[u] = current_a[u] + sum_x_children[u]
    #     - cnt[u] = 1 if current_a[u] == 1 and all children have x[v] == 0 else 0
    # - sum_x_children[u] = sum of x[v] for v in children[u]
    #
    # After flipping subtree of v:
    # - Flip current_a[u] in segment tree for subtree of v
    # - Then update x[u], cnt[u], sum_x_children[u] bottom-up from v to root
    #
    # To update bottom-up efficiently:
    # - We can store parent[u]
    # - For each node u in path from v to root:
    #     - Recompute x[u] and cnt[u]
    #     - Update sum_x_children[parent[u]] accordingly
    #     - Update global_k
    #
    # Since each query updates O(log n) nodes (path from v to root), total complexity is acceptable.

    MAXN = 250000 + 10

    # Segment tree for flipping current_a[u] in subtree
    class SegmentTree:
        __slots__ = ['n', 'tree', 'lazy']
        def __init__(self, n):
            self.n = 1
            while self.n < n:
                self.n <<= 1
            self.tree = [0]*(2*self.n)
            self.lazy = [0]*(2*self.n)

        def build(self, arr):
            for i in range(len(arr)):
                self.tree[self.n + i] = arr[i]
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

        def push(self, idx, l, r):
            if self.lazy[idx]:
                self.tree[idx] = (r - l + 1) - self.tree[idx]
                if idx < self.n:
                    self.lazy[idx<<1] ^= 1
                    self.lazy[idx<<1|1] ^= 1
                self.lazy[idx] = 0

        def update(self, L, R, idx, l, r):
            self.push(idx, l, r)
            if r < L or R < l:
                return
            if L <= l and r <= R:
                self.lazy[idx] ^= 1
                self.push(idx, l, r)
                return
            m = (l + r) >> 1
            self.update(L, R, idx<<1, l, m)
            self.update(L, R, idx<<1|1, m+1, r)
            self.tree[idx] = self.tree[idx<<1] + self.tree[idx<<1|1]

        def query(self, pos, idx, l, r):
            self.push(idx, l, r)
            if l == r:
                return self.tree[idx]
            m = (l + r) >> 1
            if pos <= m:
                return self.query(pos, idx<<1, l, m)
            else:
                return self.query(pos, idx<<1|1, m+1, r)

        def flip(self, L, R):
            self.update(L, R, 1, 0, self.n-1)

        def get(self, pos):
            return self.query(pos, 1, 0, self.n-1)

    out = []
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        graph = [[] for __ in range(n+1)]
        for __ in range(n-1):
            u,v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        # Build parent and children arrays with BFS
        from collections import deque
        parent = [0]*(n+1)
        children = [[] for __ in range(n+1)]
        visited = [False]*(n+1)
        visited[1] = True
        q = deque([1])
        while q:
            u = q.popleft()
            for w in graph[u]:
                if not visited[w]:
                    visited[w] = True
                    parent[w] = u
                    children[u].append(w)
                    q.append(w)

        # Euler tour to get in[u], out[u]
        in_order = [0]*(n+1)
        out_order = [0]*(n+1)
        time = 0
        def dfs(u):
            nonlocal time
            in_order[u] = time
            time += 1
            for w in children[u]:
                dfs(w)
            out_order[u] = time - 1
        dfs(1)

        # Build segment tree for current_a[u]
        arr = [0]*n
        for u in range(1,n+1):
            arr[in_order[u]] = a_list[u-1]
        seg = SegmentTree(n)
        seg.build(arr)

        # We need to maintain:
        # x[u] = current_a[u] + sum_x_children[u]
        # sum_x_children[u] = sum of x[v] for v in children[u]
        # cnt[u] = 1 if current_a[u] == 1 and all children have x[v] == 0 else 0
        # global_k = sum of cnt[u]

        x = [0]*(n+1)
        sum_x_children = [0]*(n+1)
        cnt = [0]*(n+1)

        # Initialize x, sum_x_children, cnt bottom-up
        order = []
        def dfs_post(u):
            for w in children[u]:
                dfs_post(w)
            order.append(u)
        dfs_post(1)

        for u in order:
            cur_a = seg.get(in_order[u])
            sxc = 0
            for w in children[u]:
                sxc += x[w]
            sum_x_children[u] = sxc
            x[u] = cur_a + sxc
            if cur_a == 1 and sxc == 0:
                cnt[u] = 1
            else:
                cnt[u] = 0

        global_k = sum(cnt)

        out.append(str(global_k))

        q_num = int(input())
        for __ in range(q_num):
            v = int(input())
            # Flip subtree of v in segment tree
            seg.flip(in_order[v], out_order[v])

            # Update x, sum_x_children, cnt bottom-up from v to root
            # We will update all ancestors of v including v
            # To do this efficiently, we collect path from v to root
            path = []
            cur = v
            while cur != 0:
                path.append(cur)
                cur = parent[cur]
            # Update in reverse order (bottom-up)
            # For each node u in path:
            #   - get current_a[u] from seg
            #   - sum_x_children[u] = sum of x[children[u]]
            #   - x[u] = current_a[u] + sum_x_children[u]
            #   - update cnt[u] and global_k accordingly
            #   - if x[u] changed, update sum_x_children[parent[u]] accordingly in next iteration

            # To update sum_x_children[parent[u]], we need to know old x[u]
            # So we store old_x[u] before update

            # We'll do a loop twice:
            # First, update x[u], cnt[u], global_k
            # Then update sum_x_children[parent[u]] for next iteration

            # To do this in one pass, we process from bottom to top:
            # For each u in path:
            #   old_x = x[u]
            #   current_a = seg.get(in_order[u])
            #   sum_x_children[u] = sum of x[children[u]] (already updated for children)
            #   x[u] = current_a + sum_x_children[u]
            #   update cnt[u], global_k
            #   if parent[u] != 0:
            #       sum_x_children[parent[u]] += x[u] - old_x

            for u in path:
                old_x = x[u]
                cur_a = seg.get(in_order[u])
                sxc = 0
                for w in children[u]:
                    sxc += x[w]
                sum_x_children[u] = sxc
                x[u] = cur_a + sxc
                old_cnt = cnt[u]
                if cur_a == 1 and sxc == 0:
                    cnt[u] = 1
                else:
                    cnt[u] = 0
                global_k += cnt[u] - old_cnt
                p = parent[u]
                if p != 0:
                    sum_x_children[p] += x[u] - old_x

            out.append(str(global_k))

    print('\n'.join(out))

if __name__ == "__main__":
    main()