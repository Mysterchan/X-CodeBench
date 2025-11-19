import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# この問題は、操作によって「三角形の辺の色をすべて反転させる」ことができる。
# 操作は任意回数可能なので、最終的に黒い辺の集合は「元の黒い辺の集合」と
# 「操作した三角形の辺の集合の対称差」で表される。
#
# 重要なことは、この操作はグラフの辺の集合に対して「三角形の辺の集合の部分空間」
# の元を加えることに相当し、最終的な黒い辺の集合は元の辺集合の「三角形の辺の集合の
# 部分空間によるコスセット」となる。
#
# この問題は、グラフの辺集合をベクトル空間（mod2）とみなしたとき、
# 三角形の辺集合が生成する部分空間の次元を考え、最終的に黒い辺の数を最大化する問題に帰着する。
#
# 結果として、最終的に黒い辺の数の最大値は、
# 「全辺数」 - 「元の黒い辺の集合と三角形部分空間の交差による制約の次元」
# によって決まる。
#
# この問題の解法は、グラフの補グラフの連結成分数を求めることに帰着する。
#
# 具体的には、補グラフの連結成分数を c とすると、
# 最大の黒い辺の数は
#   M + (N - c) * (N - c - 1) // 2
# となる。
#
# これは、補グラフの連結成分ごとに完全グラフにできるため、
# 元の黒い辺数 M に加えて、補グラフの連結成分の頂点数の組み合わせ数を足す形になる。
#
# したがって、補グラフの連結成分数を求めることが鍵。
#
# N が大きいので、補グラフの辺を直接作るのは不可能。
# そこで、補グラフの連結成分を求めるために、
# 元のグラフの隣接リストを使い、補グラフの連結成分を BFS で求める。
#
# 補グラフの辺は「元のグラフに辺がない頂点同士の辺」なので、
# BFS の際に、現在の頂点から「元のグラフの隣接頂点以外」を探索する。
#
# 効率的に探索するために、未訪問の頂点集合を管理し、
# 現在の頂点の隣接頂点を除いた未訪問頂点を一括で探索する方法をとる。
#
# これにより、補グラフの連結成分数 c を求め、
# 答えは M + sum_{i=1}^c (|C_i| * (|C_i| - 1) // 2)
# となる。

from collections import deque

# 頂点の集合を管理するために set を使うと遅いので、
# 未訪問頂点をリストで管理し、探索時に隣接頂点を除外する方法をとる。
# しかし N が大きいので set を使うのが現実的。

adj = [set() for _ in range(N+1)]
for u in range(1, N+1):
    for v in edges[u]:
        adj[u].add(v)

unvisited = set(range(1, N+1))
components = []

while unvisited:
    start = unvisited.pop()
    q = deque([start])
    comp = [start]
    while q:
        u = q.popleft()
        # uの隣接頂点は adj[u]
        # 補グラフの辺は adj[u] にない頂点との辺
        # つまり、unvisited - adj[u] が u の補グラフの隣接頂点
        neighbors = []
        # 探索対象は unvisited から adj[u] を除いたもの
        # setの差集合で求める
        candidates = unvisited - adj[u]
        for w in candidates:
            neighbors.append(w)
        for w in neighbors:
            unvisited.remove(w)
            q.append(w)
            comp.append(w)
    components.append(comp)

# 答えを計算
# 全辺数は N*(N-1)//2
# 黒い辺は M 本
# 補グラフの連結成分ごとに完全グラフにできるので、
# 各成分の頂点数を n_i とすると、
# 黒い辺の最大数 = M + sum_i n_i*(n_i-1)//2

ans = M
for comp in components:
    k = len(comp)
    ans += k*(k-1)//2

print(ans)