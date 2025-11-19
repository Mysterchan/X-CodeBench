import sys
input = sys.stdin.readline
MOD = 998244353

# 预处理组合数 C(n,k)
MAXN = 100
fact = [1]*(MAXN+1)
invfact = [1]*(MAXN+1)
for i in range(2, MAXN+1):
    fact[i] = fact[i-1]*i % MOD
invfact[MAXN] = pow(fact[MAXN], MOD-2, MOD)
for i in range(MAXN-1, 0, -1):
    invfact[i] = invfact[i+1]*(i+1) % MOD

def comb(n,k):
    if k<0 or k>n:
        return 0
    return fact[n]*invfact[k]%MOD*invfact[n-k]%MOD

# 题意分析：
# s_i 是单元格 i 的分数，分数是该单元格作为最近黑色单元格被加分的次数。
# 过程：
# 第1秒，p_1变黑，无加分。
# 第i秒(i>1)，p_i变黑，找到p_i最近的黑色单元格y，y的分数+1。
# 最近黑色单元格定义：在黑色单元格中距离p_i最近的，若有多个距离相同，取索引最小的。

# 题目给定部分s_i，求有多少排列p能产生该s。

# 关键性质：
# 1. s_i是p_i作为最近黑色单元格被加分的次数。
# 2. 每个加分对应某个后面变黑的单元格距离它最近。
# 3. 由于最近黑色单元格的定义，s_i的加分次数等于p_i的“子树大小-1”，
#    这里“子树”是指以p_i为根的某种区间结构。

# 题解思路：
# 这题是经典的“最近黑色单元格”对应的树结构问题。
# 具体地，p定义了一个“最近黑色单元格”树：
# - 根是p_1（第一个变黑的单元格）
# - 每个节点的子节点是那些以该节点为最近黑色单元格的单元格
# - s_i是节点i的子节点数（即子树大小-1）

# 因此，s_i是节点i的子树大小减1。

# 由s_i构造树的子树大小约束：
# - s_i >= 0 或 s_i = -1（未知）
# - 子树大小 = s_i + 1
# - 子树大小 >= 1

# 任务转化为：
# 给定n个节点，部分节点的子树大小(s_i+1)已知，部分未知，求满足子树大小约束的树的数量。
# 该树是“最近黑色单元格树”，即一棵有序树，节点编号1..n。

# 由于p是排列，且p_1是根，且树结构唯一确定p的顺序（先根后子树的遍历顺序），
# 题目等价于：
# - 以节点1为根，构造一棵有序树，节点子树大小满足s_i+1
# - 计算满足部分s_i未知情况下的树的数量

# 具体实现：
# 设f(l,r)表示区间[l,r]内节点构成的子树数量。
# 由于树是有序的，根为l，子树由若干连续区间组成。
# s_l+1 = 子树大小 = 1 + sum(子树大小的子节点)
# 子节点区间划分为若干连续区间，递归计算。

# 但题目中节点编号是1..n，且p是排列，p_1是根，p_2..p_n是子节点的排列顺序。
# 由于最近黑色单元格定义，树的结构是唯一的。

# 具体DP：
# 设dp[i][j]表示区间[i,j]内节点构成的子树数量。
# 根为i，子树大小为s_i+1（若已知），否则未知。
# 子树大小 = 1 + sum子树大小
# 子节点区间划分为若干连续区间，递归计算。

# 由于s_i可能未知，需枚举子树大小。

# 但此题复杂度较高，且n<=100，且s_i最大为n-1。

# 另一种思路：
# 题目中s_i是节点i的分数，即该节点作为最近黑色单元格被加分次数。
# 由题意，s_i是该节点作为最近黑色单元格的次数，即该节点的子节点数。

# 因此，s_i是节点i的子节点数。

# 由此，s_i是节点i的度数（子节点数）。

# 题目转化为：
# 给定n个节点，部分节点的度数s_i已知，部分未知，求有多少有序树满足度数约束。

# 由于树有n个节点，度数和为n-1。

# 约束：
# - sum s_i = n-1
# - s_i >= 0
# - 部分s_i已知，部分未知

# 任务：
# 计算满足部分s_i已知，部分未知，且度数和为n-1的非负整数解的数量。

# 但题目中s_i最大为n-1，且s_i=-1表示未知。

# 由于树是有序树，且根为1，排列p是先根后子树的遍历顺序。

# 计算满足度数约束的有序树数量：
# 对于有序树，度数序列确定树结构。

# 由于排列p是先根后子树的遍历顺序，且s_i是子节点数。

# 计算方法：
# 1. 验证已知s_i是否满足sum s_i <= n-1
# 2. 未知s_i用变量x_i表示，求非负整数解数量使得 sum s_i + sum x_i = n-1
# 3. 对每个未知s_i，x_i >= 0
# 4. 计算组合数 C(剩余 + 未知数 -1, 未知数 -1)

# 但题目中有额外限制：
# s_i是节点i的分数，且分数是该节点作为最近黑色单元格被加分次数。
# 该次数等于该节点的子节点数。

# 综上，题目转化为：
# 给定部分节点的子节点数，求有多少有序树满足该度数约束。

# 但题目中示例中s_i=4且n=5时答案为0，说明不能简单用组合数。

# 说明s_i不仅是子节点数，还与节点编号有关。

# 进一步分析：
# 最近黑色单元格定义：
# - 对于节点i，s_i是该节点作为最近黑色单元格被加分次数。
# - 该次数等于该节点的子节点数。

# 但子节点的定义是：
# - 对于节点i，子节点是那些在p中后出现且以i为最近黑色单元格的节点。

# 该树是“最近黑色单元格树”，且p是该树的先根遍历。

# 该树是一个区间树，且节点编号是1..n。

# 题目中s_i是节点i的子树大小减1。

# 综上，题目等价于：
# 给定n个节点，部分节点的子树大小已知，部分未知，求有多少有序树满足子树大小约束。

# 该树的先根遍历是p。

# 解决方案：
# 1. 先根遍历的第一个节点是根。
# 2. 子树大小满足：
#    size[i] = 1 + sum size[child]
# 3. 对区间[l,r]，根为l，子树大小为size[l]。
# 4. 子节点区间划分为若干连续区间，递归计算。

# 由于s_i = size[i] - 1，已知s_i则size[i] = s_i + 1。

# 设计DP：
# dp[l][r] = 该区间[l,r]构成子树的方案数
# size[l] = s_l + 1 (若已知)
# 子节点区间划分为k个连续区间，满足 sum size[child] = size[l] - 1

# 由于n<=100，枚举所有划分复杂度高。

# 优化：
# 由于子节点区间是连续的，且子树大小已知，递归枚举子树大小。

# 具体实现：
# 对区间[l,r]，根为l，size[l]已知或未知。
# 若未知，枚举size[l]从1到r-l+1。
# 子节点区间为[l+1, r]，划分为若干连续子区间，子区间大小和为size[l]-1。
# 用分割点枚举子区间，递归计算。

# 由于复杂度较高，使用记忆化搜索。

# 代码实现如下：

sys.setrecursionlimit(10**7)

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # size[i] = s[i] + 1 if s[i] != -1 else -1
    size = [x+1 if x != -1 else -1 for x in s]

    # dp[l][r]: 以l为根，区间[l,r]构成子树的方案数
    from functools import lru_cache

    @lru_cache(None)
    def dfs(l, r):
        length = r - l + 1
        if length == 1:
            # 单节点子树，size[l]必须为1或未知
            if size[l-1] != -1 and size[l-1] != 1:
                return 0
            return 1
        res = 0
        # size[l]已知或未知
        if size[l-1] != -1:
            sz = size[l-1]
            if sz > length or sz < 1:
                return 0
            # 子节点大小和 = sz - 1
            # 子节点区间为[l+1, r]
            # 将区间[l+1, r]划分为k个连续子区间，子区间大小和为sz-1
            # 用dp分割
            res = dfs_children(l+1, r, sz-1)
        else:
            # size[l]未知，枚举
            for sz in range(1, length+1):
                res += dfs_children(l+1, r, sz-1)
            res %= MOD
        return res % MOD

    # 计算区间[l,r]划分为若干连续子区间，子区间大小和为total_size
    # 每个子区间对应一个子树
    # 用记忆化搜索
    @lru_cache(None)
    def dfs_children(l, r, total_size):
        if total_size == 0:
            # 子节点为空，区间必须空
            if l > r:
                return 1
            else:
                return 0
        if l > r:
            return 0
        res = 0
        # 枚举第一个子树区间长度len_subtree
        for end in range(l, r+1):
            length = end - l + 1
            # 子树区间长度length >= size of subtree root
            # 递归计算子树方案数
            sub_res = dfs(l, end)
            if sub_res == 0:
                continue
            # 剩余区间[l+length, r]，剩余大小total_size - length
            rest_res = dfs_children(end+1, r, total_size - length)
            if rest_res == 0:
                continue
            res += sub_res * rest_res
        return res % MOD

    ans = dfs(1, n) % MOD
    print(ans)