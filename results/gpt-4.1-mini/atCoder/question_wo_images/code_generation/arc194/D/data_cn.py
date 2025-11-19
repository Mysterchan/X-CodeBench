MOD = 998244353

# 题意简述：
# 给定一个有效括号序列 S，允许任意次操作：
# 选择 S 的一个连续子串，该子串本身是有效括号序列，
# 对该子串执行“特殊反转”操作：
# 反转子串顺序并将 '(' 变 ')'，')' 变 '('。
# 求最终能得到的不同字符串数量（模 998244353）。

# 关键观察：
# 1. 该操作等价于对选中子串做“镜像反转”：
#    例如子串 "(())" 反转后变成 "(())"（本身对称），
#    子串 "()" 反转后变成 "()"
# 2. 由于 S 是有效括号序列，且操作只在有效子串上进行，
#    这实际上是对 S 的某些有效子串做“镜像反转”。
# 3. 目标是求所有通过若干次此操作能得到的不同有效括号序列数。

# 进一步分析：
# 该操作类似于对 S 的某些有效子串做“对称翻转”。
# 由于括号序列的结构是树形的（括号匹配形成的嵌套结构），
# 该操作相当于对某些子树做镜像翻转。

# 因此，问题转化为：
# 给定一个有效括号序列对应的树结构，
# 计算通过对任意子树做镜像翻转能得到的不同序列数。

# 解决方案：
# 1. 解析括号序列，构建对应的树结构。
#    每对匹配括号对应一个节点，节点的子节点是其内部的直接子括号对。
# 2. 对树进行递归DP：
#    对每个节点，计算其所有子节点的不同排列组合数。
#    由于子节点是有序的，镜像翻转会将子节点顺序反转。
#    因此，节点的不同形态数 = 子节点形态数的乘积 + 子节点形态数的乘积（反转顺序）
#    如果正序和逆序相同，则只计一次。
# 3. 叶节点（没有子节点）形态数为1。
# 4. 最终根节点的形态数即为答案。

# 注意：
# - 需要对每个节点的子节点形态数进行组合计算。
# - 判断正序和逆序是否相同，避免重复计数。

# 实现细节：
# - 用栈匹配括号，记录每对括号的子节点。
# - 用递归函数计算每个节点的形态数。
# - 由于 N ≤ 5000，树结构不会太深，递归可行。

import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

# 找到每个括号的匹配位置
stack = []
match = [-1]*N
for i, c in enumerate(S):
    if c == '(':
        stack.append(i)
    else:
        j = stack.pop()
        match[i] = j
        match[j] = i

# 构建树结构
# 节点用左括号位置标识
# 对每个左括号，找其直接子节点（在其匹配括号内的左括号）
children = [[] for _ in range(N)]
# 记录哪些是左括号节点
is_node = [False]*N
for i in range(N):
    if S[i] == '(':
        is_node[i] = True

# 对每个左括号节点，找其直接子节点
# 直接子节点是其匹配括号内，且不被其他括号包裹的左括号
# 利用栈遍历区间即可
def build_children(l, r):
    res = []
    i = l+1
    while i < r:
        if S[i] == '(':
            res.append(i)
            i = match[i]+1
        else:
            i += 1
    return res

for i in range(N):
    if is_node[i]:
        children[i] = build_children(i, match[i])

# 递归计算每个节点的形态数
# 返回值：形态数（int）
# 计算方法：
# 1. 对所有子节点递归计算形态数
# 2. 计算正序乘积和逆序乘积
# 3. 如果相同，结果为乘积，否则为乘积*2
# 4. 结果 mod MOD

def dfs(u):
    if not children[u]:
        return 1
    vals = [dfs(c) for c in children[u]]
    prod = 1
    for v in vals:
        prod = (prod * v) % MOD
    rev_prod = 1
    for v in reversed(vals):
        rev_prod = (rev_prod * v) % MOD
    if prod == rev_prod:
        return prod % MOD
    else:
        return (prod + rev_prod) % MOD

# 根节点是0号左括号
ans = dfs(0) % MOD
print(ans)