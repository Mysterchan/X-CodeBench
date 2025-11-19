R = int(input())

count = 0
# 正方形の中心が (i, j) のとき、4つの頂点は (i±0.5, j±0.5)
# 4つの頂点全てが原点からの距離 R 以下である必要がある
# 最も遠い頂点は (|i|+0.5, |j|+0.5) の距離
# よって、sqrt((|i|+0.5)^2 + (|j|+0.5)^2) <= R

# 対称性から、i >= 0, j >= 0 の範囲でカウントして4倍する
# ただし、軸上と原点は重複を避ける必要がある

R_sq = R * R

# i = 0, j = 0 の場合
if 0.5 * 0.5 + 0.5 * 0.5 <= R_sq:
    count += 1

# i = 0, j > 0 の場合
for j in range(1, R + 1):
    if (0.5) ** 2 + (j + 0.5) ** 2 <= R_sq:
        count += 1
    else:
        break

# i > 0, j = 0 の場合
for i in range(1, R + 1):
    if (i + 0.5) ** 2 + (0.5) ** 2 <= R_sq:
        count += 1
    else:
        break

# i > 0, j > 0 の場合
for i in range(1, R + 1):
    max_dist_sq_i = (i + 0.5) ** 2
    if max_dist_sq_i + 0.5 ** 2 > R_sq:
        break
    for j in range(1, R + 1):
        max_dist_sq = max_dist_sq_i + (j + 0.5) ** 2
        if max_dist_sq <= R_sq:
            count += 1
        else:
            break

# 対称性を利用
# i = 0, j > 0 と i > 0, j = 0 は同じ個数
# i > 0, j > 0 の領域は4つある
count = 1 + 2 * (count - 1 - (count - 1 - (len([j for j in range(1, R + 1) if (0.5) ** 2 + (j + 0.5) ** 2 <= R_sq]))))

# 再計算
count = 0
for i in range(-R, R + 1):
    for j in range(-R, R + 1):
        max_dist_sq = (abs(i) + 0.5) ** 2 + (abs(j) + 0.5) ** 2
        if max_dist_sq <= R_sq:
            count += 1

print(count)