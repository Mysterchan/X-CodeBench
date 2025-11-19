import sys
input = lambda: sys.stdin.readline().strip()

mod = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    if sum(a[0]) < n:
        print(0)
        continue
    b = [0] * n
    for i in range(n):
        for j in range(n):
            if a[i][j]:
                b[i] += 1 << j
    d = sorted(set(b), key = lambda x: -x.bit_count())
    k = len(d)
    g = [0] * k
    c = [0] * k
    for i in range(k):
        for j in range(n):
            if b[j] == d[i]:
                g[i] += 1 << j
                c[i] += 1
    if any(d[i] & d[j] == d[i] and g[j] & d[i] != g[j] or d[i] & d[j] != d[i] and (d[i] & g[j] or d[j] & g[i]) for i in range(1, k) for j in range(i)):
        print(0)
        continue
    ans = 1
    for i in range(k):
        for j in range(c[i] - (i == 0)):
            ans = ans * (j + 1) % mod
    print(ans)