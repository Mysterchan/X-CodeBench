import sys
input = sys.stdin.readline

def blossom(n, edges):
    # Implementation of Edmonds' Blossom algorithm for maximum matching
    # Reference: https://github.com/indy256/codelibrary/blob/master/cpp/graph/edmonds.cpp
    # Adapted to Python and 1-based indexing

    g = [[] for _ in range(n+1)]
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    match = [0]*(n+1)
    p = [0]*(n+1)
    base = list(range(n+1))
    q = []
    used = [False]*(n+1)
    blossom = [False]*(n+1)

    def lca(a,b):
        used_path = [False]*(n+1)
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == 0:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[match[b]]

    def markPath(v, b, x):
        while base[v] != b:
            u = match[v]
            w = p[u]
            base[v] = base[u] = b
            v = w
            if base[v] != b:
                p[v] = x

    def findPath(root):
        nonlocal used, p, base, q
        used = [False]*(n+1)
        p = [0]*(n+1)
        base = list(range(n+1))
        q = [root]
        used[root] = True
        for i in range(len(q)):
            v = q[i]
            for u in g[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != 0 and p[match[u]] != 0):
                    curbase = lca(v,u)
                    blossom = [False]*(n+1)
                    markPath(v, curbase, u)
                    markPath(u, curbase, v)
                    for i_ in range(1,n+1):
                        if blossom[base[i_]]:
                            base[i_] = curbase
                            if not used[i_]:
                                used[i_] = True
                                q.append(i_)
                elif p[u] == 0:
                    p[u] = v
                    if match[u] == 0:
                        return u
                    u_ = match[u]
                    used[u_] = True
                    q.append(u_)
        return 0

    res = 0
    for i in range(1,n+1):
        if match[i] == 0:
            v = findPath(i)
            if v != 0:
                res += 1
                cur = v
                while cur != 0:
                    pv = p[cur]
                    ppv = match[pv]
                    match[cur] = pv
                    match[pv] = cur
                    cur = ppv
    return res

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    edges = [tuple(map(int,input().split())) for __ in range(m)]
    # The problem reduces to finding a maximum subgraph with max degree ≤ 2,
    # which is equivalent to finding a maximum 2-matching.
    # A maximum 2-matching can be found by reducing to maximum matching in a constructed graph.
    # But since n ≤ 30, we can use a known approach:
    # The maximum 2-matching size = maximum matching in the line graph of G plus some adjustments.
    # However, here we can use a known fact:
    # Maximum 2-matching = maximum matching in the graph where each vertex can be matched up to 2 times.
    # This can be solved by splitting each vertex into two copies and connecting edges accordingly,
    # then find maximum matching in the bipartite graph.
    #
    # But simpler approach:
    # Since degree ≤ 2, the subgraph is a collection of paths and cycles.
    # Maximum 2-matching can be found by Edmonds' blossom algorithm on the original graph,
    # but with each vertex duplicated twice to allow degree 2.
    #
    # Construct a graph with 2*n vertices: for each original vertex v, create v_1 and v_2.
    # For each edge (u,v), connect u_1 to v_2 and u_2 to v_1.
    # Then find maximum matching in this bipartite graph.
    #
    # The size of maximum 2-matching = size of maximum matching in this constructed graph.

    # Build bipartite graph with left part: u_1 (1..n), right part: v_2 (n+1..2n)
    # Edges: for each (u,v), add edges u_1->v_2 and v_1->u_2

    # We'll implement a standard maximum bipartite matching (Hungarian or Hopcroft-Karp)
    # on this constructed bipartite graph.

    # Build adjacency for left part (1..n)
    adj = [[] for __ in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Build bipartite graph:
    # Left: 1..n (u_1)
    # Right: 1..n (v_2)
    # Edges: u_1 -> v_2 if (u,v) in edges

    # So right side vertices are also 1..n, but represent v_2
    # We'll run bipartite matching from left to right.

    graph = [[] for __ in range(n+1)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    matchR = [0]*(n+1)

    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == 0 or bpm(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    result = 0
    for u in range(1,n+1):
        seen = [False]*(n+1)
        if bpm(u, seen):
            result += 1

    print(result)