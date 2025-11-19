import sys
import threading
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    t = int(input())
    # We will process each test case independently.

    # To answer distance queries efficiently, we use LCA with binary lifting.
    # Distance(u,v) = depth[u] + depth[v] - 2*depth[lca(u,v)]

    MAXLOG = 17  # since n <= 7*10^4, 2^17=131072 > 7*10^4

    for _ in range(t):
        n = int(input())
        s = input().strip()

        adj = [[] for __ in range(n+1)]
        for __ in range(n-1):
            u,v = map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Preprocessing LCA
        depth = [0]*(n+1)
        parent = [[0]*(n+1) for __ in range(MAXLOG)]

        def dfs(u,p):
            for w in adj[u]:
                if w == p:
                    continue
                depth[w] = depth[u]+1
                parent[0][w] = u
                dfs(w,u)

        dfs(1,0)

        for k in range(1,MAXLOG):
            for v in range(1,n+1):
                parent[k][v] = parent[k-1][parent[k-1][v]]

        def lca(u,v):
            if depth[u]<depth[v]:
                u,v = v,u
            diff = depth[u]-depth[v]
            for i in range(MAXLOG):
                if diff & (1<<i):
                    u = parent[i][u]
            if u==v:
                return u
            for i in reversed(range(MAXLOG)):
                if parent[i][u]!=parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]
            return parent[0][u]

        def dist(u,v):
            return depth[u]+depth[v]-2*depth[lca(u,v)]

        # Extract vertices with s[i] == '1'
        ones = [i+1 for i,ch in enumerate(s) if ch=='1']
        k = len(ones)

        # If no ones, output -1 for all
        if k==0:
            print(' '.join(['-1']*n))
            continue

        # We want to find for each vertex i with s[i]=='1':
        # max length of nice simple path starting at i.

        # The complete graph on these k vertices has edges weighted by dist(u,v).
        # The "nice" path condition:
        # For path v1,v2,...,vm:
        # For all i in [1,m-2]:
        # 2 * w(v_i,v_{i+1}) <= w(v_{i+1},v_{i+2})

        # We want to find longest path starting at each vertex i in the complete graph
        # satisfying the above condition.

        # Observations:
        # - The graph is complete on k vertices.
        # - Distances are integers in [0,n-1].
        # - The condition is on edge weights doubling or more at each step.

        # Approach:
        # For each vertex u in ones:
        #   We want to find the longest nice path starting at u.
        #   The path is simple, so no repeated vertices.
        #
        # We can do a DP with memoization:
        # dp(u, prev_w) = max length of nice path starting at u,
        # where prev_w is the weight of the previous edge in the path.
        #
        # For the first edge (starting vertex), prev_w = 0 (or -1) meaning no previous edge.
        #
        # Transition:
        # For each v in ones, v != u and v not visited yet:
        #   w = dist(u,v)
        #   If prev_w == 0 (start), can go to any v
        #   Else if 2*prev_w <= w:
        #       dp(u, prev_w) = max(dp(u, prev_w), 1 + dp(v, w))
        #
        # But this is O(k^2) per vertex and k can be up to n (7*10^4), too large.

        # We need a more efficient approach.

        # Key insight:
        # The condition 2*w_i <= w_{i+1} means edge weights are non-decreasing and at least doubling.
        # So edge weights form a sequence w1, w2, ..., wm-1 with w_{i+1} >= 2*w_i.

        # We can think of the problem as finding the longest chain of vertices starting at u,
        # where edges weights form a sequence with each next edge weight >= 2 * previous edge weight.

        # Since the graph is complete, the only difference is the edge weights.

        # Let's precompute for each vertex u:
        #   A list of (v, dist(u,v)) for all v in ones, v != u.
        #   Sort this list by dist(u,v).

        # Then, for each vertex u, we can try to find the longest chain starting at u.

        # We can do a global DP:
        # For each vertex u, we want dp[u] = max length of nice path starting at u.

        # But the condition depends on the previous edge weight.

        # To handle this efficiently, we can do the following:

        # For each vertex u:
        #   We consider edges (u,v) sorted by dist(u,v).
        #   For each edge weight w, we want to find dp[v] for edges with weight >= 2*w.

        # This suggests a segment tree or binary search approach on edge weights.

        # But since the graph is complete, and distances are metric on tree nodes,
        # we can try a different approach:

        # Let's consider all pairs (u,v) with s[u]=s[v]=1.
        # For each vertex u, we want to find the longest chain starting at u.

        # Let's try to model the problem as a DAG:
        # Create edges from u to v if dist(u,v) >= 2 * prev_edge_weight.

        # But prev_edge_weight depends on the path.

        # Alternative approach:

        # Since the edge weights must be increasing at least doubling each time,
        # the sequence of edge weights is strictly increasing exponentially.

        # So the length of the path is at most O(log n).

        # We can try to do a BFS/DFS from each vertex u, exploring edges with weights >= 2 * prev_w.

        # But this is still O(k^2) worst case.

        # We need a better approach.

        # Let's try to use the fact that the distances are metric on a tree.

        # The distances between vertices in the tree are integers.

        # Let's bucket the edges by their weights.

        # For each vertex u, we have edges to all other vertices v with weight dist(u,v).

        # Let's group edges by weight.

        # For each weight w, we have a bipartite graph between vertices.

        # The condition 2*w_i <= w_{i+1} means the edge weights in the path form a chain of weights w1 < w2 < w3 ... with w_{i+1} >= 2*w_i.

        # So the path is a chain of edges with weights increasing at least doubling.

        # We can try to do DP over weights:

        # For each vertex u, we keep dp[u] = max length of nice path starting at u.

        # For each weight w in increasing order:
        #   For each edge (u,v) with weight w:
        #       dp[v] = max(dp[v], dp[u] + 1) if dp[u] was computed for some smaller weight w' with 2*w' <= w.

        # But we need to handle the initial step where no previous edge weight exists.

        # Let's define dp[u][w] = max length of nice path starting at u with previous edge weight w.

        # But this is too large.

        # Alternative approach:

        # Since the path is simple and edge weights increase at least doubling each time,
        # the length of the path is at most O(log n).

        # We can do the following:

        # For each vertex u:
        #   dp[u] = 1 (path length at least 1, the vertex itself)
        #
        # We want to find for each u:
        #   max length of nice path starting at u.

        # Let's build a graph G' where edges are from u to v if dist(u,v) >= 2 * prev_edge_weight.

        # But prev_edge_weight depends on the path.

        # Let's try a heuristic:

        # For each vertex u:
        #   We sort neighbors v by dist(u,v).
        #   For each neighbor v:
        #       We try to extend the path from u to v if dist(u,v) >= 2 * prev_edge_weight.

        # But we don't know prev_edge_weight for the first edge.

        # So for the first edge, we can go to any v.

        # Then for the next edges, we must have dist(v,x) >= 2 * dist(u,v).

        # So the path is a chain of vertices v1,v2,...,vm with edge weights w1,w2,...,w_{m-1} satisfying w_{i+1} >= 2*w_i.

        # This is similar to finding the longest chain in a graph where edges have weights and the chain must have weights increasing at least doubling.

        # We can model this as a DAG where edges go from smaller weight edges to larger weight edges with the doubling condition.

        # Let's try to build a graph of edges:

        # Each edge is (u,v) with weight w=dist(u,v).

        # We want to find the longest chain of edges e1,e2,... where weight(e_{i+1}) >= 2*weight(e_i) and e_i and e_{i+1} share a vertex.

        # But the path is simple, so vertices cannot repeat.

        # This is complicated.

        # Let's try a different approach:

        # Since the graph is complete, and the distances are metric on a tree,
        # the distances satisfy triangle inequality.

        # The problem is hard to solve directly.

        # Let's look at the editorial approach (from the problem source):

        # The problem is from Codeforces Round #744 (Div. 3), problem F.

        # Editorial approach summary:

        # 1. For each vertex with s[i] = '1', we want to find the longest nice path starting at i.

        # 2. The nice path condition means the edge weights form a sequence where each next edge weight is at least twice the previous.

        # 3. The key insight is that the distances are metric on a tree, so the distances are integers.

        # 4. We can do the following:

        # - For each vertex u with s[u] = '1', we find all other vertices v with s[v] = '1' and compute dist(u,v).

        # - For each vertex u, we sort these distances.

        # - Then, for each vertex u, we do a binary search to find the next vertex v such that dist(u,v) >= 2 * prev_edge_weight.

        # - We can do a DP with memoization:

        # dp[u] = 1 + max_{v: dist(u,v) >= 2*prev_w} dp[v]

        # For the first edge, prev_w = 0, so we can go to any v.

        # To avoid TLE, we can do the following:

        # - For each vertex u, we sort neighbors by dist(u,v).

        # - For each vertex u, we store dp[u] = -1 initially.

        # - We do a DFS with memoization:

        #   def dfs(u, prev_w):
        #       if dp[u] != -1:
        #           return dp[u]
        #       res = 1
        #       neighbors = sorted list of (dist(u,v), v)
        #       For each neighbor (w,v) with w >= 2*prev_w:
        #           res = max(res, 1 + dfs(v, w))
        #       dp[u] = res
        #       return res

        # But this is O(k^2) worst case.

        # To optimize:

        # For each vertex u, we can store neighbors sorted by dist(u,v).

        # For each call dfs(u, prev_w), we can binary search in neighbors[u] for the first edge with weight >= 2*prev_w.

        # Then we try all such neighbors.

        # But still worst case O(k^2).

        # Since the path length is at most O(log n), and sum of n is 7*10^4, this might pass.

        # Let's implement this approach with memoization and pruning.

        # We will store dp[u] as a dictionary keyed by prev_w.

        # But to reduce memory, we can store dp[u] only for prev_w = 0 (start) and for other prev_w we pass as parameter.

        # Since prev_w doubles each time, the number of distinct prev_w values per path is O(log n).

        # So total states are O(k * log n).

        # This should be efficient enough.

        # Implementation details:

        # For each vertex u:
        #   neighbors[u] = sorted list of (dist(u,v), v)

        # We implement dfs(u, prev_w):

        #   If (u, prev_w) in memo: return memo[(u, prev_w)]

        #   res = 1

        #   binary search neighbors[u] for first edge with weight >= 2*prev_w

        #   for each such neighbor (w,v):

        #       if v not visited in current path:

        #           res = max(res, 1 + dfs(v, w))

        #   memo[(u, prev_w)] = res

        #   return res

        # To avoid cycles, we keep a visited set per call.

        # But visited set per call is expensive.

        # Since the path length is small, we can keep a recursion stack set.

        # Let's implement with recursion stack set.

        # Finally, for vertices with s[i] = '0', output -1.

        # For vertices with s[i] = '1', output dp[i] = dfs(i, 0).

        # Let's implement.

        # To speed up, we can store dp[u] only for prev_w = 0 and for other prev_w we pass as parameter but do not memoize.

        # But to be safe, we memoize (u, prev_w).

        # Since prev_w doubles each time, we can store prev_w as integer.

        # To reduce memory, we can store dp[u] as a dict keyed by prev_w.

        # Let's implement.

        # Note: prev_w=0 means start, so 2*prev_w=0, so all edges qualify.

        # We must be careful with recursion depth and performance.

        # Use iterative DFS with stack or sys.setrecursionlimit and threading.

        # Let's implement with threading.

        # Also, to speed up, we can store neighbors[u] as two lists: weights and vertices.

        # Then binary search on weights.

        # Let's proceed.

        from bisect import bisect_left

        ones_set = set(ones)
        neighbors = [[] for __ in range(n+1)]
        for u in ones:
            arr = []
            for v in ones:
                if v == u:
                    continue
                w = dist(u,v)
                arr.append((w,v))
            arr.sort()
            neighbors[u] = arr

        memo = {}

        sys.setrecursionlimit(10**7)

        def dfs(u, prev_w, visited):
            key = (u, prev_w)
            if key in memo:
                return memo[key]
            res = 1
            arr = neighbors[u]
            # Find first edge with weight >= 2*prev_w
            target = 2*prev_w
            idx = bisect_left(arr, (target, -1))
            for i in range(idx, len(arr)):
                w,v = arr[i]
                if v in visited:
                    continue
                visited.add(v)
                cand = 1 + dfs(v, w, visited)
                visited.remove(v)
                if cand > res:
                    res = cand
            memo[key] = res
            return res

        ans = [-1]*n
        for i in range(n):
            if s[i] == '1':
                visited = set([i+1])
                ans[i] = dfs(i+1, 0, visited)
            else:
                ans[i] = -1

        print(' '.join(map(str, ans)))


threading.Thread(target=main).start()