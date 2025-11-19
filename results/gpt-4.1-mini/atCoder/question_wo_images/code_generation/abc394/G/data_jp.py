import sys
import collections
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(H)]

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 1. 通路は同じ階数で隣接区画間を移動可能（ただし相手のビルの階数がその階以上であること）
# 2. 階段は同じビル内で上下1階ずつ移動可能（1階未満や最上階超えは不可）
# 3. 階段の使用回数を最小化したい

# 問題の本質は「階数Xでの区画間の移動（通路）」と「同じ区画内の階段移動」の組み合わせ。
# 通路は同じ階数で隣接区画間を移動できるが、相手のビルの階数がX階以上でなければならない。

# 階数は最大10^6で大きいが、H,Wは最大500。
# Qは最大20万。

# 階数を軸にしたグラフを作るのは不可能（10^6階×H×Wは大きすぎる）。

# 重要な観察：
# 通路は同じ階数での区画間移動のみ。
# 階段は同じ区画内の上下階移動のみ。

# つまり、階数Xでの区画間の移動は、X階以上のビルの区画でのみ可能。

# これを逆に考えると、
# 各階数Xに対して、X階以上のビルの区画で構成されるグラフがある。
# そのグラフの中で、通路移動は隣接区画間の辺。
# 階段移動は同じ区画内の上下階間の辺。

# 階段の使用回数は上下階移動の回数の合計。

# 階段の使用回数を最小化するためには、
# 通路移動は階段使用回数に影響しない（通路移動は階段使用回数0）。

# つまり、階段使用回数は「階数の差の合計」となる。

# ここで、通路移動は同じ階数での区画間移動なので、
# 通路移動を使うことで、階段移動を減らせる。

# 重要なポイント：
# 通路移動は階段使用回数0で移動可能。
# 階段移動は階段使用回数1で上下1階移動。

# したがって、階段使用回数は「階数の差の合計」だけど、
# 通路移動を使って、階数を合わせる区画間移動を行うことができる。

# つまり、階段使用回数は
# |Y_i - X| + |Z_i - X| + 通路移動の階段使用回数(0)
# となるXを選んで、区画(A_i,B_i)と区画(C_i,D_i)がX階で通路移動可能な区画間の経路が存在するかを調べる問題。

# まとめると、
# ある階数Xを選び、
# - (A_i,B_i)のビルの階数がX以上であること
# - (C_i,D_i)のビルの階数がX以上であること
# - X階での通路移動で(A_i,B_i)から(C_i,D_i)へ移動可能であること
# を満たすXを選び、
# 階段使用回数は |Y_i - X| + |Z_i - X| となる。

# このXを最小化すればよい。

# つまり、Xは区画(A_i,B_i)と区画(C_i,D_i)のビルの高さの最小値以下で、
# かつX階での通路移動で2区画が連結である必要がある。

# これを効率的に求める方法は？

# 1. 各階数Xに対して、X階以上のビルの区画で構成されるグラフの連結成分を求める。
# 2. 連結成分IDを記録する。
# 3. クエリで、Xを変化させながら、(A_i,B_i)と(C_i,D_i)が同じ連結成分に属するか判定する。

# しかし、階数は最大10^6で大きすぎる。

# そこで、階数の異なる値は最大H*W個（最大25万）しかない。
# つまり、ビルの高さの異なる値の集合は最大25万。

# これらの高さを降順にソートし、
# 高さhから順に「高さh以上の区画のグラフの連結成分」をUnion-Findで管理する。

# 具体的には、
# 高さの降順に区画を追加し、
# その区画と隣接区画で高さがh以上のものとUnionする。

# これにより、
# ある高さh以上の区画の連結成分がわかる。

# クエリは、
# (A_i,B_i), (C_i,D_i)のビルの高さの最小値以下の高さhで、
# 2区画が同じ連結成分に属する最小のhを求める問題になる。

# これを二分探索で求める。

# 実装方針：
# 1. 各区画の高さを記録し、(高さ, i, j)のリストを作成し降順ソート。
# 2. Union-Findを用意。
# 3. 高さの降順に区画を追加し、隣接区画とUnion。
# 4. クエリは、(A_i,B_i), (C_i,D_i)のビルの高さの最小値を上限に二分探索。
# 5. 二分探索の判定は、ある高さhで2区画が同じ連結成分かどうか。

# ただし、Q=2*10^5なので、各クエリに対して二分探索(最大約20回)は4*10^6回の判定。
# 判定はUnion-FindのfindでO(α(N))なので可能。

# さらに高速化のために、クエリをまとめて処理する方法を使う。

# クエリの二分探索を同時に行う方法：
# - クエリごとに二分探索の範囲を管理。
# - 各高さhで、クエリの判定を行い、条件を満たすかで二分探索の範囲を更新。
# - 高さの降順に区画を追加しながら、クエリの判定を行う。

# これを「オフライン二分探索」と呼ぶ。

# 実装手順：
# - 高さの異なる値を降順にソートし、index付け。
# - 各区画の高さのindexを記録。
# - クエリは、二分探索の範囲を[0, max_height_index]で管理。
# - 各ループでmidを計算し、midの高さでUnion-Findを構築し、
#   クエリの2区画が同じ連結成分か判定。
# - 条件を満たすなら右端をmidに、満たさないなら左端をmid+1に更新。
# - 最終的に各クエリの最小の高さindexを得る。

# ただし、Union-Findを毎回作り直すのは重い。
# そこで、Union-Findを高さの降順に区画を追加しながら進め、
# クエリを高さindexごとにまとめて処理する。

# 具体的には、
# - クエリの二分探索のmidを管理し、
# - 各midに属するクエリをまとめる。
# - 高さの降順に区画を追加しながら、
#   その高さindexに対応するmidのクエリを判定。

# これを繰り返す。

# 実装詳細は以下。

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)

# 各区画を1次元に変換
def pos(i,j):
    return i*W + j

# 高さの異なる値を取得し降順ソート
heights = []
for i in range(H):
    for j in range(W):
        heights.append(F[i][j])
unique_heights = sorted(set(heights), reverse=True)
h_to_idx = {h:i for i,h in enumerate(unique_heights)}

# 各区画の高さindex
height_idx = [[h_to_idx[F[i][j]] for j in range(W)] for i in range(H)]

# 高さindexごとに区画をまとめる（降順）
# unique_heightsは降順なので、indexが小さいほど高い
pos_by_height = [[] for _ in range(len(unique_heights))]
for i in range(H):
    for j in range(W):
        pos_by_height[height_idx[i][j]].append((i,j))

# クエリの二分探索範囲
# left: 条件を満たさない高さindexの最小値
# right: 条件を満たす高さindexの最小値
# 初期はleft=0, right=len(unique_heights)
# 条件を満たす高さindexは0以上len(unique_heights)-1以下
# 条件を満たさないはlen(unique_heights)（範囲外）

left = [0]*Q
right = [len(unique_heights)]*Q

# クエリの情報を整理
# 0-indexに変換
A = [a-1 for a,b,y,c,d,z in queries]
B = [b-1 for a,b,y,c,d,z in queries]
Y = [y for a,b,y,c,d,z in queries]
C = [c-1 for a,b,y,c,d,z in queries]
D = [d-1 for a,b,y,c,d,z in queries]
Z = [z for a,b,y,c,d,z in queries]

# クエリのビル高さの最小値を求めて、その高さindexの範囲で二分探索
min_height_idx = []
for i in range(Q):
    h1 = F[A[i]][B[i]]
    h2 = F[C[i]][D[i]]
    m = min(h1,h2)
    # mの高さindexを取得
    # m以上の高さindexはh_to_idx[m]以下（unique_heightsは降順）
    # ただしmがunique_heightsにない場合は近い値を探す
    # unique_heightsは降順なので、m以上の高さはindex <= h_to_idx[m]
    # m以下の高さはindex >= h_to_idx[m]
    # ここではm以上の高さindexの最大値を求める
    # bisectで求める
    import bisect
    # unique_heightsは降順なので、降順用に変換
    # 降順配列unique_heightsに対してm以上の高さはindex <= ?
    # bisect_leftで逆順に探す
    # 逆順配列を昇順に変換して探す
    # もしくは自作二分探索
    # ここでは自作で
    # unique_heightsは降順
    # m以上の高さはunique_heights[i] >= m
    # iの最小値を求める
    # つまりunique_heights[i] < mとなる最小のiを探し、その1つ前がm以上の最大index
    # 逆順なので、iを増やすと値は小さくなる
    # なので、iを増やしてunique_heights[i]<mを探す
    # 二分探索
    l2 = 0
    r2 = len(unique_heights)
    while l2 < r2:
        mid2 = (l2+r2)//2
        if unique_heights[mid2] >= m:
            l2 = mid2+1
        else:
            r2 = mid2
    # l2はmより小さい最初のindex
    # m以上の最大indexはl2-1
    idx = l2-1
    if idx < 0:
        # mより大きい高さがない -> 条件を満たす高さはなし
        idx = -1
    min_height_idx.append(idx)

# オフライン二分探索
# 各midに属するクエリを管理
# midは高さindexの範囲[0,len(unique_heights)-1]
# mid = len(unique_heights)は条件を満たさない（範囲外）

# クエリのleft,rightを更新しながら、midごとにクエリをまとめる
# ループは最大20回程度

while True:
    mid_to_queries = [[] for _ in range(len(unique_heights)+1)]
    update = False
    for i in range(Q):
        if left[i] < right[i]:
            update = True
            mid = (left[i] + right[i]) // 2
            mid_to_queries[mid].append(i)
    if not update:
        break

    uf = UnionFind(H*W)
    # 高さindexの降順に区画を追加しUnion
    # 今回はmidが高さindexなので、mid以上の高さの区画を追加する
    # つまり、index=0からmidまでの高さの区画を追加する
    # unique_heightsは降順なのでindexが小さいほど高い
    # なので、index=0からmidまでの区画を追加
    # ただしmidは高さindexなので、mid=0は最高の高さ
    # なので、index=0からmidまでの区画を追加
    # つまり、index=0からmidまでの区画を追加
    # これを効率化するために、index=0からmidまでの区画を順に追加
    # ループでindex=0からmidまで追加
    # ただし、前回のmidと比較して差分だけ追加するのが効率的だが、
    # 今回は毎回作り直すのは重いので、別の方法を考える

    # ここでは毎回作り直すのは重いので、
    # 代わりにindex=0からmidまでの区画を追加するUnion-Findを作る
    # ただしQが多いので、毎回作り直すのは無理

    # よって、midの昇順に処理し、前回のmidとの差分だけ追加する方法に変更

    # そのため、mid_to_queriesをmidの昇順で処理し、
    # ufを使いまわす

    # ここではmid_to_queriesをmidの昇順で処理するためにbreakし、
    # ループを分ける

    break

# 上記の理由で、オフライン二分探索をmidの昇順で処理する実装に変更

# left,rightの初期化
left = [0]*Q
right = [len(unique_heights)]*Q

# クエリの集合を管理
import math

while True:
    mid_to_queries = [[] for _ in range(len(unique_heights)+1)]
    update = False
    for i in range(Q):
        if left[i] < right[i]:
            update = True
            mid = (left[i] + right[i]) // 2
            mid_to_queries[mid].append(i)
    if not update:
        break

    uf = UnionFind(H*W)
    added = [False]*(H*W)
    # unique_heightsは降順
    # index=0が最高の高さ
    # indexが大きくなるほど高さは低い

    # indexを0から順に進めていき、
    # mid_to_queries[mid]のmidに達したら判定

    # 追加済みの区画を管理
    # index=0からmax_midまで順に追加

    # max_midを求める
    max_mid = max(i for i in range(len(unique_heights)+1) if mid_to_queries[i])

    # index=0からmax_midまで順に追加
    # ただしmax_mid == len(unique_heights)は範囲外なので無視
    max_mid = min(max_mid, len(unique_heights)-1)

    # 追加済みのindexの最大値
    current = -1

    # 追加済みの区画を管理するために、index=0からmax_midまで追加
    # その後、mid_to_queries[mid]のクエリを判定

    # 追加済みのindexを管理しながらmidを進める
    # midは0からmax_midまで

    # ここでmidを0からmax_midまで順に処理
    # ただしmid_to_queries[mid]が空なら判定不要

    # 追加済みのindexをcurrentで管理し、midがcurrentより大きければ追加を進める

    # 追加済みのindexをcurrentで管理し、midがcurrentより小さければ戻れないので注意

    # なのでmidは昇順で処理

    # mid_to_queriesのindexを昇順で処理
    for mid in range(max_mid+1):
        # current < midならmidまで追加
        for hidx in range(current+1, mid+1):
            for (i,j) in pos_by_height[hidx]:
                p = pos(i,j)
                added[p] = True
                # 隣接区画で追加済みのものとunion
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= ni < H and 0 <= nj < W:
                        np = pos(ni,nj)
                        if added[np]:
                            uf.union(p,np)
        current = mid

        # mid_to_queries[mid]のクエリを判定
        for qi in mid_to_queries[mid]:
            # クエリの2区画が同じ連結成分か判定
            p1 = pos(A[qi],B[qi])
            p2 = pos(C[qi],D[qi])
            # 2区画のビルの高さがunique_heights[mid]以上か確認
            # unique_heightsは降順なので、indexが小さいほど高い
            # つまり、unique_heights[mid]は高さの閾値
            # 2区画の高さがunique_heights[mid]以上であることは
            # height_idx[A[qi]][B[qi]] <= mid
            # height_idx[C[qi]][D[qi]] <= mid
            # で判定可能
            if height_idx[A[qi]][B[qi]] <= mid and height_idx[C[qi]][D[qi]] <= mid and uf.same(p1,p2):
                right[qi] = mid
            else:
                left[qi] = mid+1

# left[i]が条件を満たす最小の高さindex
# left[i] == len(unique_heights)なら条件を満たす高さがない

# 階段使用回数は |Y_i - X| + |Z_i - X| でX = unique_heights[left[i]]

# ただしleft[i] == len(unique_heights)の場合は条件を満たす高さがないので、
# その場合はビルの高さの最小値以下で連結成分が存在しないので、
# 階段使用回数は |Y_i - min_height| + |Z_i - min_height| でmin_heightは0以下の値はないので、
# ここでは問題文の制約から必ず連結成分は存在すると考えられる。

# しかし念のため、left[i] == len(unique_heights)の場合は
# 階段使用回数は |Y_i - min_height| + |Z_i - min_height| でmin_heightは0とする。

for i in range(Q):
    if left[i] == len(unique_heights):
        # 条件を満たす高さがない場合
        # 階段使用回数は |Y_i - 1| + |Z_i - 1| （1階が最低階）
        # ただし問題文で(1 ≤ Y_i ≤ F_{A_i,B_i})なので1階は存在する
        # ここでは1階を選ぶのが最善と仮定
        ans = abs(Y[i]-1) + abs(Z[i]-1)
    else:
        X = unique_heights[left[i]]
        ans = abs(Y[i]-X) + abs(Z[i]-X)
    print(ans)