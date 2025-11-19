def solve():
    MOD = 998244353
    N = int(input())
    A = list(map(int, input().split()))
    
    # 找出所有 -1 的位置
    unknown_positions = [i for i in range(N) if A[i] == -1]
    num_unknowns = len(unknown_positions)
    
    if num_unknowns == 0:
        # 检查是否是好序列
        if is_good_sequence(A, N):
            print(1)
        else:
            print(0)
        return
    
    count = 0
    
    # 枚举所有可能的替换
    def enumerate_replacements(idx):
        nonlocal count
        if idx == num_unknowns:
            if is_good_sequence(A, N):
                count = (count + 1) % MOD
            return
        
        pos = unknown_positions[idx]
        for val in range(1, N + 1):
            A[pos] = val
            enumerate_replacements(idx + 1)
        A[pos] = -1
    
    enumerate_replacements(0)
    print(count)

def is_good_sequence(B, N):
    # 检查所有区间 [l, r]
    for l in range(N):
        for r in range(l, N):
            # 检查是否存在 x 使得条件满足
            valid = False
            for x in range(l, r + 1):
                if check_tree(B, N, l, r, x):
                    valid = True
                    break
            if not valid:
                return False
    return True

def check_tree(B, N, l, r, x):
    # 构建图并检查 l, l+1, ..., r 是否形成树
    # 使用并查集检查连通性
    parent = list(range(N))
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        pu, pv = find(u), find(v)
        if pu == pv:
            return False  # 形成环
        parent[pu] = pv
        return True
    
    edge_count = 0
    for i in range(l, r + 1):
        if i != x:
            u = i
            v = B[i] - 1  # 转换为0索引
            # 检查 v 是否在 [l, r] 范围内
            if v < l or v > r:
                return False
            if not union(u, v):
                return False  # 有环
            edge_count += 1
    
    # 检查是否连通
    # 树有 n-1 条边，其中 n 是顶点数
    num_vertices = r - l + 1
    if edge_count != num_vertices - 1:
        return False
    
    # 检查所有顶点是否在同一连通分量
    root = find(l)
    for i in range(l + 1, r + 1):
        if find(i) != root:
            return False
    
    return True

solve()