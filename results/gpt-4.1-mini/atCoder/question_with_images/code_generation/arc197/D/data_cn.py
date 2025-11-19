import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# 题意分析：
# 给定对称矩阵 A，A[i][j] = 1 当且仅当 i,j 在树根1的路径上互为祖先关系（即路径上有一方是另一方的祖先）
# 这等价于：A[i][j] = 1 当且仅当 i,j 在树中根1的路径上，路径上所有节点两两之间都满足A[u][v]=1。
# 因为路径上的节点两两祖先关系成立，故路径上的节点两两A[u][v]=1。
# 由此可推断：
# - A[i][j]=1 表示 i,j 在同一条路径上（即在树中根1的路径上互为祖先）
# - A[i][j]=0 表示 i,j 不在同一条路径上
#
# 这意味着：
# 1. A是一个关于节点的“路径连通性”关系的邻接矩阵，且是对称的。
# 2. 对于任意两个节点i,j，如果A[i][j]=1，则i,j必须在树中根1的路径上互为祖先。
#
# 观察：
# - A[i][i]=1，且A对称。
# - 以1为根的树中，路径上的节点两两之间A[i][j]=1。
# - 反之，若A[i][j]=0，则i,j不在同一条路径上。
#
# 这说明A定义了一个无环的“路径连通”关系，且1与所有节点的关系决定了树的结构。
#
# 解决方案思路：
# 1. 以1为根，树的结构决定了节点的祖先关系。
# 2. A[i][j]=1 表示 i,j 在根1的路径上互为祖先，等价于 i,j在树中根1到某节点的路径上。
# 3. 这意味着A定义了一个“路径图”，节点间的1表示它们在同一条路径上。
#
# 关键点：
# - 对于任意两个节点i,j，若A[i][j]=1，则i,j必须在同一条路径上。
# - 这意味着A的1构成的图是一个“路径图”的集合。
#
# 进一步分析：
# - 以1为根，树的路径是唯一的。
# - A[i][j]=1表示i,j在根1的路径上互为祖先。
# - 这说明A的1构成的连通块是路径。
#
# 综上，A定义了一个“路径覆盖”结构，树的构造必须满足：
# - 以1为根，树的每个子树对应A中一个连通块。
# - 每个连通块内部节点两两A[i][j]=1。
#
# 具体算法：
# - 以1为根，递归构造树。
# - 找出与根1相连的子集（子树），这些子集内部节点两两A[i][j]=1。
# - 对每个子集递归计算满足条件的树的数量。
# - 最终结果是子树数量的乘积乘以子树的排列方式（因为子树顺序不同，树不同）。
#
# 实现细节：
# - 用邻接矩阵A表示节点间关系。
# - 用递归函数dfs(nodes)计算节点集合nodes构成的子树数量。
# - dfs中：
#   - 若nodes只有一个节点，返回1。
#   - 找出根节点（子树根为nodes中的最小节点，题中根为1，递归时根为子集中的最小节点）。
#   - 找出与根节点相连的子集（子树），这些子集内部节点两两A[i][j]=1。
#   - 对每个子集递归调用dfs，计算子树数量。
#   - 结果为子树数量乘积乘以子树个数的阶乘（子树顺序不同）。
#
# 注意：
# - 题中根固定为1，递归时子树根为子集中的最小节点。
# - 需要预处理阶乘和逆元。
# - 由于N最大400，且所有测试用例N^2和最多400^2，递归+记忆化可行。
#
# 下面实现该思路。

MAXN = 400
fact = [1]*(MAXN+1)
invfact = [1]*(MAXN+1)
for i in range(2, MAXN+1):
    fact[i] = fact[i-1]*i % MOD
def modinv(x):
    return pow(x, MOD-2, MOD)
invfact[MAXN] = modinv(fact[MAXN])
for i in range(MAXN-1, 0, -1):
    invfact[i] = invfact[i+1]*(i+1)%MOD
def comb(n,k):
    if k>n or k<0:
        return 0
    return fact[n]*invfact[k]%MOD*invfact[n-k]%MOD

def main():
    T = int(input())
    # 总N^2和最多400^2，故每个测试用例N不大，允许递归+记忆化
    for _ in range(T):
        N = int(input())
        A = [list(map(int, input().split())) for __ in range(N)]

        # 预处理：构造邻接列表，方便查找子集
        # 但这里用邻接矩阵即可

        # 记忆化dfs
        from functools import lru_cache

        # 判断子集内部是否满足条件：任意i,j in subset, A[i][j]=1
        def is_clique(nodes):
            for i in range(len(nodes)):
                ni = nodes[i]
                for j in range(i+1, len(nodes)):
                    nj = nodes[j]
                    if A[ni][nj] == 0:
                        return False
            return True

        @lru_cache(None)
        def dfs(nodes_tuple):
            nodes = list(nodes_tuple)
            if len(nodes) == 1:
                return 1
            root = min(nodes)  # 子树根为子集中的最小节点
            # 找出与root相连的节点（A[root][x]=1且x!=root）
            # 这些节点组成若干连通块，每个连通块是子树
            # 先找出与root相连的节点集合
            connected = [x for x in nodes if x != root and A[root][x] == 1]
            # 这些节点在子树中必须分成若干连通块
            # 连通块定义：在nodes中，两个节点u,v连通当且仅当A[u][v]=1
            # 这里连通块是基于A中1的关系
            # 先构造子图的邻接关系（只考虑nodes中的节点）
            # 但连通块定义为A[u][v]=1的无向图的连通分量
            # 注意：A[u][v]=1是无向的，且对称
            # 先构造邻接列表
            adj = {x:[] for x in connected}
            for i in range(len(connected)):
                u = connected[i]
                for j in range(i+1, len(connected)):
                    v = connected[j]
                    if A[u][v] == 1:
                        adj[u].append(v)
                        adj[v].append(u)
            # 找连通块
            visited = set()
            components = []
            for u in connected:
                if u not in visited:
                    stack = [u]
                    comp = []
                    visited.add(u)
                    while stack:
                        cur = stack.pop()
                        comp.append(cur)
                        for w in adj[cur]:
                            if w not in visited:
                                visited.add(w)
                                stack.append(w)
                    components.append(comp)
            # 对每个连通块递归计算
            res = 1
            for comp in components:
                comp.append(root)
                comp.sort()
                comp_tuple = tuple(comp)
                # 判断comp内部是否满足条件（任意i,j A[i][j]=1）
                if not is_clique(comp):
                    return 0
                res = res * dfs(comp_tuple) % MOD
            # 子树个数为len(components)，不同子树顺序不同，乘以阶乘
            res = res * fact[len(components)] % MOD
            return res

        nodes_all = tuple(range(N))
        ans = dfs(nodes_all)
        print(ans % MOD)

if __name__ == "__main__":
    main()