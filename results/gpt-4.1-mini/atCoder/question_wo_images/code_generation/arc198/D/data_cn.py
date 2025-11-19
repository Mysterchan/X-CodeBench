import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

A = [list(map(int,list(input().strip()))) for _ in range(N)]

# 1. 根據題意，我們要找一個整數序列 x，使得：
#    - 對所有 A[i][j] = 1 的 (i,j)，從 i 到 j 的路徑上的 x 值是回文的。
#    - 若有違反，分數為 10^100。
#    - 否則分數為所有回文對 (i,j) 的數量。
#
# 2. 觀察：
#    - 回文對定義：路徑上的序列 x_{v_1}, x_{v_2}, ..., x_{v_n} 必須是回文。
#    - 對於 A[i][j] = 1，路徑 i->j 必須是回文。
#    - 這表示路徑上對稱位置的節點必須有相同的 x 值。
#
# 3. 因此，我們可以將所有 (u,v) 對應的路徑上對稱節點配對，建立一個「等價關係」：
#    - 對每個 A[i][j] = 1，路徑 i->j 上的對稱節點必須相同。
#    - 這些約束形成一個聯集集合（Union-Find）結構，將必須相同的節點合併。
#
# 4. 合併完成後，每個聯集代表一個「顏色組」。
#    - x 的值對應聯集的代表元。
#
# 5. 接著計算分數：
#    - 分數是所有回文對 (i,j) 的數量。
#    - (i,j) 是回文對當且僅當路徑 i->j 上的節點顏色序列是回文。
#    - 由於 x 值是聯集代表元，回文條件等同於路徑 i->j 上對稱位置的節點屬於同一聯集。
#
# 6. 由於我們已經合併了所有 A[i][j]=1 的路徑對稱節點，保證這些路徑是回文的。
#    - 若有矛盾，會在合併時發現。
#    - 若無矛盾，分數為所有回文對數量。
#
# 7. 計算所有回文對數量：
#    - 對所有 (i,j)，判斷路徑 i->j 是否回文。
#    - 由於 N 可達 3000，O(N^2) 判斷路徑回文需優化。
#
# 8. 優化計算回文對數量：
#    - 利用樹的特性，路徑 i->j 唯一且可用 LCA 找出。
#    - 路徑 i->j 的節點序列長度為 dist(i,j)+1。
#    - 回文條件是路徑上對稱位置的節點屬於同一聯集。
#
# 9. 觀察：
#    - 對於任意 (i,j)，路徑 i->j 是回文當且僅當：
#      對路徑上所有 k，節點 v_k 與 v_{n+1-k} 屬於同一聯集。
#
# 10. 由於聯集已經合併所有 A[i][j]=1 的路徑對稱節點，對於 A[i][j]=1 的 (i,j) 路徑必定回文。
#     - 對於 A[i][j]=0 的 (i,j)，路徑可能回文也可能不回文。
#
# 11. 我們要計算所有回文對數量：
#     - (i,i) 一定是回文對，因為路徑長度1。
#     - 對 i<j，判斷路徑 i->j 是否回文。
#
# 12. 由於判斷路徑回文複雜，我們利用以下方法：
#     - 對每個節點 u，計算其顏色組（聯集代表元）。
#     - 對於路徑 i->j，回文條件是路徑上對稱節點顏色相同。
#
# 13. 利用樹的中心對稱性：
#     - 對於路徑 i->j，路徑長度為 d+1。
#     - 路徑節點序列 v_1,...,v_{d+1}。
#     - 對 k=1..(d+1)//2，v_k 與 v_{d+2-k} 顏色相同。
#
# 14. 我們可以用雙指標 BFS 或 DFS 預處理：
#     - 對所有節點對 (u,v)，用 BFS 同時從 u,v 向中間走，檢查顏色是否相同。
#     - 但 O(N^2) BFS 不可行。
#
# 15. 另一種方法：
#     - 利用樹的結構和聯集，建立一個「顏色相等」的條件。
#     - 對於所有節點對 (u,v)，若 u,v 顏色相同，則 (u,v) 是「等價」的。
#
# 16. 利用 DP：
#     - 定義 dp[u][v] = 是否路徑 u->v 回文。
#     - dp[u][v] = True 當且僅當：
#       - 顏色[u] == 顏色[v]
#       - 若 u==v，dp[u][v]=True
#       - 若 u,v 相鄰，dp[u][v]=True 當顏色相同
#       - 否則 dp[u][v] = dp[next_u][next_v]，其中 next_u,v 是 u,v 向中間移動的節點
#
# 17. 由於樹的路徑唯一且可用 LCA 找中點，我們可以用 BFS 從所有 (u,u) 開始擴展 dp。
#
# 18. 實作：
#     - 建立一個 queue，初始放入所有 (u,u) 和相鄰且顏色相同的 (u,v)。
#     - 對於 (u,v) 在 queue 中，嘗試擴展到 (p[u],p[v])，其中 p[u],p[v] 是 u,v 的父節點或下一節點。
#     - 直到無法擴展。
#
# 19. 最後 dp[u][v] = True 的對數即為回文對數。
#
# 20. 若在合併過程中發現矛盾，輸出 10^100。

# 實作細節：

# 先建立 parent, depth 用於 LCA
LOG = 15
while (1 << LOG) <= N:
    LOG += 1

parent = [[-1]*N for _ in range(LOG)]
depth = [0]*N

def dfs(u,p):
    for w in edges[u]:
        if w == p:
            continue
        depth[w] = depth[u]+1
        parent[0][w] = u
        dfs(w,u)
dfs(0,-1)

for k in range(LOG-1):
    for v in range(N):
        if parent[k][v] < 0:
            parent[k+1][v] = -1
        else:
            parent[k+1][v] = parent[k][parent[k][v]]

def lca(u,v):
    if depth[u] > depth[v]:
        u,v = v,u
    diff = depth[v]-depth[u]
    for k in range(LOG):
        if diff & (1 << k):
            v = parent[k][v]
    if u == v:
        return u
    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

def dist(u,v):
    return depth[u]+depth[v]-2*depth[lca(u,v)]

# Union-Find 實作
class UnionFind:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x,y):
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

uf = UnionFind(N)

# 找路徑上對稱節點並合併
# 對每個 A[i][j]=1，合併路徑 i->j 上對稱節點
# 先找路徑 i->j 節點序列

# 預先建立 parent 用於回溯路徑
# parent[0] 已有

def get_path(u,v):
    # 找路徑 u->v 節點序列
    w = lca(u,v)
    path_u = []
    cur = u
    while cur != w:
        path_u.append(cur)
        cur = parent[0][cur]
    path_v = []
    cur = v
    while cur != w:
        path_v.append(cur)
        cur = parent[0][cur]
    path = path_u + [w] + path_v[::-1]
    return path

# 合併路徑上對稱節點
for i in range(N):
    for j in range(i,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            for k in range(n//2):
                if not uf.union(path[k], path[n-1-k]):
                    # union 返回 False 表示已經在同一集合，無問題
                    pass

# 檢查是否有 A[i][j]=1 但路徑不回文（理論上不會有，因為已合併）
# 但為保險，檢查路徑上對稱節點是否同集合
for i in range(N):
    for j in range(i,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            for k in range(n//2):
                if uf.find(path[k]) != uf.find(path[n-1-k]):
                    print(10**100)
                    sys.exit()

# 現在計算所有回文對數量
# dp[u][v] = 是否路徑 u->v 回文
# 利用 BFS 從 (u,u) 和相鄰且顏色相同的 (u,v) 開始擴展

from collections import deque

color = [uf.find(i) for i in range(N)]

dp = [[False]*N for _ in range(N)]
q = deque()

# 初始化 dp[u][u] = True
for u in range(N):
    dp[u][u] = True
    q.append((u,u))

# 初始化相鄰且顏色相同的節點對
for u in range(N):
    for w in edges[u]:
        if color[u] == color[w]:
            if not dp[u][w]:
                dp[u][w] = True
                dp[w][u] = True
                q.append((u,w))
                q.append((w,u))

# 父節點查找函數
def up(u):
    return parent[0][u]

# BFS 擴展
while q:
    u,v = q.popleft()
    if u == v:
        continue
    pu = up(u)
    pv = up(v)
    if pu == -1 or pv == -1:
        continue
    if color[pu] == color[pv] and not dp[pu][pv]:
        dp[pu][pv] = True
        dp[pv][pu] = True
        q.append((pu,pv))
        q.append((pv,pu))

# 計算回文對數量
ans = 0
for i in range(N):
    for j in range(N):
        if dp[i][j]:
            ans += 1

print(ans)