n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = [input().strip() for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        if all(s[i + k][j:j + m] == t[k] for k in range(m)):
            print(i + 1, j + 1)
            exit()