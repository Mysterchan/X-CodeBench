import sys

sys.setrecursionlimit(200005)

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
    a = [_-1 for _ in a]

    _, inv_E = compress_cycles(a)
    n = len(inv_E)
    E = [[] for i in range(n)]
    for i in range(n):
        for j in inv_E[i]:
            E[j].append(i)

    roots = [i for i in range(n) if len(inv_E[i]) == 0]

    dp = [[-1]*(m+1) for i in range(n)]
    def dfs(i, ub):
        if len(E[i]) == 0:
            return ub
        if dp[i][ub] == -1:
            res = 0
            for nub in range(1, ub+1):
                num = 1
                for j in E[i]:
                    num = (num * dfs(j, nub)) % MOD
                res = (res + num) % MOD
            dp[i][ub] = res
        return dp[i][ub]

    ans = 1
    for root in roots:
        ans = (ans * dfs(root, m)) % MOD
    return ans

n, m = map(int, input().split())
a = [*map(int, input().split())]
print(solve(n, m, a))