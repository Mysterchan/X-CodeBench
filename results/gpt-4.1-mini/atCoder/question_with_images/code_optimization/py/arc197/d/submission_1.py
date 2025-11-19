import sys
input = sys.stdin.readline

MOD = 998244353

def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    if N == 1:
        print(1)
        return

    # Precompute factorials once per test case
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    # Build sets C[i] as bitsets (integers) for fast subset checks
    C = [0] * N
    for i in range(N):
        bits = 0
        row = A[i]
        for j in range(N):
            if row[j]:
                bits |= 1 << j
        C[i] = bits

    # Check root inclusion: all sets must contain 0
    root_bit = 1 << 0
    for i in range(N):
        if (C[i] & root_bit) == 0:
            print(0)
            return

    # Check pairwise subset condition for edges
    # Only check pairs where A[i][j] == 1 and i < j
    for i in range(N):
        ci = C[i]
        for j in range(i + 1, N):
            if A[i][j] == 1:
                cj = C[j]
                # Check if ci subset cj or cj subset ci
                # subset: x subset y if (x & y) == x
                if not ((ci & cj) == ci or (ci & cj) == cj):
                    print(0)
                    return

    # Check triple condition:
    # For all distinct i,j,k with A[i][j] == 1 and A[j][k] == 1 and A[i][k] == 0,
    # check C[i] subset C[j] and C[k] subset C[j]
    # To optimize, for each j, find neighbors i and k and check pairs
    neighbors = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and i != j:
                neighbors[i].append(j)

    for j in range(N):
        cj = C[j]
        nbrs = neighbors[j]
        ln = len(nbrs)
        # For each pair (i,k) in neighbors[j], check if A[i][k] == 0
        # If so, check subset conditions
        # To avoid O(N^3), we do:
        # For each i in nbrs:
        #   For each k in nbrs with k > i:
        #       if A[i][k] == 0:
        #           check subsets
        # Since sum N^2 over all test cases is small, this is acceptable
        for idx_i in range(ln):
            i = nbrs[idx_i]
            ci = C[i]
            for idx_k in range(idx_i + 1, ln):
                k = nbrs[idx_k]
                if A[i][k] == 0:
                    ck = C[k]
                    if (ci & cj) != ci or (ck & cj) != ck:
                        print(0)
                        return

    # Group nodes by their C[i] sets (bitsets)
    groups = {}
    for i in range(N):
        cset = C[i]
        if cset not in groups:
            groups[cset] = []
        groups[cset].append(i)

    # Check that each group forms a clique (all pairs connected)
    # For each group, check pairs u,v in group: A[u][v] == 1
    # Since groups are sets of nodes with identical C[i], they should be cliques
    for group_nodes in groups.values():
        size = len(group_nodes)
        if size == 1:
            continue
        # Check pairs
        nodes = group_nodes
        for i in range(size):
            u = nodes[i]
            row_u = A[u]
            for j in range(i + 1, size):
                v = nodes[j]
                if row_u[v] == 0:
                    print(0)
                    return

    # Calculate answer
    ans = 1
    c0 = C[0]
    for cset, group_nodes in groups.items():
        cnt = len(group_nodes)
        if cset == c0:
            ans = ans * fact[cnt - 1] % MOD
        else:
            ans = ans * fact[cnt] % MOD

    print(ans)

T = int(input())
for _ in range(T):
    solve()