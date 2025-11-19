import sys
import threading
def main():
    import sys
    from array import array
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [0] * (N + 1)
    for i in range(1, N+1):
        A[i] = int(next(it))
    # build children adjacency
    children = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        p = A[i]
        children[p].append(i)
    # detect cycles
    visited = [False] * (N+1)
    tag = [0] * (N+1)
    is_cycle = [False] * (N+1)
    comps = []
    for i in range(1, N+1):
        if not visited[i]:
            u = i
            path = []
            # walk until hit visited
            while not visited[u]:
                tag[u] = i
                path.append(u)
                u = A[u]
            if tag[u] == i:
                # found cycle starting at u
                idx = path.index(u)
                cyc = path[idx:]
                for v in cyc:
                    is_cycle[v] = True
                comps.append(cyc)
            # mark all in path visited and clear tag
            for v in path:
                visited[v] = True
                tag[v] = 0
    # build children2: only non-cycle children
    children2 = [[] for _ in range(N+1)]
    for u in range(1, N+1):
        if not is_cycle[u]:
            # u non-cycle, but children2 used for all u
            pass
        for v in children[u]:
            if not is_cycle[v]:
                children2[u].append(v)
    # BFS to compute depth of non-cycle nodes
    from collections import deque
    depth = [-1] * (N+1)
    dq = deque()
    for u in range(1, N+1):
        if is_cycle[u]:
            depth[u] = 0
            dq.append(u)
    while dq:
        u = dq.popleft()
        for v in children2[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                dq.append(v)
    # collect non-cycle nodes, sort by depth descending
    non_cycle_nodes = [u for u in range(1, N+1) if not is_cycle[u]]
    non_cycle_nodes.sort(key=lambda x: depth[x], reverse=True)
    mod = 998244353
    # DP H arrays for non-cycle nodes
    H = {}
    # temp array reuse for dp
    for u in non_cycle_nodes:
        ch = children2[u]
        # if leaf
        if not ch:
            # H[u][k] = sum_{i=1..k} 1 = k
            arr = array('I', [0]) * (M+1)
            # need to set arr[0]=0, arr[k]=k
            for k in range(1, M+1):
                arr[k] = k
            H[u] = arr
        else:
            # compute dp[u][k] = prod_{c in ch} H[c][k]
            dp_u = array('I', [1]) * (M+1)
            dp_u[0] = 0
            for c in ch:
                Hc = H[c]
                # multiply elementwise
                for k in range(1, M+1):
                    # Python int * int % mod => int fits in 32-bit unsigned
                    dp_u[k] = (dp_u[k] * Hc[k]) % mod
            # prefix sum into H[u]
            arr = array('I', [0]) * (M+1)
            s = 0
            for k in range(1, M+1):
                s += dp_u[k]
                if s >= mod: s %= mod
                arr[k] = s
            H[u] = arr
    # Now process each cycle component
    ans = 1
    for cyc in comps:
        # collect all non-cycle children of cycle nodes
        cch = []
        for c in cyc:
            # children2[c] gives non-cycle children
            for v in children2[c]:
                cch.append(v)
        # P[t]
        P = [1] * (M+1)
        for v in cch:
            Hv = H[v]
            for t in range(1, M+1):
                P[t] = (P[t] * Hv[t]) % mod
        # sum P[1..M]
        s = 0
        for t in range(1, M+1):
            s += P[t]
            if s >= mod: s -= mod
        ans = ans * s % mod
    print(ans)

if __name__ == "__main__":
    main()