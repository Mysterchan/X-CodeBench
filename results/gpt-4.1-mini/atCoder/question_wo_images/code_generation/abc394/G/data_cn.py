import sys
input = sys.stdin.readline

H, W = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())

# 预处理每个格子的楼层数F[i][j]

# 观察题意：
# Takahashi可以在同一栋建筑内上下楼梯，楼梯次数为层数差的绝对值。
# 也可以通过空中走道在相邻区块间移动，但只能在相同层数X且该层数X不超过相邻区块的楼层数。
# 目标是最小化楼梯使用次数。

# 关键点：
# 走道移动不消耗楼梯次数，但只能在相同层数X且X <= F[i][j]和F[i'][j']的情况下移动。
# 因此，移动路径中楼梯使用次数 = 起点楼层到某个“公共层数”的楼梯次数 + 终点楼层到该“公共层数”的楼梯次数。
# 走道移动可以在该层数上任意移动（只要相邻区块楼层数>=该层数）。

# 由于走道移动限制在层数X上，且走道移动不消耗楼梯次数，
# 我们可以理解为：
# - 在某一层数X上，所有楼层数>=X的区块构成一个图（节点为区块，边为相邻区块）。
# - 在该图中，走道移动可以自由移动。
# - 因此，若起点和终点在层数X的图中连通，则楼梯使用次数 = |起点层数 - X| + |终点层数 - X|。

# 我们需要找到一个层数X，使得起点和终点在层数X的图中连通，且使楼梯次数最小。

# 由于F[i][j]最大可达10^6，不能对每个层数X枚举。
# 但层数X的选择只需考虑起点和终点楼层之间的区间内的层数。

# 进一步分析：
# 对于每个查询，楼梯次数 = |Y - X| + |Z - X| = |Y - Z| + 2 * min(|X - Y|, |X - Z|)
# 最小化楼梯次数等价于找到X使得起点和终点在层数X的图中连通，且X尽可能接近Y和Z。

# 由于走道移动只在层数X的图中连通，且图是基于区块楼层数>=X的连通性，
# 我们可以对所有区块按楼层数降序排序，使用并查集维护连通块。
# 对于每个查询，我们想找到最大X，使得X <= min(Y,Z)且起点和终点在层数X的图中连通。

# 这样，楼梯次数 = |Y - X| + |Z - X|，X越接近Y和Z，楼梯次数越小。
# 由于X <= min(Y,Z)，X最大时楼梯次数最小。

# 解决方案：
# 1. 将所有区块按F[i][j]降序排序。
# 2. 对所有查询，记录起点和终点，以及Y,Z。
# 3. 对每个查询，目标是找到最大X <= min(Y,Z)，使得起点和终点在层数X的图中连通。
# 4. 使用离线二分：
#    - 对每个查询，二分X在[1, min(Y,Z)]区间。
#    - 对所有查询的中间值mid，按mid降序处理。
#    - 维护并查集，逐步将楼层数>=当前mid的区块合并。
#    - 查询时判断起点和终点是否连通。
# 5. 最终得到每个查询的最大X。
# 6. 计算楼梯次数 = |Y - X| + |Z - X|。

# 实现细节：
# - 并查集实现。
# - 离线二分处理Q个查询。
# - 由于H*W最多25万，Q最多20万，离线二分复杂度可接受。

# 编号区块id = i*W + j

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1]*n
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
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.par[y] = x
        self.sz[x] += self.sz[y]
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)

# 预处理区块按楼层数降序排序
cells = []
for i in range(H):
    for j in range(W):
        cells.append((F[i][j], i, j))
cells.sort(reverse=True)

# 邻接方向
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

Qs = []
for _ in range(Q):
    A,B,Y,C,D,Z = map(int, input().split())
    A -= 1; B -= 1; C -= 1; D -= 1
    Qs.append((A,B,Y,C,D,Z))

# 离线二分
# 对每个查询，搜索X ∈ [1, min(Y,Z)]
# 记录答案ans[i] = 最大满足条件的X

ans = [0]*Q
left = [1]*Q
right = [min(Qs[i][2], Qs[i][5]) for i in range(Q)]

# 为了加速，预先构建一个层数到区块列表的映射
# 但层数范围大，直接映射不现实
# 改为用cells数组，指针逐步向下移动

# 离线二分的最大迭代次数约为20

for _ in range(20):
    mid_to_queries = dict()
    for i in range(Q):
        if left[i] <= right[i]:
            m = (left[i] + right[i]) // 2
            mid_to_queries.setdefault(m, []).append(i)
    if not mid_to_queries:
        break
    # 按mid降序处理
    mids = sorted(mid_to_queries.keys(), reverse=True)
    uf = UnionFind(H*W)
    # 指针p指向cells中楼层>=当前mid的区块
    p = 0
    # 维护一个visited数组，标记哪些区块已加入并查集
    visited = [False]*(H*W)
    # 对每个mid，从大到小处理
    # 为避免重复构建并查集，使用一个全局指针p，逐步加入cells中楼层>=mid的区块
    # 由于mid递减，p只会向后移动
    # 先处理最大的mid，加入所有楼层>=mid的区块
    # 然后处理下一个mid，加入楼层>=mid但<上一个mid的区块
    # 以此类推
    # 记录当前mid的p位置
    prev_p = 0
    for mid in mids:
        # 加入所有楼层>=mid的区块
        while p < len(cells) and cells[p][0] >= mid:
            f, i_, j_ = cells[p]
            idx = i_*W + j_
            visited[idx] = True
            # 尝试与邻居合并
            for dx, dy in dirs:
                ni, nj = i_ + dx, j_ + dy
                if 0 <= ni < H and 0 <= nj < W:
                    nidx = ni*W + nj
                    if visited[nidx]:
                        uf.union(idx, nidx)
            p += 1
        # 对mid对应的查询判断连通性
        for qi in mid_to_queries[mid]:
            A,B,Y,C,D,Z = Qs[qi]
            s = A*W + B
            t = C*W + D
            if visited[s] and visited[t] and uf.same(s, t):
                ans[qi] = mid
                left[qi] = mid + 1
            else:
                right[qi] = mid - 1

# 输出结果
# 楼梯次数 = |Y - X| + |Z - X|
for i in range(Q):
    A,B,Y,C,D,Z = Qs[i]
    X = ans[i]
    res = abs(Y - X) + abs(Z - X)
    print(res)