MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # The condition is: x_i ≤ x_{A_i} for every i.
    # This means for each i, x_i ≤ x_{A_i}.
    # We want to count the number of sequences x with elements in [1..M] satisfying this.

    # Let's analyze the constraints:
    # For each i, x_i ≤ x_{A_i}.
    # This implies that for any i, x_i ≤ x_{A_i}.
    # If we consider the graph with edges i -> A_i, the condition is x_i ≤ x_{A_i}.
    # So along the edge from i to A_i, the value at i is ≤ value at A_i.

    # This means that along the edges, values are non-decreasing from i to A_i.
    # Since each node has exactly one outgoing edge (to A_i), the graph is a collection of components,
    # each containing exactly one cycle (because each node has outdegree 1).

    # On the cycle, the condition x_i ≤ x_{A_i} for all i in the cycle implies
    # x_i ≤ x_{A_i} for all edges in the cycle.
    # Since the cycle edges form a cycle, the inequalities imply all x_i on the cycle are equal.

    # For nodes not on the cycle (in the tree leading to the cycle), the condition x_i ≤ x_{A_i}
    # means values are non-decreasing along the path towards the cycle.

    # So the problem reduces to:
    # For each cycle:
    #   - All nodes in the cycle have the same value v (1 ≤ v ≤ M).
    #   - For each node in the tree leading to the cycle, values are ≤ the value of the node it points to,
    #     so values are ≤ v and non-decreasing towards the cycle.
    #
    # We want to count the number of assignments of values to all nodes in the component,
    # given the cycle value v, and sum over v=1..M.

    # Approach:
    # 1. Find all cycles and their components.
    # 2. For each component:
    #    - Identify the cycle nodes.
    #    - For each cycle value v in [1..M]:
    #       - Count the number of ways to assign values to the trees leading to the cycle,
    #         with values ≤ v and non-decreasing towards the cycle.
    #    - Sum over v.
    # 3. Multiply the counts for all components modulo MOD.

    # Implementation details:
    # - Find cycles using DFS or Union-Find.
    # - For each component, find cycle nodes.
    # - For each node in the tree, we want to count the number of sequences x_i ≤ x_{A_i} ≤ v.
    #   Since edges go from i to A_i, and x_i ≤ x_{A_i}, values are non-decreasing towards the cycle.
    #
    # We can do DP from leaves towards the cycle:
    # For each node u, define dp[u][val] = number of ways to assign values to subtree rooted at u,
    # with x_u = val, and values ≤ v.
    #
    # Since x_u ≤ x_{A_u}, and A_u is the parent in the tree, we have x_u ≤ x_{A_u}.
    # So for children c of u (where u = A_c), we have x_c ≤ x_u.
    #
    # So the edges in the tree are reversed compared to the given edges:
    # Given i -> A_i, the tree edges are from child i to parent A_i.
    # So the parent is A_i, and children are nodes j with A_j = u.
    #
    # For each node u, dp[u][val] = product over children c of sum_{x_c ≤ val} dp[c][x_c].
    #
    # We can compute prefix sums to speed up sum_{x_c ≤ val} dp[c][x_c].
    #
    # For cycle nodes, all have the same value v.
    #
    # So for each v:
    #   - For each node in the tree, compute dp[u][val] for val ≤ v.
    #   - For cycle nodes, dp[u][val] = 1 if val == v else 0.
    #
    # Then the number of ways for the component with cycle value v is:
    #   product over cycle nodes u of dp[u][v] (which is 1) times product over trees attached to cycle nodes.
    #
    # Actually, cycle nodes have no children in the tree (since cycle nodes form a cycle),
    # so dp[u][v] = 1 for cycle nodes.
    #
    # The trees are rooted at cycle nodes.
    #
    # So for each cycle node u:
    #   - For each child c of u (where A_c = u and c not in cycle), compute dp[c].
    #   - Then dp[u][v] = product over children c of sum_{x_c ≤ v} dp[c][x_c].
    #   - Since cycle node u has fixed value v, dp[u][val] = 1 if val == v else 0.
    #
    # So the number of ways for the component with cycle value v is:
    #   product over cycle nodes u of product over children c of sum_{x_c ≤ v} dp[c][x_c].
    #
    # We sum this over v=1..M.

    # Let's implement this.

    # Step 1: Find cycles and components
    visited = [0]*N  # 0=unvisited,1=visiting,2=visited
    comp_id = [-1]*N
    cycle_nodes_list = []
    comp_count = 0

    def dfs_cycle(u):
        stack = []
        while True:
            if visited[u] == 0:
                visited[u] = 1
                stack.append(u)
                u = A[u]-1
            elif visited[u] == 1:
                # Found a cycle
                cycle_start = u
                cycle = []
                while True:
                    w = stack.pop()
                    cycle.append(w)
                    if w == cycle_start:
                        break
                cycle.reverse()
                return cycle, stack
            else:
                # visited[u] == 2
                return None, stack

    # We will find all components by repeatedly running dfs_cycle on unvisited nodes
    # and assign component ids.

    # Also build adjacency list for reverse edges (children)
    children = [[] for _ in range(N)]
    for i in range(N):
        children[A[i]-1].append(i)

    # To assign component ids, we do a DFS from cycle nodes to mark all nodes in component
    def mark_component(u, cid):
        stack = [u]
        comp_id[u] = cid
        while stack:
            cur = stack.pop()
            for c in children[cur]:
                if comp_id[c] == -1:
                    comp_id[c] = cid
                    stack.append(c)

    # Find all components and their cycles
    comp_cycles = []
    for i in range(N):
        if visited[i] == 0:
            cycle, stack = dfs_cycle(i)
            # Mark visited nodes in stack as visited=2
            for node in stack:
                visited[node] = 2
            if cycle is not None:
                # Mark cycle nodes visited=2
                for node in cycle:
                    visited[node] = 2
                # Assign component id
                cid = comp_count
                comp_count += 1
                # Mark all nodes reachable from cycle nodes as component cid
                for node in cycle:
                    comp_id[node] = cid
                # BFS/DFS from cycle nodes to mark component nodes
                for node in cycle:
                    mark_component(node, cid)
                comp_cycles.append((cid, cycle))

    # For nodes not assigned to any component (should not happen since graph is N nodes with outdegree 1),
    # assign them to their own component
    for i in range(N):
        if comp_id[i] == -1:
            cid = comp_count
            comp_count += 1
            comp_id[i] = cid
            comp_cycles.append((cid, []))  # no cycle, single node

    # Group nodes by component
    comp_nodes = [[] for _ in range(comp_count)]
    for i in range(N):
        comp_nodes[comp_id[i]].append(i)

    # For each component, we have:
    # - cycle nodes (from comp_cycles)
    # - other nodes in comp_nodes[cid]

    # We will do DP for each component separately and multiply results.

    ans = 1

    for cid, cycle in comp_cycles:
        nodes = comp_nodes[cid]
        cycle_set = set(cycle)

        # Build tree edges for this component:
        # For each node u in component:
        #   children[u] are nodes v with A[v] = u
        # We only consider nodes in this component.
        comp_children = [[] for _ in range(N)]
        for u in nodes:
            for c in children[u]:
                if comp_id[c] == cid:
                    comp_children[u].append(c)

        # For cycle nodes, dp[u][val] = 1 if val == v else 0
        # For non-cycle nodes, dp[u][val] = product over children c of sum_{x_c ≤ val} dp[c][x_c]

        # We will compute for each v in [1..M] the number of ways.

        # To speed up, we do the DP for each v separately.

        # Precompute topological order for the tree nodes (excluding cycle edges)
        # The cycle edges form a cycle, so we remove cycle edges from the tree.
        # The tree edges are from child to parent (i -> A[i]-1)
        # But we want to do DP from leaves to root (cycle nodes).

        # We consider the graph with edges from parent to children (comp_children),
        # but we must exclude cycle edges (edges between cycle nodes).

        # So for each node u, comp_children[u] filtered to exclude cycle nodes.

        # Actually, cycle nodes have no children in the tree (since cycle edges are excluded),
        # so comp_children[u] for cycle nodes is empty.

        # For non-cycle nodes, comp_children[u] are children in the tree.

        # We do a post-order traversal to get topological order.

        # We will do DP for each v:
        # For each node u:
        #   if u in cycle:
        #       dp[u][val] = 1 if val == v else 0
        #   else:
        #       dp[u][val] = product over children c of prefix_sum_c[val]
        # where prefix_sum_c[val] = sum_{x ≤ val} dp[c][x]

        # To optimize memory, we only keep dp arrays for current v.

        # Let's implement.

        # Build tree edges excluding cycle edges
        tree_children = [[] for _ in range(N)]
        for u in nodes:
            for c in comp_children[u]:
                if c not in cycle_set:
                    tree_children[u].append(c)

        # Find nodes in topological order (post-order) for DP
        # We do DFS from cycle nodes to cover all nodes in component

        visited_comp = [False]*N
        order = []

        def dfs_topo(u):
            visited_comp[u] = True
            for c in tree_children[u]:
                if not visited_comp[c]:
                    dfs_topo(c)
            order.append(u)

        for u in cycle:
            if not visited_comp[u]:
                dfs_topo(u)

        # order now has nodes in post-order (children before parents)

        # For each v in [1..M], compute dp and ways for this component

        comp_res = 0

        # To speed up, we can precompute dp for all v in one go using prefix sums and cumulative products.

        # But since N and M are up to 2025, and components can be large,
        # we must be careful with complexity.

        # Let's implement the DP straightforwardly.

        # dp[u] is an array of length M+1 (1-based indexing for convenience)
        # dp[u][val] = number of ways with x_u = val

        # For cycle nodes:
        # dp[u][val] = 1 if val == v else 0

        # For non-cycle nodes:
        # dp[u][val] = product over children c of prefix_sum_c[val]

        # prefix_sum_c[val] = sum_{x=1 to val} dp[c][x]

        # We'll implement for each v separately.

        # To speed up, we can precompute prefix sums for children dp arrays.

        # Let's implement.

        for v in range(1, M+1):
            dp = [None]*N
            # Initialize dp for cycle nodes
            for u in cycle:
                arr = [0]*(v+1)
                arr[v] = 1
                dp[u] = arr

            # For other nodes, dp[u] = None initially

            # Process nodes in order
            for u in order:
                if dp[u] is not None:
                    continue
                # u not in cycle
                # compute dp[u]
                # For each child c, we have dp[c] computed
                # compute prefix sums for dp[c]
                prefix_sums = []
                for c in tree_children[u]:
                    arr = dp[c]
                    prefix = [0]*(v+1)
                    s = 0
                    for val_ in range(1, v+1):
                        s = (s + arr[val_]) % MOD
                        prefix[val_] = s
                    prefix_sums.append(prefix)
                # dp[u][val] = product over children c of prefix_sums_c[val]
                arr = [0]*(v+1)
                for val_ in range(1, v+1):
                    prod = 1
                    for prefix in prefix_sums:
                        prod = (prod * prefix[val_]) % MOD
                    arr[val_] = prod
                dp[u] = arr

            # Now compute ways for this component with cycle value v
            # ways = product over cycle nodes u of product over children c of sum_{x ≤ v} dp[c][x]
            # But we already included children in dp[u] for non-cycle nodes.
            # For cycle nodes, children are only non-cycle nodes.

            # For each cycle node u:
            # ways_u = product over children c of sum_{x ≤ v} dp[c][x]
            # sum_{x ≤ v} dp[c][x] = prefix_sums_c[v]

            ways = 1
            for u in cycle:
                for c in tree_children[u]:
                    arr = dp[c]
                    s = 0
                    for val_ in range(1, v+1):
                        s = (s + arr[val_]) % MOD
                    ways = (ways * s) % MOD

            comp_res = (comp_res + ways) % MOD

        ans = (ans * comp_res) % MOD

    print(ans)


if __name__ == "__main__":
    main()