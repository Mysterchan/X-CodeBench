import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 全マスの値の総和
total_sum = sum(sum(row) for row in A)

# マス(i,j)をノード番号に変換
def node(i, j):
    return i * W + j

N = H * W

# グラフ構築（最大重みマッチング用）
# 黒白分け：チェス盤のように (i+j) % 2 == 0 を黒、1を白とする
# 黒から白への辺のみを張る
edges = [[] for _ in range(N)]

for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            u = node(i, j)
            # 右隣
            if j + 1 < W:
                v = node(i, j + 1)
                w = A[i][j] + A[i][j + 1]
                edges[u].append((v, w))
            # 下隣
            if i + 1 < H:
                v = node(i + 1, j)
                w = A[i][j] + A[i + 1][j]
                edges[u].append((v, w))

# 最大重み二部マッチング（Hungarian Algorithm）
# 黒側の頂点数 = 黒頂点数 = sum of (i+j)%2==0
# 白側の頂点数 = 白頂点数 = sum of (i+j)%2==1
# ただし、Nは全頂点数なので、黒白の数は異なる場合がある
# そのため、黒頂点数と白頂点数を数える
black_nodes = []
white_nodes = []
for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            black_nodes.append(node(i, j))
        else:
            white_nodes.append(node(i, j))

black_id = [-1] * N
for i, b in enumerate(black_nodes):
    black_id[b] = i
white_id = [-1] * N
for i, w_ in enumerate(white_nodes):
    white_id[w_] = i

n_black = len(black_nodes)
n_white = len(white_nodes)

# 重み行列を作る（黒->白）
# 初期化は-∞（ここでは非常に小さい値）
INF = 10**15
cost = [[-INF] * n_white for _ in range(n_black)]
for u in range(N):
    if black_id[u] == -1:
        continue
    for v, w in edges[u]:
        if white_id[v] == -1:
            continue
        cost[black_id[u]][white_id[v]] = w

# Hungarian Algorithm 実装
def hungarian(cost):
    n = len(cost)
    m = len(cost[0]) if n > 0 else 0
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            j1 = 0
            delta = INF
            for j in range(1, m + 1):
                if not used[j]:
                    cur = u[i0] + v[j] - cost[i0 - 1][j - 1]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    # p[j]: i matched with j
    # j=0はダミー
    match = [-1] * n
    for j in range(1, m + 1):
        if p[j] != 0:
            match[p[j] - 1] = j - 1
    # 最大重み和は -v[0]
    return -v[0], match

max_match_weight, match = hungarian(cost)

# ドミノを置いたマスの値の和は max_match_weight
# スコアは置かれていないマスの値の和なので
# total_sum - max_match_weight が答え
print(total_sum - max_match_weight)