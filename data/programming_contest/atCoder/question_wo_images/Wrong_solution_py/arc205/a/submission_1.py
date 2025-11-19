n, q = map(int, input().split())
mat = [list(input().strip()) for _ in range(n)]

res = [[0] * n for _ in range(n)]

for i in range(n - 1):
    for j in range(n - 1):
        if (mat[i][j] == '.' and mat[i + 1][j] == '.' and
            mat[i][j + 1] == '.' and mat[i + 1][j + 1] == '.'):
            res[i][j] = 1

for i in range(n):
    for j in range(n):
        top = res[i - 1][j] if i > 0 else 0
        left = res[i][j - 1] if j > 0 else 0
        diag = res[i - 1][j - 1] if i > 0 and j > 0 else 0
        res[i][j] += top + left - diag

for _ in range(q):
    u, d, l, r = map(int, input().split())

    d -= 1
    r -= 1
    if d < u or r < l:
        print(0)
        continue
    total = res[d][r]
    if l > 1:
        total -= res[d][l - 2]
    if u > 1:
        total -= res[u - 2][r]
    if l > 1 and u > 1:
        total += res[u - 2][l - 2]
    print(total)