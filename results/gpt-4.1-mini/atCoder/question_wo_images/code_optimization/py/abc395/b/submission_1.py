n = int(input())
mat = [['#'] * n for _ in range(n)]

for i in range(1, n + 1):
    j = n + 1 - i
    if i > j:
        break
    color = '#' if i % 2 == 1 else '.'
    for r in range(i - 1, j):
        for c in range(i - 1, j):
            mat[r][c] = color

for row in mat:
    print(''.join(row))