import sys
import math
sys.setrecursionlimit(10**7)

MOD = 998244353

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 题意：
# 对于序列 S，满足 gcd(S)=1，且对每个 i:
# f(S_i / S_{i+1}) = A_i
# f(x) = P*Q，其中 x = P/Q，P,Q互质正整数
# 即 f(S_i/S_{i+1}) = P*Q = A_i
# 其中 S_i/S_{i+1} = P/Q，P,Q互质，且 P*Q = A_i

# 目标：求所有良好序列的分数和（乘积 S_1 * S_2 * ... * S_N），对 MOD 取模。

# 分析：
# 对每个 A_i，枚举所有 (P,Q) 使得 P*Q = A_i 且 gcd(P,Q)=1。
# 由 S_i/S_{i+1} = P/Q => S_i * Q = S_{i+1} * P
# 这给出相邻元素的比例关系。

# 设 S_1 = x，后续元素可由比例链推导：
# S_2 = S_1 * Q_1 / P_1
# S_3 = S_2 * Q_2 / P_2 = S_1 * (Q_1 Q_2) / (P_1 P_2)
# ...
# S_i = S_1 * (∏_{j=1}^{i-1} Q_j) / (∏_{j=1}^{i-1} P_j)

# 由于 gcd(S) = 1，且 S_i 都是正整数，S_1 必须能整除所有分母的约分后部分。

# 关键是枚举所有可能的 (P_i,Q_i) 组合，使得所有 S_i 都是整数，且 gcd(S)=1。

# 由于 N 最大 1000，直接枚举所有组合不现实。
# 但题目保证良好序列数量有限。

# 解决方案：
# 动态规划：
# dp[i][q] 表示到第 i 个位置，S_i 分母约分后分子为 q 的所有方案的分数和。
# 但状态空间过大。

# 优化思路：
# 观察 S_i = S_1 * (∏ Q_j)/(∏ P_j)
# 设分子积 = num_i, 分母积 = den_i
# S_i = S_1 * num_i / den_i
# 要求 S_i 整数 => S_1 * num_i % den_i == 0
# gcd(S) = 1 => gcd(S_1, S_2, ..., S_N) = 1

# 设 S_1 = k * LCM(den_i / gcd(num_i, den_i))，k 为正整数
# 由于 gcd(S) = 1，k 必须为 1
# 这样 S_i = S_1 * num_i / den_i 都是整数

# 综上，S_1 是固定的最小值，且所有 S_i 都确定
# 乘积 = ∏ S_i = S_1^N * ∏ (num_i / den_i)

# 由于 S_1 = LCM(den_i / gcd(num_i, den_i))，且 gcd(S)=1，S_1 是唯一确定的

# 关键是枚举所有 (P_i,Q_i) 组合，使得每个 A_i = P_i * Q_i 且 gcd(P_i,Q_i)=1

# 由于 N 最大 1000，且每 A_i 最大 1000，枚举每个 A_i 的因子对最多几十个
# 通过 DFS 枚举所有组合，计算对应的乘积和

# 实现细节：
# 1. 预处理每个 A_i 的所有 (P,Q) 对
# 2. DFS 枚举所有组合，计算 num_i, den_i
# 3. 计算 S_1 = LCM(den_i / gcd(num_i, den_i))
# 4. 计算乘积 = S_1^N * ∏ (num_i / den_i)
# 5. gcd(S) = 1 保证 k=1
# 6. 累加所有乘积和，取模输出

# 为避免超时，使用记忆化剪枝。

from math import gcd
from collections import defaultdict

# 预处理每个 A_i 的所有 (P,Q)
factor_pairs = []
for val in A:
    pairs = []
    for d in range(1, int(val**0.5)+1):
        if val % d == 0:
            p, q = d, val//d
            if gcd(p,q) == 1:
                pairs.append((p,q))
            if p != q and gcd(q,p) == 1:
                pairs.append((q,p))
    factor_pairs.append(pairs)

# 由于状态空间大，使用记忆化DFS
# 状态：index i, 当前分子积 num_prod, 当前分母积 den_prod
# 但 num_prod, den_prod 会爆炸，不能直接存
# 改用记录每个位置的 (P_i,Q_i)，最后计算

# 由于乘积计算复杂，改用递归枚举所有组合，计算最终乘积和

# 为避免重复计算，使用缓存
# 但缓存键不能用大整数，改用索引和当前分子积和分母积的质因数指数表示
# 复杂度过高，改用直接DFS枚举，N最大1000，A_i最大1000，因子对最多几十个，实际可行

# 计算最终乘积：
# S_i = S_1 * (∏ Q_j)/(∏ P_j) for j=1 to i-1
# 设 prefix_num[i] = ∏ Q_j (j=1 to i-1)
# prefix_den[i] = ∏ P_j (j=1 to i-1)
# S_i = S_1 * prefix_num[i] / prefix_den[i]

# gcd(S) = 1 => S_1 = LCM over i of prefix_den[i] / gcd(prefix_num[i], prefix_den[i])

# 乘积 = ∏ S_i = S_1^N * ∏ (prefix_num[i]/prefix_den[i])

# prefix_num[1] = 1, prefix_den[1] = 1

# 实现：

def lcm(a,b):
    return a // gcd(a,b) * b

# 质因数分解缓存
prime_cache = {}

def prime_factorization(x):
    if x in prime_cache:
        return prime_cache[x]
    res = defaultdict(int)
    v = x
    d = 2
    while d*d <= v:
        while v % d == 0:
            res[d] += 1
            v //= d
        d += 1 if d==2 else 2
    if v > 1:
        res[v] += 1
    prime_cache[x] = res
    return res

# 合并质因数字典
def merge_factor_dict(a,b,op=1):
    # op=1 加，op=-1 减
    res = a.copy()
    for k,v in b.items():
        res[k] = res.get(k,0) + op*v
        if res[k] == 0:
            del res[k]
    return res

# 计算整数值
def calc_val(fac):
    res = 1
    for p,e in fac.items():
        res = (res * pow(p,e,MOD)) % MOD
    return res

ans = 0

# DFS 枚举所有组合
# 记录 prefix_num 和 prefix_den 的质因数字典
# prefix_num[1] = 1, prefix_den[1] = 1
# 对于 i 从 1 到 N-1:
# prefix_num[i+1] = prefix_num[i] * Q_i
# prefix_den[i+1] = prefix_den[i] * P_i

def dfs(i, prefix_num_fac, prefix_den_fac):
    global ans
    if i == N:
        # 计算 S_1 = LCM over i of prefix_den[i]/gcd(prefix_num[i], prefix_den[i])
        # prefix_num[1]=1, prefix_den[1]=1
        # prefix_num[i], prefix_den[i] 已知
        # 先计算每个 i 的 val = prefix_den[i] / gcd(prefix_num[i], prefix_den[i])
        # gcd对应质因数取min指数
        # val的质因数 = prefix_den[i] - min(prefix_num[i], prefix_den[i])
        # 取所有 val 的 lcm，即质因数取最大指数

        # prefix_num_fac_list, prefix_den_fac_list 需要保存
        # 这里用列表保存每个位置的质因数字典

        # 由于递归中只保存当前 prefix_num_fac 和 prefix_den_fac，
        # 需要保存所有 prefix_num_fac 和 prefix_den_fac 的快照

        # 解决：在递归中保存 prefix_num_fac 和 prefix_den_fac 的快照列表

        # 但递归中没保存，改用全局变量保存

        # 这里用全局变量 prefix_num_list, prefix_den_list

        # 计算 LCM
        lcm_fac = defaultdict(int)
        for idx in range(1,N+1):
            num_fac = prefix_num_list[idx]
            den_fac = prefix_den_list[idx]
            # 计算 gcd_fac
            gcd_fac = {}
            for p in den_fac:
                if p in num_fac:
                    gcd_fac[p] = min(num_fac[p], den_fac[p])
            # val_fac = den_fac - gcd_fac
            val_fac = den_fac.copy()
            for p,e in gcd_fac.items():
                val_fac[p] -= e
                if val_fac[p] == 0:
                    del val_fac[p]
            # 更新 lcm_fac
            for p,e in val_fac.items():
                if lcm_fac.get(p,0) < e:
                    lcm_fac[p] = e

        # 计算 S_1 = lcm_val
        S1 = calc_val(lcm_fac)

        # 计算 ∏ (prefix_num[i]/prefix_den[i]) for i=1 to N
        # prefix_num[1]=1, prefix_den[1]=1
        # product_fac = sum over i of (prefix_num_fac[i] - prefix_den_fac[i])
        product_fac = defaultdict(int)
        for idx in range(1,N+1):
            num_fac = prefix_num_list[idx]
            den_fac = prefix_den_list[idx]
            for p,e in num_fac.items():
                product_fac[p] += e
            for p,e in den_fac.items():
                product_fac[p] -= e
                if product_fac[p] == 0:
                    del product_fac[p]

        # 计算 product_val
        product_val = calc_val(product_fac)

        # 乘积 = S1^N * product_val mod
        val = pow(S1, N, MOD) * product_val % MOD

        # gcd(S)=1 已保证
        ans = (ans + val) % MOD
        return

    # 枚举 factor_pairs[i-1]
    for p,q in factor_pairs[i-1]:
        # 更新 prefix_num_fac 和 prefix_den_fac
        # prefix_num[i+1] = prefix_num[i] * q
        # prefix_den[i+1] = prefix_den[i] * p

        new_prefix_num_fac = prefix_num_fac.copy()
        q_fac = prime_factorization(q)
        for k,v in q_fac.items():
            new_prefix_num_fac[k] = new_prefix_num_fac.get(k,0) + v

        new_prefix_den_fac = prefix_den_fac.copy()
        p_fac = prime_factorization(p)
        for k,v in p_fac.items():
            new_prefix_den_fac[k] = new_prefix_den_fac.get(k,0) + v

        prefix_num_list[i+1] = new_prefix_num_fac
        prefix_den_list[i+1] = new_prefix_den_fac

        dfs(i+1, new_prefix_num_fac, new_prefix_den_fac)

prefix_num_list = [defaultdict(int) for _ in range(N+1)]
prefix_den_list = [defaultdict(int) for _ in range(N+1)]

# prefix_num[1] = 1, prefix_den[1] = 1
prefix_num_list[1] = defaultdict(int)
prefix_den_list[1] = defaultdict(int)

dfs(1, prefix_num_list[1], prefix_den_list[1])

print(ans % MOD)