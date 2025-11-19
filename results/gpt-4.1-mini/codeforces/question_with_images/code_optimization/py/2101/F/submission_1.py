import sys
input = sys.stdin.readline

MOD = 998244353
INV3 = pow(3, MOD-2, MOD)
TWO_THIRDS = 2 * INV3 % MOD

max_n = 3000
POW3 = [1] * (max_n + 1)
POW2 = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    POW3[i] = POW3[i-1] * 3 % MOD
    POW2[i] = POW2[i-1] * 2 % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[] for _ in range(2*n-1)]
    for e in range(n, 2*n-1):
        a,b = map(lambda x: int(x)-1, input().split())
        edges[a].append(e)
        edges[e].append(a)
        edges[b].append(e)
        edges[e].append(b)

    ans = 0
    # Pre-allocate arrays once to avoid repeated allocations
    par = [0]*(2*n-1)
    depth = [0]*(2*n-1)
    subt = [0]*(2*n-1)
    cnt = [0]*(2*n)
    acc = [0]*(n+1)
    poly = [0]*(n+1)
    radii = [0]*n

    for center in range(2*n-1):
        # Initialize
        for i in range(2*n-1):
            par[i] = center
            depth[i] = 0
            subt[i] = 0
        stack = edges[center][:]
        for e in edges[center]:
            subt[e] = e
            depth[e] = 1
            par[e] = center

        # DFS using stack
        idx = 0
        while idx < len(stack):
            a = stack[idx]
            idx += 1
            p = par[a]
            for b in edges[a]:
                if b == p:
                    continue
                depth[b] = depth[a] + 1
                par[b] = a
                subt[b] = subt[a]
                stack.append(b)

        # Group nodes by (depth//2)
        bins = [[] for _ in range(n)]
        for i in range(n):
            d = depth[i]
            bins[d >> 1].append(subt[i])

        # Reset poly and acc arrays
        for i in range(n+1):
            poly[i] = 0
            acc[i] = 0
        for i in range(n):
            radii[i] = 0
        for i in range(2*n):
            cnt[i] = 0

        i = 0
        for d in range(n):
            for e in bins[d]:
                cnt[e] += 1
            for e in bins[d]:
                c = cnt[e]
                if c:
                    poly[i + c] = (poly[i + c] - 1) % MOD
                    poly[i] = (poly[i] + 1) % MOD
                    cnt[e] = 0
            poly[i] = (poly[i] - 1) % MOD
            poly[i + len(bins[d])] = (poly[i + len(bins[d])] + 1) % MOD

            rd = 2 * d + (1 if center >= n else 0)
            for _ in bins[d]:
                radii[i] = rd
                acc[i+1] = (TWO_THIRDS * acc[i] + rd) % MOD
                i += 1

        rem = [0]*(n-1)
        for i in range(n-1, 0, -1):
            rem[i-1] = poly[i]
            poly[i-1] = (poly[i-1] + 2*poly[i]) % MOD
            poly[i-2] = (poly[i-2] - poly[i]) % MOD

        for i in range(n-1):
            if i > 0:
                ans = (ans + rem[i] * acc[i] * POW3[i-1]) % MOD
            ans = (ans + rem[i] * (POW3[i] - POW2[i]) * radii[i]) % MOD
            ans = (ans + rem[i] * 2 * radii[i] * POW3[i]) % MOD

    print(ans % MOD)