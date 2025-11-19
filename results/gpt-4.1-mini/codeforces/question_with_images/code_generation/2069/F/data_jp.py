import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, q = map(int, input().split())

# Union-Find (Disjoint Set Union) 実装
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1]*n
        self.cc = n  # 連結成分数

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.cc -= 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

# 動的に辺の追加・削除を行いながら連結成分数を管理する必要がある。
# しかし、Union-Findは辺の削除に対応していない。
# そこで、オフラインでクエリを処理し、辺の存在期間を管理し、
# セグメント木や分割統治で辺の追加・削除を行う手法があるが、
# 本問題は辺の追加・削除が1回ずつのトグルなので、
# 辺の存在期間は区間として管理できる。

# 方針：
# 1. 各グラフ(A,B)の辺の追加・削除をトグルとして管理し、
#    各辺の存在期間を区間として記録する。
# 2. 区間をセグメント木に割り当て、区間に対応する辺を
#    セグメント木のノードに登録する。
# 3. セグメント木をDFSで巡回しながらUnion-Findで辺を追加し、
#    クエリ時点での連結成分数を記録する。
# 4. 各クエリでのA,Bの連結成分数を用いて答えを計算する。

# 追加する必要のある辺の最小数は、
# Bの連結成分数 - Aの連結成分数 である。
# なぜなら、Aの成分でBの成分を覆うには、
# Aの成分数がBの成分数以上でなければならず、
# 足りない分だけ辺を追加してAの成分を減らす必要がある。

# 辺の管理
# 辺は (min(u,v), max(u,v)) の形で管理し、重複を防ぐ。

# 辺の存在期間を管理するために、
# 辺の追加・削除のタイムスタンプを記録し、
# 存在期間を [start, end) の区間として扱う。

# 辺の存在期間をセグメント木に登録し、
# セグメント木の各ノードにその区間に存在する辺を登録する。

# セグメント木のDFSで辺を追加し、クエリ時点での連結成分数を記録。

# これをA,Bそれぞれで行い、最後にクエリごとに答えを出力。

# --- 実装 ---

# 辺の管理用辞書
# key: (u,v), value: 最後に追加された時刻（-1なら存在しない）
edge_time_A = dict()
edge_time_B = dict()

# クエリ情報格納
queries = []
for _ in range(q):
    c, x, y = input().split()
    x = int(x)-1
    y = int(y)-1
    if x > y:
        x, y = y, x
    queries.append((c, x, y))

# 辺の存在期間を管理する関数
def build_intervals(queries, edge_time):
    intervals = []
    # 辺の存在期間を (start, end) で管理
    # 辺が最後に追加された時刻を記録し、
    # 削除時に区間を確定させる。
    # 最後に残っている辺は q を終端とする区間になる。
    for i, (c, x, y) in enumerate(queries):
        if c not in edge_time:
            continue
    # ここではedge_timeは辞書なので、上のループは不要
    # 代わりに以下の処理を行う

def get_intervals(queries, target_c):
    edge_time = dict()
    intervals = []
    for i, (c, x, y) in enumerate(queries):
        if c != target_c:
            continue
        e = (x, y)
        if e not in edge_time:
            edge_time[e] = i
        else:
            start = edge_time[e]
            intervals.append((start, i, e))
            del edge_time[e]
    # 残っている辺は最後まで存在
    for e, start in edge_time.items():
        intervals.append((start, q, e))
    return intervals

intervals_A = get_intervals(queries, 'A')
intervals_B = get_intervals(queries, 'B')

# セグメント木に区間を登録する関数
# セグメント木のノードに区間に存在する辺を登録する
class SegmentTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.data = [[] for _ in range(2*self.n)]

    def add(self, l, r, edge):
        # [l, r) に edge を追加
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.data[l].append(edge)
                l += 1
            if r & 1:
                r -= 1
                self.data[r].append(edge)
            l >>= 1
            r >>= 1

# UnionFindのスタック付きバージョン（rollback可能）
class UnionFindRollback:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.cc = n
        self.history = []

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.history.append((-1, -1, -1))
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.history.append((y, self.parent[y], self.size[x]))
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.cc -= 1
        return True

    def snapshot(self):
        return len(self.history)

    def rollback(self, snap):
        while len(self.history) > snap:
            y, py, sx = self.history.pop()
            if y == -1:
                continue
            x = self.parent[y]
            self.size[x] = sx
            self.parent[y] = py
            self.cc += 1

# セグメント木をDFSで巡回し、各クエリ時点の連結成分数を記録
def dfs(seg, uf, idx, l, r, res):
    snap = uf.snapshot()
    for (u,v) in seg.data[idx]:
        uf.union(u,v)
    if r - l == 1:
        # クエリ時点の連結成分数を記録
        res[l] = uf.cc
    else:
        m = (l+r)//2
        dfs(seg, uf, idx*2, l, m, res)
        dfs(seg, uf, idx*2+1, m, r, res)
    uf.rollback(snap)

# A,Bそれぞれのセグメント木を作成し、辺を登録
segA = SegmentTree(q)
for start, end, (u,v) in intervals_A:
    segA.add(start, end, (u,v))

segB = SegmentTree(q)
for start, end, (u,v) in intervals_B:
    segB.add(start, end, (u,v))

ufA = UnionFindRollback(n)
ufB = UnionFindRollback(n)

resA = [0]*q
resB = [0]*q

dfs(segA, ufA, 1, 0, q, resA)
dfs(segB, ufB, 1, 0, q, resB)

# 各クエリでの答えを出力
# 答え = max(0, Bの連結成分数 - Aの連結成分数)
# ただし、AがBを含むために必要な追加辺数はこれに等しい
for i in range(q):
    ans = resB[i] - resA[i]
    if ans < 0:
        ans = 0
    print(ans)