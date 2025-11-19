import sys
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def compress_cycles(a):
    n = len(a)
    graph = [[] for _ in range(n)]
    for i, to in enumerate(a):
        graph[i].append(to)

    index = [-1] * n
    lowlink = [0] * n
    on_stack = [False] * n
    stack = []
    idx = 0
    sccs = []

    def strongconnect(v):
        nonlocal idx
        index[v] = idx
        lowlink[v] = idx
        idx += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if index[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(n):
        if index[v] == -1:
            strongconnect(v)

    scc_id = [0] * n
    for i, comp in enumerate(sccs):
        for v in comp:
            scc_id[v] = i

    m = len(sccs)
    new_graph = [[] for _ in range(m)]
    for v in range(n):
        for w in graph[v]:
            if scc_id[v] != scc_id[w]:
                new_graph[scc_id[v]].append(scc_id[w])

    for i in range(m):
        new_graph[i] = list(set(new_graph[i]))

    return sccs, new_graph

def solve(n, m, a):
    a = [x-1 for x in a]

    _, inv_E = compress_cycles(a)
    n_scc = len(inv_E)
    E = [[] for _ in range(n_scc)]
    for i in range(n_scc):
        for j in inv_E[i]:
            E[j].append(i)

    roots = [i for i in range(n_scc) if len(inv_E[i]) == 0]

    # dp[i][ub]: number of sequences for node i with upper bound ub
    # We'll compute dp[i] as a list of length m+1, where dp[i][ub] = number of sequences with max value ≤ ub
    dp = [None] * n_scc

    def dfs(i):
        if dp[i] is not None:
            return dp[i]
        if len(E[i]) == 0:
            # leaf node: dp[i][ub] = ub (since x_i can be any in [1..ub])
            dp[i] = [0]*(m+1)
            for ub in range(1, m+1):
                dp[i][ub] = ub
            return dp[i]

        # For each child j in E[i], get dp[j]
        child_dp = [dfs(j) for j in E[i]]

        # We want dp[i][ub] = sum_{nub=1}^{ub} product over children of dp[j][nub]
        # To do this efficiently, precompute prefix products for each child

        # For each child, prefix sums of dp[j]
        # Actually dp[j][ub] already represents number of sequences with max ≤ ub
        # So product over children dp[j][nub] can be computed for nub=1..m

        # We'll compute for nub=1..m:
        # prod[nub] = product over children dp[j][nub]

        prod = [1]*(m+1)
        for jdp in child_dp:
            for ub in range(1, m+1):
                prod[ub] = (prod[ub] * jdp[ub]) % MOD

        # Now dp[i][ub] = sum_{nub=1}^{ub} prod[nub]
        # Precompute prefix sums of prod
        prefix = [0]*(m+1)
        for ub in range(1, m+1):
            prefix[ub] = (prefix[ub-1] + prod[ub]) % MOD

        dp[i] = prefix
        return dp[i]

    ans = 1
    for root in roots:
        dp_root = dfs(root)
        ans = (ans * dp_root[m]) % MOD
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))