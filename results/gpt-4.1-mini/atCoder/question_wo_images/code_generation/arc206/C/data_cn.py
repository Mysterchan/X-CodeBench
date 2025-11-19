import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 题目条件等价于：
# 对于每个区间[l,r]，存在一个x∈[l,r]，使得以x为根，去掉x后，
# 区间内其他点i与B_i连边，形成一棵树。
# 这意味着区间[l,r]的B_i构成一棵以x为根的树，且B_i ∈ [l,r]，且B_x = x。
# 因此，B_i的指向关系在区间内形成一棵树，且根节点指向自己。

# 由此可推断：
# 1. 对于每个区间[l,r]，存在唯一的根x，且B_x = x。
# 2. B_i ∈ [l,r] 对所有 i∈[l,r]。
# 3. 整个序列B满足：对于任意区间[l,r]，区间内的B_i构成一棵树，根为某个x∈[l,r]且B_x=x。

# 这说明B是一个“树形区间分割”的结构：
# 整个序列B可以看作一棵树的先序遍历结构，根节点的B_i = i。
# 递归地，区间[l,r]的根x满足B_x = x，且左右子区间分别是根x的子树。

# 题目给定A，部分已知，部分为-1，求满足上述条件的B的替换方案数。

# 关键点：
# - B_i = i 的位置是根节点。
# - 对区间[l,r]，根x满足 B_x = x。
# - 对于区间[l,r]，根x将区间分为左右子区间[l,x-1]和[x+1,r]，左右子区间分别是根x的子树。
# - 对于i≠x，B_i ∈ [l,r]且B_i ≠ i，且B_i是区间内的某个节点。
# - 递归求解左右子区间的方案数，乘积即为区间[l,r]的方案数。

# 由于N最大2e5，递归需要线性复杂度。
# 方案：
# - 预处理每个区间[l,r]的根x。
# - 根x必须满足A_x = x 或 A_x = -1（可替换为x）。
# - 对于区间[l,r]，根x必须在[l,r]内，且A_x ∈ {x,-1}。
# - 对区间[l,r]，尝试所有可能的根x，递归计算左右子区间方案数，累加。
# - 由于区间数O(N^2)过大，必须优化。

# 优化：
# 题目隐含结构是“区间树”，且根节点B_x = x。
# 由于B_i ∈ [1,N]，且B_x = x，且区间内形成树，B_i指向根或根的子树。
# 这对应于“区间树”的构造，且根节点唯一。

# 观察：
# - 对于区间[l,r]，根x满足A_x ∈ {x,-1}。
# - 对于区间[l,r]，根x必须是唯一的。
# - 题目示例中，根节点的选择决定了左右子区间的划分。

# 进一步简化：
# 题目等价于：
# - 找出一个区间树的构造方式，使得每个区间的根节点满足A_x ∈ {x,-1}。
# - 对于区间[l,r]，根x ∈ [l,r]且A_x ∈ {x,-1}。
# - 递归计算左右子区间方案数，乘积即为区间方案数。
# - 区间[l,r]的方案数 = sum_{x in [l,r], A_x in {x,-1}} (dp[l][x-1] * dp[x+1][r])

# 由于N大，不能用O(N^3)的DP。
# 观察：
# - 由于根节点必须满足A_x ∈ {x,-1}，且根节点唯一。
# - 题目中根节点的选择是唯一的，且区间树的根节点是区间内唯一满足A_x ∈ {x,-1}的节点。
# - 这意味着区间[l,r]的根节点是区间内唯一满足A_x ∈ {x,-1}的节点。

# 由此可得：
# - 对于区间[l,r]，根节点x是区间内唯一满足A_x ∈ {x,-1}的节点。
# - 如果区间内没有满足条件的节点，则方案数为0。
# - 如果有多个满足条件的节点，则方案数为0（根节点唯一）。
# - 递归计算左右子区间方案数，乘积即为区间方案数。

# 这样，DP复杂度降为O(N^2)。
# 仍然太大，需进一步优化。

# 进一步观察：
# - 根节点x满足A_x ∈ {x,-1}。
# - 对于区间[l,r]，根节点x唯一。
# - 这意味着区间[l,r]的根节点x是区间内满足A_x ∈ {x,-1}的唯一节点。
# - 这对应于区间树的构造，且根节点的选择唯一。

# 这提示我们：
# - 对于整个序列[1,N]，根节点x唯一。
# - 对于左右子区间递归同理。
# - 这对应于区间树的唯一划分。

# 题目中，A_i = -1时可替换为任意值。
# 对于A_i = -1，可替换为i（根节点）或其他值。
# 但根节点必须满足A_x = x或-1（可替换为x）。
# 对于非根节点i，A_i不能是i（否则i是根节点），只能是区间内其他节点。

# 综上，根节点必须是区间内唯一满足A_x ∈ {x,-1}的节点。
# 对于A_i = -1，可替换为i（使其成为根节点）或其他值（非根节点）。

# 这提示我们：
# - 对于区间[l,r]，根节点x满足A_x ∈ {x,-1}。
# - 对于A_x = -1，替换为x的方案数为1。
# - 对于A_x = x，方案数为1。
# - 对于非根节点i，A_i ≠ i，且A_i ∈ [l,r]。
# - 对于A_i = -1，非根节点，替换为区间内除i外的任意节点。

# 由于根节点唯一，且区间树结构唯一，方案数为：
# dp[l][r] = dp[l][x-1] * dp[x+1][r] * ways_for_non_root_nodes

# ways_for_non_root_nodes = ∏_{i≠x} ways_to_assign_B_i
# 对于非根节点i：
# - 如果A_i ≠ -1且A_i ≠ i，且A_i ∈ [l,r]，方案数为1。
# - 如果A_i = -1，方案数为区间内除i外的节点数，即 (r-l+1 - 1) = (r-l).

# 计算非根节点的方案数：
# ways = ∏_{i≠x} (1 if A_i != -1 else (r-l))

# 由于区间树结构唯一，且根节点唯一，递归计算即可。

# 实现步骤：
# 1. 预处理每个区间[l,r]的根节点x：
#    - 区间内唯一满足A_x ∈ {x,-1}的节点。
#    - 如果无或多于1个，dp[l][r] = 0。
# 2. 递归计算dp[l][r]：
#    - dp[l][r] = dp[l][x-1] * dp[x+1][r] * ways_for_non_root_nodes % MOD
# 3. 叶子区间dp[i][i]:
#    - 如果A_i = i或A_i = -1，dp[i][i] = 1
#    - 否则0

# 由于N大，不能用二维DP。
# 观察区间树结构：
# - 根节点x将区间[l,r]分为[l,x-1]和[x+1,r]。
# - 递归计算左右子区间。
# - 这对应于树的递归构造。

# 关键是找到根节点x。
# 由于根节点唯一，且满足A_x ∈ {x,-1}。

# 方案：
# - 递归函数 solve(l,r):
#   - 如果 l > r: return 1
#   - 找区间[l,r]中满足A_x ∈ {x,-1}的节点x
#   - 如果无或多于1个，return 0
#   - 计算左右子区间方案数
#   - 计算非根节点的方案数：
#     ways = 1
#     对于i in [l,r], i != x:
#       if A_i == -1: ways = ways * (r-l) % MOD
#       else: ways = ways * 1
#   - return dp[l][r] = left * right * ways % MOD

# 由于递归区间最多N次，复杂度O(N^2)仍大。
# 但题目隐含结构是区间树，且根节点唯一，且根节点的选择是唯一的。

# 进一步优化：
# - 由于根节点唯一，且根节点x满足A_x ∈ {x,-1}。
# - 对于区间[l,r]，根节点x是区间内唯一满足A_x ∈ {x,-1}的节点。
# - 这意味着区间树的根节点是唯一确定的。
# - 递归构造区间树，复杂度O(N)。

# 实现：
# - 预处理一个数组pos，pos[i] = i if A_i == i or A_i == -1 else None
# - 递归函数 solve(l,r):
#   - 如果 l > r: return 1
#   - 在[l,r]中找唯一满足条件的x
#   - 如果无或多于1个，return 0
#   - left = solve(l,x-1)
#   - right = solve(x+1,r)
#   - ways = 1
#   - 对i in [l,r], i != x:
#       if A_i == -1: ways = ways * (r-l) % MOD
#   - return left * right * ways % MOD

# 为了快速找到区间内满足条件的唯一x，使用线段树或预处理。
# 由于条件是A_i == i or A_i == -1，且i ∈ [1,N]，可以预处理一个辅助数组：
# - 对每个位置i，标记是否满足条件。
# - 构建前缀和数组，快速查询区间内满足条件的个数。
# - 还需找到满足条件的节点位置。
# - 由于满足条件的节点最多1个，使用二分查找或线段树查询。

# 实现细节：
# - 构建一个满足条件的布尔数组 good[i] = True if A_i == i or A_i == -1 else False
# - 构建前缀和 prefix_good
# - 对区间[l,r]，count = prefix_good[r] - prefix_good[l-1]
# - 如果 count != 1，return 0
# - 找满足条件的节点x：
#   - 线性查找区间[l,r]中good[i] == True的i
#   - 由于递归区间长度递减，整体复杂度仍可接受

# 代码实现如下：
def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    MOD = 998244353

    good = [False]*(N+1)
    for i in range(N):
        if A[i] == -1 or A[i] == i+1:
            good[i+1] = True

    prefix_good = [0]*(N+2)
    for i in range(1,N+1):
        prefix_good[i] = prefix_good[i-1] + (1 if good[i] else 0)

    from functools import lru_cache

    def count_good(l,r):
        return prefix_good[r] - prefix_good[l-1]

    @lru_cache(None)
    def solve(l,r):
        if l > r:
            return 1
        c = count_good(l,r)
        if c != 1:
            return 0
        # 找满足条件的节点x
        x = -1
        for i in range(l,r+1):
            if good[i]:
                x = i
                break
        left = solve(l,x-1)
        right = solve(x+1,r)
        ways = 1
        length = r - l
        for i in range(l,r+1):
            if i == x:
                continue
            if A[i-1] == -1:
                ways = ways * length % MOD
        return left * right % MOD * ways % MOD

    print(solve(1,N) % MOD)

if __name__ == "__main__":
    main()