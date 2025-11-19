import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 交差判定のポイント:
# 円周上の点は1からNまで時計回りに並んでいる。
# 線分 (A,B) は A < B とする。
# 2Q 個の点はすべて異なるので、線分はすべて異なる点を結ぶ。
# 交差は、2つの線分 (a,b), (c,d) が
# a < c < b < d または c < a < d < b の場合に起こる。

# 交差判定を効率的に行うために、線分を区間として扱う。
# 既に書かれた線分の区間は重ならず、交差もしない。
# つまり、書かれた線分の区間は「ネストしない」区間集合となる。

# 交差判定は、区間の入れ子関係で判定できる。
# 具体的には、区間を左端でソートし、区間の右端が増加するように管理すれば、
# 新しい区間が既存の区間と交差するかは、区間の右端の管理で判定できる。

# ここでは、区間の左端でソートしながら、右端の最大値を管理することで、
# 新しい区間が交差するかを判定する。

# しかし、クエリは順に処理しなければならないため、
# 既に書かれた線分の区間を管理し、
# 新しい区間が交差するかを判定する必要がある。

# 交差判定の条件は、
# 既存の区間 (l_i, r_i) と新しい区間 (l, r) が
# l_i < l < r_i < r または l < l_i < r < r_i の場合に交差する。

# これを効率的に判定するために、
# 既存の区間を左端でソートして管理し、
# 新しい区間の左端で二分探索し、
# その前後の区間と交差判定を行う。

import bisect

# 既に書かれた線分の区間を左端で管理
intervals = []  # (left, right)

def intersects(l, r):
    # intervals は左端でソート済み
    # 新しい区間 (l,r) と交差するか判定
    # 二分探索で挿入位置を探す
    i = bisect.bisect_left(intervals, (l, -1))
    # i の前の区間と交差するか
    if i > 0:
        L, R = intervals[i-1]
        # 交差条件: L < l < R < r または l < L < r < R
        # ここは (L < l < R < r) のみ考慮すれば十分
        # なぜなら intervals は左端でソートされており、
        # i は l の挿入位置なので i-1 の区間の左端は L < l
        # 交差は L < l < R < r の場合に起こる
        if L < l < R < r:
            return True
    # i の位置の区間と交差するか
    if i < len(intervals):
        L, R = intervals[i]
        # 交差条件: l < L < r < R
        if l < L < r < R:
            return True
    return False

for A, B in queries:
    l, r = A, B
    # A < B は保証されている
    if intersects(l, r):
        print("No")
    else:
        print("Yes")
        # 挿入して管理
        bisect.insort(intervals, (l, r))