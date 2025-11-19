import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

def solve():
    n, k = mii()
    g = [[] for _ in range(n)]
    for v, u in enumerate(mii(), 1):
        g[u-1].append(v)
    layers = [1]
    q = [0]
    flag = True
    while q and flag:
        tmp = []
        for u in q:
            if not g[u]:
                flag = False
                break
            tmp.extend(g[u])
        if flag:
            layers.append(len(tmp))
            q = tmp
    tot = sum(layers)
    if tot <= max(k, n-k):
        return len(layers)
    f = 1
    for x in layers:
        f |= f << x
    f &= (1 << (k+1)) - 1
    f >>= tot - n + k
    return len(layers) if f else len(layers) - 1


for _ in range(ii()):
    print(solve())
