H, W = map(int, input().split())
S = [input() for _ in range(H)]

min_i = 1000
min_j = 1000
max_i = 0
max_j = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if S[i][j] == '.':
            print("No")
            exit()

print("Yes")