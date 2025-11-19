MOD = 0x3b800001
TWO_THIRDS = 2*pow(3,-1,MOD)%MOD
POW3 = [1]
POW2 = [1]
for i in range(3000):
    POW3.append( POW3[-1]*3%MOD )
    POW2.append( POW2[-1]*2%MOD )

for _ in range(int(input())):
    n = int(input())
    edges = [[] for _ in range(2*n-1)]
    for e in range(n,2*n-1):
        a,b = [int(t)-1 for t in input().split()]
        edges[a].append(e); edges[e].append(a)
        edges[b].append(e); edges[e].append(b)

    ans = 0
    for center in range(2*n-1):
        par = [center]*(2*n-1)
        depth = [0]*(2*n-1)
        subt = [0]*(2*n-1)

        stack = edges[center][:]
        for e in edges[center]:
            subt[e] = e
            depth[e] = 1

        while stack:
            a = stack.pop()
            p = par[a]
            for b in edges[a]:
                if b == p: continue
                depth[b] = depth[a] + 1
                par[b] = a
                subt[b] = subt[a]
                stack.append(b)

        bins = [[] for _ in range(n)]
        for i, d in enumerate(depth[:n]):
            bins[d >> 1].append(subt[i])

        acc = [0]*(n+1)
        poly = [0]*(n+1)
        radii = [0]*n

        i = 0
        cnt = [0]*(2*n)
        for d in range(n):
            for e in bins[d]: cnt[e] += 1
            for e in bins[d]:
                if cnt[e]:
                    poly[ i+cnt[e] ] -= 1
                    poly[i] += 1
                    cnt[e] = 0
            poly[i] -= 1
            poly[ i+len(bins[d]) ] += 1

            rd = 2*d + (center >= n)
            for _ in range( len(bins[d]) ):
                radii[i] = rd
                acc[i+1] = (TWO_THIRDS*acc[i] + rd)%MOD
                i += 1

        rem = [0]*(n-1)
        for i in range(n,1,-1):
            rem[i-2] = poly[i]
            poly[i-1] += 2*poly[i]
            poly[i-2] -= poly[i]

        for i in range(n-1):
            if i: ans += rem[i] * acc[i] * POW3[i-1]
            ans += rem[i] * (POW3[i] - POW2[i]) * radii[i]
            ans += rem[i] * 2 * radii[i] * POW3[i]
    print( ans%MOD )
