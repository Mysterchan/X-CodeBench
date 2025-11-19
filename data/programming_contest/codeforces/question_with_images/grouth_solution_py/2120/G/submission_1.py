def solve():
    n,m,k = [int(t) for t in input().split()]
    adj = [[int(t)-1 for t in input().split()] for _ in range(m)]
    edges = [[] for _ in range(n)]
    for x,y in adj:
        edges[y].append(x)
        edges[x].append(y)
    deg = [len(edges[i]) for i in range(n)]

    if all(e%2 == 0 for e in deg): return 1
    f1 = 0
    f2 = 0
    for i in range(n):
        odd = sum((deg[j]-deg[i])&1 for j in edges[i])
        even = deg[i] - odd
        f1 += odd
        f2 += odd*even
    f1 //= 2
    if k == 1: return f1 in (0,2)
    if k == 2: return f2 in (0,2)
    if f2 == 0: return 1

    odd1,odd2 = [i for i in range(n) if deg[i]&1]
    if odd1 in edges[odd2]: return 0
    if deg[odd1] == deg[odd2] == 1:
        z = n
        for c in odd1,odd2:
            prev = c
            cnt = 0
            while deg[c] <= 2:
                cnt += 1
                x = edges[c][0]
                if x == prev: x = edges[c][1]
                prev,c = c,x
            z = min(z,cnt)
        return k <= z
    if f1 == m*n: return 1
    return 0

for _ in range(int(input())): print("Yes" if solve() else "No")
