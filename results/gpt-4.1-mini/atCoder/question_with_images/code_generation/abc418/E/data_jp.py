import sys
from math import gcd
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 台形は、4点のうち2組の辺が平行である多角形。
# 3点が同一直線上にないので、辺の平行判定は傾きで行う。
# 台形の条件は、4点のうち2組の辺が平行であること。
# つまり、4点のうち2本の辺の傾きが等しい組み合わせを探す。

# アプローチ:
# 1. 全ての点のペアの傾きを計算し、傾きごとにペアをグループ化する。
# 2. 同じ傾きのペアの中から、4点を選ぶ方法を考える。
#    - 同じ傾きの辺が2本あれば、その4点で台形ができる。
#    - ただし、4点がすべて異なる必要がある。
# 3. 傾きごとに、点のペアの集合から4点を選ぶ組み合わせ数を計算する。
#    - 同じ傾きの辺のペアの中で、4点が重複しない組み合わせを数える。
# 4. すべての傾きについて合計する。

# 傾きは分数で表現し、符号と約分を行う。
# 垂直線は (1,0) とする。

from collections import defaultdict

slope_pairs = defaultdict(list)

for i in range(N):
    x1, y1 = points[i]
    for j in range(i+1, N):
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            slope = (1, 0)
        else:
            g = gcd(dy, dx)
            dy //= g
            dx //= g
            # dx > 0 に統一
            if dx < 0:
                dx = -dx
                dy = -dy
            slope = (dy, dx)
        slope_pairs[slope].append((i, j))

# 同じ傾きの辺のペアの中で、4点が重複しない組み合わせを数える。
# つまり、2つの辺 (a,b), (c,d) があって、{a,b} と {c,d} が重ならない場合。
# これらの2辺で作る4点は台形の頂点となる。

# 計算量を抑えるために、各傾きの辺のリストで2重ループを回す。
# 最大で約N^2/2の辺があるが、傾きごとに分散するので実用的。

ans = 0
for edges in slope_pairs.values():
    m = len(edges)
    # 辺の組み合わせを全探索
    # 4点が重複しないかチェック
    # 辺は (i,j) で i<j なので、重複チェックは簡単
    for i in range(m):
        a, b = edges[i]
        for j in range(i+1, m):
            c, d = edges[j]
            # 4点がすべて異なるか
            if a != c and a != d and b != c and b != d:
                ans += 1

print(ans)