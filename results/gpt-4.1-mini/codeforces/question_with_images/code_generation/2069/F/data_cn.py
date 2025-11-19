import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())

# 使用離線處理邊的添加與刪除，因為邊會反覆添加刪除
# 我們需要知道每條邊在什麼時間段存在於圖中

# 對於兩個圖 A, B 分別維護邊的存在時間區間
# key: (min(u,v), max(u,v))
# value: list of (start_time, end_time)
# end_time = q+1 表示一直存在到最後

edges_A = dict()
edges_B = dict()

# 用於記錄當前邊是否存在
exist_A = dict()
exist_B = dict()

queries = []
for i in range(q):
    c, x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        x, y = y, x
    queries.append((c, x, y))

def add_edge_record(edges, exist, c, x, y, t):
    key = (x, y)
    if key not in exist or not exist[key]:
        # 邊不存在，添加開始時間
        exist[key] = True
        if key not in edges:
            edges[key] = []
        edges[key].append([t, None])
    else:
        # 邊存在，結束時間
        exist[key] = False
        edges[key][-1][1] = t

for t, (c, x, y) in enumerate(queries, 1):
    if c == 'A':
        add_edge_record(edges_A, exist_A, c, x, y, t)
    else:
        add_edge_record(edges_B, exist_B, c, x, y, t)

# 對於還存在的邊，結束時間設為 q+1
for key in edges_A:
    if edges_A[key][-1][1] is None:
        edges_A[key][-1][1] = q+1
for key in edges_B:
    if edges_B[key][-1][1] is None:
        edges_B[key][-1][1] = q+1

# 使用線段樹結合並查集離線處理
# 線段樹節點代表時間區間，將邊加入該區間
# 遍歷線段樹，維護兩個圖的聯通分量，計算答案

class DSU:
    __slots__ = ['parent', 'size', 'cc']
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.cc = n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.cc -= 1
        return True
    def snapshot(self):
        return (self.parent[:], self.size[:], self.cc)
    def rollback(self, snap):
        self.parent, self.size, self.cc = snap

# 線段樹結構
# 節點存邊列表，邊為(u,v)
# 節點區間為 [l,r)
class SegmentTree:
    __slots__ = ['n', 'tree']
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.tree = [[] for _ in range(self.n<<1)]
    def add(self, l, r, edge):
        # 將edge加入[l,r)
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.tree[l].append(edge)
                l += 1
            if r & 1:
                r -= 1
                self.tree[r].append(edge)
            l >>= 1
            r >>= 1

# 對兩個圖分別建立線段樹
segA = SegmentTree(q+1)
segB = SegmentTree(q+1)

for (u,v), intervals in edges_A.items():
    for l, r in intervals:
        segA.add(l, r, (u-1, v-1))
for (u,v), intervals in edges_B.items():
    for l, r in intervals:
        segB.add(l, r, (u-1, v-1))

# 我們需要維護兩個DSU，分別表示圖A和圖B的聯通分量
# 並且要計算每個查詢時刻，為了使A包含B，最少需要添加多少邊

# 分析：
# 圖A包含圖B，等價於B中每個聯通分量是A中某個聯通分量的子集
# 換句話說，B的聯通分量數量 >= A的聯通分量數量
# 且B的聯通分量可以被A的聯通分量覆蓋
# 由於頂點數相同，且A和B的頂點集合相同
# 需要添加的邊數 = B的聯通分量數 - A的聯通分量數
# 因為添加邊可以合併A的聯通分量，使A的聯通分量數減少
# 使A的聯通分量數 <= B的聯通分量數，且覆蓋B的分量

# 因此每次查詢後答案 = max(0, B_cc - A_cc)

# 我們只需維護兩個DSU的聯通分量數，並在每個時間點輸出答案

# 使用線段樹遍歷，分別對A和B的邊進行union，並在葉節點輸出答案

# 由於兩個圖的邊分別在不同線段樹，我們需要同時遍歷兩個線段樹
# 但時間區間相同，且查詢時間點為1..q
# 我們可以合併兩個線段樹的邊，或者分別遞歸遍歷兩個線段樹，並同步輸出

# 方案：
# 對時間區間[1,q]，遞歸遍歷線段樹節點
# 在節點中分別union A和B的邊
# 到達葉節點時輸出答案
# 回溯時rollback union操作

# 為了回溯，我們需要記錄union操作的狀態

class RollbackDSU:
    __slots__ = ['parent', 'size', 'cc', 'history']
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.cc = n
        self.history = []
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            self.history.append((-1, -1, -1))
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.history.append((b, self.parent[b], self.size[a]))
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.cc -= 1
        return True
    def snapshot(self):
        return len(self.history)
    def rollback(self, snap):
        while len(self.history) > snap:
            b, pb, sa = self.history.pop()
            if b == -1:
                continue
            a = self.parent[b]
            self.size[a] = sa
            self.parent[b] = pb
            self.cc += 1

A_dsu = RollbackDSU(n)
B_dsu = RollbackDSU(n)

res = [0]*(q+1)

def dfs(l, r, idx):
    snapA = A_dsu.snapshot()
    snapB = B_dsu.snapshot()
    # union A edges
    for u,v in segA.tree[idx]:
        A_dsu.union(u,v)
    # union B edges
    for u,v in segB.tree[idx]:
        B_dsu.union(u,v)
    if r - l == 1:
        # leaf node, output answer for time l
        # 答案 = max(0, B_cc - A_cc)
        res[l] = max(0, B_dsu.cc - A_dsu.cc)
    else:
        mid = (l+r)//2
        dfs(l, mid, idx*2)
        dfs(mid, r, idx*2+1)
    A_dsu.rollback(snapA)
    B_dsu.rollback(snapB)

dfs(1, segA.n, 1)

for i in range(1, q+1):
    print(res[i])