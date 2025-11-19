H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 黒マスの最小の行・列、最大の行・列を求める
min_r, max_r = H, -1
min_c, max_c = W, -1

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            if i < min_r:
                min_r = i
            if i > max_r:
                max_r = i
            if j < min_c:
                min_c = j
            if j > max_c:
                max_c = j

# 黒マスが1つ以上存在することは問題文の制約で保証されているのでmin_r, max_r, min_c, max_cは有効

# 長方形の範囲内に白マスがあればNo
for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        if S[i][j] == '.':
            print("No")
            exit()

# 長方形の範囲外に黒マスがあればNo
for i in range(H):
    for j in range(W):
        if (i < min_r or i > max_r or j < min_c or j > max_c) and S[i][j] == '#':
            print("No")
            exit()

# それ以外はYes
print("Yes")