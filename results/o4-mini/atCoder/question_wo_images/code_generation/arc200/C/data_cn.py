import sys
input = sys.stdin.readline

# 题意简述：
# 有N个人，每人有一个时间区间[L_i, R_i]，且所有L_i和R_i均不同。
# 有N个座位1..N，给每个人分配一个座位P_i。
# 每个人i在时间L_i到达，穿过座位1..P_i-1坐下，时间R_i离开，穿过座位1..P_i-1离开。
# 不满意度是其他人在i的时间区间(L_i,R_i)内穿过座位P_i的次数。
# 目标：找到字典序最小的排列P，使得所有人的总不满意度最小。

# 观察：
# 不满意度来源于其他人在i的时间区间内穿过座位P_i。
# 穿过座位P_i意味着该人座位编号 > P_i（因为穿过1..P_i-1）。
# 因此，不满意度来自于时间区间重叠且座位编号大小关系。

# 关键：
# 不满意度 = sum over i of count of j != i with intervals overlapping i's open interval and P_j > P_i.

# 这等价于：
# 对所有i,j，若时间区间重叠且P_j > P_i，则i的不满意度加1。

# 目标是最小化总不满意度 = sum over all overlapping pairs (i,j) with P_j > P_i。

# 这等价于：
# 对所有重叠的区间对(i,j)，如果P_i < P_j，则不满意度贡献0，否则贡献1。
# 因为不满意度是j穿过i座位时产生的，j穿过座位P_i意味着P_j > P_i。

# 也就是说：
# 对所有重叠的区间对(i,j)，如果座位编号P_i < P_j，则不满意度贡献0；
# 如果P_i > P_j，则贡献1。

# 因此，总不满意度 = 重叠区间对中逆序对的数量。

# 结论：
# 总不满意度 = 重叠区间对中逆序对数。

# 目标：
# 在所有排列中，找到使得重叠区间对中逆序对数最小的字典序最小排列。

# 这相当于：
# 对重叠区间对(i,j)，希望P_i < P_j，避免逆序。
# 也就是对重叠区间对建立一个偏序关系 i < j。

# 由于重叠是对称的，重叠区间对(i,j)是无向边。
# 但我们需要一个有向关系来约束P_i < P_j。

# 解决方案：
# 将所有区间按L_i排序。
# 对于重叠区间对(i,j)，如果L_i < L_j，则强制P_i < P_j。
# 这样构造一个有向无环图（DAG），边从L_i较小的区间指向L_j较大的区间。
# 因为L_i不同且L_i < L_j，边不会形成环。

# 在这个DAG中，P是一个拓扑排序。
# 目标是找到字典序最小的拓扑排序。

# 字典序最小的拓扑排序：
# 在每一步选择入度为0的节点中编号最小的。

# 实现步骤：
# 1. 读入N和区间。
# 2. 按L_i排序，记录原编号。
# 3. 构造图：
#    对所有i<j，判断区间i和j是否重叠。
#    如果重叠且L_i < L_j，则加边 i->j。
# 4. 对图做字典序最小拓扑排序，输出对应原编号的排列。

# 复杂度：
# N最多500，构造图O(N^2)，拓扑排序O(N^2)可接受。

def intervals_overlap(a, b):
    # a,b为(L,R)
    # 判断区间是否重叠（开区间）
    # 题中不满意度计算区间为(L_i,R_i)开区间
    # 两区间开区间重叠条件：
    # max(L_a,L_b) < min(R_a,R_b)
    return max(a[0], b[0]) < min(a[1], b[1])

T = int(input())
for _ in range(T):
    N = int(input())
    intervals = []
    for i in range(N):
        L,R = map(int,input().split())
        intervals.append((L,R,i+1))
    # 按L排序
    intervals.sort(key=lambda x:x[0])
    # 构图
    # 节点0..N-1对应intervals中元素
    graph = [[] for _ in range(N)]
    indeg = [0]*N
    for i in range(N):
        for j in range(i+1,N):
            if intervals_overlap(intervals[i], intervals[j]):
                # L_i < L_j，边 i->j
                graph[i].append(j)
                indeg[j] += 1
    # 字典序最小拓扑排序
    import heapq
    heap = []
    for i in range(N):
        if indeg[i]==0:
            heapq.heappush(heap,i)
    res = []
    while heap:
        u = heapq.heappop(heap)
        res.append(intervals[u][2])
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                heapq.heappush(heap,v)
    print(*res)