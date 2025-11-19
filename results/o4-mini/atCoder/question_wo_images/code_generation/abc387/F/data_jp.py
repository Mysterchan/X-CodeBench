import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(10000)
    mod = 998244353
    data = sys.stdin.read().split()
    N = int(data[0]); M = int(data[1])
    A = list(map(lambda x: int(x)-1, data[2:]))

    # 1) Precompute S[k] = sum_{t=1..M} t^k mod, for k=0..N
    S = [0] * (N+1)
    for t in range(1, M+1):
        p = 1
        for k in range(0, N+1):
            S[k] = (S[k] + p) % mod
            p = p * t % mod

    # 2) Detect cycles in the functional graph
    visited = [0] * N   # 0=unvisited, -1=visiting, 1=done
    in_cycle = [False] * N
    rep = [-1] * N      # representative (root) for each cycle node
    cycle_roots = []

    for i in range(N):
        if visited[i] != 0:
            continue
        stack = []
        pos = {}
        u = i
        while visited[u] == 0:
            pos[u] = len(stack)
            visited[u] = -1
            stack.append(u)
            u = A[u]
        if visited[u] == -1:
            # found a cycle starting at u
            idx = pos[u]
            cycle = stack[idx:]
            root = u
            cycle_roots.append(root)
            for v in cycle:
                in_cycle[v] = True
                rep[v] = root
        for v in stack:
            visited[v] = 1

    # 3) Count non-cycle nodes feeding into each cycle
    count = {root: 0 for root in cycle_roots}
    for i in range(N):
        if not in_cycle[i]:
            u = i
            # follow until a cycle node
            while not in_cycle[u]:
                u = A[u]
            root = rep[u]
            count[root] += 1

    # 4) Multiply contributions
    ans = 1
    for root in cycle_roots:
        k = count[root]
        ans = ans * S[k] % mod

    print(ans)

if __name__ == "__main__":
    main()