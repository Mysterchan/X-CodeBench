import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# LISの長さを求めるための tails 配列
tails = []
# length[i]: A[i] を末尾に持つ LIS の長さ
length = [0] * N

for i, a in enumerate(A):
    pos = bisect.bisect_left(tails, a)
    if pos == len(tails):
        tails.append(a)
    else:
        tails[pos] = a
    length[i] = pos + 1

# length[i] の最大値は tails の長さ以下なので、最大は N
max_len = len(tails)

# 各長さ l (1-based) の要素の A[i] を格納
# length[i] = l の i の A[i] をまとめる
pos_lists = [[] for _ in range(max_len + 1)]
for i in range(N):
    pos_lists[length[i]].append(A[i])

# 各 pos_lists[l] をソートしておく（A[i] は元々の順序だが、X_i 以下の要素を高速に数えたいので）
for l in range(1, max_len + 1):
    pos_lists[l].sort()

# クエリ処理
# クエリ: R_i, X_i
# R_i までの部分列で、X_i 以下の要素のみで LIS の最大長を求める
# length[i] は A[i] を末尾に持つ LIS の長さ
# しかし length[i] は全体の LIS の長さであり、R_i までの制限はない
# そこで、R_i までの制限を考慮するために、length[i] の情報を R_i で区切る必要がある

# しかし、length[i] は LIS の長さであり、i の位置は固定
# R_i までの制限は i <= R_i であるため、i の位置で制限できる
# つまり、i <= R_i かつ A[i] <= X_i の要素の中で最大の length[i] を求める問題

# これを高速に処理するために、length[i] の情報を Fenwick Tree (BIT) で管理する
# ただし length[i] は 1~max_len の範囲
# i の位置でソートされた配列で Fenwick Tree を作り、A[i] の値でフィルタリングするのは難しい

# 代替案：
# length[i] の値は LIS の長さであり、1 <= length[i] <= max_len
# i <= R_i かつ A[i] <= X_i の要素の中で最大の length[i] を求める
# これを高速に行うには、i でソートされた配列を用意し、
# A[i] の値でフィルタリングしつつ length[i] の最大値を求めるデータ構造が必要

# しかし、A[i] の値は最大10^9で大きいので座標圧縮が必要
# さらに、クエリは R_i と X_i の2つの制約がある

# 解法：
# 1. i でソートされた配列は元々 A の順序
# 2. Fenwick Tree を i で構築し、A[i] の値でフィルタリングはできない
# 3. そこで、A[i] の値でソートした配列を作り、Fenwick Tree を構築し、
#    クエリは X_i 以下の A[i] のみを考慮するため、A[i] <= X_i の範囲で Fenwick Tree を使う
# 4. しかし R_i の制約があるため、i <= R_i の制約も必要
# 5. つまり、2次元の制約 (i <= R_i, A[i] <= X_i) で length[i] の最大値を求める問題

# 2次元の範囲最大クエリを高速に処理するには、座標圧縮と2D Fenwick Treeやセグメントツリーが必要
# しかし、N,Q=2*10^5 で2D Fenwick Treeは重い

# 代替案：
# クエリを offline で処理する
# クエリを R_i の昇順にソートし、A[i] を i の昇順で処理しながら Fenwick Tree に length[i] を更新
# Fenwick Tree は A[i] の値で座標圧縮し、A[i] <= X_i の範囲で最大 length[i] を取得

# 実装手順：
# 1. A[i] の値を座標圧縮
# 2. クエリを R_i の昇順にソート
# 3. i を 1 から N まで走査し、Fenwick Tree に length[i] を A[i] の圧縮値の位置に更新
# 4. クエリの R_i に達したら、Fenwick Tree で A[i] <= X_i の最大 length[i] を取得
# 5. 結果を元のクエリ順に出力

# Fenwick Tree (BIT) の実装（最大値取得用）
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def update(self, i, x):
        while i <= self.n:
            if self.data[i] < x:
                self.data[i] = x
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            if self.data[i] > res:
                res = self.data[i]
            i -= i & -i
        return res

# 座標圧縮
vals = list(set(A))
vals.sort()
def compress(x):
    return bisect.bisect_left(vals, x) + 1  # 1-based

A_comp = [compress(a) for a in A]

queries = []
for idx in range(Q):
    R_i, X_i = map(int, input().split())
    queries.append((R_i, X_i, idx))

queries.sort(key=lambda x: x[0])  # R_i の昇順

ft = FenwickTree(len(vals))
res = [0] * Q

cur = 0
for R_i, X_i, idx in queries:
    # i を R_i まで進めて Fenwick Tree に length[i] を更新
    while cur < R_i:
        cur += 1
        ft.update(A_comp[cur - 1], length[cur - 1])
    # X_i 以下の A[i] の圧縮値の最大値を取得
    # X_i の圧縮値を求める
    pos = bisect.bisect_right(vals, X_i)
    if pos == 0:
        res[idx] = 0
    else:
        res[idx] = ft.query(pos)

print('\n'.join(map(str, res)))