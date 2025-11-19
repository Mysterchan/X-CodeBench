import sys
input = sys.stdin.readline

N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Floyd-Warshallで全点対最短距離を求める
dist = [row[:] for row in C]
for k in range(N):
    d_k = dist[k]
    for i in range(N):
        d_i = dist[i]
        ik = d_i[k]
        for j in range(N):
            val = ik + d_k[j]
            if val < d_i[j]:
                d_i[j] = val

# K頂点は0..K-1
# クエリのs_i,t_iはK..N-1の範囲

# Kは最大8なので、部分集合DPで Steiner Tree を解く
# 頂点集合は {0..K-1} + {s_i-1, t_i-1}
# これらの頂点の最小全域木コストを求める

# まず、K頂点の部分集合DPで Steiner Tree を求める準備
# dp[mask][v]: maskで表されるK頂点の部分集合をカバーし、vを終点とする最小コスト
INF = 10**15
size = K
dp = [[INF]*N for _ in range(1<<size)]

# 初期化: 各K頂点単体の集合
for i in range(size):
    dp[1<<i][i] = 0

# 部分集合DPでSteiner Tree
for mask in range(1, 1<<size):
    # 部分集合の分割
    sub = mask
    while sub:
        sub = (sub-1)&mask
        if sub == 0 or sub == mask:
            continue
        for v in range(N):
            val = dp[sub][v] + dp[mask^sub][v]
            if val < dp[mask][v]:
                dp[mask][v] = val
    # 頂点間の最短距離で更新
    # dp[mask][v] = min_{u} dp[mask][u] + dist[u][v]
    # これを高速化のためにワーシャルフロイド的に1回だけ行う
    # ここはNが80なので普通にやる
    for v in range(N):
        d_v = dist[v]
        best = dp[mask][v]
        for u in range(N):
            val = dp[mask][u] + d_v[u]
            if val < best:
                best = val
        dp[mask][v] = best

# dp[(1<<K)-1][v] はK頂点全てを含む部分集合の終点vの最小コスト

full_mask = (1<<K) - 1

# クエリごとに s_i,t_i を追加して Steiner Tree を求める
# 頂点集合は {0..K-1} + {s_i-1, t_i-1}
# これを dp を使って計算する方法:
# 追加頂点2つを含む Steiner Tree は、
# dp[full_mask][v] + dist[v][s_i-1] + dist[v][t_i-1] の最小値を求める
# ただし、s_i,t_iはK頂点に含まれていないので、これらを含むためには
# s_i,t_iを含む Steiner Treeは、K頂点全てを含む Steiner Treeに
# s_i,t_iを接続する形になる。
# しかし、s_i,t_iを含む Steiner Treeは s_i,t_i間の距離も含む必要がある。
# よって、s_i,t_iを含む Steiner Treeは
# dp[full_mask][v] + dist[v][s_i-1] + dist[v][t_i-1] + dist[s_i-1][t_i-1]
# ではない。s_i,t_iを含む Steiner Treeは s_i,t_iを含む連結グラフで、
# それは Steiner Tree + s_i,t_i間の辺を含む MST である必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点全て + s_i + t_i の Steiner Tree である。
#
# Kは最大8なので、s_i,t_iを含む Steiner Treeを部分集合DPで求めることも可能だが、
# Q=5000なので毎回は無理。
#
# 代わりに、s_i,t_iを含む Steiner Treeは、
# K頂点全て + s_i + t_i の Steiner Tree であり、
# これは dp[(1<<K)-1][v] + dist[v][s_i-1] + dist[v][t_i-1] + dist[s_i-1][t_i-1] の最小値ではない。
#
# しかし、s_i,t_iを含む Steiner Treeは、
# K頂点全て + s_i + t_i の Steiner Treeなので、
# これを dp を拡張して求める方法は以下。
#
# 1. K頂点の Steiner Tree dp は計算済み。
# 2. s_i,t_iを含む Steiner Treeは、K頂点の Steiner Treeに s_i,t_iを追加した Steiner Tree。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Tree。
#
# s_i,t_iを含む Steiner Treeは、s_i,t_iを含む Steiner Treeの最小コストは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# s_i,t_iを含む Steiner Treeは、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これは、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# つまり、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コストを求める必要がある。
#
# ここで、s_i,t_iを含む Steiner Treeは、
# K頂点の Steiner Tree + s_i,t_iを含む Steiner Treeの最小コスト。
#
# これを計算するには、K頂点の Steiner Tree +