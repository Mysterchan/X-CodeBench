N, X = map(int, input().split())
AC = [[] for _ in range(3)]
for _ in range(N):
    v, a, c = map(int, input().split())
    AC[v-1].append((a, c))

L = []
for i in range(3):
    l = [0]*(X+1)
    for a, c in AC[i]:
        for x in range(X, c-1, -1):
            l[x] = max(l[x], l[x-c] + a)

    L.append(l)

ans = 0
for c0 in range(X, -1, -1):
    a0 = L[0][c0]
    if a0 <= ans:
        break
    for c1 in range(X-c0, -1, -1):
        a1 = L[1][c1]
        if a1 <= ans:
            break
        c2 = X-c0-c1
        a2 = L[2][c2]
        ans = max(ans, min(a0, a1, a2))

print(ans)