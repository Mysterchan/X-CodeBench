import sys
from collections import defaultdict, deque

def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Convert to 0-indexed
    A = [a - 1 for a in A]
    
    # Find SCCs in functional graph
    visited = [False] * N
    scc_id = [-1] * N
    scc_count = 0
    
    for start in range(N):
        if visited[start]:
            continue
        
        # Find cycle from this component
        path = []
        curr = start
        positions = {}
        
        while curr not in positions and not visited[curr]:
            positions[curr] = len(path)
            path.append(curr)
            curr = A[curr]
        
        if visited[curr]:
            # Reached already processed component
            for node in path:
                visited[node] = True
                scc_id[node] = scc_count
                scc_count += 1
        else:
            # Found a cycle
            cycle_start = positions[curr]
            
            # Nodes before cycle are separate SCCs
            for i in range(cycle_start):
                visited[path[i]] = True
                scc_id[path[i]] = scc_count
                scc_count += 1
            
            # Cycle nodes form one SCC
            for i in range(cycle_start, len(path)):
                visited[path[i]] = True
                scc_id[path[i]] = scc_count
            scc_count += 1
    
    # Build DAG of SCCs
    scc_size = [0] * scc_count
    scc_out = [set() for _ in range(scc_count)]
    in_degree = [0] * scc_count
    
    for i in range(N):
        scc_size[scc_id[i]] += 1
        if scc_id[i] != scc_id[A[i]]:
            if scc_id[A[i]] not in scc_out[scc_id[i]]:
                scc_out[scc_id[i]].add(scc_id[A[i]])
                in_degree[scc_id[A[i]]] += 1
    
    # DP on DAG
    dp = [0] * scc_count
    
    # Topological sort
    queue = deque()
    for i in range(scc_count):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = M
    
    while queue:
        u = queue.popleft()
        
        for v in scc_out[u]:
            # Values in v must be >= values in u
            # If u can have values 1..dp[u], then v can have values 1..M
            # But we need x_u <= x_v, and all nodes in SCC have same value
            # So if u has k choices, v has M-k+1 to M, but that's wrong
            # Actually: if u takes value from 1..dp[u], v takes from that value..M
            dp[v] = (dp[v] + dp[u]) % MOD
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Answer is product over all SCCs
    result = 1
    for i in range(scc_count):
        result = (result * dp[i]) % MOD
    
    print(result)

solve()