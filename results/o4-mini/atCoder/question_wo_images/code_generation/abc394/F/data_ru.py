import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin
    NEG = -10**18
    N_line = data.readline().strip()
    if not N_line:
        print(-1)
        return
    n = int(N_line)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u,v = map(int, data.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    # Post-order traversal to get processing order and parent
    parent = [0] * (n + 1)
    order = []
    stack = [(1, 0, False)]
    parent[1] = 0
    while stack:
        u, p, visited = stack.pop()
        if visited:
            order.append(u)
        else:
            parent[u] = p
            stack.append((u, p, True))
            for v in adj[u]:
                if v == p:
                    continue
                stack.append((v, u, False))

    # dp1_best1[u]: max nodes in subtree of u (including u),
    #    when edge to parent is selected, and subtree has at least one internal (deg-4) node.
    # dp1_max[u] = max(dp1_best1[u], 1)
    dp1_best1 = [NEG] * (n + 1)
    dp1_max   = [0] * (n + 1)

    ans = NEG

    for u in order:
        # Gather children's dp1_max and dp1_best1
        p1max = []
        max_child_best1 = NEG
        child_count = 0
        pu = parent[u]
        for v in adj[u]:
            if v == pu:
                continue
            child_count += 1
            # dp1_max[v] and dp1_best1[v]
            mv = dp1_max[v]
            p1max.append(mv)
            if dp1_best1[v] > max_child_best1:
                max_child_best1 = dp1_best1[v]

        if child_count > 0:
            p1max.sort(reverse=True)
        # Compute dp1_best1[u]
        if child_count >= 3:
            s3 = p1max[0] + p1max[1] + p1max[2]
            dp1_best1[u] = 1 + s3
        else:
            dp1_best1[u] = NEG
        # dp1_max[u]
        if dp1_best1[u] > 1:
            dp1_max[u] = dp1_best1[u]
        else:
            dp1_max[u] = 1

        # Compute dp0_best1[u], consider u as root (no parent-edge)
        # candidate_leaf: u degree=1, pick one child v s.t. v subtree has internal
        if max_child_best1 > NEG:
            cand_leaf = 1 + max_child_best1
        else:
            cand_leaf = NEG
        # candidate_internal: u degree=4, pick 4 children by dp1_max
        if child_count >= 4:
            s4 = p1max[0] + p1max[1] + p1max[2] + p1max[3]
            cand_internal = 1 + s4
        else:
            cand_internal = NEG

        dp0_best1_u = cand_leaf if cand_leaf > cand_internal else cand_internal
        if dp0_best1_u > ans:
            ans = dp0_best1_u

    # Output result
    if ans < 0:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()