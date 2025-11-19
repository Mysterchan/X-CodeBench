import sys
from collections import defaultdict, deque

def tarjan_scc(n, adj):
    index_counter = [0]
    stack = []
    lowlinks = [0] * (n + 1)
    index = [0] * (n + 1)
    on_stack = [False] * (n + 1)
    index_set = [False] * (n + 1)
    sccs = []
    
    def strongconnect(v):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        index_set[v] = True
        stack.append(v)
        on_stack[v] = True
        
        for w in adj[v]:
            if not index_set[w]:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif on_stack[w]:
                lowlinks[v] = min(lowlinks[v], index[w])
        
        if lowlinks[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)
    
    for v in range(1, n + 1):
        if not index_set[v]:
            strongconnect(v)
    
    return sccs

def solve():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    
    MOD = 998244353
    
    adj = defaultdict(list)
    for i in range(1, n + 1):
        adj[i].append(a[i])
    
    sccs = tarjan_scc(n, adj)
    num_sccs = len(sccs)
    
    node_to_scc = {}
    for idx, scc in enumerate(sccs):
        for node in scc:
            node_to_scc[node] = idx
    
    scc_adj = defaultdict(set)
    for i in range(1, n + 1):
        scc_i = node_to_scc[i]
        scc_ai = node_to_scc[a[i]]
        if scc_i != scc_ai:
            scc_adj[scc_i].add(scc_ai)
    
    indegree = [0] * num_sccs
    for i in range(num_sccs):
        for j in scc_adj[i]:
            indegree[j] += 1
    
    dp = [[0] * (m + 1) for _ in range(num_sccs)]
    
    queue = deque()
    for i in range(num_sccs):
        if indegree[i] == 0:
            queue.append(i)
            for val in range(1, m + 1):
                dp[i][val] = 1
    
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in scc_adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    for u in topo_order:
        for v in scc_adj[u]:
            for val_v in range(1, m + 1):
                for val_u in range(1, val_v + 1):
                    dp[v][val_v] = (dp[v][val_v] + dp[u][val_u]) % MOD
    
    result = sum(dp[i][val] for i in range(num_sccs) for val in range(1, m + 1)) % MOD
    print(result)

solve()